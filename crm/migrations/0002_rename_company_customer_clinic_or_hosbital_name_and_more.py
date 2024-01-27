# Generated by Django 4.2.9 on 2024-01-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='company',
            new_name='clinic_or_hosbital_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='industry',
            field=models.CharField(default='غير معلوم', max_length=120),
        ),
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('PDF', 'PDF'), ('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('PDF', 'PDF'), ('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE')], default='TEXT', max_length=10),
        ),
    ]