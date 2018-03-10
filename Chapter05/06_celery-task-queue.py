import celery


app = celery.Celery('06_celery-task-queue',
                   broker='redis://localhost',
                   backend='redis://localhost')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add.apply_async(args=[4, 6], queue='low-priority')
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)