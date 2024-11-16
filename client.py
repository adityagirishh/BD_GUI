from yadtq import YADTQ

if __name__ == "__main__":
    yadtq = YADTQ()
    task_ids = [
        yadtq.submit_task("add", [1, 2]),
        yadtq.submit_task("sub", [2, 3]),
        yadtq.submit_task("multiply", [1, 2]),
        yadtq.submit_task("add", [2, 3]),
        yadtq.submit_task("sub", [3, 6])
    ]
    print("Tasks submitted:")
    for task_id in task_ids:
        print(f" - Task ID: {task_id}")
    print("You can monitor task progress using the worker or monitor scripts.")

