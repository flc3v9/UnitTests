import unittest
from datetime import datetime

def check_length(symbol_length):
    length = len(symbol_length)

    if 1 <= length <= 7:
            return True
    else:
        return False
    
def check_uppercase(symbol_case):
    return symbol_case.isupper()

def check_alpha(symbol_alpha):
    return symbol_alpha.isalpha()


class TestStockVisualizerInput(unittest.TestCase):

    # capitalized, 1-7 alpha characters
    def test_symbol(self):
        symbol_1 = "IBM"
        symbol_2 = "GOOGL"
        symbol_3 = "testing123"

        self.assertEqual(check_uppercase(symbol_1), True)
        self.assertEqual(check_uppercase(symbol_2), True)
        self.assertEqual(check_uppercase(symbol_3), False)

        self.assertEqual(check_alpha(symbol_1), True)
        self.assertEqual(check_alpha(symbol_2), True)
        self.assertEqual(check_alpha(symbol_3), False)

        self.assertEqual(check_length(symbol_1), True)
        self.assertEqual(check_length(symbol_2), True)
        self.assertEqual(check_length(symbol_3), False)


    # 1 numeric character (1 or 2)
    def test_chart_type(self):
        bar = 1
        line = 2

        self.assertEqual(bar, 1)
        self.assertEqual(line, 2)

    # 1 numeric character (1-4)
    def test_time_series(self):
        intraday = 1
        daily = 2
        weekly = 3
        monthly = 4

        self.assertEqual(intraday, 1)
        self.assertEqual(daily, 2)
        self.assertEqual(weekly, 3)
        self.assertEqual(monthly, 4)
        

    # date type, YYYY-MM-DD
    def test_start_date(self):
        today = "2023-04-16"
        format = "%Y-%m-%d"
        converted_date = datetime.strptime(today, format)

        self.assertEqual(converted_date, datetime(2023, 4, 16))

    # date type, YYYY-MM-DD
    def test_end_date(self):
        today = "2023-04-16"
        format = "%Y-%m-%d"
        converted_date = datetime.strptime(today, format)

        self.assertEqual(converted_date, datetime(2023, 4, 16))

if __name__ == "__main__":
    unittest.main()