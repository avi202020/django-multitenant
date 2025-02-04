# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 11:51
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion

from django_multitenant.db import migrations as tenant_migrations


def get_operations():
    operations = [
        migrations.RunSQL(
            "ALTER TABLE tests_tenantnotidmodel DROP CONSTRAINT tests_tenantnotidmodel_pkey CASCADE;",
            reverse_sql="ALTER TABLE tests_tenantnotidmodel ADD CONSTRAINT tests_tenantnotidmodel_pkey PRIMARY KEY (tenant_column);",
        ),
        migrations.RunSQL(
            "ALTER TABLE tests_somerelatedmodel DROP CONSTRAINT tests_somerelatedmodel_pkey CASCADE;",
            reverse_sql="ALTER TABLE tests_somerelatedmodel ADD CONSTRAINT tests_somerelatedmodel_pkey PRIMARY KEY (related_tenant_id, id);",
        ),
    ]

    if settings.USE_CITUS:
        operations += [
            tenant_migrations.Distribute("TenantNotIdModel"),
            tenant_migrations.Distribute("SomeRelatedModel"),
        ]

    operations += [
        migrations.RunSQL(
            "ALTER TABLE tests_somerelatedmodel ADD CONSTRAINT tests_somerelatedmodel_pkey PRIMARY KEY (related_tenant_id, id);",
            reverse_sql="ALTER TABLE tests_somerelatedmodel DROP CONSTRAINT tests_somerelatedmodel_pkey CASCADE;",
        ),
        migrations.RunSQL(
            "ALTER TABLE tests_tenantnotidmodel ADD CONSTRAINT tests_tenantnotidmodel_pkey PRIMARY KEY (tenant_column);",
            reverse_sql="ALTER TABLE tests_tenantnotidmodel DROP CONSTRAINT tests_tenantnotidmodel_pkey CASCADE;",
        ),
    ]

    return operations


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0002_distribute"),
    ]

    operations = get_operations()
