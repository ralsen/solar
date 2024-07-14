#!/usr/bin/env python3 xxx
# -*- coding: utf-8 -*-
import logging
import yaml
import socket
import datetime
import os
import time

logger = logging.getLogger(__name__)

def init(ProgName):
    global ini

    ini = {}
    current_dir = os.getcwd()
    current_dir += '/..'
    with open(f'{current_dir}/yml/config.yml', 'r') as ymlfile:
        yml = yaml.safe_load(ymlfile)

    RootPath = current_dir #yml['ROOT_PATH']
    ini['LogPath'] = RootPath + yml['pathes']['LOG']
    ini['DataPath'] = RootPath + yml['pathes']['DATA']
    ini['RRDPath'] = RootPath + yml['pathes']['RRD']
    ini['YMLPath'] = RootPath + yml['pathes']['YML']
    ini['DevServerName'] = yml['Communication']['DevServerName']
    ini['DevServerPort'] = yml['Communication']['DevServerPort']
    ini['debugdatefmt'] = yml['debug']['datefmt']
    ini['logSuffix'] = yml['suffixes']['log']
    ini['dataSuffix'] = yml['suffixes']['data']
    ini['humanTimestamp'] = yml['misc']['humanTimestamp']
    ini['Mailing'] = yml['debug']['Mailing']
    ini['ShellyMeter'] = yml['Communication']['ShellyMeter']
    ini['ShellyMeterSleep'] = yml['Timers']['ShellyMeterSleep']
    

    """
    data = dict()
    data["System"] = dict()
    data["System"]["MyName"] = socket.getfqdn()
    data["System"]["My_IP"] = socket.gethostbyname(data["System"]["MyName"])
    data["System"]["starttime_ticks"] = int(time.time())
    data["System"]["starttime_app"] = datetime.datetime.fromtimestamp(time.time()).strftime(('%d.%m.%Y %H:%M:%S'))
    data["System"]["uptime_app"] = 0
    data["System"]["uptime_sys"] = 0
    data["System"]["ProgName"] = ProgName
    """


