from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20230609_0156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',), 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
    ]
