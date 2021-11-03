import unittest
import requests
from server_constants import API_URL

class FlaskTests(unittest.TestCase):

    GET_USERS_URL="{}/getusers".format(API_URL)
    ADD_USER_URL="{}/adduser".format(API_URL)
    USER={
        "first_name":"Israel",
        "last_name": "Israeli",
        "user_id": "06854571"
    }
    def test_get_all_users(self):
        response = requests.get(self.GET_USERS_URL)
        self.assertEqual(response.status_code,200)

    def test_add_new_user(self):
        response = requests.post(self.ADD_USER_URL,json=self.USER)
        self.assertEqual(response.status_code,201)