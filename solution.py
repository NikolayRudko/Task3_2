import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.body_whl = body_whl
        self._get_parameters()

    def _get_parameters(self):
        parameters = self.body_whl.split('x')

        def _isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if all(list(map(_isfloat, parameters))):
            body_length, body_width, body_height = map(float, parameters)
        else:
            body_length, body_width, body_height = 0.0, 0.0, 0.0

        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        keys = next(reader)
        for row in reader:
            machine = {k: v for k, v in zip(keys, row)}
            if _isvalid(machine):
                if machine["car_type"] == "car":
                    car = Car(brand=machine["brand"],
                              photo_file_name=machine['photo_file_name'],
                              carrying=machine['carrying'],
                              passenger_seats_count=machine['passenger_seats_count'])
                elif machine["car_type"] == "truck":
                    car = Truck(brand=machine["brand"],
                                photo_file_name=machine['photo_file_name'],
                                carrying=machine['carrying'],
                                body_whl=machine['body_whl'])
                elif machine["car_type"] == "truck":
                    car = SpecMachine(brand=machine["brand"],
                                      photo_file_name=machine['photo_file_name'],
                                      carrying=machine['carrying'],
                                      extra=machine["extra"])
                else:
                    print("Error!!!!")
                car_list.append(car)
    return car_list


def _isvalid(machine):
    car_type = ("car", "truck", "spec_machine")
    photo_file_ext = (".jpg", ".jpeg", ".png", ".gif")
    if not machine:
        return False
    if machine["car_type"] not in car_type:
        return False
    if not machine["photo_file_name"].endswith(photo_file_ext):
        return False
    return True
