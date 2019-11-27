"""

XML metadata parsing

This module contains the MetaBlob class for holding a dictionary (dict) of satellite metadata
read from a .xml file created by someone in espaLand

more to come ...

watch this space ...

"""

import re
import pprint
from xml.etree import ElementTree

class MetaBlob:


    def __init__(self, directory, raw_xml):

        self.directory = directory
        self.xmlstring = raw_xml 
        self.set_global_metadata()
        self.set_geography_coords()
        self.set_projection_coords()
        self.set_band_file_names()

    def set_global_metadata(self):
        xmlstring = self.xmlstring

        xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
        doc = ElementTree.fromstring(xmlstring)
        
        # self.data_provider = doc.find('.//data_provider').text
        self.data_provider = doc.find('.//ORIGIN').text
        # self.satellite = doc.find('.//SATELLITE').text
        self.satellite = doc.find('.//SPACECRAFT_ID').text
        # self.instrument = doc.find('.//INSTRUMENT').text
        self.instrument = doc.find('.//SENSOR_ID').text
        # self.acquisition_date = doc.find('.//ACQUISITION_DATE').text
        self.acquisition_date = doc.find('.//DATE_ACQUIRED').text
        self.scene_center_time = doc.find('.//SCENE_CENTER_TIME').text
        self.product_id =  doc.find('.//LANDSAT_PRODUCT_ID').text
        self.lpgs_metadata_file = doc.find('.//FILE_NAME_METADATA_XML').text



    def get_global_metadata(self):
        print (self.data_provider)
        print (self.satellite)
        print (self.instrument)
        print (self.acquisition_date)
        print (self.scene_center_time)
        print (self.product_id)
        print (self.lpgs_metadata_file)



    def set_geography_coords(self):
        xmlstring = self.xmlstring

        xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
        doc = ElementTree.fromstring(xmlstring)

        self.ul_lat = doc.find('.//CORNER_UL_LAT_PRODUCT').text
        self.ul_lon = doc.find('.//CORNER_UL_LON_PRODUCT').text

        self.ur_lat = doc.find('.//CORNER_UR_LAT_PRODUCT').text
        self.ur_lon = doc.find('.//CORNER_UR_LON_PRODUCT').text

        self.ll_lat = doc.find('.//CORNER_LL_LAT_PRODUCT').text
        self.ll_lon = doc.find('.//CORNER_LL_LON_PRODUCT').text

        self.lr_lat = doc.find('.//CORNER_LR_LAT_PRODUCT').text
        self.lr_lon = doc.find('.//CORNER_LR_LON_PRODUCT').text

        self.coord = {
          'ul':
             {'lon': self.ul_lon,
              'lat': self.ul_lat},
          'ur':
             {'lon': self.ur_lon,
              'lat': self.ur_lat},
          'lr':
             {'lon': self.lr_lon,
              'lat': self.lr_lat},
          'll':
             {'lon': self.ll_lon,
              'lat': self.ll_lat}}


    def get_geography_coords(self):
        print(self.west)
        print(self.east)
        print(self.north)
        print(self.south)
        print(self.coord)

    def set_projection_coords(self):
        xmlstring = self.xmlstring

        xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
        doc = ElementTree.fromstring(xmlstring)

        ul_lat = doc.find('.//CORNER_UL_LAT_PRODUCT').text
        ul_lon = doc.find('.//CORNER_UL_LON_PRODUCT').text

        lr_lat = doc.find('.//CORNER_LR_LAT_PRODUCT').text
        lr_lon = doc.find('.//CORNER_LR_LON_PRODUCT').text

        self.westx = ul_lon
        self.northy = ul_lat
        self.eastx = lr_lon
        self.southy = lr_lat


    def get_projection_coords(self):
        #print(self.projection_information)
        print(self.westx)
        print(self.eastx)
        print(self.northy)
        print(self.southy)



    def set_band_file_names(self):
        """ parse the xml metadata and return the band names in a dict """
        self.band_dict = {}
        xmlstring = self.xmlstring
        xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
        doc = ElementTree.fromstring(xmlstring)

        bands = [
                "FILE_NAME_BAND_1",
                "FILE_NAME_BAND_2",
                "FILE_NAME_BAND_3",
                "FILE_NAME_BAND_4",
                "FILE_NAME_BAND_5",
                "FILE_NAME_BAND_6",
                "FILE_NAME_BAND_7",
                "FILE_NAME_THERMAL_RADIANCE",
                "FILE_NAME_QUALITY_L2_AEROSOL",
                "FILE_NAME_QUALITY_L1_PIXEL",
                ]

        # print(type(xmldoc))
        for band_name in bands:
            print(band_name)
            band_file_name = self.directory + doc.find(".//" + band_name).text
            print(band_file_name)
            self.band_dict[band_name] = band_file_name
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint (self.band_dict)

