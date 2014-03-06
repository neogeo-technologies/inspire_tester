# -*- coding: UTF-8 -*-

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

import xml.dom.minidom
import lxml.etree as etree
import urlparse
from urllib import urlencode

# ------------------------------------------------------------------------------

# Namespaces for element in the WMS capabilities
NS130 = "{http://www.opengis.net/wms}"
NS111 = ""

# Clean-up the uri
# Add ? if not present
# Remove service, request and version parameters
def cleanupServiceUrl(url):
  """Clean-up the uri by removing extra parameters
  """
  if url == None:
    return None
  
  params = []
  if url.find('?') != -1:
      params = urlparse.parse_qsl(url.split('?')[1])
  new_params = [x for x in params if x[0].lower() not in ('service',
                                                          'request', 'version')]
  
  return url.split('?')[0] + '?' + urlencode(tuple(new_params))


# Get the GetCapabilities URL from the service URL
# Thanks to OWSLib
def getGetCapabilitiesUrlFromServiceUrl(service_url, wms_version):
  """Return a the GetCapabilities URL
  """
  qs = []
  if service_url.find('?') != -1:
      qs = urlparse.parse_qsl(service_url.split('?')[1])

  params = [x[0] for x in qs]

  if 'service' not in params:
      qs.append(('service', 'WMS'))
  if 'request' not in params:
      qs.append(('request', 'GetCapabilities'))
  if 'version' not in params:
      qs.append(('version', wms_version))

  urlqs = urlencode(tuple(qs))
  return service_url.split('?')[0] + '?' + urlqs


# Get a pretty print version of the capabilities
def getPrettyPrintCapabilities(strCapabilities):
  
  prettyCapabilities = None
  
  # First attempt with minidom
  try:
    xml_doc = xml.dom.minidom.parseString(strCapabilities)
    prettyCapabilities = xml_doc.toprettyxml(indent="  ")
  except:
    pass
  
  # Second attempt with lxml (does not work with Unicode strings with encoding
  # declaration)
  if prettyCapabilities == None:
    try:
      xml_doc = etree.fromstring(strCapabilities)
      prettyCapabilities = etree.tostring(xml_doc, pretty_print = True)
      return prettyCapabilities
    except:
      prettyCapabilities = strCapabilities

  # Removal of blank lines (can be optimised)
  prettyCapabilitiesWithoutBlankLine = ""
  for line in prettyCapabilities.split('\n'):
    if line.strip():
      prettyCapabilitiesWithoutBlankLine += line + '\n'

  return prettyCapabilitiesWithoutBlankLine

# Get the version of the WMS specification used in the capabilities doc
def getWMSVersion(strCapabilities):
  try:
    etreeCapabilities = etree.fromstring(strCapabilities)
    version = etreeCapabilities.get("version").strip()
    
    root_tag = etreeCapabilities.tag
    if version == "1.3.0":
      if root_tag != "%sWMS_Capabilities" % (NS130):
        return None
    else:
      if root_tag != "WMT_MS_Capabilities":
        return None
        
    return version

  except Exception, e:
    return None

# Get the name of the service (the title actually)
def getServiceName(strCapabilities):
  version = getWMSVersion(strCapabilities)
  if version == "1.3.0":
    ns = NS130
  else:
    ns = NS111
  
  xpath = "./%sService/%sTitle" % (ns, ns)
  
  try:
    etreeCapabilities = etree.fromstring(strCapabilities)
    return etreeCapabilities.findall(xpath)[0].text.strip()
  except Exception, e:
    return None


# Get the WGS84 bounding box of the service
def getServiceBBox(strCapabilities):
  return None


