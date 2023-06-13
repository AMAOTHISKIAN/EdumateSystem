@Online

sudo apt-get update 
sudo apt-get install libgdal-dev
GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'

except if not work
 sudo apt-get install build-essential python3-dev



@Offline

import os
os.environ['GDAL_LIBRARY_PATH'] = os.path.join(BASE_DIR, 'lib', 'libgdal.so')
