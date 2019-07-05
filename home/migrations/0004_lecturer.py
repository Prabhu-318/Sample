# Generated by Django 2.2.2 on 2019-07-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lect_name', models.CharField(max_length=30, null=True, unique=True, verbose_name='Lecturer Name')),
                ('d', models.CharField(blank=True, choices=[('ISE', 'Information Science'), ('ECE', 'Electronics and communication'), ('CV', 'Civil')], max_length=30, null=True, verbose_name='department')),
            ],
        ),
    ]