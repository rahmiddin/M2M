# Generated by Django 4.1.1 on 2022-09-10 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_scope_articles_alter_scope_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes1', to='articles.article'),
        ),
    ]
