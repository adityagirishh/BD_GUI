from backend import RedisBackend

class ResultBackend:
    def __init__(self):
        self.backend = RedisBackend()

    def add_result(self, task_id, status, result=None):
        self.backend.set_task_status(task_id, status, result)

    def get_result(self, task_id):
        return self.backend.get_task_status(task_id)

    def get_all_results(self):
        return self.backend.get_all_tasks()

    def delete_result(self, task_id):
        self.backend.delete_task(task_id)
