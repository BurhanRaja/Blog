# Generated by Django 4.0.3 on 2022-04-26 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_reply',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.comment'),
        ),
    ]
