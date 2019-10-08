import unittest
import math
from homework import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rectangle = Rectangle
        self.normal_rectangle = Rectangle(2, 4)
        self.square_rectangle = Rectangle(2, 2)
        self.normal_rectangle_diagonal = math.sqrt(
            math.pow(self.normal_rectangle.height, 2) + math.pow(self.normal_rectangle.width, 2))
        self.square_rectangle_diagonal = math.sqrt(
            math.pow(self.square_rectangle.height, 2) + math.pow(self.square_rectangle.width, 2))
        self.square_radius_of_inscribed_circle = self.square_rectangle_diagonal / (2 * math.sqrt(2))


    def tearDown(self) -> None:
        del self.rectangle


    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.normal_rectangle.get_rectangle_perimeter(), 12)


    def test_get_rectangle_square(self):
        self.assertEqual(self.square_rectangle.get_rectangle_square(), 4)


    def test_get_sum_of_corners_success(self):
        for i in range(1, 5):
            self.assertEqual(self.normal_rectangle.get_sum_of_corners(i), i * 90)


    def test_get_sum_of_corners_error(self):
        for i in range(5, 100):
            self.assertRaises(ValueError)


    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.normal_rectangle.get_rectangle_diagonal(), self.normal_rectangle_diagonal)
        self.assertEqual(self.square_rectangle.get_rectangle_diagonal(), self.square_rectangle_diagonal)


    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.normal_rectangle.get_radius_of_circumscribed_circle(), self.normal_rectangle_diagonal / 2)
        self.assertEqual(self.square_rectangle.get_radius_of_circumscribed_circle(), self.square_rectangle_diagonal / 2)


    def test_get_radius_of_inscribed_circle_success(self):
        self.assertEqual(self.square_rectangle.get_radius_of_inscribed_circle(), self.square_radius_of_inscribed_circle)


    def test_get_radius_of_inscribed_circle_error(self):
        if self.normal_rectangle.height != self.normal_rectangle.width:
            self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()

