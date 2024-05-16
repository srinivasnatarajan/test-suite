import hashlib
import os
import random
import uuid
from datetime import datetime
from time import time
from uuid import UUID
from faker import Faker


from openpyxl import Workbook


class RandomValues:
    @staticmethod
    def random_string(size: int = 5):   # includes numbers+characters
        return hashlib.md5(os.urandom(128)).hexdigest()[:int(size)]

    @staticmethod
    def random_alphaString(size: int):  # only characters
        fake = Faker()
        char_list = fake.random_letters(size)
        s = [char.upper() for char in char_list]
        return ''.join(s)

    @staticmethod
    def random_integer(digits: int) -> int:
        return random.randint(10 ** (int(digits) - 1), 10 ** int(digits))

    @staticmethod
    def random_email_id() -> str:
        domains = ["hotmail.com", "gmail.com", "aol.com",
                   "mail.com", "mail.kz", "yahoo.com"]
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        return 'automation_vnruser_' + str(random.choice(letters)) + str(RandomValues.random_integer(5)) + '@' + str(
            random.choice(domains))

    @staticmethod
    def get_random_mobile_number(code: str = '91') -> str:
        return code + str(random.randint(7000000000, 8999999999))

    @staticmethod
    def generate_coupon_file(self, sku_id, denomination, no_of_coupons=5, with_redeemLink=True, with_pin=True, only_couponCode=False):
        coupons = []
        for _ in range(self.no_of_coupon):
            random_uuid = uuid.uuid4()
            code = ''.join(random_uuid.hex)
            coupons.append('BULK_TRS07' + code[:18])
        return list(set(coupons))

    def generate_coupons(self, no_of_coupons=5):
        coupons = []
        for _ in range(no_of_coupons):
            random_uuid = uuid.uuid4()
            code = ''.join(random_uuid.hex)
            coupons.append('BULK_TRS07' + code[:18])
        return list(set(coupons))

    def get_date_and_time(self, millisecond=False):
        if not millisecond:
            return datetime.now()
        else:
            return int(time() * 1000)

    @staticmethod
    def get_uuid() -> UUID:
        return uuid.uuid4()

    @staticmethod
    def generate_name():
        fake = Faker()
        return fake.word()

    @staticmethod
    def generate_first_name():
        fake = Faker()
        return fake.first_name()

    @staticmethod
    def generate_last_name():
        fake = Faker()
        return fake.last_name()

    @staticmethod
    def generate_email():
        fake = Faker()
        return fake.email()

    @staticmethod
    def generate_password():
        fake = Faker()
        return fake.password()
