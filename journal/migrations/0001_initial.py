# Generated by Django 4.2.6 on 2023-10-25 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_auto_20231021_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('favorite_quotes', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]