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

from wms_tester.models import WMSService
from wms_tester.models import Evaluation

import owslib.wms
from owslib.etree import etree
import urllib2
import xml.dom.minidom


def prettyfyXmlString(xml_string):
    
    prettyfied_string = xml_string
    
    try:
        prettyfied_string = xml_string.strip()
        prettyfied_string = prettyfied_string.replace("\n", "")
        prettyfied_string = prettyfied_string.replace("\r", "")
        prettyfied_string = prettyfied_string.replace("\t", "")
        xml_doc = xml.dom.minidom.parseString(prettyfied_string)
        prettyfied_string = xml_doc.toprettyxml(indent="  ")
    finally:
        pass
    
    return prettyfied_string

def getWMSCapabilities(service_url):
    capabilities = None
    if service_url == None:
        service_url = "http://apollopro.erdas.com/erdas-apollo/map/MAPDRESSING"

    try:
        capabilities_reader = owslib.wms.WMSCapabilitiesReader('1.3.0')
        capabilities_url = capabilities_reader.capabilities_url(service_url)
        capabilities = urllib2.urlopen(capabilities_url).read()
        capabilities = prettyfyXmlString(capabilities)
    
    # If an HTTP error occurs, send back an exception
    
    # If the response is not an XML string, send back another exception
    
    # Send back another exception if the root of the XML string is not an element like :
    # http://www.opengis.net/wms:WMS_Capabilities
    # or
    # WMT_MS_Capabilities
    
    except Exception, e:
        capabilities = e
        
    return capabilities

    # test if it is a capabilities document or not
    
    # store the capabilities in a local repository
    
    # display the document
    

class Report:
    def __init__(self):
        self.serviceUrl = ""
        self.date = ""
        self.testVersion = ""
        self.reportItems = []
    
    def parseStr(self, reportAsString):
        pass

class ReportItem:
    def __init__(self):
        self.title = ""
        self.desc = ""
        self.severity = ""
