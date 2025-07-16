from celery import Celery

# app = Celery("celery_signal_test", broker="redis://localhost:6379/0")
app = Celery("celery_signal_test", broker="redis://redis:6379/0")  # For docker tests

app.conf.update(
    task_track_started=True,
    worker_send_task_events=True,
    worker_shutdown_timeout=60,  # graceful shutdown timeout
)

import celery_signal_test.tasks
