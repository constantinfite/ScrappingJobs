import unittest
from src.transformers import location


class test_location(unittest.TestCase):

    def test_get_departement(self):
        fake_locations = ["Carros (06)", "France", "Marseille (13)"]
        expected_department = [6, 0, 13]

        computed_departement = location.get_departement(fake_locations)
        self.assertEqual(expected_department, computed_departement)

    def test_get_city(self):
        fake_locations = fake_post_date = ["Carros (06)", "France", "Marseille (13)"]
        expected_cities = ["Carros", "France", "Marseille"]

        computed_cities = location.get_city(fake_locations)
        self.assertEqual(expected_cities, computed_cities)


if __name__ == '__main__':
    unittest.main()
