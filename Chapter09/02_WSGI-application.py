from wsgiref.simple_server import make_server


def application(environ, start_response):
    """text/plain으로 wsgi 환경변수를 반환."""
    body = '\n'.join([
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ])

    start_response("200 OK", [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ])

    return [body.encode()]


# 서버 초기화
httpd = make_server('localhost', 8051, application)
# 요청 하나를 기다려서 처리한 뒤에 종료
httpd.handle_request()
# 요청 및 응답을 확인하려면 'curl -v http://localhost:8051' 명령 실행.