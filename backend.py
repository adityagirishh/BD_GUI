import redis
import json

class RedisBackend:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def set_task_status(self, task_id, status, result=None):
        task_data = {"status": status}
        if result is not None:
            task_data["result"] = result
        self.redis.set(task_id, json.dumps(task_data))

    def get_task_status(self, task_id):
        task_data = self.redis.get(task_id)
        return json.loads(task_data) if task_data else {"status": "unknown"}

    def get_all_tasks(self):
        keys = self.redis.keys("*")
        return {key: json.loads(self.redis.get(key)) for key in keys}

    def delete_task(self, task_id):
        self.redis.delete(task_id)
