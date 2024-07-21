class Car:
    def __init__(self, brand, model, year, price):
        self.brand_name = brand
        self.model = model
        self.year = year
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def show(self):
        print(f"This is {self.brand_name}. It is {self.model}. year : {self.year} price : {self.price}")


# car1 = Car("Toyota", "Altis", "2021", "896500")
# car1.show()
