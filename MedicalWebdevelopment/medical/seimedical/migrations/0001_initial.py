# Generated by Django 3.2.9 on 2022-06-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30, null=True)),
                ('Email', models.EmailField(max_length=30, null=True)),
                ('Number_of_Passport', models.CharField(max_length=30, null=True)),
                ('Contact_number', models.CharField(max_length=30, null=True)),
                ('Name_of_medical_examiner', models.TextField(max_length=30, null=True)),
                ('Approvel_number', models.TextField(max_length=50, null=True)),
                ('Job_title', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('feedback', models.TextField(max_length=50)),
            ],
        ),
    ]