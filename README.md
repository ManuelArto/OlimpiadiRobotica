# Olimpiadi_Robotica_Public

Tema: Realizzare un progetto in ambito sociale che possa essere utile per le persone affette da disabilità.


Il progetto ha l’obiettivo di integrare in uno stesso sistema la gestione dei vari dispositivi domotici interni della casa 
per agevolare le persone con ridotte funzionalità.
Il progetto fa uso della scheda makey makey, due Raspberry PI e un sonoff. 

Ci sono due python file: uno per il Raspberry connesso alla camera chiamato "Camera.py" nella cartella "Raspberry_Camera", l'altro per il Raspberry connesso al LCD hdmi screen e alla scheda makey makey chiamato "Easy_Streamer.py" nella cartella "Raspberry_Makey".

Per eseguire il file Camera.py dovrai scaricare la libreria RPLCD e il modulo Rpi.GPIO.

Per eseguire il file Easy_Streamer.py dovrai scaricare la libreria opencv-python. Avrai anche bisogno di create un IFTTT account e creare un applet che ti permette di accendere e spegnere un sonoff via una richiesta web. Dovrai successivamente inserire la chiave nel programma. Poi dovrai inserire nel file Mail.py le credenziali dell'account gmail da dove vorrai mandare la email.
