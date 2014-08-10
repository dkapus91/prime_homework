'''
Created on 2014.08.09.

@author: David
'''
import unittest
import prime

class Test(unittest.TestCase):
    def test_starting_out(self):
        
        self.assertEqual(prime.prime_factory(2), [2])
        self.assertEqual(prime.prime_factory(11), [11])
        self.assertEqual(prime.prime_factory(128), [2,2,2,2,2,2,2])
        self.assertEqual(prime.prime_factory(571), [571])
        self.assertEqual(prime.prime_factory(1000), [2,2,2,5,5,5])
        self.assertEqual(prime.prime_factory(2310), [2,3,5,7,11])
        self.assertEqual(prime.prime_factory(10234), [2, 7, 17, 43])
        self.assertEqual(prime.prime_factory(20000), [2, 2, 2, 2, 2, 5, 5, 5, 5])
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()