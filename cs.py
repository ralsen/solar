import socket
import threading
import json
import datetime
import time

# Konstanten
SERVER_HOST = '0.0.0.0'  # Lauschen auf allen Schnittstellen für den Server
CLIENT_SERVER_HOST = '192.168.2.2'  # IP-Adresse des Servers für den Client
PORT = 65432           # Port für die Verbindung

def handle_client(conn, addr, counter):
    print(f"Verbindung hergestellt mit {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            received_message = data.decode()
            
            # Prüfen, ob es ein JSON-Dictionary ist
            try:
                received_dict = json.loads(received_message)
                if isinstance(received_dict, dict):
                    print("Empfangener Counter", received_dict.get('counter'))
                    print("Empfangene Nachricht:", received_dict.get('message'))
                    print("Empfangenes Dictionary:", received_dict.get('dictionary'))
                    
                    # Antwort mit zusätzlichem Zähler
                    response_dict = {
                        'original_message': received_dict.get('message'),
                        'dictionary': received_dict.get('dictionary'),
                        'counter': str(datetime.datetime.now()) #.fromtimestamp(time.time()).strftime(('%d.%m.%Y %H:%M:%S'))
                    }
                    counter += 1
                    response_json = json.dumps(response_dict)
                    conn.sendall(response_json.encode())
            except json.JSONDecodeError:
                print("Ungültige Nachricht erhalten")
                conn.sendall(data)

def start_server():
    counter = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER_HOST, PORT))
        s.listen()
        print("Server läuft und wartet auf Verbindungen...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr, counter)).start()

def start_client():
    tier = {'Hund': 'wau', 'Katze': 'miau'}
    counter = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((CLIENT_SERVER_HOST, PORT))
        while True:
            msg = "Client message" #input("Nachricht eingeben: ")
            message_dict = {
                'counter': counter,
                'message': str(datetime.datetime.now()),
                'dictionary': tier
            }
            counter += 1
            time.sleep(1)
            msg_json = json.dumps(message_dict)
            s.sendall(msg_json.encode())
            data = s.recv(1024)
            received_response = json.loads(data.decode())
            print(f"Antwort vom Server: {received_response}")

def main():
    mode = input("Server (s) oder Client (c) starten? ")
    if mode == 's':
        start_server()
    elif mode == 'c':
        start_client()
    else:
        print("Ungültige Eingabe. Bitte 's' oder 'c' eingeben.")

if __name__ == "__main__":
    main()
