from google.cloud import pubsub_v1
import os
import unittest

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/buddy/buddypal/buddypal-118be5edd0f1.json"
topic_name = 'projects/buddypal/topics/BuddyPal'


def tests_pass():
    publisher = pubsub_v1.PublisherClient()
    publisher.publish(topic_name, b'Passed')
    print("Tests passed")


def tests_fail():
    publisher = pubsub_v1.PublisherClient()
    publisher.publish(topic_name, b'Failed')
    print("Tests failed")


class TestStringMethods(unittest.TestCase):

    def test_add_two_numbers(self):
        assert

if __name__ == '__main__':
    unittest.main()
