# dog类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name.title() + ' is ' + str(self.age) + ' years!')

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


my_dog = Dog('york', 6)
my_dog.sit()
my_dog.roll_over()


# 汽车类
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + self.make + self.model
        return long_name  # 不太明白为何要用return

    def reading_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')
        # 用于更新odometer P145

    def updata_odometer(self, mile):
        self.odometer_reading = mile


my_car = Car(' audi ', 'a4 ', 2016)
print(my_car.get_descriptive_name())
my_car.updata_odometer(23)
my_car.reading_odometer()

# 汽车子类，接上面的car类


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' -KWH battery')

    def reading_odometer(self):  # 重置上一个父类
        print('yes sir')


my_tesla = ElectricCar('teala', 'model S', 2016)
my_tesla.describe_battery()
my_tesla.reading_odometer()
