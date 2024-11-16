import json
import time
from kafka import KafkaConsumer
from redis import Redis

class Worker:
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self.consumer = KafkaConsumer(
            'tasks',
            bootstrap_servers='localhost:9092',
            group_id='worker-group',
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
        self.redis = Redis(host='localhost', port=6379, db=0)

    def process_task(self, task):
        task_id = task["task-id"]
        task_type = task["task"]
        args = task["args"]

        self.redis.set(task_id, json.dumps({"status": "processing"}))
        time.sleep(3)  # Simulate task execution time

        try:
            if task_type == "add":
                result = sum(args)
            elif task_type == "sub":
                result = args[0] - args[1]
            elif task_type == "multiply":
                result = args[0] * args[1]
            else:
                raise ValueError(f"Unsupported task type: {task_type}")

            self.redis.set(task_id, json.dumps({"status": "success", "result": result}))
        except Exception as e:
            self.redis.set(task_id, json.dumps({"status": "failed", "error": str(e)}))

    def run(self):
        print(f"Worker {self.worker_id} started.")
        for message in self.consumer:
            task = message.value
            print(f"Worker {self.worker_id} processing task: {task}")
            self.process_task(task)

