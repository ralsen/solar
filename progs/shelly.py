from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import urllib.parse
import traceback
import time
import socket
import datetime
import threading
import sys
import logging 
import os
import json
import time


import config as cfg

logger = logging.getLogger(__name__)
logging.getLogger('urllib3').setLevel(logging.WARNING)

counter = 0

if __name__ == '__main__':
    current_file_path = os.path.realpath(__file__)
    current_file_name = os.path.basename(current_file_path)

    cfg.init(current_file_name)
    x = datetime.datetime.now()

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s :: %(levelname)-7s :: [%(name)+15s] [%(lineno)+3s] :: %(message)s',
        datefmt=cfg.ini['debugdatefmt'],
        handlers=[
            logging.FileHandler(f"{cfg.ini['LogPath']}/{current_file_name[:-3]}_{socket.gethostname()+x.strftime(cfg.ini['logSuffix'])}.log"),
            logging.StreamHandler()
        ])

    logger.info("")
    logger.info(f'---------- starting {current_file_path} at {x} ----------') 

    ServerName = cfg.ini['DevServerName']
    ServerPort = cfg.ini['DevServerPort']

    response = requests.get(cfg.ini['ShellyMeter'])

    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        data = response.json()
        print("Erfolgreich abgerufen:")
        powerdif = data['total']
        print(f"Total: {data['total']}")
        print('-----------------------')
    else:
        logger.error(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
    while True: # Daten abrufen
        response = requests.get(cfg.ini['ShellyMeter'])

        # Überprüfen, ob die Anfrage erfolgreich war
        if response.status_code == 200:
            data = response.json()
            print(f"Erfolgreich abgerufen nach {round(counter/60, 2)} Minuten")
            print(f"Power: {data['power']} W")
            print(f"Total: {data['total']} Wm")
            print(f"diff:  {data['total'] - powerdif} Wm ≙ {round((data['total'] - powerdif)/60000, 2)} kWh")
        else:
            logger.info(f"Fehler beim Abrufen der Daten: {response.status_code}")
        
        dataset = {}
        dataset['name'] = 'Solar'
        dataset['Type'] = 'Shelly_Plug'        
        dataset['Power'] = data['power']
        dataset['Total'] = data['total']
        dataset['diff_Wm'] = data['total'] - powerdif
        dataset['diff_kWh'] = round((data['total'] - powerdif)/60000, 2)
        url = 'http://' + f"{cfg.ini['DevServerName']}:{cfg.ini['DevServerPort']}"
        headers = {
            'Content-Type': 'application/json'
            }

        response = requests.post(url, data=json.dumps(dataset), headers=headers)

        #print(f'Status Code: {response.status_code}')
        print(f'Response: {response.text}')
        print('-----------------------')
        time.sleep(cfg.ini['ShellyMeterSleep'])
        counter += cfg.ini['ShellyMeterSleep']
