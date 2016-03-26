import datetime

from dateutil.relativedelta import relativedelta

from view import GithubApiView
import unittest


class GithubApiViewTest(unittest.TestCase):
    DATE_FORMAT = '%Y-%m-%d'

    def setUp(self):
        self.view = GithubApiView()

    def test_parse_creation_date_sanity(self):
        now = datetime.datetime.now()
        date = {'past-week': '>=' + (now - relativedelta(weeks=1)).strftime(self.DATE_FORMAT),
                'past-month': '>=' + (now - relativedelta(months=1)).strftime(self.DATE_FORMAT),
                'past-year': '>=' + (now - relativedelta(years=1)).strftime(self.DATE_FORMAT),
                None: '<=' + now.strftime(self.DATE_FORMAT)}

        expected = date['past-week']
        extracted = self.view._parse_creation_date('past-week')
        self.assertEqual(expected, extracted)

