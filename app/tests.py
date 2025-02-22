from django.test import TestCase ,override_settings
from django.test.client import Client
from http import HTTPStatus
# Create your tests here.


class IPBlackListMiddlewareTest(TestCase):
    def setUp(self):
        self.client=Client()
        
    @override_settings(BANNED_IPS=None)  
    def test_request_successful_without_blacklist_setting(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,HTTPStatus.OK)
    @override_settings(BANNED_IPS=['192.168.1.2'])  
    def test_request_successful_without_blacklist_setting_1(self):
        response = self.client.get('/',REMOTE_ADDR="192.168.1.3")
        self.assertEqual(response.status_code,HTTPStatus.OK)
    @override_settings(BANNED_IPS=['192.168.1.2'])  
    def test_request_successful_without_blacklist_setting_2(self):
        response = self.client.get('/',REMOTE_ADDR="192.168.1.2")
        self.assertEqual(response.status_code,HTTPStatus.FORBIDDEN)