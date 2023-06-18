from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_recipe_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='recipe_count',
        ),
    ]
