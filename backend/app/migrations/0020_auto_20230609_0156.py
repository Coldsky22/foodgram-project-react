from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_favorites_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',), 'verbose_name': 'Ингредиент', 'verbose_name_plural': ('Ингредиенты',)},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=models.TextField(blank=True, max_length=10000, verbose_name='Описание рецепта'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set(),
        ),
    ]
