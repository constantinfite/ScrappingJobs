import unittest
from datetime import date, timedelta
from src.transformers import post_date


class test_post_date(unittest.TestCase):

    def test_convert_to_digit(self):
        fake_post_date = ["Postedil y a 15 jours", "Postedil y a 30+ jours", "PostedAujourd'hui",
                          "PostedPubliée à l'instant", "Recrutement régulier"]
        expected_post_date = [15, 30, 0, 0, 0]

        computed_post_date = post_date.convert_to_digit(fake_post_date)
        self.assertEqual(expected_post_date, computed_post_date)

    def test_convert_to_date(self):
        today_date = date.today()
        fake_post_date = [15, 30, 0]
        expected_post_date = [today_date - timedelta(days=15), today_date - timedelta(days=30),
                              today_date - timedelta(days=0)]

        computed_post_date = post_date.convert_to_date(fake_post_date)
        self.assertEqual(expected_post_date, computed_post_date)


if __name__ == '__main__':
    unittest.main()
