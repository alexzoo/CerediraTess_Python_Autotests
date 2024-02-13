import allure


@allure.feature('Test Avito search')
def test_avito_search(start_page):
    orgtechics_and_supply_page = start_page.goto_orgtechnics_and_supplies_page()
    orgtechics_and_supply_page.search_item('Принтер')
    orgtechics_and_supply_page.click_checkbox_new()  # add parameter
    orgtechics_and_supply_page.change_region('Владивосток')
    orgtechics_and_supply_page.show_results()
    orgtechics_and_supply_page.sort_results()  # add parameter
    orgtechics_and_supply_page.print_prices_for_first_five_items()

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