import allure


@allure.feature('Test Avito search')
def test_avito_search(start_page):
    start_page.select_category_and_subcategory('Электроника', 'Оргтехника и расходники')
    search_page = start_page.goto_search_page()
    search_page.make_search('Принтер')
    search_page.apply_search_filter('Новые', True)
    search_page.change_region('Владивосток')
    search_page.sort_results('Дороже')
    search_page.print_prices_for_items(5)