# Get the main informations stored in the capabilities
# The returned value is a Python dictionary
def getWmsPropertiesAsDict(etreeCapabilities):
  """Create a summary of the capabilities of a WMS service"""
  
  ns = "" # namespace for the wms capabilities elements
  result = dict()


  # Service type


  # Service version
  try:
    wmsVersion = etreeCapabilities.get("version")
    result["WMS_version"] = wmsVersion
  except:
    result["WMS_version"] = None

  if wmsVersion == "1.3.0":
    ns = NS130
  else:
    ns = NS111

  # Service title
  try:
    serviceTitle = etreeCapabilities.findall("./%sService/%sTitle" % (ns, ns))[0].text
    result["Service_Title"] = serviceTitle
  except:
    result["Service_Title"] = None

  # Service abstract
  try:
    serviceAbstract = etreeCapabilities.findall("./%sService/%sAbstract" % (ns, ns))[0].text
    result["Service_Abstract"] = serviceAbstract
  except:
    result["Service_Abstract"] = None

  # Service online resource
  try:
    onlineResource = etreeCapabilities.findall("./%sService/%sOnlineResource" % (ns, ns))[0].get("{http://www.w3.org/1999/xlink}href")
    result["Service_OnlineResource"] = onlineResource
  except:
    result["Service_OnlineResource"] = None

  # Service keywords
  try:
    keywords = etreeCapabilities.findall("./%sService//%sKeyword" % (ns, ns))
    if len(keywords) > 0:
      serviceKeywords = [keyword.text for keyword in keywords if keyword.text != None]
    else:
      serviceKeywords = []
    result["Service_Keywords"] = serviceKeywords
  except:
    result["Service_Keywords"] = []

  # Service contact information
  try:
    person_primary_elements = etreeCapabilities.findall("./%sService//%sContactPersonPrimary/*" % (ns, ns))
    person_primary = [e.text for e in person_primary_elements if e.text != None]
    result["Service_Contact_Person"] = ", ".join(person_primary)
  except:
    result["Service_Contact_Person"] = None

  try:
    contact_organisation = etreeCapabilities.findall("./%sService//%sContactOrganization" % (ns, ns))
    result["Service_Contact_Organization"] = contact_organisation[0].text.strip()
  except:
    result["Service_Contact_Organization"] = None

  try:
    contact_position = etreeCapabilities.findall("./%sService//%sContactPosition" % (ns, ns))
    result["Service_Contact_Position"] = contact_position[0].text
  except:
    result["Service_Contact_Position"] = None

  try:
    contact_email = etreeCapabilities.findall("./%sService//%sContactElectronicMailAddress" % (ns, ns))
    result["Service_Contact_ElectronicMailAddress"] = contact_email[0].text.strip()
  except:
    result["Service_Contact_ElectronicMailAddress"] = None

  try:
    contact_address_elements = etreeCapabilities.findall("./%sService//%sContactAddress/*" % (ns, ns))
    contact_address = [e.text for e in contact_address_elements if e.text != None]
    result["Service_Contact_Address"] = ", ".join(contact_address)
  except:
    result["Service_Contact_Address"] = None

  # Service fees
  try:
    serviceFees = etreeCapabilities.findall("./%sService/%sFees" % (ns, ns))[0].text
    result["Service_Fees"] = serviceFees
  except:
    result["Service_Fees"] = None

  # Service access constraints
  try:
    serviceAccessConstraints = etreeCapabilities.findall("./%sService/%sAccessConstraints" % (ns, ns))[0].text
    result["Service_AccessConstraints"] = serviceAccessConstraints
  except:
    result["Service_AccessConstraints"] = None

  # Requests
  # Support for GetCapabilities
  try:
    result["GetCapabilities_support"] = getSupportedBindingsForRequest(etreeCapabilities, ns, "GetCapabilities")
  except:
    result["GetCapabilities_support"] = None
  
  try:
    result["GetCapabilities_formats"] = getSupportedFormatsForRequest(etreeCapabilities, ns, "GetCapabilities")
  except:
    result["GetCapabilities_formats"] = None
  
  # Support for GetMap
  try:
    result["GetMap_support"] = getSupportedBindingsForRequest(etreeCapabilities, ns, "GetMap")
  except:
    result["GetMap_support"] = None
  
  try:
    result["GetMap_formats"] = getSupportedFormatsForRequest(etreeCapabilities, ns, "GetMap")
  except:
    result["GetMap_formats"] = None
  
  # Support for GetFeatureInfo
  try:
    result["GetFeatureInfo_support"] = getSupportedBindingsForRequest(etreeCapabilities, ns, "GetFeatureInfo")
  except:
    result["GetFeatureInfo_support"] = None
  
  try:
    result["GetFeatureInfo_formats"] = getSupportedFormatsForRequest(etreeCapabilities, ns, "GetFeatureInfo")
  except:
    result["GetFeatureInfo_formats"] = None
  

  # Layers
  try:
    nbOfLayers = len(etreeCapabilities.findall(".//%sLayer" % (ns)))
    result["Nb_of_layers"] = nbOfLayers
  except:
    result["Nb_of_layers"] = None

  try:
    nbOfNamedLayers = len(etreeCapabilities.findall(".//%sLayer/%sName" % (ns, ns)))
    result["Nb_of_named_layers"] = nbOfNamedLayers
  except:
    result["Nb_of_named_layers"] = 0

  try:
    nbOfFirstLevelLayers = len(etreeCapabilities.findall("./%sCapability/%sLayer" % (ns, ns)))
    result["Nb_of_1st_lev_layers"] = nbOfFirstLevelLayers
  except:
    result["Nb_of_1st_lev_layers"] = 0

  try:
    nbOfSecondLevelLayers = len(etreeCapabilities.findall("./%sCapability/%sLayer/%sLayer" % (ns, ns, ns)))
    result["Nb_of_2nd_lev_layers"] = nbOfSecondLevelLayers
  except:
    result["Nb_of_2nd_lev_layers"] = 0

  try:
    nbOfThirdLevelLayers = len(etreeCapabilities.findall("./%sCapability/%sLayer/%sLayer/%sLayer" % (ns, ns, ns, ns)))
    result["Nb_of_3rd_lev_layers"] = nbOfThirdLevelLayers
  except:
    result["Nb_of_3rd_lev_layers"] = 0

  try:
    maxLevel = 0
    layerPath = './%sCapability/%sLayer' % (ns, ns)
    while len(etreeCapabilities.findall(layerPath))>0:
      layerPath += '/%sLayer' % (ns)
      maxLevel += 1
    result["Max_layer_level"] = maxLevel
  except:
    result["Max_layer_level"] = -1

  try:
    nbOfLayersWithAbstract = len(etreeCapabilities.findall(".//%sLayer/%sAbstract" % (ns, ns)))
    result["Nb_of_layers_with_abstract"] = nbOfLayersWithAbstract
  except:
    result["Nb_of_layers_with_abstract"] = 0

  try:
    nbOfLayersWithKeywords = len(etreeCapabilities.findall(".//%sLayer/%sKeywordList" % (ns, ns)))
    result["Nb_of_layers_with_keywords"] = nbOfLayersWithKeywords
  except:
    result["Nb_of_layers_with_keywords"] = 0

  try:
    nbOfLayersWithScaleHint = len(etreeCapabilities.findall(".//%sLayer/%sScaleHint" % (ns, ns)))
    result["Nb_of_layers_with_scale_hint"] = nbOfLayersWithScaleHint
  except:
    result["Nb_of_layers_with_scale_hint"] = 0

  try:
    nbOfLayerDimensions = len(etreeCapabilities.findall(".//%sLayer/%sDimension" % (ns, ns)))
    result["Nb_of_layer_dimensions"] = nbOfLayerDimensions
  except:
    result["Nb_of_layer_dimensions"] = 0

  try:
    nbOfLayerExtents = len(etreeCapabilities.findall(".//%sLayer/%sExtent" % (ns, ns)))
    result["Nb_of_layer_extents"] = nbOfLayerExtents
  except:
    result["Nb_of_layer_extents"] = 0
  
  try:
    nbOfLayerMetadataURLs = len(etreeCapabilities.findall(".//%sLayer/%sMetadataURL" % (ns, ns)))
    result["Nb_of_layer_metadata_URLs"] = nbOfLayerMetadataURLs
  except:
    result["Nb_of_layer_metadata_URLs"] = 0

  try:
    nbOfLayerAttributions = len(etreeCapabilities.findall(".//%sLayer/%sAttribution" % (ns, ns)))
    result["Nb_of_layer_attributions"] = nbOfLayerAttributions
  except:
    result["Nb_of_layer_attributions"] = 0
    
  try:
    nbOfLayerIdentifiers = len(etreeCapabilities.findall(".//%sLayer/%sIdentifier" % (ns, ns)))
    result["Nb_of_layer_identifiers"] = nbOfLayerIdentifiers
  except:
    result["Nb_of_layer_identifiers"] = 0
    
  try:
    nbOfLayerFeatureListURLs = len(etreeCapabilities.findall(".//%sLayer/%sFeatureListURL" % (ns, ns)))
    result["Nb_of_layer_feature_list_URLs"] = nbOfLayerFeatureListURLs
  except:
    result["Nb_of_layer_feature_list_URLs"] = 0

  try:
    nbOfLayerDataURL = len(etreeCapabilities.findall(".//%sLayer/%sDataURL" % (ns, ns)))
    result["Nb_of_layer_data_URLs"] = nbOfLayerDataURL
  except:
    result["Nb_of_layer_data_URLs"] = 0

  # Overall bounding box (WGS84)
  try:
    if wmsVersion == "1.3.0":
      # west
      etree_coords = etreeCapabilities.findall('.//%swestBoundLongitude' % (ns))
      coords = [float(e.text) for e in etree_coords]
      west = min(coords)
      
      # east
      etree_coords = etreeCapabilities.findall('.//%seastBoundLongitude' % (ns))
      coords = [float(e.text) for e in etree_coords]
      east = max(coords)
      
      # north
      etree_coords = etreeCapabilities.findall('.//%snorthBoundLatitude' % (ns))
      coords = [float(e.text) for e in etree_coords]
      north = max(coords)
  
      # south
      etree_coords = etreeCapabilities.findall('.//%ssouthBoundLatitude' % (ns))
      coords = [float(e.text) for e in etree_coords]
      south = min(coords)
      
      result["BoundingBox_south"] = south
      result["BoundingBox_north"] = north
      result["BoundingBox_east"] = east
      result["BoundingBox_west"] = west
      
    else:
      etree_bounding_boxes = etreeCapabilities.findall('.//%sLatLonBoundingBox' % (ns))
      west_coords = [float(e.attrib["minx"]) for e in etree_bounding_boxes]
      east_coords = [float(e.attrib["maxx"]) for e in etree_bounding_boxes]
      north_coords = [float(e.attrib["maxy"]) for e in etree_bounding_boxes]
      south_coords = [float(e.attrib["miny"]) for e in etree_bounding_boxes]
      north = max(north_coords)
      south = min(south_coords)
      east = max(east_coords)
      west = min(west_coords)
      
      result["BoundingBox_south"] = south
      result["BoundingBox_north"] = north
      result["BoundingBox_east"] = east
      result["BoundingBox_west"] = west
      
  except:
    result["BoundingBox"] = None

  # CRS
  if wmsVersion == "1.3.0":
    try:
      srsSet = set([])
      for element in etreeCapabilities.findall('.//%sCRS' % (ns)):
        srsSet.update(element.text.split(' '))
      result["Nb_of_CRS"] = len(srsSet)
    except:
      result["Nb_of_CRS"] = 0
  else:
    try:
      srsSet = set([])
      for element in etreeCapabilities.findall('.//%sSRS' % (ns)):
        srsSet.update(element.text.split(' '))
      result["Nb_of_CRS"] = len(srsSet)
    except:
      result["Nb_of_CRS"] = 0

  return result


# Get the bindings supported by the service for a given request
def getSupportedBindingsForRequest(etreeCapabilities, ns, request_name):
  result = []
  xpath = "./%sCapability/%sRequest/%s%s/%sDCPType/%sHTTP/*" % (ns, ns, ns, request_name, ns, ns)
  request_bindings = etreeCapabilities.findall(xpath)
  
  for e in request_bindings:
    # Remove the namespace from the tag
    result.append(e.tag.split("}")[-1])
    
  return result


# Get the formats supported by the service for a given request
def getSupportedFormatsForRequest(etreeCapabilities, ns, request_name):
  xpath = "./%sCapability/%sRequest/%s%s/%sFormat" % (ns, ns, ns, request_name, ns)
  request_formats = etreeCapabilities.findall(xpath)
  return [e.text for e in request_formats if e.text != None]

  
