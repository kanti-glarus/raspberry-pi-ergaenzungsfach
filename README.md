# Raspberry Pi

With this short instruction you can make your RaspberryPi ready for the development.

It explains:

- How to setup your Notebook and your Raspberry Pi.
- How to connect with the Raspberry Pi.
- How to code on the Raspberry Pi.

## Zugänge

**Netzwerk**

- SSID: raspi-net-local 
- psk/wpa2: raspberrypi 


**<a name="raspberrypi">Raspberry Pi</a>**

- IP: individuell
- User: `pi`
- Passwort: `kantiglarus`

**<a name="ssh">SSH-Verbindung</a>**

Via Kommandozeile:

```
ssh pi@<individual ip>
```

z.B. `ssh pi@192.168.23.123`

## Software

**Editor**

- Visual Studio Code
- Extensions:
  - Python
  - Remote - SSH

**Programmiersprache**

- Python

**Kommandozeile**

- cmd (bereits installiert)

**Verbindung**

- ssh (bereits installiert)
- Remotedesktopverbindung (bereits installiert)

## Verbindung

- Remotedesktopverbindung (bereits installiert)
  - Computer: `<individual IP>`
  - Benutzername: `pi`
  - Passwort: [siehe Raspberry Pi](#raspberrypi)

- SSH-Verbindung
  - [siehe SSH-Verbindung](#ssh)

- Remote-Verbindung in Visual Studio Code
  - Wähle `Remote-SSH: Connect to Host`
  - Tippe `pi@<individual IP>`
  - Gib das korrekte Passwort ein
  - Wähle `Linux` als Plattform, falls die Frage auftaucht
  - SSH-Verbindung wird nun aufgebaut
  - Wähle `Add Workspace Folder`: `/home/pi/projects`

  
## Basic Setup
 
**Komponenten**

- Raspberry Pi 4B
- Grove Pi+
- Micro-SD-Karte 16 GB
- Grove-LCD RGB Backlight v4.0
- Grove Verbindungskabel
- Stromkabel Raspberry Pi

## About this project

This project is an educational project at the [Kantonsschule Glarus](https://www.kanti-glarus.ch).
The project is initiated by [btemperli](https://github.com/btemperli). It takes place in the last year of the Computer Science / Informatik at the "Ergänzungsfach".
It is based on Raspberry Pi 4 & Grove Pi plus. 