# Generated by Django 4.0.3 on 2023-06-01 21:22

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200)),
                ('meeting_link', models.CharField(max_length=20, null=True)),
                ('position', models.CharField(max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('company_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('company_name', models.CharField(max_length=20, null=True)),
                ('company_description', models.CharField(max_length=50, null=True)),
                ('company_valuation', models.CharField(max_length=20, null=True)),
                ('company_employees', models.CharField(max_length=20, null=True)),
                ('company_investment', models.CharField(max_length=20, null=True)),
                ('company_type', models.CharField(choices=[('startup', 'Startup'), ('corporation', 'Corporation')], default='startup', max_length=20)),
                ('company_industry', models.CharField(choices=[('agriculture', 'Agriculture'), ('construction', 'Construction'), ('education', 'Education'), ('energy', 'Energy'), ('engineering', 'Engineering'), ('environment', 'Environment'), ('finance', 'Finance'), ('food-beverages', 'Food & Beverages'), ('healthcare', 'Healthcare'), ('hospitality', 'Hospitality'), ('information-technology', 'Information Technology'), ('internet', 'Internet'), ('legal', 'Legal'), ('logistics', 'Logistics'), ('manufacturing', 'Manufacturing'), ('media', 'Media'), ('mining', 'Mining'), ('music', 'Music'), ('pharmaceuticals', 'Pharmaceuticals'), ('public-administration', 'Public Administration'), ('real-estate', 'Real Estate'), ('recreation', 'Recreation'), ('retail', 'Retail'), ('science', 'Science'), ('services', 'Services'), ('technology', 'Technology'), ('telecommunications', 'Telecommunications'), ('textiles', 'Textiles'), ('transportation', 'Transportation'), ('travel', 'Travel')], default='agriculture', max_length=50)),
                ('interests', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('business-development', 'Business Development'), ('collaboration', 'Collaboration'), ('contracting-services', 'Contracting Services'), ('distribution', 'Distribution'), ('equity-investment', 'Equity Investment'), ('franchising', 'Franchising'), ('joint-venture', 'Joint Venture'), ('licensing', 'Licensing'), ('mergers-acquisitions', 'Mergers & Acquisitions'), ('outsourcing', 'Outsourcing'), ('product-development', 'Product Development'), ('research-development', 'Research & Development'), ('sales-marketing', 'Sales & Marketing'), ('sponsorship', 'Sponsorship'), ('strategic-alliance', 'Strategic Alliance'), ('supply-chain', 'Supply Chain'), ('technology-transfer', 'Technology Transfer'), ('venture-capital', 'Venture Capital'), ('white-labeling', 'White Labeling')], default='collaboration', max_length=20), blank=True, size=None)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=50, null=True)),
                ('interest', models.CharField(choices=[('business-development', 'Business Development'), ('collaboration', 'Collaboration'), ('contracting-services', 'Contracting Services'), ('distribution', 'Distribution'), ('equity-investment', 'Equity Investment'), ('franchising', 'Franchising'), ('joint-venture', 'Joint Venture'), ('licensing', 'Licensing'), ('mergers-acquisitions', 'Mergers & Acquisitions'), ('outsourcing', 'Outsourcing'), ('product-development', 'Product Development'), ('research-development', 'Research & Development'), ('sales-marketing', 'Sales & Marketing'), ('sponsorship', 'Sponsorship'), ('strategic-alliance', 'Strategic Alliance'), ('supply-chain', 'Supply Chain'), ('technology-transfer', 'Technology Transfer'), ('venture-capital', 'Venture Capital'), ('white-labeling', 'White Labeling')], default='collaboration', max_length=20)),
                ('receiver', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]