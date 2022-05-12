# Preparation

Wie wird das Raspberry Projekt vorbereitet?

## SD-Karte vorbereiten

1. Raspberry Pi OS Image auf SD-Karte laden, siehe [Software](https://www.raspberrypi.com/software/)
2. User definieren:
   1. `$ cd /Volumes/boot; touch userconf`
   2. Passwort generieren: `echo 'mypassword' | openssl passwd -stdin`
   3. Inhalt abfüllen: `username:output-of-mypassword`
3. SSH aktivieren: leere `ssh`-Datei auf die Karte ins `root`-Verzeichnis laden.
    1. `$ cd /Volumes/boot; touch ssh`
4. Wifi-Setup vornehmen, so dass sich das Raspberry Pi direkt verbinden kann
    1. `$ cd /Volumes/boot; touch wpa_supplicant.conf`
    1. `$ nano wpa_supplicant.conf`
    1. Inhalt abfüllen:
        ``` 
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1
        country=CH

        network={
            ssid="raspi-net-local"
            psk="raspberrypi"
        }
        ```
5. SD-Karte in Raspberry Pi einstecken und starten.
6. Mit der IP-Adresse des Raspberry Pi's verbinden: `$ ssh pi@192.168.1.xxx`
    1. Passwort: `raspberry`
7. Neues Passwort setzen: `$ passwd`
    1. Altes Passwort `raspberry` eingeben
    1. Neues Passwort `kantiglarus` eingeben
    1. Neues Passwort `kantiglarus` wiederholen
8. Updaten: `$ sudo apt-get update`
9. Upgraden: `$ sudo apt-get upgrade`
10. VNC aktivieren für Windows `Remotedesktopverbindung`: `$ sudo apt-get install xrdp`
11. Folgende Dienste im `raspi-config` aktivieren
     1. `Interfacing Options` / `VNC`
     1. `Interfacing Options` / `Camera`
     1. `Interfacing Options` / `I2C`
     1. `Advanced Options` / `Expand Filesystem` (SD-Karte voll ausnützen)
12. Grove Pi installieren:
     1. `$ sudo curl -kL dexterindustries.com/update_grovepi | bash`
     1. `$ sudo reboot`
     1. `$ cd Dexter/GrovePi/Firmware; bash ./firmware_update.sh` (hint: evtl `sudo ./firmware_update.sh`)
     1. `$ cd Dexter/GrovePi/Script; sudo bash ./install.sh`
     1. `$ cd Dexter/GrovePi/Script; bash ./update_grovepi.sh`
13. Nach Bedarf .alias-File anpassen:
14. Projektordner erstellen und unsere [Beispiele](../projects) kopieren.
15. Die Datei `/home/pi/projects/ip/ip-output.sh` als `service` ausführen:
     1. `$ sudo systemctl edit --force --full show_ip.service`
     2. Folgenden Inhalt abfüllen:
         ```
         [Unit]
         Description=My Script Service
         Wants=network-online.target
         After=network-online.target
    
         [Service]
         Type=simple
         User=pi
         WorkingDirectory=/home/pi
         ExecStart=/home/pi/projects/ip/ip-output.sh
    
         [Install]
         WantedBy=multi-user.target
         ```
     3. Service checken: `$ systemctl status show_ip.service`
     4. Service aktivieren: `$ systemctl enable show_ip.service`
     5. Service starten: `$ systemctl start show_ip.service`
   
16. Testen
17. Image erstellen:
     1. `$ diskutil list`
     1. Boot-Disk wird in etwa so ausschauen: `/dev/disk2`
     1. Image erstellen: `$ sudo dd if=/dev/rdisk2 of=/pfad/von/image.img`
    
## Image verteilen

1. Boot-Disk finden: `$ diskutil list`
1. Disk unmounten: `$ diskutil unmountDisk /dev/disk2`
1. Image auf Disk laden: `$ sudo dd if=/pfad/von/image.img of=/dev/rdisk2 bs=1m`