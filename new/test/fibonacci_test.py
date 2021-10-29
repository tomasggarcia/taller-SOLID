import io
import unittest
import unittest.mock
from modules.calculate_one_fibonacci import Fibonacci
from excercise import Excercise



#  python3 -m unittest fibonacci_test.py 
class TestFibonacci(unittest.TestCase):

    fibonacci_instance = Fibonacci()        
    calculate_instance = Excercise()

    # Iteracion 1
    def test_fibonacci_method(self):
        result = self.__when_call_fibonacci()
        self.__then_the_result_is_a_correct_fibonacci_array(result)

    def __when_call_fibonacci(self):
        return [self.fibonacci_instance.__call__(n) for n in range(4)]
    
    def __then_the_result_is_a_correct_fibonacci_array(self,fibonacci_array):
        self.assertEqual([0, 1, 1, 2],fibonacci_array)


    # Iteracion 2
    def test_horizontal_orientation(self):
        horizontal_input = self.__given_an_horizontal_input()
        result = self.__when_call_calculate_fibonacci_with(horizontal_input)
        self.__then_the_orientation_is_horizontal(result)

    def __given_an_horizontal_input(self):
        return '-o=hd 4'

    def __when_call_calculate_fibonacci_with(self, input):
        return self.calculate_instance.fibonacci(input)
    
    def __then_the_orientation_is_horizontal(self,result):
        self.assertEqual('0, 1, 1, 2',result)

