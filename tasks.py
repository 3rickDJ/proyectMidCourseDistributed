from celery import Celery
from PIL import Image

app = Celery('tasks', broker='amqp://erick@localhost/erickMac')

@app.task
def resize_image(image_path, output_path, size):
    with Image.open(image_path) as image:
        image.thumbnail(size)
        image.save(output_path)

def add(x, y):
    return x + y
