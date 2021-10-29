from calculate_one_fibonacci import Fibonacci

class Excercise():

    def __init__(self):
        self.calculate_one_instance = Fibonacci()
        self.save = False
        self.m_mode = ''
        estados = {
            '-m=s': 'Sumador',

        }

    # busco en el estado con el input
    # estados.get('-m=s') => instancia
    # ejecuto la instancia

    # Principio abierto-cerrado para refactorizar y no tener que modificar la clase Exersice
    # cuando aparezcan nuevos parametros

    def fibonacci(self, input:str):
        # chequeo que tenga modo
        if '-m' in input:
            self.m_mode = input[(input.index('-m')+3)]
        # checkeo el orden
        if '-o' in input:
            number = self.get_number(input)
            fibonacci_array = self.get_fibonacci_array(int(number))

            # si el modo es s, sumo el array de fibonaccis
            if self.m_mode == 's':
                self.print_sum(fibonacci_array)
            else:
                direction_char = input[(input.index('-o')+4)]
                orientation_char = input[(input.index('-o')+3)]
                directed_fibonacci_array = self.modify_by_direction(fibonacci_array, direction_char)
                self.print_by_orientation(directed_fibonacci_array, orientation_char)

        else:
            print('Entrada Invalida')

    # Devuelve la parte del string que es numero
    def get_number(self,input_string):
        for i,c in enumerate(input_string):
            if c.isdigit():
                return input_string[i:]
        return False

    # Devuelve el array de numeros fibonacci
    def get_fibonacci_array(self, input:int):
        return [self.calculate_one_instance.calculate(n) for n in range(input)]

    def modify_by_direction(self, array:list, direcction:str):
        if direcction == 'i':
            return array[::-1]
        return array

    def print_by_orientation(self, array:list, orientation:str):
        if orientation == 'h':
            for i in array: print(i, end=' ')
            print('')

        if orientation == 'v':
            for i in array: print(i)

    def print_sum(self,array):
        print(sum(array))
