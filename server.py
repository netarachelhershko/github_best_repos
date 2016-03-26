from view import GithubApiView

from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)
    app.add_url_rule('/api/v1/hottestRepositories', view_func=GithubApiView.as_view('GithubView'))
    app.run(host='0.0.0.0', port=8080, debug=False)
