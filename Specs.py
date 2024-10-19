from Cars import Cars

class Specs(Cars):
    def __init__(self, make, model, year, engine_type, horsepower):
        super().__init__(make, model, year)  # Inherit the parent class's constructors
        self.engine_type = engine_type
        self.horsepower = horsepower

    # Getters
    def get_engine_type(self):
        return self.engine_type

    def get_horsepower(self):
        return self.horsepower

    # Setters
    def set_engine_type(self, engine_type):
        self.engine_type = engine_type

    def set_horsepower(self, horsepower):
        self.horsepower = horsepower
    # Display info
    def display_specs(self):
        print(f"Engine Type: {self.engine_type}")
        print(f"Horsepower: {self.horsepower}")

    def display_car_info(self):
        super().display_car_info()
        self.display_specs()
