from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = request.GET.get('page', 1)
    one_list = []
    with open('data-398-2018-08-30.csv', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for line in reader:
            inner_dict = {}
            inner_dict['Name'] = line['Name']
            inner_dict['Street'] = line['Street']
            inner_dict['District'] = line['District']
            one_list.append(inner_dict)
    paginator = Paginator(one_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': one_list,
        'page': page,
    }
    print(one_list[1201:1203])
    print(page, page.has_next(), page.next_page_number(), paginator.num_pages)
    print(paginator)
    return render(request, 'stations/index.html', context)
