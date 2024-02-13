import allure


@allure.feature('Test Avito search')
def test_avito_search(start_page):
    search_page = start_page.goto_search_page()
    search_page.search_form('Принтер')
    search_page.click_checkbox_new()  # add parameter
    search_page.change_region('Владивосток')
    search_page.show_results()
    search_page.sort_results()  # add parameter
    search_page.print_prices_for_items()

"""
1.Перейти по ссылке https://www.avito.ru/penza/transport?cd=1 (При
использовании ссылки на главную страницу, сайт ругается на DDOS атаки, пишите эту как стартовую, трудностей не будет)
2.Выбрать категорию “Оргтехника и расходники”
3.В поле поиска написать “Принтер”
4.Активировать чекбокс “только с фото”
5.Кликнуть по выпадающему списку регионов
6.Ввести регион “Владивосток”
7.Нажать на кнопку “Показать n объявлений”
8.В выпадающем списке сортировки выбрать “Дороже”
9.Вывести в консоль Значение цены первых 5 товаров
10.Закрыть браузер
"""