# Generated by Django 4.1.1 on 2022-09-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_article_articles_tag_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.tag'),
        ),
    ]
