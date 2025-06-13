import unittest
from geometry.shapes import Circle, Triangle


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), 3.14159, places=4)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)

    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # Not a valid triangle

    def test_right_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right())

    def test_non_right_triangle(self):
        t = Triangle(3, 4, 6)
        self.assertFalse(t.is_right())


if __name__ == "__main__":
    unittest.main()
