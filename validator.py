from consts import LANGUAGES, DATE_FILTERS


class Validator(object):
    def __init__(self):
        self.error = None

    def validate(self, language, creation_date):
        """
        :param language: str - One of the programming languages defined in consts.LANGUAGES
        :param creation_date: str - one of 'past-week', 'past-month', 'past-year', or None
        :return: True if valid, else False
        """
        return self.language_validator(language) and self.creation_date_validator(creation_date)

    def get_error(self):
        """
        :return: The error object, if a validation failed.
        """
        return self.error

    def language_validator(self, language):
        """
        :param language: str - One of the programming languages defined in consts.LANGUAGES
        :return: True if valid, else False
        """
        if language not in LANGUAGES:
            self.error = {'error_code': 1, 'error': "invalid language"}
            return False
        return True

    def creation_date_validator(self, creation_date):
        """
        :param creation_date: str - one of 'past-week', 'past-month', 'past-year', or None
        :return: True if valid, else False
        """
        if creation_date not in DATE_FILTERS:
            self.error = {'error_code': 2, 'error': "invalid creation date"}
            return False
        return True
