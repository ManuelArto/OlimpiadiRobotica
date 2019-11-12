""" Author: Arto Manuel, Gabriele Genovese, Federico Crescentini
    MAKEY MAKEY CHALLENGE
    ############################################################
    This is the program running on the Raspberry connected to the LCD 5 inches screen.
    It capture the streaming from the camera of the other raspberry.
    There are three actions activated by the input of a button connected to the makey makey board:
        - Door: send a message to the Raspberry_Camera to simulate the opening and closing of the door
        - Sonoff: send a request to my ifttt account that turn on or off a defined sonoff connected to a light
        - Mail: send an email of help to the person of a defined list
"""
import cv2
import threading
import requests
from Mail import Mail


door_event = {False: 'closeDoor', True: 'openDoor'}  # HTTP
closed = False
def door():
    print("door")
    try:
        global closed
        while True:
            r = requests.get(f"http://192.168.0.101:8000/{door_event[closed]}")     # IP of the Raspberry_Camera
            if r.status_code == 200:
                break
        closed = not closed
    except Exception:
        print("UNABLE TO SEND COMMAND TO SONOFF\n")


sonoff_event = {False: 'turn_ON', True: 'turn_OFF'}  # IFTTT
state = True
def sonoff():
    print("sonoff")
    try:
        global state
        while True:
            r = requests.post(
                f"https://maker.ifttt.com/trigger/{sonoff_event[state]}/with/key/{YOUR_IFTTT_KEY}")
            if r.status_code == 200:
                break
        state = not state
    except Exception:
        print("UNABLE TO SEND COMMAND TO SONOFF\n")


mail = Mail()
def email():
    print("email")
    mail.send()


cap = cv2.VideoCapture('http://192.168.0.101:8000/stream.mjpg')     # IP of the Raspberry_Camera
def start_stream():
    cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Video', frame)

        key = cv2.waitKey(10)
        if key in actions.keys():
            t = threading.Thread(target=actions[key])
            t.start()
        elif key == ord('q'):
            exit(0)


actions = {
    ord('d'): door,
    ord('s'): sonoff,
    ord('e'): email
}

if __name__ == '__main__':
    start_stream()
