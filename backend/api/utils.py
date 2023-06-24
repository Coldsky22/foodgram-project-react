from os import remove
from app.models import Ingredient
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()


def file_creation(shoping_list):
    with open("example.txt", "w+") as file_name:
        for line_list in shoping_list:
            ingredient = Ingredient.objects.get(pk=line_list['ingredient'])
            file_name.write(f'{ingredient.name} 'f'({ingredient.measurement_unit})'f' - {line_list["count"]}\n')
    with open("example.txt", "r") as read_file:
        response = HttpResponse(read_file.read(),content_type="text/plain,charset=utf8")
        message = 'attachment; filename="{}.txt"'.format('file_name')
        response['Content-Disposition'] = message
        remove("example.txt")
    return response

# print(Ingredient.objects.get(pk=line_list['ingredient']).name )