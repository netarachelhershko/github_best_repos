from validator import Validator
import unittest


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_language_validator_sanity(self):
        self.assertTrue(self.validator.language_validator("CSS"))

    def test_language_validator_sanity_test_invalid_input(self):
        self.assertFalse(self.validator.language_validator("abcd454"))
        expected = {'error_code': 1, 'error': "invalid language"}
        extracted = self.validator.get_error()
        self.assertEqual(expected, extracted)

    def test_creation_date_sanity(self):
        self.assertTrue(self.validator.creation_date_validator("past-week"))

    def test_creation_date_sanity_test_invalid_input(self):
        self.assertFalse(self.validator.creation_date_validator("abcd454"))
        expected = {'error_code': 2, 'error': "invalid creation date"}
        extracted = self.validator.get_error()
        self.assertEqual(expected, extracted)
