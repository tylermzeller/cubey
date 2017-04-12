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

    def test_times_triggeru2(self):
        c = qb.Cube()
        d = qb.Cube()
        for times in [1, 2, 3, 4]:
            c.trigger_u2(times)
            for i in range(times):
                d.trigger_u2()
            self.assertEqual(c, d)

    def test_times_trigger_0(self):
        c = qb.Cube()
        c.trigger_u2(0)
        self.assertTrue(c.is_solved())

    def test_times_triggeru2_large_positive(self):
        c = qb.Cube()
        d = qb.Cube()
        large_positive_times = 9999999999
        effective_times = large_positive_times % 2
        c.trigger_u2(large_positive_times)
        d.trigger_u2(effective_times)
        self.assertEqual(c, d)

    def test_times_trigger_u2_negative(self):
        c = qb.Cube()
        c.trigger_u2(-1)
        self.assertTrue(c.is_solved())

    def test_trigger_u2_2(self):
        c = qb.Cube()
        c.trigger_u2(2)
        self.assertTrue(c.is_solved())

    def test_sune_6(self):
        c = qb.Cube()
        c.sune(6)
        self.assertTrue(c.is_solved())

    '''
    ---------------------------------------------------------------------------
    |    Helper Methods:                                                      |
    ---------------------------------------------------------------------------
    '''
    def test_flatten_face_rows(self):
        a = [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
        b = qb.Cube._flatten_face_rows(a)
        self.assertEqual(b, [49, 84, 51, 80, 7, 37, 20, 34, 70])

    def test_reconstruct_face_rows(self):
        a = [49, 84, 51, 80, 7, 37, 20, 34, 70]
        b = qb.Cube._reconstruct_face_rows(a)
        self.assertEqual(b, [[49, 84, 51], [80, 7, 37], [20, 34, 70]])

    def test_flatten_face_columns(self):
        a = [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
        b = qb.Cube._flatten_face_columns(a)
        self.assertEqual(b, [49, 80, 20, 84, 7, 34, 51, 37, 70])

    def test_reconstruct_face_columns(self):
        a = [49, 80, 20, 84, 7, 34, 51, 37, 70]
        b = qb.Cube._reconstruct_face_columns(a)
        self.assertEqual(b, [[49, 84, 51], [80, 7, 37], [20, 34, 70]])

    def test_rotate_face_cw(self):
        a = [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
        qb.Cube._rotate_face_cw(a)
        self.assertEqual(a, [[20, 80, 49], [34, 7, 84], [70, 37, 51]])

    def test_rotate_face_ccw(self):
        a = [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
        qb.Cube._rotate_face_ccw(a)
        self.assertEqual(a, [[51, 37, 70], [84, 7, 34], [49, 80, 20]])

if __name__ == '__main__':
    unittest.main()
