# Generated by Django 4.0.3 on 2023-06-01 23:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_sender_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_employees',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_investment',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_type',
            field=models.CharField(choices=[('startup', 'Startup'), ('corporation', 'Corporation')], default='startup', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_valuation',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('business-development', 'Business Development'), ('collaboration', 'Collaboration'), ('contracting-services', 'Contracting Services'), ('distribution', 'Distribution'), ('equity-investment', 'Equity Investment'), ('franchising', 'Franchising'), ('joint-venture', 'Joint Venture'), ('licensing', 'Licensing'), ('mergers-acquisitions', 'Mergers & Acquisitions'), ('outsourcing', 'Outsourcing'), ('product-development', 'Product Development'), ('research-development', 'Research & Development'), ('sales-marketing', 'Sales & Marketing'), ('sponsorship', 'Sponsorship'), ('strategic-alliance', 'Strategic Alliance'), ('supply-chain', 'Supply Chain'), ('technology-transfer', 'Technology Transfer'), ('venture-capital', 'Venture Capital'), ('white-labeling', 'White Labeling')], default='collaboration', max_length=50, null=True), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='meeting_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
