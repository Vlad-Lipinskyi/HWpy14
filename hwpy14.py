print("Завдання 1")

lastName = input("На яке прізвище Ви хочете замовити столик: ")

def orderTable(lastName, amount=2):
    print(f"Столик заброньовано на прізвище {lastName} для {amount} осіб")

print(" ")
print("Завдання 2")

print(orderTable(lastName))

orderTable(lastName, 4)