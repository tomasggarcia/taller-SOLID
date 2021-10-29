from fibonacci_calculator import FibonacciCalculator

# -o=vd 43

if __name__ == "__main__":
    entrada = input('ingrese el comando: ')
    fibonacciCalculator = FibonacciCalculator()
    resultado = fibonacciCalculator.calulate(entrada[6:])
    if entrada[4] == 'd':
        print(resultado)
    if entrada[4] == 'i':
        print(resultado.reverse())