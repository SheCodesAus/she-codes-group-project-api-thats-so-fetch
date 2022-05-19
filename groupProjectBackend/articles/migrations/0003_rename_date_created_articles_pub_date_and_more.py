# Generated by Django 4.0.4 on 2022-05-19 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='date_created',
            new_name='pub_date',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='description',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='is_open',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='owner',
        ),
        migrations.AddField(
            model_name='articles',
            name='content',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_id', to='articles.category'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
