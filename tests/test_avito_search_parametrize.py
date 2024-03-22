import allure
import pytest
from pages.start_page import StartPage


@allure.feature('Test Avito search parametrize')
@pytest.mark.parametrize("category, subcategory, search_query, filter_name, filter_state, region, sort_order, items", [
    ('Электроника', 'Оргтехника и расходники', 'Сканер', 'Новые', True, 'Новосибирская область', 'Дешевле', 5),
    ('Электроника', 'Оргтехника и расходники', 'Факс', 'Новые', False, 'Москва', 'Дороже', 3)
], ids=[
    'Electronics-Scanner-Novosib-Lowprice',
    'Electronics-Fax-Moscow-Highprice',
])
def test_avito_search_parametrize(page, category, subcategory, search_query, filter_name, filter_state, region,
                                  sort_order, items):
    page = StartPage(page)
    page.open_page()
    page.select_category_and_subcategory(category, subcategory)
    search_page = page.goto_search_page()
    search_page.make_search(search_query)
    search_page.apply_search_filter(filter_name, filter_state)
    search_page.change_region(region)
    search_page.sort_results(sort_order)
    search_page.print_prices_for_items(items)
