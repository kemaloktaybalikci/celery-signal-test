# run_task.py
from celery_signal_test.tasks import long_task

if __name__ == "__main__":
    result = long_task.delay()
    print(f"Task triggered. ID: {result.id}")
