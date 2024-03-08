from celery import Celery

# Configura Celery para usar RabbitMQ como broker
app = Celery('neuroglia',
             broker='amqp://public:1234@localhost/public',
             backend='rpc://',
             include=['neuroglia.tasks'])

# Opcional: Configuraciones de Celery adicionales
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
