from time import sleep


def test_avito_search(start_page):
    orgtechics_and_supply_page = start_page.goto_orgtechnics_and_supplies_page()
    orgtechics_and_supply_page.search_item('Принтер')
    orgtechics_and_supply_page.click_checkbox_new()
    orgtechics_and_supply_page.change_region('Владивосток')
    orgtechics_and_supply_page.show_results()
    orgtechics_and_supply_page.sort_results()
    orgtechics_and_supply_page.print_prices_for_first_five_items()

