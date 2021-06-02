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
#auto_ack=False -> non forniremo la ricevuta di ritorno (l'acknowledgement per la ricezione del messaggio)
channel.basic_consume(queue='worker_queue', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
