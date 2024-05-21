# Generated by Django 5.0.1 on 2024-03-14 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_Bank_Management_System', '0010_delete_user26'),
    ]

    operations = [
        migrations.CreateModel(
            name='User26',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group1', models.CharField(max_length=50)),
                ('blood_group2', models.IntegerField()),
            ],
            options={
                'db_table': 'User26',
            },
        ),
    ]
