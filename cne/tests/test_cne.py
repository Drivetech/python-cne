from unittest import TestCase

import cne


class TestCne(TestCase):
    def test_is_dict(self):
        data = cne.get()
        self.assertTrue(isinstance(data, dict))

    def test_is_int(self):
        data = cne.get(fuel_type='gasolina_93')
        self.assertTrue(isinstance(data, int))
