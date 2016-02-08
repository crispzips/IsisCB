# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 19:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftACRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_on', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False, help_text='Indicates whether or not a record has been inspected, and a corresponding entry/entries in isisdata have been created. When True, a record should be hidden from the curation interface by default.')),
                ('type_controlled', models.CharField(max_length=2)),
                ('type_broad_controlled', models.CharField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_on', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False, help_text='Indicates whether or not a record has been inspected, and a corresponding entry/entries in isisdata have been created. When True, a record should be hidden from the curation interface by default.')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftAuthority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_on', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False, help_text='Indicates whether or not a record has been inspected, and a corresponding entry/entries in isisdata have been created. When True, a record should be hidden from the curation interface by default.')),
                ('name', models.CharField(max_length=1000)),
                ('name_last', models.CharField(blank=True, max_length=255, null=True)),
                ('name_first', models.CharField(blank=True, max_length=255, null=True)),
                ('name_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('type_controlled', models.CharField(blank=True, max_length=2, null=True)),
                ('imported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftAuthorityLinkedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_on', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False, help_text='Indicates whether or not a record has been inspected, and a corresponding entry/entries in isisdata have been created. When True, a record should be hidden from the curation interface by default.')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('authority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linkeddata', to='zotero.DraftAuthority')),
                ('imported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftCitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_on', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False, help_text='Indicates whether or not a record has been inspected, and a corresponding entry/entries in isisdata have been created. When True, a record should be hidden from the curation interface by default.')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('type_controlled', models.CharField(blank=True, max_length=2, null=True)),
                ('publication_date', models.CharField(blank=True, max_length=100, null=True)),
                ('page_start', models.CharField(blank=True, max_length=10, null=True)),
                ('page_end', models.CharField(blank=True, max_length=10, null=True)),
                ('volume', models.CharField(blank=True, max_length=10, null=True)),
                ('issue', models.CharField(blank=True, max_length=10, null=True)),
                ('imported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftCitationLinkedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imported_on', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False, help_text='Indicates whether or not a record has been inspected, and a corresponding entry/entries in isisdata have been created. When True, a record should be hidden from the curation interface by default.')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('citation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linkeddata', to='zotero.DraftCitation')),
                ('imported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldResolutionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_field', models.CharField(max_length=100)),
                ('for_value', models.CharField(max_length=1000)),
                ('to_value', models.CharField(max_length=1000)),
                ('for_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fieldresolutions_for', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='InstanceResolutionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_instance_id', models.PositiveIntegerField()),
                ('to_instance_id', models.PositiveIntegerField()),
                ('for_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instanceresolutions_for', to='contenttypes.ContentType')),
                ('to_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instanceresolutions_to', to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='draftattribute',
            name='citation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='zotero.DraftCitation'),
        ),
        migrations.AddField(
            model_name='draftattribute',
            name='imported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='draftacrelation',
            name='authority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citation_relations', to='zotero.DraftAuthority'),
        ),
        migrations.AddField(
            model_name='draftacrelation',
            name='citation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authority_relations', to='zotero.DraftCitation'),
        ),
        migrations.AddField(
            model_name='draftacrelation',
            name='imported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
