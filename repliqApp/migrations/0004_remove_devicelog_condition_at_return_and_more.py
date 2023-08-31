# Generated by Django 4.2.4 on 2023-08-31 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repliqApp', '0003_devicelog_due_date_devicelog_is_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicelog',
            name='condition_at_return',
        ),
        migrations.AddField(
            model_name='devicelog',
            name='return_condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Used', 'Used'), ('Damaged', 'Damaged')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='condition_at_checkout',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Damaged', 'Damaged')], max_length=255),
        ),
    ]
