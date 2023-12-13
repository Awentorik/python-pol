import doctest


class BankCard:
    def __init__(self, balance: float, card_number: str):
        """
        Создание и подготовка к работе объекта "Банковская карта"

        :param balance: Баланс на карте
        :param card_number: Номер карты

        Примеры:
        >>> card = BankCard(10000.0, "1234567890123456")
        """
        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        if not isinstance(card_number, str):
            raise TypeError("Номер карты должен быть строкой")
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Номер карты должен состоять из 16 цифр")

        self.balance = balance
        self.card_number = card_number

    def check_balance(self) -> float:
        """
        Проверка баланса карты

        :return: Текущий баланс

        Примеры:
        >>> card = BankCard(10000.0, "1234567890123456")
        >>> card.check_balance()
        """
        ...

    def deposit(self, amount: float) -> None:
        """
        Пополнение баланса карты

        :param amount: Сумма пополнения
        :raise ValueError: Если сумма пополнения отрицательная

        Примеры:
        >>> card = BankCard(10000.0, "1234567890123456")
        >>> card.deposit(5000.0)
        """
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств с карты

        :param amount: Сумма снятия
        :raise ValueError: Если сумма снятия превышает баланс или отрицательная

        Примеры:
        >>> card = BankCard(10000.0, "1234567890123456")
        >>> card.withdraw(5000.0)
        """
        ...


class Smartphone:
    def __init__(self, model: str, battery_charge: float):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param model: Модель смартфона
        :param battery_charge: Заряд батареи

        Примеры:
        >>> phone = Smartphone("Model X", 100.0)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(battery_charge, (int, float)) or battery_charge < 0 or battery_charge > 100:
            raise ValueError("Заряд батареи должен быть числом от 0 до 100")

        self.model = model
        self.battery_charge = battery_charge

    def make_call(self, duration: int) -> None:
        """
        Совершение звонка

        :param duration: Продолжительность звонка в минутах
        :raise ValueError: Если продолжительность звонка отрицательная

        Примеры:
        >>> phone = Smartphone("Model X", 100.0)
        >>> phone.make_call(10)
        """
        ...

    def charge_battery(self, charge_amount: float) -> None:
        """
        Зарядка батареи

        :param charge_amount: Количество заряда в процентах
        :raise ValueError: Если количество заряда отрицательное или превышает 100

        Примеры:
        >>> phone = Smartphone("Model X", 50.0)
        >>> phone.charge_battery(50.0)
        """
        ...


class SocialNetwork:
    def __init__(self, user_name: str, number_of_friends: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param user_name: Имя пользователя
        :param number_of_friends: Количество друзей

        Примеры:
        >>> network = SocialNetwork("username123", 150)
        """
        if not isinstance(user_name, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not isinstance(number_of_friends, int) or number_of_friends < 0:
            raise ValueError("Количество друзей должно быть неотрицательным числом")

        self.user_name = user_name
        self.number_of_friends = number_of_friends

    def add_friend(self, friend_name: str) -> None:
        """
        Добавление друга

        :param friend_name: Имя добавляемого друга

        Примеры:
        >>> network = SocialNetwork("username123", 150)
        >>> network.add_friend("new_friend")
        """
        ...

    def remove_friend(self, friend_name: str) -> None:
        """
        Удаление друга

        :param friend_name: Имя удаляемого друга

        Примеры:
        >>> network = SocialNetwork("username123", 150)
        >>> network.remove_friend("old_friend")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации