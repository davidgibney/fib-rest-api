#!/usr/local/bin/python3
import unittest
from app import calc_fib

class MyTest(unittest.TestCase):
    def test(self):
        # The first 21 Fibonacci numbers Fn for n = 0, 1, 2, …, 20 are:
        self.assertEqual(calc_fib(0), [0])
        self.assertEqual(calc_fib(1), [0,1])
        self.assertEqual(calc_fib(2), [0,1,1])
        self.assertEqual(calc_fib(3), [0,1,1,2])
        self.assertEqual(calc_fib(4), [0,1,1,2,3])
        self.assertEqual(calc_fib(5), [0,1,1,2,3,5])
        self.assertEqual(calc_fib(6), [0,1,1,2,3,5,8])
        self.assertEqual(calc_fib(7), [0,1,1,2,3,5,8,13])
        self.assertEqual(calc_fib(8), [0,1,1,2,3,5,8,13,21])
        self.assertEqual(calc_fib(9), [0,1,1,2,3,5,8,13,21,34])
        self.assertEqual(calc_fib(10), [0,1,1,2,3,5,8,13,21,34,55])
        self.assertEqual(calc_fib(11), [0,1,1,2,3,5,8,13,21,34,55,89])
        self.assertEqual(calc_fib(12), [0,1,1,2,3,5,8,13,21,34,55,89,144])
        self.assertEqual(calc_fib(13), [0,1,1,2,3,5,8,13,21,34,55,89,144,233])
        self.assertEqual(calc_fib(14),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377])
        self.assertEqual(calc_fib(15),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])
        self.assertEqual(calc_fib(16),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987])
        self.assertEqual(calc_fib(17),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597])
        self.assertEqual(calc_fib(18),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584])
        self.assertEqual(calc_fib(19),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181])
        self.assertEqual(calc_fib(20),
        [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765])

if __name__ == '__main__':
    unittest.main()

