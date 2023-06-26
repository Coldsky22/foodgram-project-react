from app.models import Ingredient
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()
filename = "foodgram_shoping_cart.txt"


def file_creation(shopping_list):
    ingredients = Ingredient.objects.select_related("recipe")
    with open(filename, "w+") as file:
        for line in shopping_list:
            ingredient = next(
                (i for i in ingredients if i.id == line["ingredient"]), None)
        if ingredient:
            file.write(
                f'{ingredient.recipe.name}:'
                f'{ingredient.name}'
                f'({ingredient.measurement_unit}) - {line["count"]}\n'
            )
    with open(filename, "rb") as read_file:
        response = HttpResponse(read_file.read(), content_type="text/plain")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
