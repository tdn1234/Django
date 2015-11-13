from django.contrib.auth.models import User
from django.test import TestCase

from userprofile.models import UserProfile


class ModelUserTestCase(TestCase):

    def test_avatar(self):
        user = UserProfile()
        user.user = User()
        self.assertEqual(user.get_user_avatar(), 'images/default.jpeg')
        path = 'images/bill.jpeg'
        user.avatar = path
        self.assertEqual(user.get_user_avatar(), path)
        user.user.username = 'bill'
        self.assertEqual('bill', user.__str__())
