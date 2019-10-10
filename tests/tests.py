import unittest
import math

from homework import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.t_rect = Rectangle
        self.t_norm_rect = Rectangle(2, 4)
        self.t_sqr_rect = Rectangle(2, 2)
        self.t_norm_rect_diagonal = math.sqrt(
            math.pow(self.t_norm_rect.height, 2) +
            math.pow(self.t_norm_rect.width, 2))
        self.t_sqr_rect_diagonal = math.sqrt(
            math.pow(self.t_sqr_rect.height, 2) +
            math.pow(self.t_sqr_rect.width, 2))
        self.t_sqr_rad_of_inscribed_circle =\
            self.t_sqr_rect_diagonal / (2 * math.sqrt(2))

    def tearDown(self) -> None:
        del self.t_rect

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.t_norm_rect.get_rectangle_perimeter(), 12)

    def test_get_rectangle_square(self):
        self.assertEqual(self.t_sqr_rect.get_rectangle_square(), 4)

    def test_get_sum_of_corners_success(self):
        for i in range(1, 5):
            with self.subTest(i=i):
                self.assertEqual(
                    self.t_norm_rect.get_sum_of_corners(i), i * 90)

    def test_get_sum_of_corners_error(self):
        for i in range(5, 100):
            with self.subTest(i=i):
                self.assertRaises(ValueError)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.t_norm_rect.get_rectangle_diagonal(),
                         self.t_norm_rect_diagonal)
        self.assertEqual(self.t_sqr_rect.get_rectangle_diagonal(),
                         self.t_sqr_rect_diagonal)

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.t_norm_rect.get_radius_of_circumscribed_circle(),
                         self.t_norm_rect_diagonal / 2)
        self.assertEqual(self.t_sqr_rect.get_radius_of_circumscribed_circle(),
                         self.t_sqr_rect_diagonal / 2)

    def test_get_radius_of_inscribed_circle_success(self):
        self.assertEqual(self.t_sqr_rect.get_radius_of_inscribed_circle(),
                         self.t_sqr_rad_of_inscribed_circle)

    def test_get_radius_of_inscribed_circle_error(self):
        self.assertRaises(ValueError,
                          self.t_norm_rect.get_radius_of_inscribed_circle)


if __name__ == '__main__':
    unittest.main()
