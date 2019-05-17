import unittest
import math_ext, sequences, primes, properties


class Math(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(math_ext.lcm(range(1, 11)), 2520)
        self.assertEqual(math_ext.lcm([8, 9, 21]), 504)
        self.assertEqual(math_ext.lcm([21, 6]), 42)

    def test_prod(self):
        self.assertEqual(math_ext.prod(range(10)), 0)
        self.assertEqual(math_ext.prod(range(1, 10)), 362880)
        self.assertEqual(math_ext.prod([9,9,8,9]), 5832)

class Sequences(unittest.TestCase):

    def test_fibonacci(self):
        fib_gen = sequences.fibonacci()
        fib_true = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
            610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
            75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309]
        for ft in fib_true:
            self.assertEqual(next(fib_gen), ft)


class Primes(unittest.TestCase):

    def test_prime_factors(self):
        self.assertEqual(primes.prime_factors(15), [3, 5])
        self.assertEqual(primes.prime_factors(460), [2, 2, 5, 23])
        self.assertEqual(primes.prime_factors(13195), [5, 7, 13, 29])

    def test_generate_primes(self):
        primes_gen = primes.generate_primes()
        primes_true = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
            53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
            127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191]
        for pt in primes_true:
            self.assertEqual(next(primes_gen), pt)

    def test_nth_prime(self):
        self.assertEqual(primes.nth_prime(6), 13)
        self.assertEqual(primes.nth_prime(26), 101)
        self.assertEqual(primes.nth_prime(54), 251)
        self.assertEqual(primes.nth_prime(58), 271)


class Properties(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(properties.is_palindrome(2345), False)
        self.assertEqual(properties.is_palindrome(2346987), False)
        self.assertEqual(properties.is_palindrome(3456543), True)
        self.assertEqual(properties.is_palindrome(9009), True)


if __name__ == '__main__':
    unittest.main()
