# IoT for 2022 TAIWAN INTERNATIONAL LIGHT FESTIVAL

This project is only for the 2022 TAIWAN INTERNATIONAL LIGHT FESTIVAL.  
It is based on [Dummy_Device_IoTtalk_v2_py](https://github.com/IoTtalk/Dummy_Device_IoTtalk_v2_py).

## Requirements
* python 3.6+

## [Python Virtual Environment](https://docs.python.org/3/tutorial/venv.html) (recommend)

```bash
python3 -m venv /path/to/venv/dir       # create venv
source /path/to/venv/dir/bin/activate   # activate venv
```

If OS is Windows:

```shell
python3 -m venv venv       # create venv
.\venv\Scripts\activate    # activate venv
```

## Install dependencies

```bash
pip install iottalk-py
```

## Config IoTtalk Server URL

Please set the variable ```api_url``` in ```sa.py```.

## Start

```bash
python3 -m iottalkpy.dai sa.py
```

## Data
This example will generate random robot data and read `Send.bin` file and send.  
And will receive robot data and `Send.bin` binary data, and then save to `ReceiveRobotData.txt` and `Receive.bin`.

* Robot
  * data format: `[float, float]`
* `Send.bin`
  * data format: `binary`