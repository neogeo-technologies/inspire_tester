# -*- coding: UTF-8 -*-

#  INSPIRE_tester Copyright 2011 Benjamin Chartier, Guillaume Sueur (Neogeo Technologies) 

#  This file is part of INSPIRE_tester.
#
#  INSPIRE_tester is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  Foobar is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with INSPIRE_tester.  If not, see <http://www.gnu.org/licenses/>.

from django.utils.translation import ugettext as _

# Levels
LEVEL_DEBUG = "debug"
LEVEL_INFO = "info"
LEVEL_WARNING = "warning"
LEVEL_ERROR = "error"
LEVEL_CRITICAL = "critical"

class Message:
  """The code is short string identifying the test.
  The requirements property is a list of requirements and recommandations
  related to the message.
  The title property is string shortly describing the nature of the test/error.
  The desc property is a string that describes the test/error in more detail. It may
  contain explanations and advises.
  The level property describes the criticity of the error: debug, info, warning, error or
  critical.
  The detail property can be used to locate the error or can contail an XML
  fragment.
  """
  
  def __init__(self, code):
    # Code of the message
    self.code = code
    
    # Array of the id of the requirements and recommandations related to the
    # test / message
    self.requirements = MESSAGE[self.code]["requirements"]
    
    # Title of the message
    self.title = MESSAGE[self.code]["title"]
    
    # Description of the message
    self.desc = MESSAGE[self.code]["desc"]
    
    # Level of the message
    self.level = MESSAGE[self.code]["level"]
    
    if self.level == LEVEL_DEBUG:
      self.level_style = "level_debug"
    elif self.level == LEVEL_INFO:
      self.level_style = "level_info"
    elif self.level == LEVEL_WARNING:
      self.level_style = "level_warning"
    elif self.level == LEVEL_ERROR:
      self.level_style = "level_error"
    elif self.level == LEVEL_CRITICAL:
      self.level_style = "level_critical"
    
    self.detail = ""

  def __unicode__(self):
    return u"%s - %s" % (self.code, self.success)

MESSAGE = {}

# Info - Test scope and completeness
MESSAGE["0"] = {
  "requirements": [],
  "title": _("msg_title_000 test scope and completeness"),
  "desc":  _("msg_desc_000 test scope and completeness"),
  "level": LEVEL_INFO,
}

# WMS version
MESSAGE["1"] = {
  "requirements": ["TG_Req#01", "TG_Req#02"],
  "title": _("msg_title_001 WMS version"),
  "desc":  _("msg_desc_001 WMS version"),
  "level": LEVEL_CRITICAL
}

# GetCapabilities support
MESSAGE["2"] = {
  "requirements": ["TG_Req#03"],
  "title": _("msg_title_002 GetCapabilities support"),
  "desc":  _("msg_desc_002 GetCapabilities support"),
  "level": LEVEL_CRITICAL
}

# GetMap support
MESSAGE["3"] = {
  "requirements": ["TG_Req#03"],
  "title": _("msg_title_003 GetMap support"),
  "desc":  _("msg_desc_003 GetMap support"),
  "level": LEVEL_CRITICAL
}

# HTTP Get binding for GetCapabilities
MESSAGE["4"] = {
  "requirements": ["TG_Rec#01"],
  "title": _("msg_title_004 HTTP GET binding GetCapabilities"),
  "desc":  _("msg_desc_004 HTTP GET binding GetCapabilities"),
  "level": LEVEL_WARNING
}

# HTTP Get binding for GetMap
MESSAGE["5"] = {
  "requirements": ["TG_Rec#01"],
  "title": _("msg_title_005 HTTP GET binding GetMap"),
  "desc":  _("msg_desc_005 HTTP GET binding GetMap"),
  "level": LEVEL_WARNING
}

# Extended capabilities - MetadataUrl
MESSAGE["6"] = {
  "requirements": ["TG_Req#06"],
  "title": _("msg_title_006 info scenario 1"),
  "desc":  _("msg_desc_006 info scenario 1"),
  "level": LEVEL_INFO
}

MESSAGE["6.1"] = {
  "requirements": ["TG_Req#06"],
  "title": _("msg_title_006.1 info scenario 2"),
  "desc":  _("msg_desc_006.1 info scenario 2"),
  "level": LEVEL_INFO
}

