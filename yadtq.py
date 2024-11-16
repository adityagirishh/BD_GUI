import uuid
import json
from kafka import KafkaProducer, KafkaConsumer
from redis import Redis

class YADTQ:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.redis = Redis(host='localhost', port=6379, db=0)

    def submit_task(self, task_type, args):
        task_id = str(uuid.uuid4())
        task = {"task-id": task_id, "task": task_type, "args": args}
        self.redis.set(task_id, json.dumps({"status": "queued"}))
        self.producer.send('tasks', value=task)
        return task_id

    def get_task_status(self, task_id):
        task_data = self.redis.get(task_id)
        if task_data:
            return json.loads(task_data)
        return {"status": "unknown"}

