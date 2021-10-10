import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProjectTwo.settings")
import django
django.setup()


# Fake script
import random
from ProjectApp.models import Userinfo
from faker import Faker

fake_gen=Faker()


def populate(n=5):
    for entry in range(n):
        fake_name=fake_gen.name().split()
        f_name=fake_name[0]
        last_name=fake_name[1]
        fake_email=fake_gen.email()

        user=Userinfo.objects.get_or_create(name=f_name,l_name=last_name,email=fake_email)[0]



if __name__=="__main__":
    print("Populating Databases")
    populate(15)
    print("complete!")
