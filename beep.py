import subprocess
import nfc

def on_connect(tag):
    print (tag._nfcid)

cnt = 0
while True:
    with nfc.ContactlessFrontend('usb:054c:06c1') as cf:
        cf.connect(rdwr={'on-connect': on_connect})

        cnt = cnt % 3

        if cnt == 0:
            subprocess.call("mpg321 /home/pi/projects/pipi/pipi.mp3", shell=True)
        elif cnt == 1:
            subprocess.call("mpg321 /home/pi/projects/pipi/pinpon.mp3", shell=True)
        elif cnt == 2:
            subprocess.call("mpg321 /home/pi/projects/pipi/pyui.mp3", shell=True)

        cnt += 1
