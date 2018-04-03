import unittest
import flask
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

    return flask.Response("hello world", headers={"ETag": "hword"})


class TestApp(unittest.TestCase):
    def test_get_index(self):
        test_app = application.test_client()
        result = test_app.get()
        self.assertEqual(200, result.status_code)

    def test_get_index_if_match_positive(self):
        test_app = application.test_client()
        result = test_app.get(headers={"If-Match": "hword"})
        self.assertEqual(200, result.status_code)

    def test_get_index_if_match_negative(self):
        test_app = application.test_client()
        result = test_app.get(headers={"If-Match": "foobar"})
        self.assertEqual(304, result.status_code)

    def test_get_index_if_none_match_positive(self):
        test_app = application.test_client()
        result = test_app.get(headers={"If-None-Match": "hword"})
        self.assertEqual(304, result.status_code)

    def test_get_index_if_none_match_negative(self):
        test_app = application.test_client()
        result = test_app.get(headers={"If-None-Match": "foobar"})
        self.assertEqual(200, result.status_code)


if __name__ == "__main__":
    application.run()
