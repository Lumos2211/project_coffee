import requests
from bs4 import BeautifulSoup

def responce_func():
    menu = []

    url = "https://yandex.ru/maps/org/imok_coffee_x_friends/46289150680/menu/?ll=39.041833%2C45.017104&z=14"

    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск всех элементов с классом
    menu_containers = soup.find_all(class_="related-item-list-view")

    for container in menu_containers:
        try:
            # Название (обязательное поле)
            name_element = container.find(class_="related-item-list-view__title")
            if not name_element:
                continue  # Пропускаем если нет названия
            
            name = name_element.text.strip()
            
            # Объем (может не быть)
            volume_element = container.find(class_="related-item-list-view__volume")
            volume = volume_element.text.strip() if volume_element else ""
            
            # Цена (обязательное поле)
            price_element = container.find(class_="related-item-list-view__price")
            if not price_element:
                continue  # Пропускаем если нет цены
            
            price = price_element.text.strip()
            
            # Описание (может не быть)
            info_element = container.find(class_="related-item-list-view__description")
            info = info_element.text.strip() if info_element else ""
            
            # Формируем строку
            if volume:
                menu_item = f"{name} {volume}: {price}"
            else:
                menu_item = f"{name}: {price}"
                
            if info:
                menu_item += f" ({info})"
            
            menu.append(menu_item)
            
        except AttributeError as e:
            print(f"Ошибка парсинга элемента: {e}")
            continue
        except Exception as e:
            print(f"Другая ошибка: {e}")
            continue

    return menu