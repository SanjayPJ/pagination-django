import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mysite.settings')

import django
django.setup()

import random
from blog.models import Article
from faker import Faker

fakegen = Faker()

for i in range(20):
    fake_title = fakegen.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    fake_body = fakegen.paragraph(nb_sentences=300, variable_nb_sentences=True, ext_word_list=None)
    user1 = Article.objects.get_or_create(title=fake_title, body=fake_body)