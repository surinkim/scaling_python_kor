import queue
import threading
import uuid

import flask
from werkzeug import routing


application = flask.Flask(__name__)
JOBS = queue.Queue()
RESULTS = {}


class UUIDConverter(routing.BaseConverter):

    @staticmethod
    def to_python(value):
        try:
            return uuid.UUID(value)
        except ValueError:
            raise routing.ValidationError

    @staticmethod
    def to_url(value):
        return str(value)


application.url_map.converters['uuid'] = UUIDConverter


@application.route("/sum/<uuid:job>", methods=['GET'])
def get_job(job):
    if job not in RESULTS:
        return flask.Response(status=404)
    if RESULTS[job] is None:
        return flask.jsonify({"status": "waiting"})
    return flask.jsonify({"status": "done", "result": RESULTS[job]})


@application.route("/sum", methods=['POST'])
def post_job():
    # 무작위로 작업 id를 생성한다.
    job_id = uuid.uuid4()
    # 실행할 작업을 저장한다.
    RESULTS[job_id] = None
    JOBS.put((job_id, flask.request.args.getlist('number', type=float)
        ))
    return flask.Response(
        headers={"Location": flask.url_for("get_job", job=job_id)},
        status=202)


def compute_jobs():
    while True:
        job_id, number = JOBS.get()
        RESULTS[job_id] = sum(number)

if __name__ == "__main__":
    t = threading.Thread(target=compute_jobs)
    t.daemon = True
    t.start()
    application.run(debug=True)