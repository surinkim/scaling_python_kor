import celery


app = celery.Celery('03_celery-task',
    broker='redis://localhost',
    backend='redis://localhost')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add.delay(4, 4)
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)