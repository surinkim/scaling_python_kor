import os

import flask
from gabbi import driver
import werkzeug


application = flask.Flask(__name__)


class NotModified(werkzeug.exceptions.HTTPException):
    code = 304


@application.route("/", methods=['GET'])
def get_index():
    # 이 예제는 항상 동일한 컨텐츠를 사용하므로, Etag도 고정된 값이다.
    ETAG = "hword"

    if_match = flask.request.headers.get("If-Match")
    if if_match is not None and if_match != ETAG:
        raise NotModified

    if_none_match = flask.request.headers.get("If-None-Match")
    if if_none_match is not None and if_none_match == ETAG:
        raise NotModified

    return flask.Response("hello world",
                         headers={"ETag": "hword"})

# 아래 명령으로 테스트를 실행한다.
# python3 -m unittest -v 25_gabbi-flask.py
def load_tests(loader, tests, pattern):
    return driver.build_tests(os.path.dirname(__file__),
                             loader, intercept=lambda: application)


if __name__ == "__main__":
    application.run()