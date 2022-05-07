# Generated by Django 4.0.4 on 2022-05-07 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, to='chat.contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.ManyToManyField(blank=True, to='chat.message')),
                ('participants', models.ManyToManyField(related_name='chats', to='chat.contact')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.contact'),
            preserve_default=False,
        ),
    ]
