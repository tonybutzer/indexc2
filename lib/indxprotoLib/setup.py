from setuptools import setup

setup(name='indxprotoLib',
      maintainer='Tony Butzer',
      maintainer_email='tonybutzer@gmail.com',
      version='1.0.1',
      description='helper functions for indexing collection2 from xml/MTL ',
      packages=[
          'indxprotoLib',
      ],
      install_requires=[
          #'folium',
          'elasticsearch',
          # 'boto3',
          #'pyproj',
      ],

      )