MESSAGE["6.2"] = {
  "requirements": ["TG_Req#06"],
  "title": _("msg_title_006.2 more than one inspire_common:MetadataUrl"),
  "desc":  _("msg_desc_006.2 more than one inspire_common:MetadataUrl"),
  "level": LEVEL_ERROR
}

# Service Title
MESSAGE["10.0"] = {
  "requirements": ["TG_Req#10"],
  "title": _("msg_title_010.0 service title missing"),
  "desc":  _("msg_desc_010.0 service title missing"),
  "level": LEVEL_ERROR
}

# Service Abstract
MESSAGE["10.1"] = {
  "requirements": ["TG_Req#10"],
  "title": _("msg_title_010.1 service abstract missing"),
  "desc":  _("msg_desc_010.1 service abstract missing"),
  "level": LEVEL_ERROR
}

# Extended capabilities
MESSAGE["10.2"] = {
  "requirements": [],
  "title": _("msg_title_010.2 inspire_vs:ExtendedCapabilities missing"),
  "desc":  _("msg_desc_010.2 inspire_vs:ExtendedCapabilities missing"),
  "level": LEVEL_ERROR
}

MESSAGE["11"] = {
  "requirements": ["TG_Req#11"],
  "title": _("msg_title_011 inspire_common:ResourceType missing"),
  "desc":  _("msg_desc_011 inspire_common:ResourceType missing"),
  "level": LEVEL_ERROR
}

MESSAGE["11.1"] = {
  "requirements": ["TG_Req#11"],
  "title": _("msg_title_011.1 invalid inspire_common:ResourceType value"),
  "desc":  _("msg_desc_011.1 invalid inspire_common:ResourceType value"),
  "level": LEVEL_ERROR
}

# Extended capabilities - Spatial data service type
MESSAGE["15"] = {
  "requirements": ["TG_Req#15"],
  "title": _("msg_title_015 inspire_common:SpatialDataServiceType missing"),
  "desc":  _("msg_desc_015 inspire_common:SpatialDataServiceType missing"),
  "level": LEVEL_ERROR
}

MESSAGE["15.1"] = {
  "requirements": ["TG_Req#15"],
  "title": _("msg_title_015.1 invalid inspire_common:SpatialDataServiceType value"),
  "desc":  _("msg_desc_015.1 invalid inspire_common:SpatialDataServiceType value"),
  "level": LEVEL_ERROR
}

# infoMapAccessService keyword
MESSAGE["16"] = {
  "requirements": ["TG_Req#16", "TG_Req#17"],
  "title": _("msg_title_016 infoMapAccessService keyword"),
  "desc":  _("msg_desc_016 infoMapAccessService keyword"),
  "level": LEVEL_ERROR
}

# Extended capabilities - temporal reference
MESSAGE["20"] = {
  "requirements": ["TG_Req#20", "MD_Reg#5"],
  "title": _("msg_title_020 temporal reference subelement missing"),
  "desc":  _("msg_desc_020 temporal reference subelement missing"),
  "level": LEVEL_ERROR
}

MESSAGE["20.1"] = {
  "requirements": ["TG_Req#20"],
  "title": _("msg_title_020.1 temporal reference - date of last revision"),
  "desc":  _("msg_desc_0020.1 temporal reference - date of last revision"),
  "level": LEVEL_WARNING
}

MESSAGE["21"] = {
  "requirements": ["TG_Req#21"],
  "title": _("msg_title_021 temporal reference missing"),
  "desc":  _("msg_desc_021 temporal reference missing"),
  "level": LEVEL_ERROR
}

# Conformity
MESSAGE["22"] = {
  "requirements": ["TG_Req#22", "TG_Req#23"],
  "title": _("msg_title_022 conformity"),
  "desc":  _("msg_desc_022 conformity"),
  "level": LEVEL_ERROR
}

# wms:Fees
MESSAGE["24"] = {
  "requirements": ["TG_Req#10", "TG_Req#24"],
  "title": _("msg_title_024 wms:Fees missing"),
  "desc":  _("msg_desc_024 wms:Fees missing"),
  "level": LEVEL_ERROR
}

MESSAGE["24.1"] = {
  "requirements": ["TG_Req#24"],
  "title": _("msg_title_024.1 wms:Fees - no conditions apply - conditions unknown"),
  "desc":  _("msg_desc_024.1 wms:Fees - no conditions apply - conditions unknown"),
  "level": LEVEL_INFO
}

