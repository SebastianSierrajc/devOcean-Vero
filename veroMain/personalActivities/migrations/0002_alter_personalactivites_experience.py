# Generated by Django 3.2.7 on 2021-10-27 23:28


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalActivities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalactivites',
            name='experience',
            field=models.CharField(blank=True, default=10, max_length=1000000),
        ),
    ]