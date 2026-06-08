def celsius_para_fahrenheit():

    celsius = float(input("Digite a temperatura em graus Celsius: "))

    fahrenheit = (celsius * 9/5) + 32

    print(f"{celsius:.1f} °C equivalem a {fahrenheit:.1f} °F")

if __name__ == "__main__":
    celsius_para_fahrenheit()