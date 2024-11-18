import tkinter as tk
import time
from yadtq_module.task_queue import TaskQueue
from yadtq_module.result_backend import ResultBackend

def process_tasks(worker_id):
    broker = "localhost:9092"
    topic = "tasks"
    task_queue = TaskQueue(broker, topic)
    result_backend = ResultBackend()

    consumer = task_queue.consume_tasks()
    for message in consumer:
        task = message.value
        task_id = task["task_id"]
        task_type = task["task"]
        args = task["args"]

        result_backend.add_result(task_id, "processing")
        try:
            if task_type == "add":
                result = sum(args)
            elif task_type == "sub":
                result = args[0] - args[1]
            elif task_type == "multiply":
                result = args[0] * args[1]
            else:
                raise ValueError("Unknown task type")

            time.sleep(2)  # Simulate delay
            result_backend.add_result(task_id, "success", result)
        except Exception as e:
            result_backend.add_result(task_id, "failed", str(e))

def main(worker_id):
    root = tk.Tk()
    root.title(f"Worker {worker_id}")

    tk.Label(root, text=f"Worker {worker_id} Running").pack()
    tk.Button(root, text="Start", command=lambda: process_tasks(worker_id)).pack()

    root.mainloop()

if __name__ == "__main__":
    import sys
    worker_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    main(worker_id)
