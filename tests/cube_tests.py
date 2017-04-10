import unittest
import cubey as qb

class TestCubeMethods(unittest.TestCase):

    def test_solved(self):
        c = qb.Cube()
        self.assertTrue(c.is_solved())

    def test_equal(self):
        c = qb.Cube()
        d = qb.Cube()
        self.assertTrue(c == d)

    def test_times_trigger(self):
        c = qb.Cube()
        d = qb.Cube()
        for times in [1, 2, 3, 4]:
            c.trigger(times)
            for i in range(times):
                d.trigger()
            self.assertEqual(c, d)

    def test_times_trigger_0(self):
        c = qb.Cube()
        c.trigger(0)
        self.assertTrue(c.is_solved())

    def test_times_trigger_large_positive(self):
        c = qb.Cube()
        d = qb.Cube()
        large_positive_times = 9999999999
        effective_times = large_positive_times % 4
        c.trigger(large_positive_times)
        d.trigger(effective_times)
        self.assertEqual(c, d)

    def test_times_trigger_negative(self):
        c = qb.Cube()
        c.trigger(-1)
        self.assertTrue(c.is_solved())
    
    def test_trigger_4(self):
        c = qb.Cube()
        c.trigger(4)
        self.assertTrue(c.is_solved())

    def test_sune_6(self):
        c = qb.Cube()
        c.sune(6)
        self.assertTrue(c.is_solved())

if __name__ == '__main__':
    unittest.main()
