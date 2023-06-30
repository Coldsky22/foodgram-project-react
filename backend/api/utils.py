from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db.models import F

from app.models import Ingredient

User = get_user_model()
filename = "foodgram_shopping_cart.txt"


def file_creation(shopping_list):
    ingredients = Ingredient.objects.select_related("recipe")
    ingredients = ingredients.annotate(
        recipe_name=F("recipe__name"),
        ingredient_name=F("name"),
        measurement_unit=F("measurement_unit"),
    )
    
    shopping_lines = []
    for line in shopping_list:
        ingredient = next(
            (i for i in ingredients if i.id == line["ingredient"]), None
        )
        if ingredient:
            shopping_lines.append(
                f'{ingredient.recipe_name}:'
                f'{ingredient.ingredient_name}'
                f'({ingredient.measurement_unit}) - {line["count"]}\n'
            )

    content = "".join(shopping_lines)
    response = HttpResponse(content, content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response