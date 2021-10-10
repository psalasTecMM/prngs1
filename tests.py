import unittest

# import your python package here
# See: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
# Example
# from alumno.[nombre_archivo] import [function1, function2, ...]


class PRNGTest(unittest.TestCase):
    def test_mid_square(self):
        r1 = mid_square(3, 5735)
        self.assertEqual(r1, [0.8902, 0.2456, 0.319])
        self.assertEqual(len(r1), 3)
        r2 = mid_square(3, 1000)
        self.assertEqual(r2, [0.0, 0.0, 0.0])
        self.assertEqual(len(r2), 3)
        r3 = mid_square(3, 675248)
        self.assertEqual(r3, [0.959861, 0.333139, 0.981593])
        self.assertEqual(len(r3), 3)

    def test_mid_product(self):
        r1 = mid_product(3, 5015, 5734)
        self.assertEqual(r1, [0.756, 0.349, 0.3844])
        self.assertEqual(len(r1), 3)

    def test_constant_multiplier(self):
        r1 = constant_multiplier(3, 6965, 9803)
        self.assertEqual(r1, [0.2778, 0.3487, 0.2869])
        self.assertEqual(len(r1), 3)

    def test_get_middle_number(self):
        self.assertEqual(get_middle_numbers(4, 30976), 3097)
        self.assertEqual(get_middle_numbers(4, 6031936), 319)
        self.assertEqual(get_middle_numbers(4, 28756010), 7560)


if __name__ == '__main__':
    unittest.main()
