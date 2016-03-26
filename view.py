from dateutil.relativedelta import relativedelta
from consts import GITHUB_API_URL
from validator import Validator
from flask.views import View
from flask import request
import datetime
import requests
import json


class GithubApiView(View):
    """ The main API handler (Works for HTTP GET). """
    methods = ['GET']
    DATE_FORMAT = '%Y-%m-%d'
    MAX_RESULTS = 10

    def __init__(self):
        self.validator = Validator()

    def dispatch_request(self):
        """
        Validates & Parses user input, then queries github API and returns
        either an object (or an error object, if any).
        """
        language = request.args.get('language') or 'Any'
        creation_date = request.args.get('created')

        if not self.validator.validate(language, creation_date):
            return json.dumps(self.validator.get_error())

        query = 'language:{0}+created:{1}'.format(language, self._parse_creation_date(creation_date))
        repositories = requests.get(GITHUB_API_URL.format(query=query)).json()['items'][:self.MAX_RESULTS]
        results = [self._build_repository_object(r) for r in repositories]
        return json.dumps({'error_code': 0, 'error': None, 'results': results})

    def _parse_creation_date(self, creation_date):
        now = datetime.datetime.now()
        date = {'past-week': '>=' + (now - relativedelta(weeks=1)).strftime(self.DATE_FORMAT),
                'past-month': '>=' + (now - relativedelta(months=1)).strftime(self.DATE_FORMAT),
                'past-year': '>=' + (now - relativedelta(years=1)).strftime(self.DATE_FORMAT),
                None: '<=' + now.strftime(self.DATE_FORMAT)}
        return date[creation_date]

    @staticmethod
    def _build_repository_object(repository):
        return {'id': repository['id'],
                'full_name': repository['full_name'],
                'html_url': repository['html_url'],
                'description': repository['description'],
                'private': repository['private'],
                'created_at': repository['created_at'],
                'updated_at': repository['updated_at'],
                'clone_url': repository['clone_url'],
                'size': repository['size'],
                'stargazers_count': repository['stargazers_count'],
                'language': repository['language'],
                'forks_count': repository['forks_count']}
