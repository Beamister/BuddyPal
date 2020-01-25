from google.cloud import pubsub_v1

topic_name = 'projects/buddypal/topics/BuddyPal'


def tests_pass():
    print("Tests passed")


def tests_fail():
    print("Tests failed")


tests_fail()

publisher = pubsub_v1.PublisherClient()
publisher.publish(topic_name, b'My first message!')
print("Published")
