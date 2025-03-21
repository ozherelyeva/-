from typing import Optional

class Car:
    """
    Базовый класс, представляющий автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        _mileage (int): Пробег автомобиля (инкапсулированный атрибут).
    """

    def __init__(self, brand: str, model: str, year: int, mileage: int = 0) -> None:
        """
        Конструктор базового класса Car.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            mileage (int): Пробег автомобиля (по умолчанию 0).
        """
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = mileage  # Инкапсулированный атрибут, так как пробег не должен изменяться напрямую.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car.

        Возвращает:
            str: Строка с информацией об автомобиле.
        """
        return f"{self.brand} {self.model} ({self.year}), пробег: {self._mileage} км"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Car.

        Возвращает:
            str: Официальное строковое представление.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, mileage={self._mileage})"

    def drive(self, distance: int) -> None:
        """
        Увеличивает пробег автомобиля на указанное расстояние.

        Аргументы:
            distance (int): Расстояние, на которое проехал автомобиль.
        """
        if distance > 0:
            self._mileage += distance
        else:
            raise ValueError("Расстояние должно быть положительным числом.")

    def get_mileage(self) -> int:
        """
        Возвращает текущий пробег автомобиля.

        Возвращает:
            int: Текущий пробег автомобиля.
        """
        return self._mileage


class PassengerCar(Car):
    """
    Дочерний класс, представляющий легковой автомобиль.

    Атрибуты:
        passenger_capacity (int): Вместимость пассажиров.
    """

    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int, mileage: int = 0) -> None:
        """
        Конструктор класса PassengerCar.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            passenger_capacity (int): Вместимость пассажиров.
            mileage (int): Пробег автомобиля (по умолчанию 0).
        """
        super().__init__(brand, model, year, mileage)
        self.passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта PassengerCar.

        Возвращает:
            str: Строка с информацией о легковом автомобиле.
        """
        return f"{self.brand} {self.model} ({self.year}), пассажировместимость: {self.passenger_capacity}, пробег: {self.get_mileage()} км"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта PassengerCar.

        Возвращает:
            str: Официальное строковое представление.
        """
        return f"PassengerCar(brand={self.brand}, model={self.model}, year={self.year}, passenger_capacity={self.passenger_capacity}, mileage={self.get_mileage()})"

    def drive(self, distance: int) -> None:
        """
        Перегруженный метод drive для легкового автомобиля.
        Увеличивает пробег автомобиля на указанное расстояние и выводит сообщение.

        Аргументы:
            distance (int): Расстояние, на которое проехал автомобиль.
        """
        super().drive(distance)  # Наследуем поведение базового класса.
        print(f"Легковой автомобиль {self.brand} {self.model} проехал {distance} км.")


class Truck(Car):
    """
    Дочерний класс, представляющий грузовой автомобиль.

    Атрибуты:
        load_capacity (float): Грузоподъемность автомобиля (в тоннах).
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float, mileage: int = 0) -> None:
        """
        Конструктор класса Truck.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            load_capacity (float): Грузоподъемность автомобиля (в тоннах).
            mileage (int): Пробег автомобиля (по умолчанию 0).
        """
        super().__init__(brand, model, year, mileage)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Truck.

        Возвращает:
            str: Строка с информацией о грузовом автомобиле.
        """
        return f"{self.brand} {self.model} ({self.year}), грузоподъемность: {self.load_capacity} т, пробег: {self.get_mileage()} км"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Truck.

        Возвращает:
            str: Официальное строковое представление.
        """
        return f"Truck(brand={self.brand}, model={self.model}, year={self.year}, load_capacity={self.load_capacity}, mileage={self.get_mileage()})"

    def load_cargo(self, weight: float) -> str:
        """
        Метод для загрузки груза в автомобиль.

        Аргументы:
            weight (float): Вес груза (в тоннах).

        Возвращает:
            str: Сообщение о результате загрузки.
        """
        if weight <= self.load_capacity:
            return f"Груз весом {weight} т успешно загружен в {self.brand} {self.model}."
        else:
            return f"Груз весом {weight} т превышает грузоподъемность {self.brand} {self.model}."


# Пример использования
passenger_car = PassengerCar("Toyota", "Corolla", 2020, 5)
truck = Truck("Volvo", "FH16", 2018, 20.0)

print(passenger_car)  # Toyota Corolla (2020), пассажировместимость: 5, пробег: 0 км
print(truck)  # Volvo FH16 (2018), грузоподъемность: 20.0 т, пробег: 0 км

passenger_car.drive(150)  # Легковой автомобиль Toyota Corolla проехал 150 км.
truck.drive(300)

print(passenger_car.get_mileage())  # 150
print(truck.get_mileage())  # 300

print(truck.load_cargo(15))  # Груз весом 15 т успешно загружен в Volvo FH16.
print(truck.load_cargo(25))  # Груз весом 25 т превышает грузоподъемность Volvo FH16.