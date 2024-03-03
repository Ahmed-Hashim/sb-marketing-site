# Generated by Django 4.2.9 on 2024-03-03 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_position'),
        ('crm', '0011_customer_time_date_to_meeting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='assigend_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='members.profile'),
        ),
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('IMAGE', 'IMAGE'), ('PDF', 'PDF'), ('VIDEO', 'VIDEO')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('IMAGE', 'IMAGE'), ('PDF', 'PDF'), ('VIDEO', 'VIDEO')], default='TEXT', max_length=10),
        ),
    ]
