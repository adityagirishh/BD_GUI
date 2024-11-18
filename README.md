<img width="302" alt="Screenshot 2024-11-18 at 12 04 10 PM" src="https://github.com/user-attachments/assets/fd50c9bc-db4a-4ab7-975a-57e5db920d56">
this one has a GUI too

Commands to Set Up the Environment
Clone the Repository:

bash
Copy code
git clone https://github.com/adityagirishh/BD_GUI.git
cd BD_GUI
Start Kafka and Zookeeper (via Docker Compose): Ensure Docker is installed and running:

bash
Copy code
docker-compose up -d
Set Up Backend: Install dependencies and start the Redis backend:

bash
Copy code
cd backend
pip install -r requirements.txt
python backend.py
Start Worker Nodes: Open three separate terminals for the workers:

bash
Copy code
cd workers
pip install -r requirements.txt
python worker.py --worker-id worker1
python worker.py --worker-id worker2
python worker.py --worker-id worker3
Start the Client: In a new terminal:

bash
Copy code
cd client
pip install -r requirements.txt
python client.py
Procedure to Enter Input
Submit a Task via the Client:

A GUI will appear for task submission.
Select a task type (e.g., add, sub, multiply) from the dropdown.
Enter the task arguments in the input fields.
Click the "Submit Task" button.
Monitor the Logs:

Workers: Each worker terminal will log the tasks they are processing, e.g.:

[Worker-1] Received Task ID: d5750c0e-ed82 | Task: add | Args: [1, 2]
[Worker-1] Task Completed: Result = 3
Client: The GUI will display the submitted task's ID and its status.
Query Task Status:

In the client GUI, enter the task ID and click "Check Status."
The status will be fetched from Redis and displayed, e.g.:

Task ID: d5750c0e-ed82
Status: Success
Result: 3
Expected Output
Client GUI Output (Logs and Results)
Task Submission:


Task Submitted: 
Task ID: d5750c0e-ed82
Status: Queued
Task Status Query (after completion):

plaintext
Copy code
Task ID: d5750c0e-ed82
Status: Success
Result: 3
Worker Logs (from Worker Terminals):
Each worker will log tasks it processes. For example:

plaintext
Copy code
[Worker-2] Received Task ID: a6b07d8e-dbe7 | Task: multiply | Args: [4, 5]
[Worker-2] Task Completed: Result = 20
Demonstrating Parallel Execution and Fault Tolerance
Submit several tasks in rapid succession:

For instance, submit these tasks via the client:
Task 1: add, [1, 2]
Task 2: sub, [10, 4]
Task 3: multiply, [3, 7]
Expected Behavior:

Workers will pick up tasks in parallel, ensuring load balancing.
Each worker's terminal will display the task it processes.
Redis will reflect the status and results of each task.
Simulate Fault Tolerance:

Stop a worker (e.g., worker1) and observe how tasks are redistributed to the other workers.
Restart the stopped worker and observe it rejoining the task processing pool.
