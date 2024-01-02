# Generated by Django 5.0 on 2024-01-02 11:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
