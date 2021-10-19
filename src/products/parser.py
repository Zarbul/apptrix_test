from django.shortcuts import redirect
from .models import Product
import requests
from bs4 import BeautifulSoup

URL = 'https://www.citilink.ru/catalog/noutbuki/'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"


def get_html(url):
    session = requests.session()
    r = requests.get(url)
    html = r.text
    return html


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    category = soup.find('div', class_='Subcategory__title-container').find('h1').text
    category = category.strip().replace(' ', '')
    products_card = soup.find('div', class_='ProductCardCategoryList__list').find_all('div', class_='product_data__gtm-js')
    for product in products_card:
        price = product.find('span', class_='ProductCardHorizontal__price_current-price').text
        price = price.strip().replace(' ', '')
        name = product.find('div', class_='ProductCardHorizontal__header-block').find('a').text
        name = name.strip().replace(' ', '')
        image = product.find('div', class_='ProductCardHorizontal__image-block').find('img')['src']
        Product.objects.create(product_name=name, price=price, image=image, category_name=category)


def parser(*args):
    get_data(get_html(URL))
    return redirect('/api/list/')
