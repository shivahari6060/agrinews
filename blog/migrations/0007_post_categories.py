# Generated by Django 3.0.4 on 2020-04-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
