# -*- coding: utf-8 -*-

#  INSPIRE_tester Copyright 2011 Benjamin Chartier, Guillaume Sueur (Neogeo Technologies) 

#  This file is part of INSPIRE_tester.
#
#  INSPIRE_tester is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  INSPIRE_tester is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with INSPIRE_tester.  If not, see <http://www.gnu.org/licenses/>.

from inspire_tester.wms_tester.models import WMSService

from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.conf import settings
from django.utils.encoding import *

from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import MultiPolygon

import wmsUtils.wmsMisc
import wmsUtils.inspireTests

import urllib2
import lxml.etree
import xml.etree.ElementTree as etree

import datetime
from django.utils.translation import ugettext as _


def index(request):
  
  capabilities = ""
  wms_properties = ""
  test_results = ""
  wms_version = None
  save_in_database = False
  
  # Get the parameters of the request
  service_uri = wmsUtils.wmsMisc.cleanupServiceUrl(request.GET.get('uri', None))
  use_cached_cap = request.GET.get('use_cached_cap', 0)

  if service_uri == None or len(service_uri.strip()) == 0:
    last_services = getLastServices()
    c = {
            "media_url" : settings.MEDIA_URL,
            "service_uri" : "",
            "use_cached_cap": True,
            "last_services": last_services,
        }
    c.update(csrf(request))
    
    return render_to_response('wms_tester/index.html', 
        c,
        context_instance=RequestContext(request),
        mimetype="text/html"
        )
    
  # Get the capabilities document
  if use_cached_cap != 0 and isCapabilitiesInCache(service_uri):
    capabilities = getCachedCapabilities(service_uri)
  else:
    try:
      capabilities = getNotCachedCapabilities(service_uri)
    except urllib2.HTTPError, e:
      message = _("An %s HTTP error has been encountered") % (e.code)
      #Une erreur HTTP %s a été rencontrée en essayant d'accéder au service dont vous avez fourni l'URL. Veuillez vérifier l'URL du service ou réessayer ultérieurement."
      return buildErrorMessagePage(request, service_uri, message)
    except urllib2.URLError, e:
      message = _("The provided URL doesn't seem to be correct. Please check your service URL.")
      return buildErrorMessagePage(request, service_uri, message)
    except Exception, e:
      message = _("The provided URL doesn't seem to match a WMS service. We can't proceed to any further test on this URL")
      return buildErrorMessagePage(request, service_uri, message)

    try:
      # Test if it is a capabilities document or not
      # a capabilities document is an XML document
      # with a WMT_MS_Capabilities element for WMS 1.1.1
      # with a WMS_Capabilities element with the namespace "http://www.opengis.net/wms" for WMS 1.3.0
      service_version = wmsUtils.wmsMisc.getWMSVersion(capabilities)
        
      if service_version == None:
          message = _("The response coming back from the service does not seem to a Capabilities document. This service may not be a WMS service.")
          return buildErrorMessagePage(request, service_uri, message)
            
    except Exception, e:
      message = _("The response coming back from the service does not seem to a Capabilities document. This service may not be a WMS service.")
      return buildErrorMessagePage(request, service_uri, message)
    
    # Flag to remember to update the database for this service
    save_in_database = True
    
  # Analyse the contents of the Capabilties doc
  etree_cap = etree.fromstring(capabilities)
  wms_properties = wmsUtils.wmsMisc.getWmsPropertiesAsDict(etree_cap)
  inspire_properties = wmsUtils.inspireTests.getInspirePropertiesAsDict(etree_cap)
  
  # Update the database for this service
  if save_in_database:
    updateDatabaseForService(service_uri, wms_properties, capabilities)
  
  # Prettyfy the capabilities before displaying it
  capabilities = wmsUtils.wmsMisc.getPrettyPrintCapabilities(capabilities)

  # Test the conformance to INSPIRE technical guidances
  test_messages = wmsUtils.inspireTests.testInspireCompliance(wms_properties, inspire_properties)
  test_results = {}
  test_results[wmsUtils.testMessage.LEVEL_DEBUG] = len([m for m in test_messages if m.level == wmsUtils.testMessage.LEVEL_DEBUG])
  test_results[wmsUtils.testMessage.LEVEL_INFO] = len([m for m in test_messages if m.level == wmsUtils.testMessage.LEVEL_INFO])
  test_results[wmsUtils.testMessage.LEVEL_WARNING] = len([m for m in test_messages if m.level == wmsUtils.testMessage.LEVEL_WARNING])
  test_results[wmsUtils.testMessage.LEVEL_ERROR] = len([m for m in test_messages if m.level == wmsUtils.testMessage.LEVEL_ERROR])
  test_results[wmsUtils.testMessage.LEVEL_CRITICAL] = len([m for m in test_messages if m.level == wmsUtils.testMessage.LEVEL_CRITICAL])

  # Prepare the context to be used by the template
  c = {
          "media_url" : settings.MEDIA_URL,
          "capabilities" : capabilities,
          "wms_properties" : wms_properties,
          "inspire_properties" : inspire_properties,
          "test_messages" : test_messages,
          "test_results" : test_results,
          "use_cached_cap": use_cached_cap,
          "service_uri": service_uri,
      }

  # Display the document
  return render_to_response('wms_tester/index.html', 
      c,
      context_instance=RequestContext(request),
      mimetype="text/html"
      )
        
