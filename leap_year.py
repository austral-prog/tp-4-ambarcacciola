def leap_year(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False

if __name__ == "__main__":
    anio = int(input("Ingrese un año: "))
    if leap_year(anio):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
