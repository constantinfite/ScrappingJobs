import unittest
from src.transformers import extracted_date

class test_extracted_date(unittest.TestCase):
    def test_something(self):
        fake_extracted_date = ["Postedil y a 15 jours", "Postedil y a 30+ jours"]
        expected_extracted_date = [15, 30]

        extracted_date.transform_extract_date(fake_extracted_date)
        self.assertEqual(fake_extracted_date, expected_extracted_date)


if __name__ == '__main__':
    unittest.main()
