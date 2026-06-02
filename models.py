class Vehicle:

    def __init__(self, brand, model, year, engine, mileage, drivetrain, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.mileage = mileage
        self.drivetrain = drivetrain
        self.price = price

    def update_mileage(self, additional_miles):
        if additional_miles > 0:
            self.mileage += additional_miles
        return self.mileage

    def get_status(self):
        return f"{self.brand} {self.model} ({self.year}) ({self.engine}) | {self.drivetrain} | Пробег: {self.mileage} | Цена: {self.price} лв."