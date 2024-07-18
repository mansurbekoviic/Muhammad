class Car:
    def __init__(self, yil, model):
        self.yil = yil
        self.model = model

    def start_engine(self):
        print(f"The {self.yil} {self.model} engine is started.")

my_car = Car("Rolls Royce", "Phantom")
print(my_car.yil)
print(my_car.model)