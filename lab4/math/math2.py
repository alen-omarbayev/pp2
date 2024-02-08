def trapezoidal(h, value1, value2):
    return (value1+value2)*h/2

h=int(input("Height: "))
value1=int(input("Base, first value: "))
value2=int(input("Base, second value: "))
print(f"Expected output: {trapezoidal(h, value1, value2)}")