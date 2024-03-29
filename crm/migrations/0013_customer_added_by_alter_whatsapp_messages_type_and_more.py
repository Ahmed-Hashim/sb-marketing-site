# Generated by Django 4.2.9 on 2024-03-07 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0012_alter_customer_assigend_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('VIDEO', 'VIDEO'), ('TEXT', 'TEXT'), ('IMAGE', 'IMAGE')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('VIDEO', 'VIDEO'), ('TEXT', 'TEXT'), ('IMAGE', 'IMAGE')], default='TEXT', max_length=10),
        ),
    ]
