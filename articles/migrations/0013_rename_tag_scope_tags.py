# Generated by Django 4.1.1 on 2022-09-10 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_scope_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='tag',
            new_name='tags',
        ),
    ]
