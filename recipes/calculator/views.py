from django.http import HttpRequest
from django.shortcuts import render
import re

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def serving(data_dict: dict, servings: str):
    """
    the function for ingredients amount calculation
    """
    for ingredient, amount in data_dict.items():
        data_dict[ingredient] = amount * int(servings)
    return data_dict


def rendering(request, dish):
    """
    For code minimizing
    """
    portions = request.GET.get('servings')
    if portions:
        dish_quantity = serving(DATA[dish], portions)
    else:
        dish_quantity = DATA[dish]
    context_dict = {'dish': dish_quantity, }
    return context_dict


def view_omlet(request):
    context = rendering(request, 'omlet')
    return render(request, 'calculator/index.html', context)


def view_pasta(request):
    context = rendering(request, 'pasta')
    return render(request, 'calculator/index.html', context)


def view_buter(request):
    context = rendering(request, 'buter')
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
