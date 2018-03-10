import celery

app = celery.Celery('05_celery-chain',
                   broker='redis://localhost',
                   backend='redis://localhost')


@app.task
def add(x, y):
    return x + y


@app.task
def multiply(x, y):
    return x * y


if __name__ == '__main__':
    chain = celery.chain(add.s(4, 6), multiply.s(10))
    print("Chain: %s" % chain)
    result = chain()
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)