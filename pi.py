from gpiozero import LED, Buzzer
from time import sleep

ledRed = LED(17)
ledGreen = LED(18)
buzzer = Buzzer(27)

buildFailed = False

while buildFailed:
    ledRed.on()
    buzzer.on()
    sleep(1)
    ledRed.off()
    buzzer.off()
    sleep(1)

while not buildFailed:
    ledGreen.on()