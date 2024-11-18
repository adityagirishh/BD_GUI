import tkinter as tk
from yadtq_module.result_backend import ResultBackend

def update_status(text_widget):
    result_backend = ResultBackend()
    tasks = result_backend.get_all_results()

    text_widget.delete(1.0, tk.END)
    for task_id, data in tasks.items():
        text_widget.insert(tk.END, f"Task ID: {task_id}, Status: {data['status']}, Result: {data.get('result')}\n")

def main():
    root = tk.Tk()
    root.title("Task Monitor")

    text_widget = tk.Text(root, height=20, width=50)
    text_widget.pack()

    tk.Button(root, text="Refresh", command=lambda: update_status(text_widget)).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
