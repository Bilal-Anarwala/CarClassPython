class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # The getters
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    # The setters
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    # Displaying it all
    def display_car_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

if __name__ == "__main__":
    # Create basic car objects
    bilals_car = Cars("Toyota", "Supra", 1998)
    drews_car = Cars("Mitsubishi", "Eclipse", 1995)
    andrays_car = Cars("BMW", "M335i", 2016)
    mohammads_car = Cars("Tesla", "Model 3", 2021)
    robertos_car = Cars("Nissan", "GTR", 2001)
    nabeels_car = Cars("Dodge", "Viper ACR", 2016)
    tylers_car = Cars("Corvette", "Z06", 2010)
    syeds_car = Cars("Mazda", "Miata", 2016)
