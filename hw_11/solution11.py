class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        else:
            return "У вас обычная газировка"

# Вкус задан
strawberry_soda = Soda("клубничным")
print(strawberry_soda)

# Газировка без вкуса
regular_soda = Soda()
print(regular_soda)

class Math:
    def addition(self, a, b):
        print(a + b)

    def subtraction(self, a, b):
        print(a - b)

    def multiplication(self, a, b):
        print(a * b)

    def division(self, a, b):
        if b != 0:
            print(a / b)
        else:
            print("Ошибка: деление на ноль.")

math_operations = Math()

math_operations.addition(8, 4)
math_operations.subtraction(8, 4)
math_operations.multiplication(8, 4)
math_operations.division(8, 4)

class SuperStr(str):
    def is_repeatance(self, s: str) -> bool:
        if not isinstance(s, str) or not s or not self:
            return False
        if len(self) % len(s) != 0:
            return False
        n = len(self) // len(s)
        return s * n == self

    def is_palindrom(self) -> bool:
        s_lower = self.lower()
        return s_lower == s_lower[::-1]

s1 = SuperStr("ababab")
print(s1.is_repeatance("ab"))
print(s1.is_repeatance("abc"))
print(s1.is_repeatance(""))

s2 = SuperStr("Madam")
print(s2.is_palindrom())

s3 = SuperStr("")
print(s3.is_palindrom())


