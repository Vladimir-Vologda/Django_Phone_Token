from django.test import TestCase

from users.sendler import send_code


class TestSendlerCode(TestCase):

    def test_generate_code(self):

        self.phone = ''
        self.code = send_code(phone=self.phone)
        self.str_code = str(self.code)

        self.assertTrue(self.code)
        self.assertEqual(len(self.str_code), 5)

        # print(self.code)
