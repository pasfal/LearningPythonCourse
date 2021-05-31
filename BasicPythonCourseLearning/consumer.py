import pika

print("Collegamento a RabbitMQ in corso...")

#Parametri di connessione a RabbitMQ su localhost
connectionParameters = pika.ConnectionParameters(host="localhost")

#Stabiliamo una connessione a RabbitMQ e creaimo un canale
connection = pika.BlockingConnection(connectionParameters)
channel = connection.channel()

#Creazione di una coda che verrà utilizzata dai consumer per leggere i messaggi
queue = channel.queue_declare(queue="worker_queue")

print("...Collegamento terminato")

def callback(channel, method, properties, msg):
    print(f"Ricevuto il messaggio {msg}\n")

#Consume dei messaggi
#no_ack=True -> non forniremo la ricevuta di ritorno (l'acknowlegment per la ricezione del messaggio)
channel.basic_consume(callback, queue="worker_queue", no_ack=True)
channel.start_consuming()

connection.close()