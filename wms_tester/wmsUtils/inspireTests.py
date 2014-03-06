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

import xml.etree.ElementTree as etree
from django.utils.translation import ugettext as _

import testMessage

# ------------------------------------------------------------------------------

# Namespaces for element from INSPIRE technical guidances
NS_INSPIRE_COM = "{http://inspire.ec.europa.eu/schemas/common/1.0}"
NS_INSPIRE_VS = "{http://inspire.ec.europa.eu/schemas/inspire_vs/1.0}"
NS_WMS_130 = "{http://www.opengis.net/wms}"
NS_XSI = "{http://www.w3.org/2001/XMLSchema-instance}"

MEMBER_STATES_LANGUAGES = [ "bul", "cze", "dan", "dut", "eng", "est", "fin",
                            "fre", "ger", "gle", "gre", "hun", "ita", "lav",
                            "lit", "mlt", "pol", "por", "rum", "slo", "slv",
                            "spa", "swe"]

MD_RESTRICTION_CODES = [ "copyright", "patent", "patentPending",
                         "trademark", "license", "intellectualPropertyRights",
                         "restricted", "otherRestrictions"]

MD_CONDITIONS = ["no conditions apply","conditions unknown"]

MD_ROLES = [ "custodian", "owner", "user", "distributor", "originator",
             "pointOfContact", "principalInvestigator", "processor",
             "publisher", "author" ]

SERVICE_TYPES = [
  "humanInteractionService", "humanCatalogueViewer", "humanGeographicViewer",
"humanGeographicSpreadsheetViewer", "humanServiceEditor",
"humanChainDefinitionEditor", "humanWorkflowEnactmentManager",
"humanGeographicFeatureEditor", "humanGeographicSymbolEditor",
"humanFeatureGeneralizationEditor", "humanGeographicDataStructureViewer",
"infoManagementService", "infoFeatureAccessService",
"infoMapAccessService", "infoCoverageAccessService",
"infoSensorDescriptionService", "infoProductAccessService",
"infoFeatureTypeService", "infoCatalogueService",
"infoRegistryService", "infoGazetteerService",
"infoOrderHandlingService", "infoStandingOrderService",
"taskManagementService", "chainDefinitionService",
"workflowEnactmentService", "subscriptionService",
"spatialProcessingService", "spatialCoordinateConversionService",
"spatialCoordinateTransformationService",
"spatialCoverageVectorConversionService",
"spatialImageCoordinateConversionService",
"spatialRectificationService", "spatialOrthorectificationService",
"spatialSensorGeometryModelAdjustmentService",
"spatialImageGeometryModelConversionService",
"spatialSubsettingService", "spatialSamplingService",
"spatialTilingChangeService", "spatialDimensionMeasurementService",
"spatialFeatureManipulationService", "spatialFeatureMatchingService",
"spatialFeatureGeneralizationService", "spatialRouteDeterminationService",
"spatialPositioningService", "spatialProximityAnalysisService",
"thematicGoparameterCalculationService", "thematicClassificationService",
"thematicSubsettingService", "thematicSpatialCountingService",
"thematicChangeDetectionService",
"thematicGeographicInformationExtractionService",
"thematicImageProcessingService", "thematicReducedResolutionGenerationService",
"thematicImageManipulationService", "thematicImageUnderstandingService",
"thematicImageSynthesisService", "thematicObjectDetectionService",
"thematicGeoparsingService", "thematicGeocodingService",
"temporalProcessingService", "temporalReferenceSystemTransformationService",
"temporalSubsettingService", "temporalSamplingService",
"temporalProximityAnalysisService", "metadataProcessingService",
"metadataStatisticalCalculationService", "metadataGeographicAnnotationService",
"comService", "comEncodingService", "comTransferService",
"comGeographicCompressionService", "comGeographicFormatConversionService",
"comMessagingService", "comRemoteFileAndExecutableManagement"
]

