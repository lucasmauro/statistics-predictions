import unittest
import statistics as stats


class Tests(unittest.TestCase):

    def test_average(self):
        self.assertEqual(25.35, stats.average([10.1, 20.8, 30.4, 40.1]))

    def test_median(self):
        self.assertEqual(3.0192, stats.median([1.0494, 2.689, 3.3494, 4.3374]))
        self.assertEqual(3.0192, stats.median([3.3494, 2.689, 1.0494, 4.3374]))
        self.assertEqual(3.35, stats.median([1.9, 2.105, 3.35, 4.401, 5.55]))
        self.assertEqual(3.35, stats.median([3.35, 5.55, 1.9, 4.401, 2.105]))

    def test_range(self):
        self.assertEqual(0, stats.range([1, 1]))
        self.assertEqual(1, stats.range([1, 2]))
        self.assertEqual(78891, stats.range([19874, 65084, 98765]))

    def test_standard_deviation(self):
        self.assertEqual(0, stats.standard_deviation([1, 1]))
        self.assertEqual(0.5, stats.standard_deviation([1, 2]))
        self.assertEqual(11.776565713313877, stats.standard_deviation([1963, 1983, 1989, 1994]))

    def test_sum(self):
        self.assertEqual(2, stats.sum([1, 1]))
        self.assertEqual(230880, stats.sum([9480, 6548, 65018, 149834]))

    def test_variance(self):
        self.assertEqual(0, stats.variance([1, 1, 1, 1, 1]))
        self.assertEqual(0.25, stats.variance([1, 2]))
        self.assertEqual(138.6875, stats.variance([1963, 1983, 1989, 1994]))

if __name__ == '__main__':
    unittest.main()
