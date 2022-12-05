from pages.lot_page import CheckLot


class TestCheckLot:
    def test_check_lot_name(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert 'Винтажная бутылка(ДИПЛОМНЫЙ ПРОЕКТ!)' in check_lot.check_lot_name()

    def test_check_lot_price(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert '₽8,000,000' in check_lot.check_lot_price()

    def test_check_lot_tag_1(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert 'ретро' in check_lot.check_lot_tag_1()

    def test_check_lot_tag_2(self, driver):
        check_lot = CheckLot(driver)
        check_lot.open_site()
        check_lot.check_lot_item()
        assert 'редкость' in check_lot.check_lot_tag_2()
