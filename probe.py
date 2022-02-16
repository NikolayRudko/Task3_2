import csv
import os

from solution import *


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        keys = next(reader)  # пропускаем заголовок
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
                    car = SpecMachine(rand=machine["brand"],
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
    if machine["car_type"] not in car_type:
        return False
    if not machine["photo_file_name"].endwith(photo_file_ext):
        return False
    return True


print(get_car_list("cars_week3.csv"))
