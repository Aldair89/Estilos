def option1():
    # Estilo procedural
    print("Hola a todos.")

def option2():
    # Estilo orientado a objetos
    class MyClass:
        def __init__(self, name):
            self.name = name
        
        def greet(self):
            print(f"Hola, {self.name}!")

    obj = MyClass("John")
    obj.greet()

def option3():
    # Programación funcional
    def square(x):
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    squares = list(map(square, numbers))
    print(squares)

def option4():
    # Estilo modular
    import math

    radius = 5
    area = math.pi * radius ** 2
    print(f"Area del circulo: {area}")

def option5():
    # Programación declarativa
    numbers = [1, 2, 3, 4, 5]
    squares = [x ** 2 for x in numbers]
    print(squares)

def option6():
    # Estilo recursivo
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))

def option7():
    # Estilo procedural estructurado
    def greet(name):
        print(f"holas, {name}!")

    def main():
        name = input("ingresa tu nombre: ")
        greet(name)

    main()

def option8():
    # Estilo programación concurrente
    import threading

    def print_numbers():
        for i in range(10):
            print(i)

    def print_letters():
        for letter in "abcdefghij":
            print(letter)

    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def option9():
    # Estilo programación defensiva
    def divide(a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    try:
        result = divide(10, 0)
        print(result)
    except ValueError as e:
        print(e)

def option10():
    # Estilo programación interactiva
    while True:
        user_input = input("Introduzca un número (0 para salir): ")
        if user_input == "0":
            break
        else:
            number = int(user_input)
            print(f"Cuadrado del numero: {number ** 2}")

def print_banner():
    banner = """
    ██████╗ ███████╗███╗   ███╗██████╗  ██████╗ ██╗  ██╗███████╗
    ██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝
    ██████╔╝█████╗  ██╔████╔██║██████╔╝██║   ██║█████╔╝ ███████╗
    ██╔══██╗██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║   ██║██╔═██╗ ╚════██║
    ██║  ██║███████╗██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██╗███████║
    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """
    print(banner)

# Imprimir banner estilo "hacker"
print_banner()

# Menú de opciones
print("Estilos de programación")
print("-----------------------")
print("1. Estilo procedural")
print("2. Estilo orientado a objetos")
print("3. Programación funcional")
print("4. Estilo modular")
print("5. Programación declarativa")
print("6. Estilo recursivo")
print("7. Estilo procedural estructurado")
print("8. Estilo programación concurrente")
print("9. Estilo programación defensiva")
print("10. Estilo programación interactiva")
print("-----------------------")
choice = input("Seleccione una opción (1-10): ")

if choice == "1":
    option1()
elif choice == "2":
    option2()
elif choice == "3":
    option3()
elif choice == "4":
    option4()
elif choice == "5":
    option5()
elif choice == "6":
    option6()
elif choice == "7":
    option7()
elif choice == "8":
    option8()
elif choice == "9":
    option9()
elif choice == "10":
    option10()
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
