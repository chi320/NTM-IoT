import base64
from logging import exception
from random import  uniform

# The registeration api url, you can use IP or Domain.
api_url = 'http://localhost/csm'  # default

device_name = '01.IoTJP'
device_addr = "7fe83541-a9b4-4247-adc7-ae062bcd0422"

persistent_binding = True
username = 'iotjp'

# The Device Model in IoTtalk, please check IoTtalk document.
device_model = 'IoTJP_Device'

# The input/output device features, please check IoTtalk document.
idf_list = ['Picture-I', 'Robot-I']
odf_list = ['Picture-O', 'Robot-O']

push_interval = 10
interval = {
    'Picture-I': 3,
    'Robot-I': 1,
}


def on_register(dan):
    print('register successfully')


def Picture_I():
    '''Send raw data
    '''
    try:
        with open('Send.jpg', 'rb') as f:
            data = f.read()
            return str(base64.b64encode(data).decode('ascii'))
    except exception as e:
        print(e)


def Robot_I():
    '''Send Robot data
    '''
    return str(uniform(0, 360))



def Picture_O(data: list):
    '''Receive raw data and save it
    '''
    try:
        with open('Receive.jpg', 'wb') as f:
            f.write(base64.b64decode(data[0]))
    except exception as e:
        print(e)


def Robot_O(data: list):
    '''Receive Robot data
    '''
    try:
        with open('ReceiveRobotData.txt', 'w') as f:
            print(data[0])
            f.write(str(data[0]))
    except exception as e:
        print(e)
