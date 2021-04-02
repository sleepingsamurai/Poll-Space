# Generated by Django 3.1.5 on 2021-04-02 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_question', models.TextField()),
                ('poll_option1', models.CharField(max_length=100)),
                ('poll_option2', models.CharField(max_length=100)),
                ('poll_option3', models.CharField(max_length=100)),
                ('poll_option4', models.CharField(max_length=100)),
                ('poll_option1_count', models.IntegerField(default=0)),
                ('poll_option2_count', models.IntegerField(default=0)),
                ('poll_option3_count', models.IntegerField(default=0)),
                ('poll_option4_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.polls')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]