INSPIRE_LAYERS = [
  {'language': 'bul', 'layers': [
    {'theme': u'Географски наименования', 'title': u'Географски наименования', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administrative Units', 'title': u'Административна единица', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administrative Units', 'title': u'Административна граница', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administrative Units', 'title': u'Кондоминиум', 'name': 'AU.Condominium'},
    {'theme': u'Administrative Units', 'title': u'Регион по NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Адреси', 'title': u'Адреси', 'name': 'AD.Address'},
    {'theme': u'Кадастрални парцели', 'title': u'Кадастрален парцел', 'name': 'CP.CadastralParcel'},
    {'theme': u'Кадастрални парцели', 'title': u'Кадастрално зониране', 'name': 'CP.CadastralZoning'},
    {'theme': u'Кадастрални парцели', 'title': u'Кадастрална граница', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Транспортни мрежи', 'title': u'Общ транспортен възел', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Транспортни мрежи', 'title': u'Обща транспортна връзка', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Транспортни мрежи', 'title': u'Обща транспортна зона', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Пътна връзка', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона за движение на превозни средства', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона за услуги за пътя', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Пътна зона', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Железопътна връзка', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на железопътна гара', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на железопътна разпределителна гара', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Железопътна зона', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Връзка на водни пътища', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на фарватер', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Пристанищна зона', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Въздушна връзка', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Транспортни мрежи', 'title': u'Летищна зона', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на писта', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на въздушно пространство', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на площадка', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Зона на път за рулиране', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Транспортни мрежи', 'title': u'Въжена връзка', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Хидрография', 'title': u'Водна маса', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Хидрография', 'title': u'Граница земя — вода', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Хидрография', 'title': u'Водосбор', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Хидрография', 'title': u'Хидрографска мрежа', 'name': 'HY.Network'},
    {'theme': u'Хидрография', 'title': u'Хидроточка, представляваща интерес', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Хидрография', 'title': u'Създаден от човека обект', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Хидрография', 'title': u'Бряг, мочурище', 'name': 'HY.HydroObject'},
    {'theme': u'Хидрография', 'title': u'Река по Рамковата директива за водите', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Хидрография', 'title': u'Езеро по Рамковата директива за водите', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Хидрография', 'title': u'Преходни води по Рамковата директива за водите', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Хидрография', 'title': u'Крайбрежни води по Рамковата директива за водите', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Хидрография', 'title': u'Океански регион', 'name': 'HY.OceanRegion'},
    {'theme': u'Защитени обекти', 'title': u'Защитени обекти', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'cze', 'layers': [
    {'theme': u'Zeměpisné názvy a jména', 'title': u'Zeměpisné názvy a jména', 'name': 'GN.GeographicalNames'},
    {'theme': u'Územní správní jednotky', 'title': u'Územní správní jednotka', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Územní správní jednotky', 'title': u'Správní hranice', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Územní správní jednotky', 'title': u'Kondominium', 'name': 'AU.Condominium'},
    {'theme': u'Územní správní jednotky', 'title': u'Region NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresa', 'title': u'Adresy', 'name': 'AD.Address'},
    {'theme': u'Parcely katastru nemovitostí', 'title': u'Parcela katastru nemovitostí', 'name': 'CP.CadastralParcel'},
    {'theme': u'Parcely katastru nemovitostí', 'title': u'Území členění – katastrální území', 'name': 'CP.CadastralZoning'},
    {'theme': u'Parcely katastru nemovitostí', 'title': u'Hranice parcely katastru nemovitostí', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Dopravní sítě', 'title': u'Obecný dopravní uzel', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Dopravní sítě', 'title': u'Obecná dopravní spojnice', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Dopravní sítě', 'title': u'Obecná oblast dopravy', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Dopravní sítě', 'title': u'Silniční spojnice', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast provozu vozidel', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast silniční služby', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Dopravní sítě', 'title': u'Koruna silnice', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Dopravní sítě', 'title': u'Spojnice kolejové dráhy', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast stanice kolejové dráhy', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast nákladní kolejové skupiny', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast kolejové dráhy', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Dopravní sítě', 'title': u'Spojnice vodní cesty', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast plavební dráhy', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast přístavu', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Dopravní sítě', 'title': u'Letecké spojení', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast letiště', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast dráhy', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast vzdušného prostoru', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast odbavovací plochy', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Dopravní sítě', 'title': u'Oblast pojezdové dráhy', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Dopravní sítě', 'title': u'Spojnice lanové dráhy', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Vodstvo', 'title': u'Vodní útvar', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Vodstvo', 'title': u'Hranice zátopy', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Vodstvo', 'title': u'Povodí', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Vodstvo', 'title': u'Hydrografická síť', 'name': 'HY.Network'},
    {'theme': u'Vodstvo', 'title': u'Hydrografický zájmový bod', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Vodstvo', 'title': u'Objekt vytvořený člověkem', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Vodstvo', 'title': u'Pobřeží, mokřad', 'name': 'HY.HydroObject'},
    {'theme': u'Vodstvo', 'title': u'Řeka podle rámcové směrnice o vodě', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Vodstvo', 'title': u'Jezero podle rámcové směrnice o vodě', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Vodstvo', 'title': u'Brakické vody podle rámcové směrnice o vodě', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Vodstvo', 'title': u'Pobřežní vody podle rámcové směrnice o vodě', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Vodstvo', 'title': u'Oblast oceánu', 'name': 'HY.OceanRegion'},
    {'theme': u'Chráněná území', 'title': u'Chráněná území', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'dan', 'layers': [
    {'theme': u'Stednavne', 'title': u'Stednavne', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administrative enheder', 'title': u'Administrativ enhed', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administrative enheder', 'title': u'Administrativ grænse', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administrative enheder', 'title': u'Kondominium', 'name': 'AU.Condominium'},
    {'theme': u'Administrative enheder', 'title': u'NUTS-region', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresser', 'title': u'Adresser', 'name': 'AD.Address'},
    {'theme': u'Matrikulære parceller', 'title': u'Matrikulær parcel', 'name': 'CP.CadastralParcel'},
    {'theme': u'Matrikulære parceller', 'title': u'Matrikulær zoneinddeling', 'name': 'CP.CadastralZoning'},
    {'theme': u'Matrikulære parceller', 'title': u'Matrikulær grænse', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transportnet', 'title': u'Generisk transportknude', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transportnet', 'title': u'Generisk transportforbindelse', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transportnet', 'title': u'Generisk transportområde', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transportnet', 'title': u'Vejstrækning', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transportnet', 'title': u'Færdselsareal', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transportnet', 'title': u'Vejserviceringsområde', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transportnet', 'title': u'Vejareal', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transportnet', 'title': u'Jernbaneforbindelse', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transportnet', 'title': u'Jernbanestationsområde', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transportnet', 'title': u'Rangerbanegårdsområde', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transportnet', 'title': u'Jernbaneområde', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transportnet', 'title': u'Farvandsforbindelse', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transportnet', 'title': u'Sejløbssareal', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transportnet', 'title': u'Havneområde', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transportnet', 'title': u'Luftfartsforbindelse', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transportnet', 'title': u'Flyvepladsområde', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transportnet', 'title': u'Landingsbaneområde', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transportnet', 'title': u'Luftrumsareal', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transportnet', 'title': u'Forpladsområde', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transportnet', 'title': u'Rullebaneområde', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transportnet', 'title': u'Kabelbaneforbindelse', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografi', 'title': u'Vandområde', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografi', 'title': u'Grænse mellem land og vand', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografi', 'title': u'Tilstrømning', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografi', 'title': u'Hydrografisk net', 'name': 'HY.Network'},
    {'theme': u'Hydrografi', 'title': u'Hydrografisk interessepunkt', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografi', 'title': u'Menneskeskabt objekt', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografi', 'title': u'Bred, vådområde', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografi', 'title': u'Vandløb i henhold til vandrammedirektivet', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografi', 'title': u'Sø i henhold til vandrammedirektivet', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografi', 'title': u'Overgangsvande i henhold til vandrammedirektivet', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografi', 'title': u'Kystvande i henhold til vandrammedirektivet', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografi', 'title': u'Oceanområde', 'name': 'HY.OceanRegion'},
    {'theme': u'Beskyttede lokaliteter', 'title': u'Beskyttede lokaliteter', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'dut', 'layers': [
    {'theme': u'Geografische namen', 'title': u'Geografische namen', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administratieve eenheden', 'title': u'Bestuurseenheid', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administratieve eenheden', 'title': u'Bestuursgrens', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administratieve eenheden', 'title': u'Condominium', 'name': 'AU.Condominium'},
    {'theme': u'Administratieve eenheden', 'title': u'NUTS-regio', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adressen', 'title': u'Adressen', 'name': 'AD.Address'},
    {'theme': u'Kadastrale percelen', 'title': u'Kadastraal perceel', 'name': 'CP.CadastralParcel'},
    {'theme': u'Kadastrale percelen', 'title': u'Kadastrale zonering', 'name': 'CP.CadastralZoning'},
    {'theme': u'Kadastrale percelen', 'title': u'Kadastrale grens', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Vervoersnetwerken', 'title': u'Generisch vervoersknooppunt', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Vervoersnetwerken', 'title': u'Generische vervoerslink', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Vervoersnetwerken', 'title': u'Generisch vervoersgebied', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Weglink', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Vervoersnetwerken', 'title': u'Voertuigverkeersgebied', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Pechstrook', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Weggebied', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Spoorweglink', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Vervoersnetwerken', 'title': u'Spoorwegstationgebied', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Spoorwegterreingebied', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Spoorweggebied', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Waterweglink', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Vervoersnetwerken', 'title': u'Vaargeulgebied', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Havengebied', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Luchtverbinding', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Vervoersnetwerken', 'title': u'Luchthavengebied', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Start-/landingsbaan', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Luchtruimgebied', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Parkeerplatformgebied', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Taxibaan', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Vervoersnetwerken', 'title': u'Kabelbaanlink', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografie', 'title': u'Waterlichaam', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografie', 'title': u'Land-watergrens', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografie', 'title': u'Stroomgebied', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografie', 'title': u'Hydrografisch netwerk', 'name': 'HY.Network'},
    {'theme': u'Hydrografie', 'title': u'Nuttige hydroplaats', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografie', 'title': u'Door de mens gemaakt object', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografie', 'title': u'Kust, watergebied', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografie', 'title': u'KRW-rivier', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografie', 'title': u'KRW-meer', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografie', 'title': u'KRW-overgangswater', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografie', 'title': u'KRW-kustwater', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografie', 'title': u'Oceaangebied', 'name': 'HY.OceanRegion'},
    {'theme': u'Beschermde gebieden', 'title': u'Beschermde gebieden', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'eng', 'layers': [
    {'theme': u'Geographical Names', 'title': u'Geographical Names', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administrative Units', 'title': u'Administrative unit', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administrative Units', 'title': u'Administrative boundary', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administrative Units', 'title': u'Condominium', 'name': 'AU.Condominium'},
    {'theme': u'Administrative Units', 'title': u'NUTS Region', 'name': 'AU.NUTSRegion'},
    {'theme': u'Addresses', 'title': u'Addresses', 'name': 'AD.Address'},
    {'theme': u'Cadastral Parcels', 'title': u'Cadastral Parcel', 'name': 'CP.CadastralParcel'},
    {'theme': u'Cadastral Parcels', 'title': u'Cadastral Zoning', 'name': 'CP.CadastralZoning'},
    {'theme': u'Cadastral Parcels', 'title': u'Cadastral Boundary', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transport networks', 'title': u'Generic Transport Node', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transport networks', 'title': u'Generic Transport Link', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transport networks', 'title': u'Generic Transport Area', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transport networks', 'title': u'Road Link', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transport networks', 'title': u'Vehicle traffic Area', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transport networks', 'title': u'Road Service Area', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transport networks', 'title': u'Road Area', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transport networks', 'title': u'Railway Link', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transport networks', 'title': u'Railway Station Area', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transport networks', 'title': u'Railway Yard Area', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transport networks', 'title': u'Railway Area', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transport networks', 'title': u'Waterway Link', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transport networks', 'title': u'Fairway Area', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transport networks', 'title': u'Port Area', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transport networks', 'title': u'Air Link', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transport networks', 'title': u'Aerodrome Area', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transport networks', 'title': u'Runway Area', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transport networks', 'title': u'Airspace Area', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transport networks', 'title': u'Apron Area', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transport networks', 'title': u'Taxiway Area', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transport networks', 'title': u'Cableway Link', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrography', 'title': u'Waterbody', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrography', 'title': u'Land-Water Boundary', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrography', 'title': u'Catchment', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrography', 'title': u'Hydrographic Network', 'name': 'HY.Network'},
    {'theme': u'Hydrography', 'title': u'Hydro Point of Interest', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrography', 'title': u'Man-made Object', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrography', 'title': u'Shore, Wetland', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrography', 'title': u'WFD-River', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrography', 'title': u'WFD-Lake', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrography', 'title': u'WFD-Transitional water', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrography', 'title': u'WFD-Coastal water', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrography', 'title': u'Ocean Region', 'name': 'HY.OceanRegion'},
    {'theme': u'Protected Sites', 'title': u'Protected Sites', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'est', 'layers': [
    {'theme': u'Kohanimed kihid', 'title': u'Kohanimed', 'name': 'GN.GeographicalNames'},
    {'theme': u'Haldusüksused kihid', 'title': u'Haldusüksus', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Haldusüksused kihid', 'title': u'Halduspiir', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Haldusüksused kihid', 'title': u'Kondomiinium', 'name': 'AU.Condominium'},
    {'theme': u'Haldusüksused kihid', 'title': u'NUTSi piirkond', 'name': 'AU.NUTSRegion'},
    {'theme': u'Aadressid kihid', 'title': u'Aadressid', 'name': 'AD.Address'},
    {'theme': u'Katastriüksused kihid', 'title': u'Katastriüksus', 'name': 'CP.CadastralParcel'},
    {'theme': u'Katastriüksused kihid', 'title': u'Katastripiirkond', 'name': 'CP.CadastralZoning'},
    {'theme': u'Katastriüksused kihid', 'title': u'Katastriüksuse piir', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Üldine transpordisõlm', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Üldine transpordilink', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Üldine transpordipind', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Teelink', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Sõidukite liiklemisala', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Tee-teenindusala', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Tee-ala', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Raudteelink', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Raudteejaamaala', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Rongide sorteerimisjaama ala', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Raudtee-ala', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Veeteelink', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Faarvaatriala', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Sadamaala', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Lennulink', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Lennuväljaala', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Lennurajaala', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Õhuruumiala', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Perrooniala', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Ruleerimistee-ala', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transpordivõrgud kihid', 'title': u'Köisteelink', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Veekogu', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Maa ja vee piir', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Valgala', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Hüdrograafiline võrk', 'name': 'HY.Network'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Hüdrograafiline huvipunkt', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Inimtekkeline objekt', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Kallas, märgala', 'name': 'HY.HydroObject'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Veepoliitika raamdirektiivi kohane jõgi', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Veepoliitika raamdirektiivi kohane järv', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Veepoliitika raamdirektiivi kohane üleminekuvesi', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Veepoliitika raamdirektiivi kohane rannikuvesi', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hüdrograafia kihid', 'title': u'Ookeanipiirkond', 'name': 'HY.OceanRegion'},
    {'theme': u'Kaitsealused kohad kihid', 'title': u'Kaitsealused kohad', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'fin', 'layers': [
    {'theme': u'Paikannimet', 'title': u'Paikannimet', 'name': 'GN.GeographicalNames'},
    {'theme': u'Hallinnolliset yksiköt', 'title': u'Hallintoyksikkö', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Hallinnolliset yksiköt', 'title': u'Hallinnollinen raja', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Hallinnolliset yksiköt', 'title': u'Yhteishallintoalue', 'name': 'AU.Condominium'},
    {'theme': u'Hallinnolliset yksiköt', 'title': u'NUTS-alue', 'name': 'AU.NutsRegion'},
    {'theme': u'Osoitteet', 'title': u'Osoitteet', 'name': 'AD.Address'},
    {'theme': u'Kiinteistöt', 'title': u'Palsta', 'name': 'CP.CadastralParcel'},
    {'theme': u'Kiinteistöt', 'title': u'Palstojen ryhmittelyalue', 'name': 'CP.CadastralZoning'},
    {'theme': u'Kiinteistöt', 'title': u'Kiinteistöraja', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Liikenneverkot', 'title': u'Geneerinen liikennesolmupiste', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Liikenneverkot', 'title': u'Geneerinen liikennelinkki', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Liikenneverkot', 'title': u'Geneerinen liikennealue', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Liikenneverkot', 'title': u'Tielinkki', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Liikenneverkot', 'title': u'Ajoneuvoliikennealue', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Liikenneverkot', 'title': u'Tiepalvelualue', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Liikenneverkot', 'title': u'Tiealue', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Liikenneverkot', 'title': u'Raidelinkki', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Liikenneverkot', 'title': u'Rautatieasema-alue', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Liikenneverkot', 'title': u'Ratapiha-alue', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Liikenneverkot', 'title': u'Raidealue', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Liikenneverkot', 'title': u'Vesitielinkki', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Liikenneverkot', 'title': u'Väyläalue', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Liikenneverkot', 'title': u'Satama-alue', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Liikenneverkot', 'title': u'Ilmalinkki', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Liikenneverkot', 'title': u'Lentopaikka-alue', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Liikenneverkot', 'title': u'Kiitotiealue', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Liikenneverkot', 'title': u'Ilmatila-alue', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Liikenneverkot', 'title': u'Asematasoalue', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Liikenneverkot', 'title': u'Rullausalue', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Liikenneverkot', 'title': u'Kaapelitielinkki', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografia', 'title': u'Vaka- ja virtavedet', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografia', 'title': u'Rantaviiva', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografia', 'title': u'Valuma-alue', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografia', 'title': u'Hydrografinen verkosto', 'name': 'HY.Network'},
    {'theme': u'Hydrografia', 'title': u'Vesistön erityiskohde', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografia', 'title': u'Vesirakenne', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografia', 'title': u'Ranta, kosteikko', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografia', 'title': u'VPD Joki', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografia', 'title': u'VPD Järvi', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografia', 'title': u'VPD Jokisuun vaihettumisalue', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografia', 'title': u'VPD Rannikkovesi', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografia', 'title': u'Valtamerialue', 'name': 'HY.OceanRegion'},
    {'theme': u'Suojellut alueet', 'title': u'Suojelukohteet', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'fre', 'layers': [
    {'theme': u'Dénominations géographiques', 'title': u'Dénominations géographiques', 'name': 'GN.GeographicalNames'},
    {'theme': u'Unités administratives', 'title': u'Unité administrative', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Unités administratives', 'title': u'Limite administrative', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Unités administratives', 'title': u'Condominium', 'name': 'AU.Condominium'},
    {'theme': u'Unités administratives', 'title': u'Région NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresses', 'title': u'ADRESSES', 'name': 'AD.ADDRESS'},
    {'theme': u'Parcelles cadastrales', 'title': u'Parcelle cadastrale', 'name': 'CP.CadastralParcel'},
    {'theme': u'Parcelles cadastrales', 'title': u'Zonage cadastral', 'name': 'CP.CadastralZoning'},
    {'theme': u'Parcelles cadastrales', 'title': u'Limite cadastrale', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Réseaux de transport', 'title': u'Nœud de transport générique', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Réseaux de transport', 'title': u'Tronçon de transport générique', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de transport générique', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Réseaux de transport', 'title': u'Tronçon de route', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de circulation des véhicules', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de service routier', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de route', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Réseaux de transport', 'title': u'Tronçon de voie ferrée', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de gare ferroviaire', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de gare de triage', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de voie ferrée', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Réseaux de transport', 'title': u'Tronçon de voie navigable', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Réseaux de transport', 'title': u'Chenal de navigation', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire portuaire', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Réseaux de transport', 'title': u'Tronçon de voie aérienne', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Réseaux de transport', 'title': u'Aire d\'aérodrome', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de piste', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Réseaux de transport', 'title': u'Zone d\'espace aérien', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de trafic', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Réseaux de transport', 'title': u'Aire de circulation', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Réseaux de transport', 'title': u'Tronçon de voie câblée', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrographie', 'title': u'Masse d\'eau', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrographie', 'title': u'Limite terre-eau', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrographie', 'title': u'Bassin versant', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrographie', 'title': u'Réseau hydrographique', 'name': 'HY.Network'},
    {'theme': u'Hydrographie', 'title': u'Point d\'intérêt hydrographique', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrographie', 'title': u'Objet artificiel', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrographie', 'title': u'Rivage, zone humide', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrographie', 'title': u'Rivière DCE', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrographie', 'title': u'Lac DCE', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrographie', 'title': u'Eaux de transition DCE', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrographie', 'title': u'Eaux côtières DCE', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrographie', 'title': u'Région océanique', 'name': 'HY.OceanRegion'},
    {'theme': u'Sites protégés', 'title': u'Sites protégés', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'ger', 'layers': [
    {'theme': u'Geografische Bezeichnungen', 'title': u'Geografische Bezeichnungen', 'name': 'GN.GeographicalNames'},
    {'theme': u'Verwaltungseinheiten', 'title': u'Verwaltungseinheit', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Verwaltungseinheiten', 'title': u'Verwaltungsgrenze', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Verwaltungseinheiten', 'title': u'Kondominium', 'name': 'AU.Condominium'},
    {'theme': u'Verwaltungseinheiten', 'title': u'NUTS-Region', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adressen', 'title': u'Adressen', 'name': 'AD.Address'},
    {'theme': u'Flurstücke/Grundstücke (Katasterparzellen)', 'title': u'Flurstück', 'name': 'CP.CadastralParcel'},
    {'theme': u'Flurstücke/Grundstücke (Katasterparzellen)', 'title': u'Katasterbezirk', 'name': 'CP.CadastralZoning'},
    {'theme': u'Flurstücke/Grundstücke (Katasterparzellen)', 'title': u'Flurstücksgrenze', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Verkehrsnetze', 'title': u'Generischer Verkehrsknotenpunkt', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Verkehrsnetze', 'title': u'Generisches Verkehrssegment', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Verkehrsnetze', 'title': u'Generischer Verkehrsbereich', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Straßensegment', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Verkehrsnetze', 'title': u'Verkehrsfläche', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Servicebereich', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Straßenfläche', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Eisenbahnverbindung', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Verkehrsnetze', 'title': u'Bahnhofsgelände', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Rangierbahnhofsgelände', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Bahngelände', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Wasserstraßenverbindung', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Verkehrsnetze', 'title': u'Fahrrinnenbereich', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Hafengelände', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Luftverbindung', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Verkehrsnetze', 'title': u'Flugplatzgelände', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Landebahngelände', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Luftraumbereich', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Vorfeldgelände', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Rollfeld', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Verkehrsnetze', 'title': u'Seilbahnverbindung', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografie', 'title': u'Gewässer', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografie', 'title': u'Uferlinie', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografie', 'title': u'Einzugsgebiet', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografie', 'title': u'Hydrografisches Netzwerk', 'name': 'HY.Network'},
    {'theme': u'Hydrografie', 'title': u'Interessanter hydrologischer Punkt', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografie', 'title': u'Bauwerk am Gewässer', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografie', 'title': u'Küste, Feuchtgebiet', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografie', 'title': u'WRRL-Fließgewässer', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografie', 'title': u'WRRL-See', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografie', 'title': u'WRRL-Übergangsgewässer', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografie', 'title': u'WRRL-Küstengewässer', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografie', 'title': u'Ozeanische Region', 'name': 'HY.OceanRegion'},
    {'theme': u'Schutzgebiete', 'title': u'Schutzgebiete', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'gle', 'layers': [
    {'theme': u'Geographical Names', 'title': u'Geographical Names', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administrative Units', 'title': u'Administrative unit', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administrative Units', 'title': u'Administrative boundary', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administrative Units', 'title': u'Condominium', 'name': 'AU.Condominium'},
    {'theme': u'Administrative Units', 'title': u'NUTS Region', 'name': 'AU.NUTSRegion'},
    {'theme': u'Addresses', 'title': u'Addresses', 'name': 'AD.Address'},
    {'theme': u'Cadastral Parcels', 'title': u'Cadastral Parcel', 'name': 'CP.CadastralParcel'},
    {'theme': u'Cadastral Parcels', 'title': u'Cadastral Zoning', 'name': 'CP.CadastralZoning'},
    {'theme': u'Cadastral Parcels', 'title': u'Cadastral Boundary', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transport networks', 'title': u'Generic Transport Node', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transport networks', 'title': u'Generic Transport Link', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transport networks', 'title': u'Generic Transport Area', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transport networks', 'title': u'Road Link', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transport networks', 'title': u'Vehicle traffic Area', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transport networks', 'title': u'Road Service Area', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transport networks', 'title': u'Road Area', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transport networks', 'title': u'Railway Link', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transport networks', 'title': u'Railway Station Area', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transport networks', 'title': u'Railway Yard Area', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transport networks', 'title': u'Railway Area', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transport networks', 'title': u'Waterway Link', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transport networks', 'title': u'Fairway Area', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transport networks', 'title': u'Port Area', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transport networks', 'title': u'Air Link', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transport networks', 'title': u'Aerodrome Area', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transport networks', 'title': u'Runway Area', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transport networks', 'title': u'Airspace Area', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transport networks', 'title': u'Apron Area', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transport networks', 'title': u'Taxiway Area', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transport networks', 'title': u'Cableway Link', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrography', 'title': u'Waterbody', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrography', 'title': u'Land-Water Boundary', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrography', 'title': u'Catchment', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrography', 'title': u'Hydrographic Network', 'name': 'HY.Network'},
    {'theme': u'Hydrography', 'title': u'Hydro Point of Interest', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrography', 'title': u'Man-made Object', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrography', 'title': u'Shore, Wetland', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrography', 'title': u'WFD-River', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrography', 'title': u'WFD-Lake', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrography', 'title': u'WFD-Transitional water', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrography', 'title': u'WFD-Coastal water', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrography', 'title': u'Ocean Region', 'name': 'HY.OceanRegion'},
    {'theme': u'Protected Sites', 'title': u'Protected Sites', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'gre', 'layers': [
    {'theme': u'Τοπωνύμια', 'title': u'Τοπωνύμια', 'name': 'GN.GeographicalNames'},
    {'theme': u'Διοικητικές ενότητες', 'title': u'Διοικητική ενότητα', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Διοικητικές ενότητες', 'title': u'Διοικητικό όριο', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Διοικητικές ενότητες', 'title': u'Συγκυριαρχία', 'name': 'AU.Condominium'},
    {'theme': u'Διοικητικές ενότητες', 'title': u'Περιφέρεια NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Διευθύνσεις', 'title': u'Διευθύνσεις', 'name': 'AD.Address'},
    {'theme': u'Γεωτεμάχια κτηματολογίου', 'title': u'Γεωτεμάχιο κτηματολογίου', 'name': 'CP.CadastralParcel'},
    {'theme': u'Γεωτεμάχια κτηματολογίου', 'title': u'Κτηματολογικοί τομείς/ενότητες', 'name': 'CP.CadastralZoning'},
    {'theme': u'Γεωτεμάχια κτηματολογίου', 'title': u'Κτηματολογικό όριο', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Γενικός κόμβος μεταφορών', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Γενικός σύνδεσμος μεταφορών', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Γενική επιφάνεια μεταφορών', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Οδικός σύνδεσμος', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Επιφάνεια κυκλοφορίας οχημάτων', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Χώρος οδικής εξυπηρέτησης', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Επιφάνεια οδού', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Σιδηροδρομικός σύνδεσμος', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Επιφάνεια σιδηροδρομικού σταθμού', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Επιφάνεια σιδηροδρομικού σταθμού διαλογής', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Επιφάνεια σιδηροδρομικής γραμμής', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Σύνδεσμος πλωτών οδών', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Δίαυλος ναυσιπλοΐας', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Έκταση λιμένα', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Εναέριος σύνδεσμος', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Έκταση αεροδρομίου', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Έκταση διαδρόμου προσαπογείωσης', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Επιφάνεια εναέριου χώρου', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Χώρος στάθμευσης αεροσκαφών', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Χώρος τροχοδρόμου', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Δίκτυα μεταφορών', 'title': u'Σύνδεσμος εναέριου σιδηροδρόμου', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Υδρογραφία', 'title': u'Υδάτινη μάζα', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Υδρογραφία', 'title': u'Όριο ξηράς-υδάτων', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Υδρογραφία', 'title': u'Λεκάνη απορροής', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Υδρογραφία', 'title': u'Υδρογραφικό δίκτυο', 'name': 'HY.Network'},
    {'theme': u'Υδρογραφία', 'title': u'Υδρογραφικό σημείο ενδιαφέροντος', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Υδρογραφία', 'title': u'Τεχνητό αντικείμενο', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Υδρογραφία', 'title': u'Ακτή, υγρότοπος', 'name': 'HY.HydroObject'},
    {'theme': u'Υδρογραφία', 'title': u'Ποταμός ΟΠΥ', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Υδρογραφία', 'title': u'Λίμνη ΟΠΥ', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Υδρογραφία', 'title': u'Μεταβατικά ύδατα ΟΠΥ', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Υδρογραφία', 'title': u'Παράκτια ύδατα ΟΠΥ', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Υδρογραφία', 'title': u'Περιοχή ωκεανού', 'name': 'HY.OceanRegion'},
    {'theme': u'Προστατευόμενες περιοχές', 'title': u'Προστατευόμενες περιοχές', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'hun', 'layers': [
    {'theme': u'Földrajzi nevek téradattéma rétege', 'title': u'Földrajzi nevek', 'name': 'GN.GeographicalNames'},
    {'theme': u'Közigazgatási egységek', 'title': u'Közigazgatási egység', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Közigazgatási egységek', 'title': u'Közigazgatási határ', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Közigazgatási egységek', 'title': u'Kondomínium', 'name': 'AU.Condominium'},
    {'theme': u'Közigazgatási egységek', 'title': u'NUTS-régió', 'name': 'AU.NUTSRegion'},
    {'theme': u'Címek', 'title': u'Címek', 'name': 'AD.Address'},
    {'theme': u'Kataszteri parcellák', 'title': u'Kataszteri parcella', 'name': 'CP.CadastralParcel'},
    {'theme': u'Kataszteri parcellák', 'title': u'Kataszteri földterület-besorolás', 'name': 'CP.CadastralZoning'},
    {'theme': u'Kataszteri parcellák', 'title': u'Kataszteri határ', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Általános közlekedési csomópont', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Általános közlekedési kapcsolat', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Általános közlekedési terület', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Közúti kapcsolat', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Járműforgalmi terület', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Közúti szolgálati terület', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Közúti terület', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Vasúti kapcsolat', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Vasúti állomásterület', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Teherpályaudvar-terület', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Vasúti terület', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Hajóúti kapcsolat', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Hajóútterület', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Kikötőterület', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Légi kapcsolat', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Repülőtéri terület', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Kifutóterület', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Légtérterület', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Forgalmielőtér-terület', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Gurulóút-terület', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Közlekedési hálózatok', 'title': u'Kötélpálya-kapcsolat', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Vízrajz', 'title': u'Víztest', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Vízrajz', 'title': u'Föld–víz határ', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Vízrajz', 'title': u'Vízgyűjtő', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Vízrajz', 'title': u'Vízrajzi hálózat', 'name': 'HY.Network'},
    {'theme': u'Vízrajz', 'title': u'Fontos vízrajzi pont', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Vízrajz', 'title': u'Épített objektum', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Vízrajz', 'title': u'Part, vizes élőhely', 'name': 'HY.HydroObject'},
    {'theme': u'Vízrajz', 'title': u'Vízügyi keretirányelv szerinti folyó', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Vízrajz', 'title': u'Vízügyi keretirányelv szerinti tó', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Vízrajz', 'title': u'Vízügyi keretirányelv szerinti átmeneti víz', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Vízrajz', 'title': u'Vízügyi keretirányelv szerinti parti tengervizek', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Vízrajz', 'title': u'Óceáni régió', 'name': 'HY.OceanRegion'},
    {'theme': u'Védett helyek', 'title': u'Védett helyek', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'ita', 'layers': [
    {'theme': u'geografici', 'title': u'Nomi geografici', 'name': 'GN.GeographicalNames'},
    {'theme': u'Unità amministrative', 'title': u'Unità amministrativa', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Unità amministrative', 'title': u'Confine amministrativo', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Unità amministrative', 'title': u'Condominium', 'name': 'AU.Condominium'},
    {'theme': u'Unità amministrative', 'title': u'Regione NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Indirizzi', 'title': u'Indirizzi', 'name': 'AD.Address'},
    {'theme': u'Parcels', 'title': u'Parcella catastale', 'name': 'CP.CadastralParcel'},
    {'theme': u'Parcels', 'title': u'Zonizzazione catastale', 'name': 'CP.CadastralZoning'},
    {'theme': u'Parcels', 'title': u'Confine catastale', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Reti di trasporto', 'title': u'Nodo di trasporto generico', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Reti di trasporto', 'title': u'Collegamento di trasporto generico', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Reti di trasporto', 'title': u'Area di trasporto generico', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Reti di trasporto', 'title': u'Collegamento stradale', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Reti di trasporto', 'title': u'Area di circolazione di veicoli', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area di servizio stradale', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area della strada', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Reti di trasporto', 'title': u'Collegamento ferroviario', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Reti di trasporto', 'title': u'Area di stazione ferroviaria', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area di scalo ferroviario', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area ferroviaria', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Reti di trasporto', 'title': u'Collegamento di vie di navigazione', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Reti di trasporto', 'title': u'Area di corridoio di navigazione', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area portuale', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Reti di trasporto', 'title': u'Collegamento aereo', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Reti di trasporto', 'title': u'Area di aerodromo', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Reti di trasporto', 'title': u'Zona di pista', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area di spazio aereo', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area di movimento', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Reti di trasporto', 'title': u'Area di rullaggio', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Reti di trasporto', 'title': u'Collegamento a fune', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Idrografia', 'title': u'Corpo idrico', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Idrografia', 'title': u'Confine terra-acqua', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Idrografia', 'title': u'Bacino', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Idrografia', 'title': u'Rete idrografica', 'name': 'HY.Network'},
    {'theme': u'Idrografia', 'title': u'Punto di interesse idrografico', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Idrografia', 'title': u'Oggetto artificiale', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Idrografia', 'title': u'Riva, zona umida', 'name': 'HY.HydroObject'},
    {'theme': u'Idrografia', 'title': u'Fiume-DQA', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Idrografia', 'title': u'Lago-DQA', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Idrografia', 'title': u'Acque di transizione-DQA', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Idrografia', 'title': u'Acqua costiera-DQA', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Idrografia', 'title': u'Regione oceanica', 'name': 'HY.OceanRegion'},
    {'theme': u'Protected Sites', 'title': u'Siti protetti', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'lav', 'layers': [
    {'theme': u'Toponīmi', 'title': u'Ģeogrāfiskie nosaukumi', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administratīvas vienības', 'title': u'Administratīvā vienība', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administratīvas vienības', 'title': u'Administratīvā robeža', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administratīvas vienības', 'title': u'Kondomināts', 'name': 'AU.Condominium'},
    {'theme': u'Administratīvas vienības', 'title': u'NUTS reģions', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adreses', 'title': u'Adreses', 'name': 'AD.Address'},
    {'theme': u'Kadastrālie zemes gabali', 'title': u'Kadastrālais zemes gabals', 'name': 'CP.CadastralParcel'},
    {'theme': u'Kadastrālie zemes gabali', 'title': u'Kadastrālais zonējums', 'name': 'CP.CadastralZoning'},
    {'theme': u'Kadastrālie zemes gabali', 'title': u'Kadastrālā robeža', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transporta tīkli', 'title': u'Vispārējs transporta mezglpunkts', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transporta tīkli', 'title': u'Vispārējs transporta posms', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transporta tīkli', 'title': u'Vispārēja transporta teritorija', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transporta tīkli', 'title': u'Autoceļa posms', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transporta tīkli', 'title': u'Transportlīdzekļu satiksmes zona', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transporta tīkli', 'title': u'Autoceļa apkalpes zona', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transporta tīkli', 'title': u'Autoceļa teritorija', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transporta tīkli', 'title': u'Dzelzceļa posms', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transporta tīkli', 'title': u'Dzelzceļa stacijas teritorija', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transporta tīkli', 'title': u'Vagonu parka teritorija', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transporta tīkli', 'title': u'Dzelzceļa teritorija', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transporta tīkli', 'title': u'Ūdensceļa posms', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transporta tīkli', 'title': u'Kuģu ceļa teritorija', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transporta tīkli', 'title': u'Ostas teritorija', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transporta tīkli', 'title': u'Gaisa transporta posms', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transporta tīkli', 'title': u'Lidlauka teritorija', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transporta tīkli', 'title': u'Skrejceļa teritorija', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transporta tīkli', 'title': u'Gaisa telpas teritorija', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transporta tīkli', 'title': u'Lidlauka perona teritorija', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transporta tīkli', 'title': u'Manevrēšanas zona', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transporta tīkli', 'title': u'Trošu ceļa posms', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hidrogrāfija', 'title': u'Ūdens objekts', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hidrogrāfija', 'title': u'Sauszemes un ūdens robeža', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hidrogrāfija', 'title': u'Sateces baseins', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hidrogrāfija', 'title': u'Hidrogrāfiskais tīkls', 'name': 'HY.Network'},
    {'theme': u'Hidrogrāfija', 'title': u'Hidrogrāfiski ievērojams punkts', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hidrogrāfija', 'title': u'Cilvēka veidots objekts', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hidrogrāfija', 'title': u'Krasts, mitrājs', 'name': 'HY.HydroObject'},
    {'theme': u'Hidrogrāfija', 'title': u'ŪPD upe', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hidrogrāfija', 'title': u'ŪPD ezers', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hidrogrāfija', 'title': u'ŪPD pārejas ūdeņi', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hidrogrāfija', 'title': u'ŪPD piekrastes ūdeņi', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hidrogrāfija', 'title': u'Okeāna reģions', 'name': 'HY.OceanRegion'},
    {'theme': u'Aizsargājamas teritorijas', 'title': u'Aizsargājamas teritorijas', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'lit', 'layers': [
    {'theme': u'Geografiniai pavadinimai', 'title': u'Geografiniai pavadinimai', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administraciniai vienetai', 'title': u'Administracinis vienetas', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administraciniai vienetai', 'title': u'Administracinė riba', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administraciniai vienetai', 'title': u'Kondominiumas', 'name': 'AU.Condominium'},
    {'theme': u'Administraciniai vienetai', 'title': u'NUTS regionas', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresai', 'title': u'Adresai', 'name': 'AD.Address'},
    {'theme': u'Kadastro sklypai', 'title': u'Kadastro sklypas', 'name': 'CP.CadastralParcel'},
    {'theme': u'Kadastro sklypai', 'title': u'Kadastrinės zonos', 'name': 'CP.CadastralZoning'},
    {'theme': u'Kadastro sklypai', 'title': u'Kadastro sklypo riba', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transporto tinklai', 'title': u'Bendrasis transporto mazgas', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transporto tinklai', 'title': u'Bendroji transporto sąsaja', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transporto tinklai', 'title': u'Bendroji transporto zona', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transporto tinklai', 'title': u'Kelio sąsaja', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transporto tinklai', 'title': u'Transporto priemonių eismo zona', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transporto tinklai', 'title': u'Kelio paslaugų zona', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transporto tinklai', 'title': u'Kelio zona', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transporto tinklai', 'title': u'Geležinkelio sąsaja', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transporto tinklai', 'title': u'Geležinkelio stoties zona', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transporto tinklai', 'title': u'Rūšiavimo (manevravimo) stoties zona', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transporto tinklai', 'title': u'Geležinkelio zona', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transporto tinklai', 'title': u'Vandens kelio sąsaja', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transporto tinklai', 'title': u'Farvaterio zona', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transporto tinklai', 'title': u'Uosto zona', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transporto tinklai', 'title': u'Oro sąsaja', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transporto tinklai', 'title': u'Aerodromo zona', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transporto tinklai', 'title': u'Kilimo ir tūpimo tako zona', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transporto tinklai', 'title': u'Oro erdvės zona', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transporto tinklai', 'title': u'Perono zona', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transporto tinklai', 'title': u'Riedėjimo tako zona', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transporto tinklai', 'title': u'Lynų kelio sąsaja', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hidrografija', 'title': u'Vandens telkinys', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hidrografija', 'title': u'Sausumos ir vandens riba', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hidrografija', 'title': u'Baseinas', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hidrografija', 'title': u'Hidrografinis tinklas', 'name': 'HY.Network'},
    {'theme': u'Hidrografija', 'title': u'Ypač svarbus hidrografinis taškas', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hidrografija', 'title': u'Dirbtinis objektas', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hidrografija', 'title': u'Krantas, pelkė', 'name': 'HY.HydroObject'},
    {'theme': u'Hidrografija', 'title': u'BVPD – upė', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hidrografija', 'title': u'BVPD – ežeras', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hidrografija', 'title': u'BVPD – tarpiniai vandenys', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hidrografija', 'title': u'BVPD – pakrančių vanduo', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hidrografija', 'title': u'Vandenyno regionas', 'name': 'HY.OceanRegion'},
    {'theme': u'Saugomos teritorijos', 'title': u'Saugomos teritorijos', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'mlt', 'layers': [
    {'theme': u'Ismijiet Ġeografiċi', 'title': u'ISMIJIET ĠEOGRAFIĊI', 'name': 'GN.GEOGRAPHICALNAMES'},
    {'theme': u'Unitajiet Amministrattivi', 'title': u'UNITÀ AMMINISTRATTIVA', 'name': 'AU.ADMINISTRATIVEUNIT'},
    {'theme': u'Unitajiet Amministrattivi', 'title': u'LIMITU AMMINISTRATTIV', 'name': 'AU.ADMINISTRATIVEBOUNDARY'},
    {'theme': u'Unitajiet Amministrattivi', 'title': u'CONDOMINIUM', 'name': 'AU.CONDOMINIUM'},
    {'theme': u'Unitajiet Amministrattivi', 'title': u'REĠJUN NUTS', 'name': 'AU.NUTSREGION'},
    {'theme': u'Addresses', 'title': u'INDIRIZZI', 'name': 'AD.ADDRESS'},
    {'theme': u'CadastralParcels', 'title': u'MEDDA KATASTALI', 'name': 'CP.CADASTRALPARCEL'},
    {'theme': u'CadastralParcels', 'title': u'TQASSIM F\'ŻONI KATASTALI', 'name': 'CP.CADASTRALZONING'},
    {'theme': u'CadastralParcels', 'title': u'LIMITU KATASTALI', 'name': 'CP.CADASTRALBOUNDARY'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Nodu tat-Trasport Ġeneriku', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Link tat-Trasport Ġeneriku', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tat-Trasport Ġenerika', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Link tat-Toroq', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tat-Traffiku tal-Vetturi', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja ta\' Servizz fit-Triq', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tat-Triq', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Link Ferrovjarju', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja ta\' Stazzjon Ferrovjarja', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja ta\' Depost Ferrovjarju', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja Ferrovjarja', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Link ta\' Passaġġi fuq l-Ilma', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tal-Kanali Navigabbli', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tal-Port', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Link tal-Ajru', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja ta\' Ajrudrom', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tar-Runway', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Żona ta\' Spazju tal-Ajru', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tar-Rampa', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Erja tat-Taxiway', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Netwerks tat-Trasport', 'title': u'Link ta\' Rotta b\'Kablaġġ', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Idrografija', 'title': u'Korp tal-ilma', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Idrografija', 'title': u'Limitu bejn l-Art u l-Ilma', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Idrografija', 'title': u'Ġbir tal-ilma tax-xita', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Idrografija', 'title': u'Netwerk Idrografiku', 'name': 'HY.Network'},
    {'theme': u'Idrografija', 'title': u'Punt ta\' Interess Idro', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Idrografija', 'title': u'Oġġett Magħmul mill-Bniedem', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Idrografija', 'title': u'Shore, Wetland', 'name': 'HY.HydroObject'},
    {'theme': u'Idrografija', 'title': u'Xmara-WFD', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Idrografija', 'title': u'Lag-WFD', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Idrografija', 'title': u'Ilma Tranżizzjonali-WFD', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Idrografija', 'title': u'Ilma kostali-WFD', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Idrografija', 'title': u'Reġjun tal-Oċean', 'name': 'HY.OceanRegion'},
    {'theme': u'Siti Protetti', 'title': u'Siti Protetti', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'pol', 'layers': [
    {'theme': u'Nazwy geograficzne', 'title': u'Nazwy geograficzne', 'name': 'GN.GeographicalNames'},
    {'theme': u'Jednostki administracyjne', 'title': u'Jednostka administracyjna', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Jednostki administracyjne', 'title': u'Granica administracyjna', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Jednostki administracyjne', 'title': u'Kondominium', 'name': 'AU.Condominium'},
    {'theme': u'Jednostki administracyjne', 'title': u'Region NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresy', 'title': u'Adresy', 'name': 'AD.Address'},
    {'theme': u'Działki katastralne', 'title': u'Działka katastralna', 'name': 'CP.CadastralParcel'},
    {'theme': u'Działki katastralne', 'title': u'Obszar katastralny', 'name': 'CP.CadastralZoning'},
    {'theme': u'Działki katastralne', 'title': u'Granica katastralna', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Sieci transportowe', 'title': u'Ogólny węzeł transportowy', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Sieci transportowe', 'title': u'Ogólne połączenie transportowe', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Sieci transportowe', 'title': u'Ogólny obszar transportowy', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Sieci transportowe', 'title': u'Połączenie drogowe', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar ruchu pojazdów', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar serwisu drogowego', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar drogi', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Sieci transportowe', 'title': u'Połączenie kolejowe', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar dworca kolejowego', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar stacji kolejowej', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar kolejowy', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Sieci transportowe', 'title': u'Połączenie w drodze wodnej', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar toru wodnego', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar portu', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Sieci transportowe', 'title': u'Połączenie lotnicze', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar lotniska', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar drogi startowej', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar przestrzeni powietrznej', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar płyty postojowej', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Sieci transportowe', 'title': u'Obszar drogi kołowania', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Sieci transportowe', 'title': u'Połączenie w sieci kolei linowej', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografia', 'title': u'Jednolita część wód', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografia', 'title': u'Linia rozgraniczająca wodę od lądu', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografia', 'title': u'Zlewisko', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografia', 'title': u'Sieć hydrograficzna', 'name': 'HY.Network'},
    {'theme': u'Hydrografia', 'title': u'Istotny punkt hydrograficzny', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografia', 'title': u'Obiekt sztuczny', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografia', 'title': u'Brzeg, Teren podmokły', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografia', 'title': u'Rzeka w rozumieniu RDW', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografia', 'title': u'Jezioro w rozumieniu RDW', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografia', 'title': u'Wody przejściowe w rozumieniu RDW', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografia', 'title': u'Wody przybrzeżne w rozumieniu RDW', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografia', 'title': u'Region oceaniczny', 'name': 'HY.OceanRegion'},
    {'theme': u'Obszary chronione', 'title': u'Obszary chronione', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'por', 'layers': [
    {'theme': u'Toponímia', 'title': u'Toponímia', 'name': 'GN.GeographicalNames'},
    {'theme': u'Unidades Administrativas', 'title': u'Unidade administrativa', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Unidades Administrativas', 'title': u'Fronteira administrativa', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Unidades Administrativas', 'title': u'Condomínio', 'name': 'AU.Condominium'},
    {'theme': u'Unidades Administrativas', 'title': u'Região NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Endereços', 'title': u'Endereços', 'name': 'AD.Address'},
    {'theme': u'Parcelas Cadastrais', 'title': u'Parcela cadastral', 'name': 'CP.CadastralParcel'},
    {'theme': u'Parcelas Cadastrais', 'title': u'Zonamento cadastral', 'name': 'CP.CadastralZoning'},
    {'theme': u'Parcelas Cadastrais', 'title': u'Limite cadastral', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Redes de Transporte', 'title': u'Nó de transporte genérico', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Redes de Transporte', 'title': u'Segmento de transporte genérico', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Redes de Transporte', 'title': u'Área de transporte genérica', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Redes de Transporte', 'title': u'Segmento da estrada', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Redes de Transporte', 'title': u'Área de circulação de veículos', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área de serviço rodoviário', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área da estrada', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Redes de Transporte', 'title': u'Segmento de via férrea', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Redes de Transporte', 'title': u'Área de estação ferroviária', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área de estação de triagem', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área de linha férrea', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Redes de Transporte', 'title': u'Segmento de via navegável', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Redes de Transporte', 'title': u'Área de navegação', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área portuária', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Redes de Transporte', 'title': u'Segmento de via aérea', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Redes de Transporte', 'title': u'Área de aeródromo', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área de pista', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área de espaço aéreo', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Redes de Transporte', 'title': u'Plataforma de estacionamento', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Redes de Transporte', 'title': u'Área de circulação', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Redes de Transporte', 'title': u'Segmento de via cablada', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hidrografia', 'title': u'Massa de água', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hidrografia', 'title': u'Fronteira terra-água', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hidrografia', 'title': u'Bacia hidrográfica', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hidrografia', 'title': u'Rede hidrográfica', 'name': 'HY.Network'},
    {'theme': u'Hidrografia', 'title': u'Ponto de interesse hidrográfico', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hidrografia', 'title': u'Objecto artificial', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hidrografia', 'title': u'Margem, zona húmida', 'name': 'HY.HydroObject'},
    {'theme': u'Hidrografia', 'title': u'Rio DQA', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hidrografia', 'title': u'Lago DQA', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hidrografia', 'title': u'Águas de transição DQA', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hidrografia', 'title': u'Águas costeiras DQA', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hidrografia', 'title': u'Região oceânica', 'name': 'HY.OceanRegion'},
    {'theme': u'Sítios Protegidos', 'title': u'Sítios protegidos', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'rum', 'layers': [
    {'theme': u'Geographical Names', 'title': u'Denumiri geografice', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administrative Units', 'title': u'Unitate administrativă', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administrative Units', 'title': u'Frontieră administrativă', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administrative Units', 'title': u'Condominiu', 'name': 'AU.Condominium'},
    {'theme': u'Administrative Units', 'title': u'Regiune NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adrese', 'title': u'Adrese', 'name': 'AD.Address'},
    {'theme': u'Parcele cadastrale', 'title': u'Parcelă cadastrală', 'name': 'CP.CadastralParcel'},
    {'theme': u'Parcele cadastrale', 'title': u'Zonare cadastrală', 'name': 'CP.CadastralZoning'},
    {'theme': u'Parcele cadastrale', 'title': u'Frontieră cadastrală', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transport networks', 'title': u'Nod de transport generic', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transport networks', 'title': u'Legătură de transport generic', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transport networks', 'title': u'Zonă de transport generic', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transport networks', 'title': u'Legătură rutieră', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transport networks', 'title': u'Zonă de circulație a vehiculelor', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transport networks', 'title': u'Zonă de servicii rutiere', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transport networks', 'title': u'Zonă rutieră', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transport networks', 'title': u'Legătură feroviară', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transport networks', 'title': u'Zona gării', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transport networks', 'title': u'Zona gării de triaj', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transport networks', 'title': u'Zona căii ferate', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transport networks', 'title': u'Legătură de cale navigabilă', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transport networks', 'title': u'Zona șenalului navigabil', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transport networks', 'title': u'Zona portuară', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transport networks', 'title': u'Legătură aeriană', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transport networks', 'title': u'Zona aerodromului', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transport networks', 'title': u'Zona pistei de decolare și de aterizare', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transport networks', 'title': u'Zona spațiului aerian', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transport networks', 'title': u'Zona platformei', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transport networks', 'title': u'Zona pistei de rulare', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transport networks', 'title': u'Cale de transport pe cablu', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hidrografie', 'title': u'Corp de apă', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hidrografie', 'title': u'Limita uscat-apă', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hidrografie', 'title': u'Captare', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hidrografie', 'title': u'Rețea hidrografică', 'name': 'HY.Network'},
    {'theme': u'Hidrografie', 'title': u'Punct de interes hidrografic', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hidrografie', 'title': u'Obiect artificial', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hidrografie', 'title': u'Țărm, Zonă umedă', 'name': 'HY.HydroObject'},
    {'theme': u'Hidrografie', 'title': u'Râu DCA', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hidrografie', 'title': u'Lac DCA', 'name': 'HY.Reporting. WFDLake'},
    {'theme': u'Hidrografie', 'title': u'Apă de tranziție DCA', 'name': 'HY.Reporting. WFDTransitionalWater'},
    {'theme': u'Hidrografie', 'title': u'Apă costieră DCA', 'name': 'HY.Reporting. WFDCoastalWater'},
    {'theme': u'Hidrografie', 'title': u'Regiune oceanică', 'name': 'HY.OceanRegion'},
    {'theme': u'Zone protejate', 'title': u'Zone protejate', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'slo', 'layers': [
    {'theme': u'Zemepisné názvy', 'title': u'Zemepisné názvy', 'name': 'GN.GeographicalNames'},
    {'theme': u'Správne jednotky', 'title': u'Správna jednotka', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Správne jednotky', 'title': u'Správna hranica', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Správne jednotky', 'title': u'Kondomínium', 'name': 'AU.Condominium'},
    {'theme': u'Správne jednotky', 'title': u'Región NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresy', 'title': u'Adresy', 'name': 'AD.Address'},
    {'theme': u'Katastrálne parcely', 'title': u'Katastrálna parcela', 'name': 'CP.CadastralParcel'},
    {'theme': u'Katastrálne parcely', 'title': u'Katastrálne rozdelenie na zóny', 'name': 'CP.CadastralZoning'},
    {'theme': u'Katastrálne parcely', 'title': u'Katastrálna hranica', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Dopravné siete', 'title': u'Generický dopravný uzol', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Dopravné siete', 'title': u'Generické dopravné spojenie', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Dopravné siete', 'title': u'Generická oblasť dopravy', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Dopravné siete', 'title': u'Cestné spojenie', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť premávky vozidiel', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť cestných služieb', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť cesty', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Dopravné siete', 'title': u'Železničné spojenie', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť železničnej stanice', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť nákladnej stanice', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť železnice', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Dopravné siete', 'title': u'Spojenie vodných ciest', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť plavebnej dráhy', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť prístavu', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Dopravné siete', 'title': u'Letecké spojenie', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť letiska', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť vzletovej a pristávacej dráhy', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť vzdušného priestoru', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť odbavovacej plochy', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Dopravné siete', 'title': u'Oblasť rolovacej dráhy', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Dopravné siete', 'title': u'Spojenie lanových dráh', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografia', 'title': u'Vodný útvar', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografia', 'title': u'Hranica zem – voda', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografia', 'title': u'Povodie', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografia', 'title': u'Hydrografická sieť', 'name': 'HY.Network'},
    {'theme': u'Hydrografia', 'title': u'Hydrografický bod záujmu', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografia', 'title': u'Umelý objekt', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografia', 'title': u'Pobrežie, mokraď', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografia', 'title': u'Rieka podľa WFD', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografia', 'title': u'Jazero podľa WFD', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografia', 'title': u'Brakická voda podľa WFD', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografia', 'title': u'Pobrežná voda podľa WFD', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografia', 'title': u'Oceánsky región', 'name': 'HY.OceanRegion'},
    {'theme': u'Chránené územia', 'title': u'Chránené územia', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'slv', 'layers': [
    {'theme': u'Zemljepisna imena', 'title': u'Zemljepisna imena', 'name': 'GN.Geographicalnames'},
    {'theme': u'Upravne enote', 'title': u'Upravna enota', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Upravne enote', 'title': u'Upravna meja', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Upravne enote', 'title': u'Kondominij', 'name': 'AU.Condominium'},
    {'theme': u'Upravne enote', 'title': u'Regija NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Naslovi', 'title': u'Naslovi', 'name': 'AD.Address'},
    {'theme': u'Katastrske parcele', 'title': u'Katastrska parcela', 'name': 'CP.CadastralParcel'},
    {'theme': u'Katastrske parcele', 'title': u'Delitev na katastrske enote', 'name': 'CP.CadastralZoning'},
    {'theme': u'Katastrske parcele', 'title': u'Katastrska meja', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Prometna omrežja', 'title': u'Generično prometno vozlišče', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Prometna omrežja', 'title': u'Generični prometni odsek', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Prometna omrežja', 'title': u'Generično območje prometa', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Prometna omrežja', 'title': u'Cestni odsek', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Prometna omrežja', 'title': u'Vozišče', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Prometna omrežja', 'title': u'Cestno počivališče', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Prometna omrežja', 'title': u'Cestni svet', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Prometna omrežja', 'title': u'Železniški odsek', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Prometna omrežja', 'title': u'Območje železniške postaje', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Prometna omrežja', 'title': u'Območje ranžirne postaje', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Prometna omrežja', 'title': u'Območje železnice', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Prometna omrežja', 'title': u'Odsek plovne poti', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Prometna omrežja', 'title': u'Območje plovne poti', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Prometna omrežja', 'title': u'Pristaniško območje', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Prometna omrežja', 'title': u'Zračni odsek', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Prometna omrežja', 'title': u'Območje aerodroma', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Prometna omrežja', 'title': u'Območje vzletno-pristajalne steze', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Prometna omrežja', 'title': u'Območje zračnega prostora', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Prometna omrežja', 'title': u'Območje ploščadi', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Prometna omrežja', 'title': u'Območje vozne steze', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Prometna omrežja', 'title': u'Žičnični odsek', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hidrografija', 'title': u'Telo vode', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hidrografija', 'title': u'Meja kopnega', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hidrografija', 'title': u'Prispevna površina', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hidrografija', 'title': u'Hidrografska mreža', 'name': 'HY.Network'},
    {'theme': u'Hidrografija', 'title': u'Hidrografska pomembna točka', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hidrografija', 'title': u'Grajen objekt', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hidrografija', 'title': u'Obala, mokrišče', 'name': 'HY.HydroObject'},
    {'theme': u'Hidrografija', 'title': u'Reka po vodni direktivi', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hidrografija', 'title': u'Jezero po vodni direktivi', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hidrografija', 'title': u'Somornica po vodni direktivi', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hidrografija', 'title': u'Obalno morje po vodni direktivi', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hidrografija', 'title': u'Oceansko območje', 'name': 'HY.OceanRegion'},
    {'theme': u'Zavarovana območja', 'title': u'Zavarovana območja', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'spa', 'layers': [
    {'theme': u'Nombres geográficos', 'title': u'Nombres geográficos', 'name': 'GN.GeographicalNames'},
    {'theme': u'Unidades administrativas', 'title': u'Unidad administrativa', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Unidades administrativas', 'title': u'Límite administrativo', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Unidades administrativas', 'title': u'Condominio', 'name': 'AU.Condominium'},
    {'theme': u'Unidades administrativas', 'title': u'Región NUTS', 'name': 'AU.NUTSRegion'},
    {'theme': u'Direcciones', 'title': u'Direcciones', 'name': 'AD.Address'},
    {'theme': u'Parcelas catastrales', 'title': u'Parcela catastral', 'name': 'CP.CadastralParcel'},
    {'theme': u'Parcelas catastrales', 'title': u'Zonificación catastral', 'name': 'CP.CadastralZoning'},
    {'theme': u'Parcelas catastrales', 'title': u'Límite catastral', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Redes de transporte', 'title': u'Nodo de transporte genérico', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Redes de transporte', 'title': u'Enlace de transporte genérico', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Redes de transporte', 'title': u'Área de transporte genérica', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Redes de transporte', 'title': u'Enlace de carretera', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Redes de transporte', 'title': u'Área de tráfico de vehículos', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de servicio de carretera', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de carretera', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Redes de transporte', 'title': u'Enlace ferroviario', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Redes de transporte', 'title': u'Área de estación ferroviaria', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de operaciones ferroviarias', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Redes de transporte', 'title': u'Área ferroviaria', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Redes de transporte', 'title': u'Enlace de vía navegable', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Redes de transporte', 'title': u'Área de paso', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Redes de transporte', 'title': u'Área portuaria', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Redes de transporte', 'title': u'Enlace aéreo', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Redes de transporte', 'title': u'Área de aeródromo', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de pista', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de espacio aéreo', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de plataforma', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Redes de transporte', 'title': u'Área de calle de rodaje', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Redes de transporte', 'title': u'Enlace de cable transportador', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hidrografía', 'title': u'Masa de agua', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hidrografía', 'title': u'Frontera tierra-agua', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hidrografía', 'title': u'Captación', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hidrografía', 'title': u'Red hidrográfica', 'name': 'HY.Network'},
    {'theme': u'Hidrografía', 'title': u'Punto de interés hidrográfico', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hidrografía', 'title': u'Objeto artificial', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hidrografía', 'title': u'Costa, humedal', 'name': 'HY.HydroObject'},
    {'theme': u'Hidrografía', 'title': u'Río DMA', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hidrografía', 'title': u'Lago DMA', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hidrografía', 'title': u'Aguas de transición DMA', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hidrografía', 'title': u'Aguas costeras DMA', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hidrografía', 'title': u'Región oceánica', 'name': 'HY.OceanRegion'},
    {'theme': u'Lugares protegidos', 'title': u'Lugares protegidos', 'name': 'PS.ProtectedSite'}
  ]},
  {'language': 'swe', 'layers': [
    {'theme': u'Ortnamn', 'title': u'Ortnamn', 'name': 'GN.GeographicalNames'},
    {'theme': u'Administrativa enheter', 'title': u'Administrativ enhet', 'name': 'AU.AdministrativeUnit'},
    {'theme': u'Administrativa enheter', 'title': u'Administrativ gräns', 'name': 'AU.AdministrativeBoundary'},
    {'theme': u'Administrativa enheter', 'title': u'Condominium', 'name': 'AU.Condominium'},
    {'theme': u'Administrativa enheter', 'title': u'NUTS-område', 'name': 'AU.NUTSRegion'},
    {'theme': u'Adresser', 'title': u'Adresser', 'name': 'AD.Address'},
    {'theme': u'Fastighetsområden', 'title': u'Fastighetsområde', 'name': 'CP.CadastralParcel'},
    {'theme': u'Fastighetsområden', 'title': u'Fastighetsindelning', 'name': 'CP.CadastralZoning'},
    {'theme': u'Fastighetsområden', 'title': u'Fastighetsgräns', 'name': 'CP.CadastralBoundary'},
    {'theme': u'Transportnät', 'title': u'Generisk transportnod', 'name': 'TN.CommonTransportElements.TransportNode'},
    {'theme': u'Transportnät', 'title': u'Generisk transportlänk', 'name': 'TN.CommonTransportElements.TransportLink'},
    {'theme': u'Transportnät', 'title': u'Generisk transportyta', 'name': 'TN.CommonTransportElements.TransportArea'},
    {'theme': u'Transportnät', 'title': u'Väglänk', 'name': 'TN.RoadTransportNetwork.RoadLink'},
    {'theme': u'Transportnät', 'title': u'Fordonstrafikområde', 'name': 'TN.RoadTransportNetwork.VehicleTrafficArea'},
    {'theme': u'Transportnät', 'title': u'Vägserviceområde', 'name': 'TN.RoadTransportNetwork.RoadServiceArea'},
    {'theme': u'Transportnät', 'title': u'Vägområde', 'name': 'TN.RoadTransportNetwork.RoadArea'},
    {'theme': u'Transportnät', 'title': u'Järnvägslänk', 'name': 'TN.RailTransportNetwork.RailwayLink'},
    {'theme': u'Transportnät', 'title': u'Järnvägsstationsområde', 'name': 'TN.RailTransportNetwork.RailwayStationArea'},
    {'theme': u'Transportnät', 'title': u'Bangårdsområde', 'name': 'TN.RailTransportNetwork.RailwayYardArea'},
    {'theme': u'Transportnät', 'title': u'Järnvägsområde', 'name': 'TN.RailTransportNetwork.RailwayArea'},
    {'theme': u'Transportnät', 'title': u'Vattenvägslänk', 'name': 'TN.WaterTransportNetwork.WaterwayLink'},
    {'theme': u'Transportnät', 'title': u'Farledsområde', 'name': 'TN.WaterTransportNetwork.FairwayArea'},
    {'theme': u'Transportnät', 'title': u'Hamnområde', 'name': 'TN.WaterTransportNetwork.PortArea'},
    {'theme': u'Transportnät', 'title': u'Flyglänk', 'name': 'TN.AirTransportNetwork.AirLink'},
    {'theme': u'Transportnät', 'title': u'Flygplatsområde', 'name': 'TN.AirTransportNetwork.AerodromeArea'},
    {'theme': u'Transportnät', 'title': u'Start- och landningsområde', 'name': 'TN.AirTransportNetwork.RunwayArea'},
    {'theme': u'Transportnät', 'title': u'Luftrumsområde', 'name': 'TN.AirTransportNetwork.AirspaceArea'},
    {'theme': u'Transportnät', 'title': u'Plattområde', 'name': 'TN.AirTransportNetwork.ApronArea'},
    {'theme': u'Transportnät', 'title': u'Taxibaneområden', 'name': 'TN.AirTransportNetwork.TaxiwayArea'},
    {'theme': u'Transportnät', 'title': u'Linbanelänk', 'name': 'TN.CableTransportNetwork.CablewayLink'},
    {'theme': u'Hydrografi', 'title': u'Vattenförekomst', 'name': 'HY.PhysicalWaters.Waterbodies'},
    {'theme': u'Hydrografi', 'title': u'Strandlinje', 'name': 'HY.PhysicalWaters.LandWaterBoundary'},
    {'theme': u'Hydrografi', 'title': u'Tillrinning', 'name': 'HY.PhysicalWaters.Catchments'},
    {'theme': u'Hydrografi', 'title': u'Hydrografiskt nät', 'name': 'HY.Network'},
    {'theme': u'Hydrografi', 'title': u'Hydrografiskt intressant plats', 'name': 'HY.PhysicalWaters.HydroPointOfInterest'},
    {'theme': u'Hydrografi', 'title': u'Konstgjort objekt', 'name': 'HY.PhysicalWaters.ManMadeObject'},
    {'theme': u'Hydrografi', 'title': u'Strand, våtmark', 'name': 'HY.HydroObject'},
    {'theme': u'Hydrografi', 'title': u'WFD Vattendrag', 'name': 'HY.Reporting.WFDRiver'},
    {'theme': u'Hydrografi', 'title': u'WFD Sjö', 'name': 'HY.Reporting.WFDLake'},
    {'theme': u'Hydrografi', 'title': u'WFD Vatten i övergångszon', 'name': 'HY.Reporting.WFDTransitionalWater'},
    {'theme': u'Hydrografi', 'title': u'WFD Kustvatten', 'name': 'HY.Reporting.WFDCoastalWater'},
    {'theme': u'Hydrografi', 'title': u'Oceanområde', 'name': 'HY.OceanRegion'},
    {'theme': u'Skyddade områden', 'title': u'Skyddade områden', 'name': 'PS.ProtectedSite'}
  ]} ]

def findInspireLayerWithName(layer_name, response_lang):
  """Find the INSPIRE layer matching the given layer name and language
  """

  layers_for_lang = [l for l in INSPIRE_LAYERS
                     if l['language'] == response_lang][0].get('layers', [])
  layers_with_name = [l for l in layers_for_lang if l['name'] == layer_name]
  
  if len(layers_with_name) > 0 :
    return layers_with_name[0]
  else:
    return None


def findInspireLayerWithTitle(layer_title, response_lang):
  """Find the INSPIRE layer matching the given layer title and language
  """
  
  layers_for_lang = [l for l in INSPIRE_LAYERS
                     if l['language'] == response_lang][0].get('layers', [])

  layers_with_title = [l for l in layers_for_lang \
                    if l['theme'] in layer_title and l['title'] in layer_title]

  if len(layers_with_title) > 0 :
    return layers_with_title[0]
  else:
    return None


def getInspirePropertiesAsDict(etreeCapabilities):
  """Create a dictionary of INSPIRE informations contained
  in the WMS capabilities.
  """
  
  result = {}
  
  # Service version
  try:
    wms_version = etreeCapabilities.get("version")
  except:
    wms_version = None

  if wms_version == None or wms_version < "1.3.0":
    return result
  
  # infoMapAccessService keyword
  try:
    etree_keywords = etreeCapabilities.findall("./%sService//%sKeyword" % (NS_WMS_130, NS_WMS_130))
    keywords = [e.text.strip() for e in etree_keywords if e.get("vocabulary", None) == "ISO"]
    result["Keyword_ISO_keywords"] = keywords
  except:
    result["Keyword_ISO_keywords"] = []
  
  # inspire_vs:ExtendedCapabilities (nb of elements)
  try:
    etree_extendedCapabilities = etreeCapabilities.findall("./%sCapability/%sExtendedCapabilities" % (NS_WMS_130, NS_INSPIRE_VS))
    result["ExtendedCapabilities_nb_elements"] = len(etree_extendedCapabilities)
  except:
    result["ExtendedCapabilities_nb_elements"] = 0
  
  # inspire_common:SupportedLanguages (nb of elements)
  try:
    etree_supportedLanguages = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sSupportedLanguages" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["SupportedLanguages_nb_elements"] = len(etree_supportedLanguages)
  except:
    result["SupportedLanguages_nb_elements"] = 0

  # inspire_common:DefaultLanguage (default language)
  try:
    etree_default_languages = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sSupportedLanguages/%sDefaultLanguage/%sLanguage" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["DefaultLanguage"] = [e.text.strip() for e in etree_default_languages]
  except:
    result["DefaultLanguage"] = []
  
  # inspire_common:SupportedLanguages (other supported languages)
  try:
    etree_supported_languages = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sSupportedLanguages/%sSupportedLanguage/%sLanguage" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["SupportedLanguages"] = [e.text.strip() for e in etree_supported_languages]
  except:
    result["SupportedLanguages"] = []
  
  # inspire_common:ResponseLanguage
  try:
    etree_supported_languages = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sResponseLanguage/%sLanguage" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["ResponseLanguage"] = [e.text.strip() for e in etree_supported_languages]
  except:
    result["ResponseLanguage"] = []

  # Service MetadataURL
  try:
    etree_service_metadataUrl = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sMetadataUrl" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["MetadataURL_nb_elements"] = len(etree_service_metadataUrl)
  except:
    result["MetadataURL_nb_elements"] = 0

  # Service Spatial Data Service Type
  try:
    etree_service_spatial_data_service_type = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sSpatialDataServiceType" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["SpatialDataServiceType"] = etree_service_spatial_data_service_type[0].text
  except:
    result["SpatialDataServiceType"] = None
  
  # Service Resource Type
  try:
    etree_service_resource_type = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sResourceType" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["SpatialResourceType"] = etree_service_resource_type[0].text
  except:
    result["SpatialResourceType"] = None
  
  # Temporal reference
  try:
    etree_temporal_reference = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sTemporalReference" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["TemporalReference_nb_elements"] = len(etree_temporal_reference)
  except:
    result["TemporalReference_nb_elements"] = 0
  
  # Date of creation
  try:
    etree_date_of_creation = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sTemporalReference/%sDateOfCreation" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["DateOfCreation"] = etree_date_of_creation[0].text.strip()
  except:
    result["DateOfCreation"] = None
  
  # Date of publication
  try:
    etree_date_of_publication = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sTemporalReference/%sDateOfPublication" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["DateOfPublication"] = etree_date_of_publication[0].text.strip()
  except:
    result["DateOfPublication"] = None
  
  # Date of last revision
  try:
    etree_date_of_last_revision = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sTemporalReference/%sDateOfLastRevision" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["DateOfLastRevision"] = etree_date_of_last_revision[0].text.strip()
  except:
    result["DateOfLastRevision"] = None
  
  # Temporal extent
  try:
    etree_date_of_last_revision = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sTemporalReference/%sTemporalExtent" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["TemporalExtent_nb_elements"] = len(etree_date_of_last_revision)
  except:
    result["TemporalExtent_nb_elements"] = 0

  # Conformity
  try:
    etree_conformity = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sConformity" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["Conformity_nb_elements"] = len(etree_conformity)
  except:
    result["Conformity_nb_elements"] = 0
  
  # metadata point of contact
  try:
    etree_md_poc_organization_name = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sMetadataPointOfContact/%sOrganisationName" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["MD_Contact_Organization_Name"] = etree_md_poc_organization_name[0].text.strip()
  except:
    result["MD_Contact_Organization_Name"] = None

  try:
    etree_md_poc_email = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sMetadataPointOfContact/%sEmailAddress" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM, NS_INSPIRE_COM))
    result["MD_Contact_Email"] = etree_md_poc_email[0].text.strip()
  except:
    result["MD_Contact_Email"] = None

  try:
    etree_md_date = etreeCapabilities.findall(
      ".//%sExtendedCapabilities/%sMetadataDate" %
      (NS_INSPIRE_VS, NS_INSPIRE_COM))
    result["MD_Date"] = etree_md_date[0].text.strip()
  except:
    result["MD_DATE"] = None


  # Layers
  result["Layers"] = []
  etree_layers = etreeCapabilities.findall(
    ".//%sLayer" % (NS_WMS_130))
  
  for etree_layer in etree_layers:
    
    # Layer name
    try:
      layer_name = None
      etree_name = etree_layer.findall("./%sName" % (NS_WMS_130))
      if len(etree_name) == 1:
        layer_name = etree_name[0].text.strip()
    except:
      pass
    
    # Layer title
    try:
      layer_title = None
      etree_title = etree_layer.findall("./%sTitle" % (NS_WMS_130))
      if len(etree_title) == 1:
        layer_title = etree_title[0].text.strip()
    except:
      pass

    # Layer CRS
    try:
      layer_CRS = []
      etree_CRS = etree_layer.findall("./%sCRS" % (NS_WMS_130))
      if len(etree_CRS) > 0:
        layer_CRS = [e.text.strip() for e in etree_CRS]
    except:
      pass

    # Layer BBox CRS
    try:
      layer_bbox_CRS = []
      etree_bboxes = etree_layer.findall("./%sBoundingBox" % (NS_WMS_130))
      if len(etree_bboxes) > 0:
        layer_bbox_CRS = [e.attrib.get("CRS").strip() for e in etree_bboxes]
    except:
      pass

    # Layer style names
    try:
      layer_style_names = []
      etree_style_names = etree_layer.findall("./%sStyle/%sName" %  (NS_WMS_130, NS_WMS_130))
      if len(etree_style_names) > 0:
        layer_style_names = [e.text.strip() for e in etree_style_names]
    except:
      pass
    
    # Authority URL
    try:
      layer_auth_url = ""
      etree_auth_url = etree_layer.findall("./%sAuthorityURL" %  (NS_WMS_130))
      if len(etree_auth_url) > 0:
        layer_auth_url = etree_auth_url[0].attrib.get("name").strip()
    except:
      pass

    # Identifier
    try:
      layer_identifier = ""
      etree_identifier = etree_layer.findall("./%sIdentifier" % (NS_WMS_130))
      if len(etree_identifier) > 0:
        layer_identifier = etree_identifier[0].text.strip()
    except:
      pass
    
    # Layer Legend
    try:
      layer_legend = False
      etree_legend = etree_layer.findall("./%sStyle/%sLegendURL/%sOnlineResource" % (NS_WMS_130,NS_WMS_130, NS_WMS_130))
      if len(etree_legend) > 0:
        layer_legend = True
    except:
      pass

    layer = {
      'name': layer_name,
      'title': layer_title,
      'CRS': layer_CRS,
      'bbox_CRS': layer_bbox_CRS,
      'style_names': layer_style_names,
      'auth_url': layer_auth_url,
      'identifier':layer_identifier,
      'legend':layer_legend
      }
    result["Layers"].append(layer)

  return result

def testInspireCompliance(wms_dict, inspire_dict):
  """Test compliance of the service.
  This function returns a list of messages.
  """
  result = []

  m = testMessage.Message("0")
  result.append(m)

  if wms_dict["WMS_version"] != "1.3.0":
    m = testMessage.Message("1")
    result.append(m)
    
    return result
  
  if wms_dict["GetCapabilities_support"] == None:
    m = testMessage.Message("2")
    result.append(m)
  elif "Get" not in wms_dict["GetCapabilities_support"]:
    m = testMessage.Message("4")
    result.append(m)

  if wms_dict["GetMap_support"] == None:
    m = testMessage.Message("3")
    result.append(m)
  elif "Get" not in wms_dict["GetMap_support"]:
    m = testMessage.Message("5")
    result.append(m)

  if wms_dict["Service_Title"] == None or \
      len(wms_dict["Service_Title"].strip()) == 0:
    m = testMessage.Message("10.0")
    result.append(m)

  if wms_dict["Service_Abstract"] == None or \
      len(wms_dict["Service_Abstract"].strip()) == 0:
    m = testMessage.Message("10.1")
    result.append(m)
  
  if inspire_dict.get("ExtendedCapabilities_nb_elements", 0) != 1:
    m = testMessage.Message("10.2")
    result.append(m)


  if inspire_dict.get("MetadataURL_nb_elements", 0) == 1:
    m = testMessage.Message("6")
    result.append(m)

  if inspire_dict.get("MetadataURL_nb_elements", 0) > 1:
    m = testMessage.Message("6.2")
    result.append(m)
  
  if inspire_dict.get("MetadataURL_nb_elements", 0) == 0:
    m = testMessage.Message("6.1")
    result.append(m)
    
    if inspire_dict.get("SpatialResourceType", None) == None:
      m = testMessage.Message("11")
      result.append(m)
    
    if inspire_dict.get("SpatialDataServiceType", None) == None:
      m = testMessage.Message("15")
      result.append(m)
  
    if inspire_dict.get("TemporalReference_nb_elements", 0) == 0:
      m = testMessage.Message("21")
      result.append(m)
    else:
      if inspire_dict.get("DateOfCreation", None) == None and \
        inspire_dict.get("DateOfPublication", None) == None and \
        inspire_dict.get("DateOfLastRevision", None) == None and \
        inspire_dict.get("TemporalExtent_nb_elements", 0) == 0:
        m = testMessage.Message("20")
        result.append(m)
      if inspire_dict.get("DateOfLastRevision", None) == None:
        m = testMessage.Message("20.1")
        result.append(m)

    if inspire_dict.get("Conformity_nb_elements", 0) == 0:
      m = testMessage.Message("22")
      result.append(m)


    if inspire_dict.get("MD_Contact_Organization_Name", None) in [None, ""]:
      m = testMessage.Message("27.1")
      result.append(m)

    if inspire_dict.get("MD_Contact_Email", None) in [None, ""]:
      m = testMessage.Message("27.2")
      result.append(m)

    if inspire_dict.get("MD_Date", None) in [None, ""]:
      m = testMessage.Message("29.1")
      result.append(m)


  if inspire_dict.get("SpatialResourceType", None) != None and \
    inspire_dict.get("SpatialResourceType", None) != "service":
    m = testMessage.Message("11.1")
    m.detail = \
      _("Found value(s): %(found)s - Expected value(s): %(expected)s") \
      % {'found': inspire_dict.get("SpatialResourceType", _("<None>")),
         'expected': "service"}
    result.append(m)
    
  if inspire_dict.get("SpatialDataServiceType", None) != None and \
    inspire_dict.get("SpatialDataServiceType", None) != "view":
    m = testMessage.Message("15.1")
    m.detail = \
      _("Found value(s): %(found)s - Expected value(s): %(expected)s") \
      % {'found': inspire_dict.get("SpatialDataServiceType", _("<None>")),
         'expected': "view"}
    result.append(m)

  service_type_found = False
  for k in inspire_dict.get("Keyword_ISO_keywords", []):
    if k in SERVICE_TYPES:
      service_type_found = True
  if not service_type_found:
    m = testMessage.Message("16")
    m.detail = \
      _("Expected value(s): %(expected)s") \
      % {'expected': ", ".join(SERVICE_TYPES)}
    result.append(m)


  if wms_dict.get("Service_Fees", None) == None:
    m = testMessage.Message("24")
    result.append(m)
  elif wms_dict.get("Service_Fees", "").lower() == "none":
    m = testMessage.Message("24.2")
    result.append(m)
  elif wms_dict.get("Service_Fees", "").lower() not in MD_CONDITIONS:
    m = testMessage.Message("24.1")
    result.append(m)

  if wms_dict.get("Service_AccessConstraints", None) == None:
    m = testMessage.Message("24.3")
    result.append(m)
  elif wms_dict.get("Service_AccessConstraints", "") != "None" and \
    wms_dict.get("Service_AccessConstraints", "") not in MD_RESTRICTION_CODES:
    m = testMessage.Message("24.4")
    m.detail = \
      _("Found value(s): %(found)s - Expected value(s): %(expected)s") \
      % {'found': inspire_dict.get("Service_AccessConstraints", _("<None>")),
         'expected': ", ".join(MD_RESTRICTION_CODES)}
    result.append(m)


  if wms_dict.get("Service_Contact_Organization", "") in [None, ""]:
    m = testMessage.Message("25.1")
    result.append(m)

  if wms_dict.get("Service_Contact_ElectronicMailAddress", "") in [None, ""]:
    m = testMessage.Message("25.2")
    result.append(m)

  if wms_dict.get("Service_Contact_Position", None) == None:
    m = testMessage.Message("26.1")
    result.append(m)
  elif wms_dict.get("Service_Contact_Position", None) not in MD_ROLES:
    m = testMessage.Message("26.2")
    m.detail = \
      _("Found value(s): %(found)s - Expected value(s): %(expected)s") \
      % {'found': wms_dict.get("Service_Contact_Position", _("<None>")),
         'expected': ", ".join(MD_ROLES)}
    result.append(m)

  # Layers
  layers = inspire_dict.get('Layers', [])
  
  layers_err_33_1_detail = []
  layers_err_33_2_detail = []
  layers_err_36_detail = []
  layers_err_39_1_detail = []
  layers_err_42_1_detail = []
  layers_err_37_detail = [] 
  layers_err_38_detail = [] 
  layers_err_47_detail = [] 
  cpt = 0 
  for layer in layers:
    if cpt == 0:
      rootlayer = True
    else:
      rootlayer = False
    cpt += 1
    # Layer name and title
    layer_name = layer.get('name', None)
    layer_title = layer.get('title', None)
    response_lang = ''
    if len(inspire_dict.get("ResponseLanguage", [])) == 1:
      response_lang = inspire_dict["ResponseLanguage"][0]
    
    # If the layer name exists and the response language well defined
    if layer_name not in [None, ''] and \
      response_lang in MEMBER_STATES_LANGUAGES:
      
      # Find an Inspire layer matching the layer name and language
      inspire_layer = findInspireLayerWithName(layer_name, response_lang)
      
      if inspire_layer != None:
        # The layer title does not match the expected title for this
        # layer name
        if inspire_layer['title'] not in layer_title or \
          inspire_layer['theme'] not in layer_title:
          layers_err_33_1_detail.append(u"%s - %s" % (layer_name, layer_title))
        
      else:
        # Not an INSPIRED harmonised name
        layers_err_39_1_detail.append(layer_name)
        
        # Find an Inspire layer matching the layer title and language
        inspire_layer = findInspireLayerWithTitle(layer_title, response_lang)

        # Not an INSPIRE harmonised title
        if inspire_layer == None:
          layers_err_33_2_detail.append(layer_title)
    # If the language is not a member state language
    elif layer_name not in [None, '']:
      # Find an Inspire layer matching the layer name and language
      inspire_layer = findInspireLayerWithName(layer_name, 'eng')

      if inspire_layer == None:
        # Not an INSPIRED harmonised name
        layers_err_39_1_detail.append(layer_name)

    # Default style
    if layer_name not in [None, ''] and not rootlayer:
      layer_style_names = layer.get('style_names', [])
      if 'inspire_common:DEFAULT' not in layer_style_names:
        layers_err_42_1_detail.append(layer_name)

    # Layer bbox CRS
    if set(layer.get('CRS', [])) > set(layer.get('bbox_CRS', [])):
        layers_err_36_detail.append(u"%s - %s" % (layer_name, layer_title))

    # AuthorityURL and identifier
    if layer.get('identifier', None) in [None, ''] and not rootlayer:
        layers_err_37_detail.append(u"%s - %s" % (layer_name, layer_title))
    
    if layer.get('auth_url', None) in [None, ''] and not rootlayer:
        layers_err_38_detail.append(u"%s - %s" % (layer_name, layer_title))

    # LEGEND URL
    if layer.get('legend',False) in [False, '']:
        layers_err_47_detail.append(u"%s - %s" % (layer_name, layer_title))
 
  if len(layers_err_33_1_detail) > 0:
        m = testMessage.Message("33.1")
        m.detail = _("Layers: %s") % (", ".join(layers_err_33_1_detail))
        result.append(m)

  if len(layers_err_33_2_detail) > 0:
        m = testMessage.Message("33.2")
        m.detail = _("Layers: %s") % (", ".join(layers_err_33_2_detail))
        result.append(m)

  if len(layers_err_36_detail) > 0:
        m = testMessage.Message("36")
        m.detail = _("Layers: %s") % (", ".join(layers_err_36_detail))
        result.append(m)
  
  if len(layers_err_37_detail) > 0:
        m = testMessage.Message("37.1")
        m.detail = _("Layers: %s") % (", ".join(layers_err_37_detail))
        result.append(m)  
        
  if len(layers_err_38_detail) > 0:
        m = testMessage.Message("38.1")
        m.detail = _("Layers: %s") % (", ".join(layers_err_38_detail))
        result.append(m)  

  if len(layers_err_39_1_detail) > 0:
        m = testMessage.Message("39.1")
        m.detail = _("Layers: %s") % (", ".join(layers_err_39_1_detail))
        result.append(m)
        
  if len(layers_err_42_1_detail) > 0:
        m = testMessage.Message("42.1")
        m.detail = _("Layers: %s") % (", ".join(layers_err_42_1_detail))
        result.append(m)

  if len(layers_err_47_detail) > 0:
        m = testMessage.Message("47")
        m.detail = _("Layers: %s") % (", ".join(layers_err_47_detail))
        result.append(m)


  # Recommended CRS
  all_CRS_list = []
  for layer in layers:
    all_CRS_list.extend(layer.get('CRS', []))
  all_CRS_set = set(all_CRS_list)
  if len(all_CRS_set & set(['EPSG:4258', 'EPSG:4326', 'CRS:84'])) == 0:
    m = testMessage.Message("40.1")
    result.append(m)

  if inspire_dict.get("SupportedLanguages_nb_elements", 0) == 0:
    m = testMessage.Message("71.1")
    result.append(m)
  
  if inspire_dict.get("SupportedLanguages_nb_elements", 0) > 1:
    m = testMessage.Message("71.2")
    result.append(m)

  if len(inspire_dict.get("ResponseLanguage", [])) == 0:
    m = testMessage.Message("70.1")
    result.append(m)

  if len(inspire_dict.get("ResponseLanguage", [])) > 1:
    m = testMessage.Message("70.2")
    result.append(m)

  if len(inspire_dict.get("ResponseLanguage", [])) == 1:
    response_language = inspire_dict.get("ResponseLanguage", [])[0]
    supported_languages = []
    supported_languages.extend(inspire_dict.get("DefaultLanguage", []))
    supported_languages.extend(inspire_dict.get("SupportedLanguages", []))
    if response_language not in supported_languages:
      m = testMessage.Message("70.3")
      m.detail = _("Unexpected value: %s") % (response_language)
      result.append(m)

  if len(inspire_dict.get("DefaultLanguage", [])) == 0:
    m = testMessage.Message("71.3")
    result.append(m)

  if len(inspire_dict.get("DefaultLanguage", [])) > 1:
    m = testMessage.Message("71.4")
    result.append(m)

  if len(inspire_dict.get("DefaultLanguage", [])) == 1 and \
    len(inspire_dict.get("SupportedLanguages", [])) > 0:
    if inspire_dict["DefaultLanguage"][0] in inspire_dict.get("SupportedLanguages", []):
      m = testMessage.Message("71.5")
      result.append(m)

  languages = []
  languages.extend(inspire_dict.get("DefaultLanguage", []))
  languages.extend(inspire_dict.get("SupportedLanguages", []))
  languages.extend(inspire_dict.get("ResponseLanguage", []))
  set_languages = set(languages)
  for l in set_languages:
    if l not in MEMBER_STATES_LANGUAGES:
      m = testMessage.Message("71.6")
      m.detail = _("Unexpected value: %s") % (l)
      result.append(m)
    if l.lower() != l or len(l)!= 3:
      m = testMessage.Message("71.7")
      m.detail = _("Unexpected value: %s") % (l)
      result.append(m)

  return result
