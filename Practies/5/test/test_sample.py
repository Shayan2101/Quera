import unittest
from function import calc


class TestSampleMultyCalc(unittest.TestCase):

    def test_sample_return_types(self):
        n = [1, 2, 3, 4]
        self.assertIs(type(calc(n)), tuple, "خروجی کد شما باید یک tuple باشد.")
        self.assertEqual(len(list(calc(n))), 3, "خروجی کد شما باید دقیقا سه عضو داشته باشد.")
        self.assertIs(type(list(calc(n))[0]), float, "میانگین محاسبه شده در کد شما از جنس float نیست.")
        self.assertIs(type(list(calc(n))[1]), float, "میانه محاسبه شده در کد شما از جنس float نیست.")
        self.assertIs(type(list(calc(n))[2]), int, "بیشترین عضو محاسبه شده در کد شما از جنس int نیست.")

    def test_sample_with_array_of_size_3(self):
        self.assertEqual((9.666666666666666, 5, 20), calc([4, 5, 20]),
                         'خروجی تابع به ازای ورودی [20 ,5 ,4] باید (20 ,5 ,9.666666666666666) باشد.')

    def test_sample_with_array_of_size_3_multiple_3(self):
        self.assertEqual((12.0, 5, 30), calc([1, 5, 30]),
                         'خروجی تابع به ازای ورودی [30 ,5 ,1] باید (30 ,5 ,12.0) باشد.')

    def test_sample_with_array_of_size_4(self):
        self.assertEqual((20.25, 24.5, 30), calc([2, 20, 30, 29]),
                         'خروجی تابع به ازای ورودی [29 ,30 ,20 ,2] باید (30 ,24.5 ,20.25) باشد.')
