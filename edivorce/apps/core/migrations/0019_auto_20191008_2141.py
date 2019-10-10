# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-10-08 21:41
from __future__ import unicode_literals

from django.db import migrations

def string_to_json(apps, schema_editor):
    Responses = apps.get_model('core', 'UserResponse')
    for response in Responses.objects.filter(question_id='child_support_act'):
        if not (response.value.startswith('["') and response.value.endswith('"]')):
            response.value = '["%s"]' % (response.value)
            response.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_bceiduser_has_accepted_terms'),
    ]

    operations = [
        migrations.RunPython(string_to_json),
    ]