MESSAGE["24.2"] = {
  "requirements": ["TG_Req#24"],
  "title": _("msg_title_024.2 wms:Fees - none"),
  "desc":  _("msg_desc_024.2 wms:Fees - none"),
  "level": LEVEL_ERROR
}

# wms:AccessConstraints
MESSAGE["24.3"] = {
  "requirements": ["TG_Req#10"],
  "title": _("msg_title_024.3 wms:AccessConstraints missing"),
  "desc":  _("msg_desc_024.3 wms:AccessConstraints missing"),
  "level": LEVEL_ERROR
}

MESSAGE["24.4"] = {
  "requirements": ["TG_Rec#05"],
  "title": _("msg_title_024.4 unexpected wms:AccessConstraints value"),
  "desc":  _("msg_desc_024.4 unexpected wms:AccessConstraints value"),
  "level": LEVEL_WARNING
}

# wms:ContactOrganization
MESSAGE["25.1"] = {
  "requirements": ["TG_Req#25", "MD_Reg#9.1"],
  "title": _("msg_title_0025.1 wms:ContactOrganization missing"),
  "desc":  _("msg_desc_0025.1 wms:ContactOrganization missing"),
  "level": LEVEL_ERROR
}

# wms:ContactElectronicMailAddress
MESSAGE["25.2"] = {
  "requirements": ["TG_Req#25", "MD_Reg#9.1"],
  "title": _("msg_title_025.2 wms:ContactElectronicMailAddress missing"),
  "desc":  _("msg_desc_025.2 wms:ContactElectronicMailAddress missing"),
  "level": LEVEL_ERROR
}

# wms:ContactPosition
MESSAGE["26.1"] = {
  "requirements": ["TG_Req#25", "MD_Reg#9.2"],
  "title": _("msg_title_026.1 wms:ContactPosition missing"),
  "desc":  _("msg_desc_0026.1 wms:ContactPosition missing"),
  "level": LEVEL_ERROR
}

MESSAGE["26.2"] = {
  "requirements": ["TG_Req#26", "MD_Reg#9.2"],
  "title": _("msg_title_026.2 invalid wms:ContactPosition value"),
  "desc":  _("msg_desc_026.2 invalid wms:ContactPosition value"),
  "level": LEVEL_ERROR
}

# metadata point of contact
MESSAGE["27.1"] = {
  "requirements": ["TG_Req#27", "TG_Req#28"],
  "title": _("msg_title_027.1 inspire_common:MetadataPointOfContact - inspire_common:OrganisationName"),
  "desc":  _("msg_desc_027.1 inspire_common:MetadataPointOfContact - inspire_common:OrganisationName"),
  "level": LEVEL_ERROR
}

MESSAGE["27.2"] = {
  "requirements": ["TG_Req#27", "TG_Req#28"],
  "title": _("msg_title_027.2 inspire_common:MetadataPointOfContact - inspire_common:EmailAddress"),
  "desc":  _("msg_desc_027.2 inspire_common:MetadataPointOfContact - inspire_common:EmailAddress"),
  "level": LEVEL_ERROR
}

MESSAGE["29.1"] = {
  "requirements": ["TG_Req#29"],
  "title": _("msg_title_029.1 inspire_common:MetadataDate"),
  "desc":  _("msg_desc_029.1 inspire_common:MetadataDate"),
  "level": LEVEL_ERROR
}

# Layer title
MESSAGE["33.1"] = {
  "requirements": ["TG_Req#33"],
  "title": _("msg_title_033.1 layer title - not the expected title for this layer name"),
  "desc":  _("msg_desc_033.1 layer title - not the expected title for this layer name"),
  "level": LEVEL_ERROR
}

MESSAGE["33.2"] = {
  "requirements": ["TG_Req#33"],
  "title": _("msg_title_033.2 layer title - not a harmonised title"),
  "desc":  _("msg_desc_033.2 layer title - not a harmonised title"),
  "level": LEVEL_ERROR
}

# BBox CRS
MESSAGE["36"] = {
  "requirements": ["TG_Req#36"],
  "title": _("msg_title_036 layer bbox CRS"),
  "desc":  _("msg_desc_036 layer bbox CRS"),
  "level": LEVEL_ERROR
}

# Unique identifier 
MESSAGE["37.1"] = {
  "requirements": ["TG_Req#37"],
  "title": _("msg_title_037 unique identifier"),
  "desc":  _("msg_desc_037 unique identifier"),
  "level": LEVEL_ERROR
}

