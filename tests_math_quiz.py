import unittest
from math_quiz import gen_rand_number, gen_rand_operator, check_expression


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = gen_rand_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operator
            rand_operator = gen_rand_operator()
            self.assertIn(rand_operator, valid_operators)
        pass

    def test_function_C(self):
            # Test cases
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 2, '-', '2 - 2', 0),
                (6, 5, '*', '6 * 5', 30),
                (20, 20, '+', '20 + 20', 40),
                (8, 10, '+', '8 + 10', 18),
                (4, 4, '*', '4 * 4', 16),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                # Test a check_expression function
                problem, answer = check_expression(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
