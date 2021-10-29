
class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def calculate(self, n):
        if n < len(self.cache):
            return self.cache[n]
        else:
            fib_number = self.calculate(n - 1) + self.calculate(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]

if __name__ == "__main__":
    fibo_instance = Fibonacci()
    print(fibo_instance.calculate(4))
    print([fibo_instance(n) for n in range(int(input('ingrese un numero ')))])