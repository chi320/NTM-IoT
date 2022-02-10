import base64
from logging import exception

# The registeration api url, you can use IP or Domain.
api_url = 'http://localhost/csm'  # default

device_name = '01.IoTJP'
device_addr = "7fe83541-a9b4-4247-adc7-ae062bcd0425"

persistent_binding = True
username = 'iotjp'

# The Device Model in IoTtalk, please check IoTtalk document.
device_model = 'IoTJP_Device'

# The input/output device features, please check IoTtalk document.
idf_list = []
odf_list = ['PointCloud-O']


def on_register(dan):
    print('register successfully')


def PointCloud_O(data: list):
    '''Receive Point Cloud then save to file.

    Each point is XYZ coordinates which is consists of three int16 values, totaling 6 bytes.
    The Point Cloud data stream format is "XYZXYZXYZ...XYZXYZXYZ" and there are 92160 points, totaling 552,960 bytes.
    '''
    try:
        with open('Receive.bin', 'wb') as f:
            f.write(base64.b64decode(data[0]))
    except exception as e:
        print(e)
