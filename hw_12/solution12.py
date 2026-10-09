from typing import List, Union


class Product:
    def __init__(self, name: str, shop: str, price: float) -> None:
        # Закрытые поля
        self.__name: str = name
        self.__shop: str = shop
        self.__price: float = price

     # Геттеры для доступа к закрытым полям при сортировке и выводе
    @property
    def name(self) -> str:
        return self.__name

    @property
    def shop(self) -> str:
        return self.__shop

    @property
    def price(self) -> float: 
        return self.__price

    def __add__(self, other: 'Product') -> float:
        """Перегруженная операция сложения товаров по цене (+)."""
        if isinstance(other, Product):
            return self.__price + other.price
        raise TypeError("Складывать можно только объекты класса Product")

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"Товар: {self.__name} | Магазин: {self.__shop} | Цена: {self.__price} руб."


class Warehouse:
    def __init__(self, products: List[Product]) -> None:
        # Закрытый массив товаров
        self.__products: List[Product] = products

    def get_by_index(self, index: int) -> str:
        """Вывод информации о товаре по индексу."""
        try:
            return str(self.__products[index])
        except IndexError:
            return f"Ошибка: Товар с индексом {index} не найден на складе."

    def get_by_name(self, name: str) -> str:
        """Вывод информации о товаре по имени (первое совпадение или список)."""
        found_products = [p for p in self.__products if p.name.lower() == name.lower()]
        if not found_products:
            return f"Товар с названием '{name}' не найден на складе."
        return "\n".join(str(p) for p in found_products)

    def sort_by_name(self):
        """Сортировка товаров по названию."""
        self.__products.sort(key=lambda p: p.name)

    def sort_by_shop(self) -> None:
        """Сортировка товаров по магазину."""
        self.__products.sort(key=lambda p: p.shop)

    def sort_by_price(self) -> None:
        """Сортировка товаров по цене."""
        self.__products.sort(key=lambda p: p.price)

    def print_all(self) -> None:
        """Вспомогательный метод для вывода всего склада."""
        for i, prod in enumerate(self.__products):
            print(f"[{i}] {prod}")

# Создаем товары
p1 = Product("Ноутбук", "Пятый элемент", 7800.0)
p2 = Product("Телефон", "МТС", 4500.0)
p3 = Product("Ноутбук", "А1", 7400.0)
p4 = Product("Клавиатура", "Озон", 45.0)

# Тест перегруженного сложения по цене
total_price = p1 + p2
print(f"Сумма цен '{p1.name}' и '{p2.name}': {total_price} руб.\n")

# Инициализируем склад
warehouse = Warehouse([p1, p2, p3, p4])

print("--- Исходный склад ---")
warehouse.print_all()

print("\n--- Поиск по индексу [1] ---")
print(warehouse.get_by_index(1))

print("\n--- Поиск по имени 'Ноутбук' ---")
print(warehouse.get_by_name("Ноутбук"))

print("\n--- Сортировка по цене ---")
warehouse.sort_by_price()
warehouse.print_all()

print("\n--- Сортировка по названию ---")
warehouse.sort_by_name()
warehouse.print_all()

print("\n--- Сортировка по магазину ---")
warehouse.sort_by_shop()
warehouse.print_all()


from typing import Dict, List, Optional, Union


class Bus:
    def __init__(self, max_seats: int, max_speed: float) -> None:
        self.max_seats: int = max_seats
        self.max_speed: float = max_speed
        self.speed: float = 0.0

        # Словарь мест: (номер_места: "Фамилия")
        # Изначально все места свободны (значение None)
        self.seats_map: Dict[int, Optional[str]] = {
            i: None for i in range(1, max_seats + 1)
        }

    @property
    def passengers(self) -> List[str]:
        """Список фамилий пассажиров в автобусе."""
        return [name for name in self.seats_map.values() if name is not None]

    @property
    def has_empty_seats(self) -> bool:
        """Флаг наличия свободных мест."""
        return len(self.passengers) < self.max_seats

    def speed_up(self, value: float) -> None:
        """Увеличение скорости на заданное значение."""
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        self.speed = min(self.speed + value, self.max_speed)

    def speed_down(self, value: float) -> None:
        """Уменьшение скорости на заданное значение."""
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        self.speed = max(self.speed - value, 0.0)

    def _find_free_seat(self) -> Optional[int]:
        """Поиск первого свободного номера места."""
        for seat, passenger in self.seats_map.items():
            if passenger is None:
                return seat
        return None

    def board(self, names: Union[str, List[str]]) -> None:
        """Посадка одного или нескольких пассажиров."""
        if isinstance(names, str):
            names = [names]

        for name in names:
            free_seat = self._find_free_seat()
            if free_seat is None:
                print(f"Свободных мест нет! Пассажир {name} не смог сесть в автобус.")
                break
            self.seats_map[free_seat] = name

    def unboard(self, names: Union[str, List[str]]) -> None:
        """Высадка одного или нескольких пассажиров."""
        if isinstance(names, str):
            names = [names]

        for name in names:
            # Находим все места, занятые этим пассажиром
            occupied_seats = [
                seat
                for seat, psgr in self.seats_map.items()
                if psgr == name
            ]
            if not occupied_seats:
                print(f"Пассажир с фамилией {name} не найден в автобусе.")
                continue

            # Освобождаем первое найденное место с такой фамилией
            self.seats_map[occupied_seats[0]] = None

    # Магические методы
    def __contains__(self, name: str) -> bool:
        """Операция 'in' - проверка наличия пассажира по фамилии."""
        return name in self.passengers

    def __iadd__(self, name: str) -> "Bus":
        """Операция `+=` — посадка пассажира по фамилии."""
        self.board(name)
        return self

    def __isub__(self, name: str) -> "Bus":
        """Операция `-=` — высадка пассажира по фамилии."""
        self.unboard(name)
        return self

    def __repr__(self) -> str:
        return (f"Bus(Скорость: {self.speed}/{self.max_speed}, "
                f"Места: {len(self.passengers)}/{self.max_seats}, "
                f"Свободные места: {self.has_empty_seats})")

# Создаем автобус на 3 места с макс. скоростью 110 км/ч
bus = Bus(max_seats=3, max_speed=110.0)

# 1. Проверяем управление скоростью
bus.speed_up(60.0)
bus.speed_up(80.0)  # Попытка превысить макс. скорость
print(f"Текущая скорость: {bus.speed} км/ч")  # Выведет: 110.0

bus.speed_down(30.0)
print(f"Скорость после торможения: {bus.speed} км/ч")  # Выведет: 80.0

# 2. Посадка списка пассажиров
bus.board(["Ровнейко", "Иванов"])
print(f"Пассажиры: {bus.passengers}")  # ['Ровнейко', 'Иванов']
print(f"Есть свободные места? {bus.has_empty_seats}")  # True

# 3. Использование оператора +=
bus += "Загуменный"
print(f"Есть свободные места теперь? {bus.has_empty_seats}")  # False
print(f"Словарь мест: {bus.seats_map}")

# Попытка посадить еще одного (мест нет)
bus += "Кальман"

# 4. Проверка оператора in
print("Иванов в автобусе?", "Иванов" in bus)  # True
print("Кальман в автобусе?", "Кальман" in bus)  # False

# 5. Использование оператора -=
bus -= "Иванов"
print(f"Пассажиры после высадки Иванова: {bus.passengers}")
print(f"Словарь мест после высадки: {bus.seats_map}")
