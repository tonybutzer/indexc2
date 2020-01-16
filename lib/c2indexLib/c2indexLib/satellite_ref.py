""" Generic prepare script library - needs work
However puttng it in a new file is a start
"""

bands_ls8_c2l2 = [('1', 'coastal_aerosol'),
             ('2', 'blue'),
             ('3', 'green'),
             ('4', 'red'),
             ('5', 'nir'),
             ('6', 'swir_1'),
             ('7', 'swir_2'),
             ('8', 'thermal_radiance'),
             ('9', 'quality_l2_aerosol')]

band_file_map_c2_africa = {
                  'coastal_aerosol' : 'FILE_NAME_BAND_1',
                  'blue' : 'FILE_NAME_BAND_2',
                  'green' : 'FILE_NAME_BAND_3',
                  'red' : 'FILE_NAME_BAND_4',
                  'nir' : 'FILE_NAME_BAND_5',
                  'swir_1' : 'FILE_NAME_BAND_6',
                  'swir_2' : 'FILE_NAME_BAND_7',
                  'thermal_radiance' : 'FILE_NAME_THERMAL_RADIANCE',
                  'quality_l2_aerosol' : 'FILE_NAME_QUALITY_L2_AEROSOL',
                }

band_file_map = {
                  'coastal_aerosol' : 'sr_band1',
                  'blue' : 'sr_band2',
                  'green' : 'sr_band3',
                  'red' : 'sr_band4',
                  'nir' : 'sr_band5',
                  'swir_1' : 'sr_band6',
                  'swir_2' : 'sr_band7',
                  'thermal_radiance' : 'st_thermal_radiance',
                  'quality_l2_aerosol' : 'pixel_qa',
                }

def satellite_ref(sat):
    """
    load the band_names for referencing LANDSAT8  USARD
    """
    if sat == 'LANDSAT_8':
        sat_img = bands_ls8_c2l2
        prod_type = 'c1l2scenealbers'
    else:
        raise ValueError('Satellite data Not Supported')
    return sat_img, prod_type

def get_band_file_map(item):
    return band_file_map[item]
