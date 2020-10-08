# Generated by Django 2.2.15 on 2020-10-06 20:14

from django.db import migrations

def migrate_name_forward(apps, schema_editor):
    UserResponse = apps.get_model('core', 'UserResponse')
    name_you_responses = UserResponse.objects.filter(question_id='name_you')
    print(f"Converting {name_you_responses.count()} name_you responses")
    for response in name_you_responses:
        response.question_id = 'last_name_you'
        response.save()
    name_spouse_responses = UserResponse.objects.filter(question_id='name_spouse')
    print(f"Converting {name_spouse_responses.count()} name_spouse responses")    
    for response in name_spouse_responses:
        response.question_id = 'last_name_spouse'
        response.save()


def migrate_name_backwards(apps, schema_editor):
    UserResponse = apps.get_model('core', 'UserResponse')
    last_name_you_responses = UserResponse.objects.filter(question_id='last_name_you')
    print(f"Converting {last_name_you_responses.count()} last_name_you responses")
    for response in last_name_you_responses:
        response.question_id = 'name_you'
        response.save()
    last_name_spouse_responses = UserResponse.objects.filter(question_id='last_name_spouse')
    print(f"Converting {last_name_spouse_responses.count()} last_name_spouse responses")    
    for response in last_name_spouse_responses:
        response.question_id = 'name_spouse'
        response.save()    


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200928_1157'),
    ]

    operations = [
        migrations.RunPython(migrate_name_forward, migrate_name_backwards)
    ]
