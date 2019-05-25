# Generated by Django 2.2.1 on 2019-05-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('total_score', models.IntegerField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors.Professor')),
            ],
        ),
    ]
