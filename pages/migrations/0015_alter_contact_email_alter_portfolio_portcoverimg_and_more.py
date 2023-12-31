# Generated by Django 4.2.5 on 2023-10-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_portfolio_porturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portCoverImg',
            field=models.ImageField(upload_to='static/img'),
        ),
        migrations.DeleteModel(
            name='PortDetails',
        ),
    ]
