def application(environ, start_response):
    """가장 간단한 애플리케이션 객체"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']
