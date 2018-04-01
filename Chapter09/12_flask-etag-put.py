import random
import unittest

import flask
from werkzeug import exceptions


app = flask.Flask(__name__)


class NotModified(exceptions.HTTPException):
    code = 304


ETAG = random.randint(1000, 5000)
VALUE = "hello"


def check_etag(exception_class):
    global ETAG

    if_match = flask.request.headers.get("If-Match")
    if if_match is not None and if_match != str(ETAG):
        raise exception_class

    if_none_match = flask.request.headers.get("If-None-Match")
    if if_none_match is not None and if_none_match == str(ETAG):
        raise exception_class


@app.route("/", methods=['GET'])
def get_index():
    check_etag(NotModified)
    return flask.Response(VALUE, headers={"ETag": ETAG})


@app.route("/", methods=['PUT'])
def put_index():
    global ETAG, VALUE

    check_etag(exceptions.PreconditionFailed)

    ETAG += random.randint(3, 9)
    VALUE = flask.request.data
    return flask.Response(VALUE, headers={"ETag": ETAG})


class TestApp(unittest.TestCase):
    def test_put_index_if_match_positive(self):
        test_app = app.test_client()
        resp = test_app.get()
        etag = resp.headers["ETag"]
        new_value = b"foobar"
        result = test_app.put(headers={"If-Match": etag},
        data=new_value)
        self.assertEqual(200, result.status_code)
        self.assertEqual(new_value, result.data)

    def test_put_index_if_match_negative(self):
        test_app = app.test_client()
        result = test_app.put(headers={"If-Match": "wrong"})
        self.assertEqual(412, result.status_code)


if __name__ == "__main__":
    app.run()