# Generated by Django 4.2.9 on 2024-03-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_customer_assigend_to_alter_whatsapp_messages_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
    ]
