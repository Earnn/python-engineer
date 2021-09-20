from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TwitterTests(APITestCase):

    def test_get_tweets_by_hashtag_api_status_code(self):
        response = self.client.get('/hashtags/Python?limit=20', format='json')
        self.assertEqual(response.status_code, 200)

    def test_amount_of_result_of_get_tweets_by_hashtag_api(self):
        response = self.client.get('/hashtags/Python?limit=20', format='json')
        self.assertEqual(len(response.data["account"]), 20)
        response = self.client.get('/hashtags/Python', format='json')
        self.assertEqual(len(response.data["account"]), 30)

    def test_get_user_api_status_code(self):
        response = self.client.get('/users/twitter?limit=20', format='json')
        self.assertEqual(response.status_code, 200)

    def test_amount_of_result_of_get_user_api(self):
        response = self.client.get('/users/twitter?limit=10', format='json')
        self.assertEqual(len(response.data["account"]), 10)
        response = self.client.get('/users/twitter', format='json')
        self.assertEqual(len(response.data["account"]), 30)

    def test_get_correct_user(self):
        response = self.client.get('/users/DavikaH?limit=2', format='json') 
        isCorrect = True
        for obj in iter(response.data["account"]):
        	if "DavikaH" not in obj["href"]:
        		isCorrect = False

        self.assertEqual(isCorrect, True)
	
