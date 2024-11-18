import tkinter as tk
from tkinter import messagebox
import uuid
from yadtq_module.task_queue import TaskQueue
from yadtq_module.result_backend import ResultBackend

def submit_task(task_type, arg1, arg2):
    broker = "localhost:9092"
    topic = "tasks"
    task_queue = TaskQueue(broker, topic)
    result_backend = ResultBackend()

    task_id = str(uuid.uuid4())
    task = {"task_id": task_id, "task": task_type, "args": [arg1, arg2]}
    task_queue.submit_task(task)
    result_backend.add_result(task_id, "queued")
    log_action(f"Task submitted: {task_id} ({task_type}({arg1}, {arg2}))")
    messagebox.showinfo("Task Submitted", f"Task ID: {task_id}")

def log_action(action):
    with open("client_log.txt", "a") as log_file:
        log_file.write(action + "\n")

def main():
    def on_submit():
        task_type = task_type_var.get()
        try:
            arg1 = int(arg1_entry.get())
            arg2 = int(arg2_entry.get())
            submit_task(task_type, arg1, arg2)
        except ValueError:
            messagebox.showerror("Invalid Input", "Arguments must be integers")

    root = tk.Tk()
    root.title("Task Submission")

    tk.Label(root, text="Task Type:").grid(row=0, column=0)
    task_type_var = tk.StringVar(value="add")
    tk.Entry(root, textvariable=task_type_var).grid(row=0, column=1)

    tk.Label(root, text="Arg1:").grid(row=1, column=0)
    arg1_entry = tk.Entry(root)
    arg1_entry.grid(row=1, column=1)

    tk.Label(root, text="Arg2:").grid(row=2, column=0)
    arg2_entry = tk.Entry(root)
    arg2_entry.grid(row=2, column=1)

    tk.Button(root, text="Submit Task", command=on_submit).grid(row=3, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
