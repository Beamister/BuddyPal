from google.cloud import pubsub_v1
from picamera import PiCamera
from gpiozero import LED, Buzzer
from time import sleep
import os
import datetime

ledRed = LED(17)
ledGreen = LED(18)
buzzer = Buzzer(27)
camera = PiCamera()

subscription_path = 'projects/buddypal/subscriptions/BuddyPal-Sub'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/pi/BuddyPal/buddypal-ee7296cbe411.json"
subscriber = pubsub_v1.SubscriberClient()

buildFailed = False


def check_message(message):
    global buildFailed
    message_contents = message.data.decode()
    if message_contents == 'Passed':
        buildFailed = False
    else:
        buildFailed = True
        timestamp = datetime.datetime.now().strftime('%d:%m:%Y-%H:%M:%S')
        camera.capture('/home/pi/BuddyPal/images/' + timestamp + '.jpg')
        print("Image captured")
    message.ack()


future = subscriber.subscribe(subscription_path, check_message)


while True:
    if buildFailed:
        ledGreen.off()
        ledRed.on()
        buzzer.on()
        sleep(1)
        ledRed.off()
        buzzer.off()
        sleep(1)

    else:
        ledRed.off()
        buzzer.off()
        ledGreen.on()
