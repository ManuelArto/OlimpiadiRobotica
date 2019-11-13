# Olimpiadi_Robotica_Public

Tema: Realizzare un progetto in ambito sociale che possa essere utile per le persone affette da disabilità.


Il progetto ha l’obiettivo di integrare in uno stesso sistema la gestione dei vari dispositivi domotici interni della casa 
per agevolare le persone con ridotte funzionalità.
Il progetto fa uso della scheda makey makey, due Raspberry PI e un sonoff. 

There are two python file, one for the raspberry connected to the camera named "Camera.py" in the folder "Raspberry_Camera" and the other one for the raspberry connected to the LCD hdmi screen and the makey makey board named "Easy_Streamer.py" in the folder "Raspberry_Makey".

For running the Camera.py file you will need to download the library RPLCD and the Rpi.GPIO module.

For running the Easy_Streamer.py file you will need to install the library opencv-python. You have also to create an IFTTT account and create an applet that let you turn On or Off the sonoff via a web request. Then you need to insert your key in the program. Then you have to insert in the Mail.py file the email and password of the gmail account from where you want to send the email.  
