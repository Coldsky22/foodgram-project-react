import csv
import logging

from app.models import Ingredient
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("csv_file", nargs="+", type=str)
        parser.add_argument("--log_file", type=str,
                            help="path to the log file"
                            )


def handle(self, *args, **options):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    if options.get("log_file"):
        file_handler = logging.FileHandler(options["log_file"])
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    ingredients = []

    for csv_file in options["csv_file"]:
        data_reader = csv.reader(open(csv_file), delimiter=",")
        for row in data_reader:
            ingredient_data = {"name": row[0], "measurement_unit": row[1]}
            ingredients.append(ingredient_data)
            logger.info("Ingredient {} added".format(row[0]))

    try:
        Ingredient.objects.bulk_create(
            [Ingredient(**ingredient) for ingredient in ingredients],
            ignore_conflicts=True,
        )
        logger.info("Ingredients added successfully")
    except Exception as e:
        logger.error(str(e))
