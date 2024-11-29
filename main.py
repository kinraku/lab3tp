from abc import ABC, abstractmethod


# Singleton
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Factory Method
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class Product1(Product):
    def operation(self):
        return "Продукт1 создан"


class Product2(Product):
    def operation(self):
        return "Продукт2 создан"


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Создатель: {product.operation()}"


class Creator1(Creator):
    def factory_method(self) -> Product:
        return Product1()


class Creator2(Creator):
    def factory_method(self) -> Product:
        return Product2()


# Abstract Factory
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def check(self):
        pass


class WindowsButton(Button):
    def click(self):
        print("Нажата кнопка Windows")


class WindowsCheckBox(CheckBox):
    def check(self):
        print("Windows флажок выбран")


class MacButton(Button):
    def click(self):
        print("Нажата кнопка Mac")


class MacCheckBox(CheckBox):
    def check(self):
        print("Mac флажок выбран")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()


# Builder
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f"Пицца с тестом {self.dough}, соусом {self.sauce} и начинкой {self.topping}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        pass

    def build_sauce(self):
        pass

    def build_topping(self):
        pass

    def get_result(self):
        return self.pizza


class HawaiianPizzaBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.dough = "Тесто"

    def build_sauce(self):
        self.pizza.sauce = "Мягкий"

    def build_topping(self):
        self.pizza.topping = "Ветчина и ананасы"


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


# Main функция
def main():
    print("Singleton пример:")
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 is singleton2)  # True

    print("\nFactory Method пример:")
    creator1 = Creator1()
    print(creator1.some_operation())
    creator2 = Creator2()
    print(creator2.some_operation())

    print("\nAbstract Factory пример:")
    print("Фабрика Windows:")
    app_win = WindowsFactory()
    button_win = app_win.create_button()
    checkbox_win = app_win.create_checkbox()
    button_win.click()
    checkbox_win.check()

    print("Фабрика Mac:")
    app_mac = MacFactory()
    button_mac = app_mac.create_button()
    checkbox_mac = app_mac.create_checkbox()
    button_mac.click()
    checkbox_mac.check()

    print("\nBuilder пример:")
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)
    director.construct_pizza()
    pizza = builder.get_result()
    print(pizza)


if __name__ == "__main__":
    main()
