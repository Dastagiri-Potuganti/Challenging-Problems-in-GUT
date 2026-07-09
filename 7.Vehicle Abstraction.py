from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")



class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")



class Bus(Vehicle):
    def start(self):
        print("Bus starts with an ignition switch.")



car = Car()
bike = Bike()
bus = Bus()


car.start()
bike.start()
bus.start()