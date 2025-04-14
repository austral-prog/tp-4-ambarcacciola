def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    print(f"el coeficiente A de su ecuación de la recta es: {A}")
    print(f"el coeficiente B de su ecuación de la recta es: {B}")
    print(f"el coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"el coeficiente X2 de su ecuación de la recta es: {X2}")
    print(f"\nPara la siguiente ecuación: ")
    print(f"\tY = {A}X + {B}")

    P1= A*X1 + B
    P2= A*X2 + B

    print("\nDados los siguientes puntos:")
    print(f"\tP1 = ({X1},{P1})")
    print(f"\tP2 = ({X2},{P2})")

    d = ((X1 - X2)**2 + (P1 - P2)**2)**(1/2)

    print(f"\nLa distancia entre ellos es: {d}")
