import json

import flask
import redis


application = flask.Flask(__name__)


def stream_messages(channel):
    r = redis.Redis()
    p = r.pubsub()
    p.subscribe(channel)
    for message in p.listen():
        if message["type"] == "message":
            yield "data: " + json.dumps(message["data"].decode()) + "\n\n"

@application.route("/message/<channel>", methods=['GET'])
def get_messages(channel):
    return flask.Response(
        flask.stream_with_context(stream_messages(channel)),
        mimetype='text/event-stream')


@application.route("/message/<channel>", methods=['POST'])
def send_message(channel):
    data = flask.request.json
    if (not data or 'source' not in data or 'content' not in data):
        flask.abort(400)
    r = redis.Redis()
    r.publish(channel, "<{}> {}".format(data["source"], data["content"]))
    return "", 202
