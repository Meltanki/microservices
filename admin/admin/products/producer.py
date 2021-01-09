import pika, json

params = pika.URLParameters('amqps://yyfsqfau:trBS-e95nlE3UuOGvMvfk10W1_unGlIq@gull.rmq.cloudamqp.com/yyfsqfau')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
