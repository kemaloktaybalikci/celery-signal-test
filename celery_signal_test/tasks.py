import time
import logging
from celery_signal_test.celery import app
from celery import Task

logging.basicConfig(level=logging.INFO)


class CeleryTask(Task):
    acks_late = True
    task_reject_on_worker_lost = True


@app.task(base=CeleryTask, bind=True)
def long_task(self):
    logging.info(f"[TASK START] Task {self.request.id} started.")
    try:
        for i in range(30):
            time.sleep(1)
            logging.info(f"[TASK PROGRESS] {i + 1}/30 seconds")
    except Exception as e:
        logging.error(f"[TASK ERROR] Exception: {str(e)}")
        raise
    logging.info(f"[TASK END] Task {self.request.id} completed.")
