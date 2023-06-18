from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recipe_count',
            field=models.IntegerField(default=0, verbose_name='recipe_count'),
        ),
    ]
