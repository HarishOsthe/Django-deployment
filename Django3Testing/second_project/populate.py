import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()



import random
from second_app.models import AccessRecords,WebPage,Topic
from faker import Faker


fakegen = Faker()
topics = ['Social','Search','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate_data(N=5):
    for entry in range(N):
        top = add_topic
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecords.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate_data(20)
    print("Populating complete")
