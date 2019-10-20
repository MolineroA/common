import unittest

from functions import (common_between_two_lists,
                       quantity_a_in_str,
                       power_of_three,
                       add_until_a_single_digit,
                       push_zeros_to_the_end,
                       check_arithmetic_progression,
                       number_not_occur_twice,
                       find_a_missing_number,
                       count_elements_until_tuple,
                       string_reverse)


class Tests(unittest.TestCase):
    def test_common_between_two_lists(self):
        a = [1, 1, 2, 4]
        b = [1, 2, 3, 5]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(common_between_two_lists(a, b), result)

    def test_quantity_a_in_str(self):
        string = 'I am a good developer.I am also a writer'
        self.assertEqual(quantity_a_in_str(string), 5)

    def test_power_of_three_true(self):
        self.assertTrue(power_of_three(9), True)

    def test_power_of_three_false(self):
        self.assertFalse(power_of_three(10), False)

    def test_add_until_a_single_digit(self):
        self.assertEqual(add_until_a_single_digit(48), 3)

    def test_push_zeros_to_the_end(self):
        in_list = [0, 2, 3, 4, 6, 7, 10]
        out_list = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(push_zeros_to_the_end(in_list), out_list)

    def test_check_arithmetic_progression_true(self):
        in_list = [5, 7, 9, 11]
        self.assertTrue(check_arithmetic_progression(in_list), True)

    def test_check_arithmetic_progression_false(self):
        in_list = [5, 7, 9, 10]
        self.assertTrue(check_arithmetic_progression(in_list), False)

    def test_number_not_occur_twice(self):
        in_list = [5, 3, 4, 3, 4]
        self.assertEqual(number_not_occur_twice(in_list), 5)

    def test_find_a_missing_number(self):
        in_list = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(find_a_missing_number(in_list), [5])

    def test_count_elements_until_tuple(self):
        in_list = [1, 2, 3, (1, 2), 3]
        self.assertEqual(count_elements_until_tuple(in_list), 3)

    def test_string_reverse(self):
        normal_string = 'Hello World and Coders'
        reversed_string = 'sredoC dna dlroW olleH'
        self.assertEqual(string_reverse(normal_string), reversed_string)


if __name__ == '__main__':
    unittest.main()
