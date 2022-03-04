import base64
import cv2
import os
from datetime import datetime
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

dir_path = 'received'


def on_register(dan):
    if os.path.isdir(dir_path):
        print('Path exists!')
    else:
        os.mkdir(dir_path)
        print('Create floder: {dir_path}')
    print('register successfully')


# def Picture_I():
#     '''Send raw data
#     '''
#     try:
#         with open('Send.jpg', 'rb') as f:
#             data = f.read()
#             return str(base64.b64encode(data).decode('ascii'))
#     except exception as e:
#         print(e)


# def Robot_I():
#     '''Send Robot data
#     '''
#     return str(uniform(0, 360))



def Picture_O(data: list):
    '''Receive raw data and save it
    '''
    try:
        file_name = datetime.now().isoformat().replace(':', '_')
        file = bytes(base64.b64decode(data[0]))
        file_path = f'{dir_path}/{file_name}.jpg'
        with open(file_path, 'wb') as f:
            f.write(file)
        
        img = cv2.imread(file_path)
        new_img = cv2.flip(img, 0)
        cv2.imshow('image', new_img)
        
        cv2.waitKey(1)        
        
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