# Authority URL 
MESSAGE["38.1"] = {
  "requirements": ["TG_Req#38"],
  "title": _("msg_title_038 autority url"),
  "desc":  _("msg_desc_038 authority url"),
  "level": LEVEL_ERROR
}


# Layer name
MESSAGE["39.1"] = {
  "requirements": ["TG_Req#39"],
  "title": _("msg_title_039.1 layer name - not a harmonised name"),
  "desc":  _("msg_desc_039.1 layer name - not a harmonised name"),
  "level": LEVEL_ERROR
}

# Recommended CRS
MESSAGE["40.1"] = {
  "requirements": ["TG_Req#39"],
  "title": _("msg_title_040.1 recommended CRS"),
  "desc":  _("msg_desc_040.1 recommended CRS"),
  "level": LEVEL_WARNING
}

# Default style
MESSAGE["42.1"] = {
  "requirements": ["TG_Req#42"],
  "title": _("msg_title_042.1 default style missing"),
  "desc":  _("msg_desc_042.1 default style missing"),
  "level": LEVEL_ERROR
}


# LegendURL 
MESSAGE["47"] = {
  "requirements": ["TG_Req#47"],
  "title": _("msg_title_047 LegendURL missing"),
  "desc":  _("msg_desc_047 LegendURL missing"),
  "level": LEVEL_ERROR
}

# inspire_common:ResponseLanguage
MESSAGE["70.1"] = {
  "requirements": ["TG_Req#70"],
  "title": _("msg_title_070.1 inspire_common:ResponseLanguage missing"),
  "desc":  _("msg_desc_070.1 inspire_common:ResponseLanguage missing"),
  "level": LEVEL_ERROR
}

MESSAGE["70.2"] = {
  "requirements": ["TG_Req#70"],
  "title": _("msg_title_070.2 more than one inspire_common:ResponseLanguage"),
  "desc":  _("msg_desc_070.2 more than one inspire_common:ResponseLanguage"),
  "level": LEVEL_ERROR
}

MESSAGE["70.3"] = {
  "requirements": [],
  "title": _("msg_title_070.3 inspire_common:ResponseLanguage not in inspire_common:SupportedLanguages"),
  "desc":  _("msg_desc_070.3 inspire_common:ResponseLanguage not in inspire_common:SupportedLanguages"),
  "level": LEVEL_ERROR
}

# inspire_common:SupportedLanguages
MESSAGE["71.1"] = {
  "requirements": [],
  "title": _("msg_title_071.1 inspire_common:SupportedLanguages missing"),
  "desc":  _("msg_desc_071.1 inspire_common:SupportedLanguages missing"),
  "level": LEVEL_ERROR
}

MESSAGE["71.2"] = {
  "requirements": [],
  "title": _("msg_title_071.2 more than one inspire_common:SupportedLanguages"),
  "desc":  _("msg_desc_071.2 more than one inspire_common:SupportedLanguages"),
  "level": LEVEL_ERROR
}


MESSAGE["71.3"] = {
  "requirements": ["TG_Req#71"],
  "title": _("msg_title_071.3 inspire_common:DefaultLanguage missing"),
  "desc":  _("msg_desc_071.3 inspire_common:DefaultLanguage missing"),
  "level": LEVEL_ERROR
}

MESSAGE["71.4"] = {
  "requirements": ["TG_Req#71"],
  "title": _("msg_title_071.4 more than one inspire_common:DefaultLanguage"),
  "desc":  _("msg_desc_071.4 more than one inspire_common:DefaultLanguage"),
  "level": LEVEL_ERROR
}

MESSAGE["71.5"] = {
  "requirements": ["TG_Req#71"],
  "title": _("msg_title_071.5 inspire_common:DefaultLanguage in inspire_common:SupportedLanguage"),
  "desc":  _("msg_desc_071.5 inspire_common:DefaultLanguage in inspire_common:SupportedLanguage"),
  "level": LEVEL_ERROR
}

MESSAGE["71.6"] = {
  "requirements": ["TG_Req#68"],
  "title": _("msg_title_071.6 not a state member language"),
  "desc":  _("msg_desc_071.6 not a state member language"),
  "level": LEVEL_WARNING
}

MESSAGE["71.7"] = {
  "requirements": ["TG_Req#68"],
  "title": _("msg_title_071.7 not a 3 letter language"),
  "desc":  _("msg_desc_071.7 not a 3 letter language"),
  "level": LEVEL_ERROR
}
