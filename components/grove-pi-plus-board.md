# Grove Pi+ Board

[Wiki-Eintrag](https://wiki.seeedstudio.com/GrovePi_Plus/)

## Anschluss
Das Board kann direkt auf den Raspberry Pi gesteckt werden.
Das funktioniert direkt über die GPIO-Pins. Die beiden Boards liegen, sofern korrekt angeschlossen, fast komplett übereinander.
Du findest [hier](https://wiki.seeedstudio.com/GrovePi_Plus/) die Seite des Projektes und siehst gleich dort, wie das Board aufgesetzt werden muss.

## Software
Damit das Grove Pi+ Board auf dem Raspberry Pi läuft und verbunden werden kann,
wird die Grove-Library verwendet. Diese ist in unserem [Image](../README.md#raspbian) bereits vorinstalliert.

## Firmware Aktualisieren
Wenn du ein neues Board in Betrieb nimmst, musst du ziemlich sicher zuerst die Firmware aktualisieren:

```bash
$ cd Dexter/GrovePi/Firmware
$ bash ./firmware_update.sh
$ sudo reboot
```