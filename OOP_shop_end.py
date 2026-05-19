from OOP_shop import Shop,Discount

store = Shop("Сільпо", "Супермаркет")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()

shop1 = Shop("АТБ", "Дискаунтер")
shop2 = Shop("Розетка", "Маркетплейс")
shop3 = Shop("Фокстрот", "Електроніка")
shop1.describe_shop()
shop2.describe_shop()
shop3.describe_shop()

store = Shop("Пром", "Маркетплейс")
print(store.number_of_units)
store.number_of_units = 5
print(store.number_of_units)

store.set_number_of_units(10)
print(store.number_of_units)
store.increment_number_of_units(3)
print(store.number_of_units)

store_discount = Discount("Ашан", "Гіпермаркет", ["Яблука", "Молоко"])
store_discount.get_discounts_products()
