class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(self.shop_name)
        print(self.store_type)

    def open_shop(self):
        print("Онлайн-магазин відкритий")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, count):
        self.number_of_units += count

class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discounts_products(self):
        print(self.discount_products)
