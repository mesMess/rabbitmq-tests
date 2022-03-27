from multiprocessing import connection
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(1, 501):
    message = " [x] Sent 'Hello World' "
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=f'{message} {i}')
    print(f'{message} {i}')

connection.close()
