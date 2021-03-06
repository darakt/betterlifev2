# Generated by Django 3.2.13 on 2022-04-29 09:46

from django.conf import settings
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='written_by',
            field=models.ForeignKey(db_column='written_by', default=1, on_delete=models.SET(users.models.get_owner_for_deleted_comment), related_name='has_written', to=settings.AUTH_USER_MODEL),
        ),
    ]
