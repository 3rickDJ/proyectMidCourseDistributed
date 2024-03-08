from .celery import app

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def resize_image(image_path, output_path, size):
    with Image.open(image_path) as image:
        image.thumbnail(size)
        image.save(output_path)
