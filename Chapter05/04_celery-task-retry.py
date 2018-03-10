import celery


app = celery.Celery('04_celery-task-retry',
                   broker='redis://localhost',
                   backend='redis://localhost')


@app.task(bind=True, retry_backoff=True,
         retry_kwargs={'max_retries': 5})
def add(self, x, y):
    try:
        return x + y
    except OverflowError as exc:
        self.retry(exc=exc)


if __name__ == '__main__':
    result = add.delay(4, 4)
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)