from redis import Redis
import json

if __name__ == "__main__":
    redis = Redis(host='localhost', port=6379, db=0)
    print("Monitoring Task Status (Press Ctrl+C to Exit):")
    try:
        while True:
            keys = redis.keys("*")
            for key in keys:
                task_id = key.decode("utf-8")
                task_status = redis.get(task_id).decode("utf-8")
                print(f"Task ID: {task_id}, Status: {json.loads(task_status)}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting Monitoring...")

