# Generated by Django 5.0.4 on 2024-07-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_certificate_resume_phone_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EducationFile',
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={},
        ),
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=models.FileField(upload_to='certificates/'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='about_me',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='additional_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='contacts',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='desired_position',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='work_experience',
            field=models.TextField(blank=True),
        ),
    ]