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

cnt = 0

while True:
    message = str(cnt)
    cnt += 1
    #pubblichiamo sulla coda
    channel.basic_publish(exchange="", routing_key="working_queue", body=message)

    print(f"Trasmesso messaggio n. {cnt}\n")

    if cnt > 100:
        break

connection.close()