# We are creating this script to create fake data which will populate our model with dummy data
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","my_first_project.settings")


import django
django.setup()


# fake population script
import random

from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen=Faker()

topics=["Search","Social Media","Artificial Intelligence","News","Games","Sports"]


def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get random topic
        top=add_topic()

        # create the fake data for that entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()


        webpg=Webpage.objects.get_or_create(name=fake_name,url=fake_url,topic=top)[0]

        # Create Fake Access record
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=="__main__":
    print("Populating Script!")
    populate(15)
    print("Populating Complete")
