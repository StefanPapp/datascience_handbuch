from pykafka import KafkaClient


def main():
    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics[b'chatdemo']
    with topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce(('test ' + str(i ** 2)).encode())


if __name__ == '__main__':
    main()