# Do we already have the capabilities document in the database?
def isCapabilitiesInCache(service_uri):
  try:
    service = WMSService.objects.get(uri=service_uri)
    if len(service.cap_cache.strip()) > 0:
      return True
  except Exception, e:
    return False
  else:
    return False

# Retrieve the capabilities document from the database
def getCachedCapabilities(service_uri):
  service = WMSService.objects.get(uri=service_uri)
  return service.cap_cache

# Retrieve the capabilities document from the service itself.
# In fact, we send a GetCapapabilities request to the service.
# This function returns whatever it gets back from the service.
# It could be an HTTP error, une Exception or anything else.
def getNotCachedCapabilities(service_uri):
  capabilities_uri = \
      wmsUtils.wmsMisc.getGetCapabilitiesUrlFromServiceUrl(
                                                      service_uri, "1.3.0")
  capabilities = urllib2.urlopen(capabilities_uri).read()

  # The following to lines don't seem to be very useless but in fact
  # it avoids some errors related to encodings  (don't ask me why!)
  # This kind of error was encountered with the service called
  # Antarctic Cryosphere Access Portal (A-CAP)
  xml =   lxml.etree.fromstring(capabilities)
  capabilities = lxml.etree.tostring(xml)
  
  return capabilities

# Update the database for this service
def updateDatabaseForService(service_uri, wms_dict, capabilities):
  service_name = wms_dict["Service_Title"]
  try:
    polygon = Polygon((
       (wms_dict["BoundingBox_west"], wms_dict["BoundingBox_south"]),
       (wms_dict["BoundingBox_east"], wms_dict["BoundingBox_south"]),
       (wms_dict["BoundingBox_east"], wms_dict["BoundingBox_north"]),
       (wms_dict["BoundingBox_west"], wms_dict["BoundingBox_north"]),
       (wms_dict["BoundingBox_west"], wms_dict["BoundingBox_south"])
       ))
    service_bbox = MultiPolygon( polygon )
  except:
    service_bbox = None
  service_bbox = None  
  service, created = WMSService.objects.get_or_create(uri=service_uri)
  if created:
      service.uri = service_uri
  if service_name:
      service.name = service_name
  else:
      service.name = 'Unknown'
  service.cap_cache = capabilities
  service.cap_cache_date = datetime.datetime.now()
  service.wgs84_boundingbox = service_bbox
  service.save()


# Creates a response for error messages to be displayed in the browser
def buildErrorMessagePage(request, service_uri, message):
  c = {
          "media_url" : settings.MEDIA_URL,
          "message" : message,
          "service_uri" : service_uri
      }
  c.update(csrf(request))
  return render_to_response('wms_tester/error.html', 
      c,
      context_instance=RequestContext(request),
      mimetype="text/html"
      )
  

# Get the list of the last tested services
def getLastServices():
  return WMSService.objects.order_by('-cap_cache_date')[:10]

