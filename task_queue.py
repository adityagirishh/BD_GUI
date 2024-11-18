from kafka import KafkaProducer, KafkaConsumer
import json

class TaskQueue:
    def __init__(self, broker, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=broker,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def submit_task(self, task):
        self.producer.send(self.topic, task)
        self.producer.flush()

    def consume_tasks(self):
        return KafkaConsumer(
            self.topic,
            bootstrap_servers=["localhost:9092"],
            group_id="workers",
            value_deserializer=lambda m: json.loads(m.decode("utf-8"))
        )
