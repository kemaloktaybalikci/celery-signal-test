---
// Sonuç

worker: Warm shutdown (MainProcess) // Yeni task almayı durduruyor
WorkerLostError: Worker exited prematurely: signal 15 (SIGTERM) // Alt task terminate oluyor

'worker_shutdown_timeout' tanımlanır ve --pool=solo modda çalıştırılırsa alt task tamamlanıyor ama devam etmiyor.

task içinde 'acks_late=True, task_reject_on_worker_lost=True' tanımlanırsa, SIGTERM sonrasında redis tekrar çalışında tekrar taskı aynı id ile alıyor ama 1'den itibaren sayıyor. Worker her düşüp kalktığında, tekrar girebiliyor
---

1 sigint signal sonucu

2025-07-01 07:00:37,582: INFO/MainProcess] Connected to redis://localhost:6379/0
2025-07-01 07:00:37,588: INFO/MainProcess] mingle: searching for neighbors
2025-07-01 07:00:38,604: INFO/MainProcess] mingle: all alone
2025-07-01 07:00:38,622: INFO/MainProcess] celery@kemaloktay-MacBook-Pro.local ready.
2025-07-01 07:00:43,516: INFO/MainProcess] Received task: celery_signal_test.tasks.long_task[26404411-1389-4cc7-9d2d-d5ca98817636]  
2025-07-01 07:00:43,520: INFO/ForkPoolWorker-8] [TASK START] Task 26404411-1389-4cc7-9d2d-d5ca98817636 started.
2025-07-01 07:00:44,522: INFO/ForkPoolWorker-8] [TASK PROGRESS] 1/30 seconds
2025-07-01 07:00:45,524: INFO/ForkPoolWorker-8] [TASK PROGRESS] 2/30 seconds
2025-07-01 07:00:46,529: INFO/ForkPoolWorker-8] [TASK PROGRESS] 3/30 seconds
2025-07-01 07:00:47,532: INFO/ForkPoolWorker-8] [TASK PROGRESS] 4/30 seconds
2025-07-01 07:00:48,539: INFO/ForkPoolWorker-8] [TASK PROGRESS] 5/30 seconds
2025-07-01 07:00:49,541: INFO/ForkPoolWorker-8] [TASK PROGRESS] 6/30seconds

worker: Warm shutdown (MainProcess)
2025-07-01 07:00:50,764: ERROR/MainProcess] Process 'ForkPoolWorker-8' pid:76537 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,776: ERROR/MainProcess] Process 'ForkPoolWorker-7' pid:76536 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,787: ERROR/MainProcess] Process 'ForkPoolWorker-6' pid:76535 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,798: ERROR/MainProcess] Process 'ForkPoolWorker-5' pid:76534 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,809: ERROR/MainProcess] Process 'ForkPoolWorker-4' pid:76533 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,821: ERROR/MainProcess] Process 'ForkPoolWorker-3' pid:76531 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,832: ERROR/MainProcess] Process 'ForkPoolWorker-2' pid:76529 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,844: ERROR/MainProcess] Process 'ForkPoolWorker-1' pid:76528 exited with 'signal 15 (SIGTERM)'
2025-07-01 07:00:50,861: ERROR/MainProcess] Task handler raised error: WorkerLostError('Worker exited prematurely: signal 15 (SIGTERM) Job: 0.')
Traceback (most recent call last):
File "/opt/homebrew/lib/python3.8/site-packages/celery/worker/worker.py", line 205, in start
self.blueprint.start(self)
File "/opt/homebrew/lib/python3.8/site-packages/celery/bootsteps.py", line 119, in start
step.start(parent)
File "/opt/homebrew/lib/python3.8/site-packages/celery/bootsteps.py", line 369, in start
return self.obj.start()
File "/opt/homebrew/lib/python3.8/site-packages/celery/worker/consumer/consumer.py", line 318, in start
blueprint.start(self)
File "/opt/homebrew/lib/python3.8/site-packages/celery/bootsteps.py", line 119, in start
step.start(parent)
File "/opt/homebrew/lib/python3.8/site-packages/celery/worker/consumer/consumer.py", line 596, in start
c.loop(\*c.loop_args())
File "/opt/homebrew/lib/python3.8/site-packages/celery/worker/loops.py", line 83, in asynloop
next(loop)
File "/opt/homebrew/lib/python3.8/site-packages/kombu/asynchronous/hub.py", line 308, in create_loop
events = poll(poll_timeout)
File "/opt/homebrew/lib/python3.8/site-packages/kombu/utils/eventio.py", line 217, in poll
event_list = self.\_quick_poll(timeout)
File "/opt/homebrew/lib/python3.8/site-packages/celery/apps/worker.py", line 284, in \_handle_request
raise exc(exitcode)
celery.exceptions.WorkerShutdown: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/opt/homebrew/lib/python3.8/site-packages/billiard/pool.py", line 1265, in mark_as_worker_lost
raise WorkerLostError(
billiard.exceptions.WorkerLostError: Worker exited prematurely: signal 15 (SIGTERM) Job: 0.

---

celery -A celery_signal_test worker --loglevel=INFO --pool=solo

[2025-07-01 07:19:22,437: INFO/MainProcess] Connected to redis://localhost:6379/0
[2025-07-01 07:19:22,442: INFO/MainProcess] mingle: searching for neighbors
[2025-07-01 07:19:23,455: INFO/MainProcess] mingle: all alone
[2025-07-01 07:19:23,473: INFO/MainProcess] celery@kemaloktay-MacBook-Pro.local ready.
[2025-07-01 07:19:26,612: INFO/MainProcess] Received task: celery_signal_test.tasks.long_task[0e066882-ffde-490a-96b9-5d34acef48c2]  
[2025-07-01 07:19:26,612: INFO/MainProcess] [TASK START] Task 0e066882-ffde-490a-96b9-5d34acef48c2 started.
[2025-07-01 07:19:27,617: INFO/MainProcess] [TASK PROGRESS] 1/30 seconds
[2025-07-01 07:19:28,619: INFO/MainProcess] [TASK PROGRESS] 2/30 seconds
[2025-07-01 07:19:29,627: INFO/MainProcess] [TASK PROGRESS] 3/30 seconds
[2025-07-01 07:19:30,633: INFO/MainProcess] [TASK PROGRESS] 4/30 seconds
[2025-07-01 07:19:31,639: INFO/MainProcess] [TASK PROGRESS] 5/30 seconds

worker: Warm shutdown (MainProcess)

---

tasks]
. celery_signal_test.tasks.long_task

[2025-07-01 07:24:39,704: INFO/MainProcess] Connected to redis://localhost:6379/0
[2025-07-01 07:24:39,710: INFO/MainProcess] mingle: searching for neighbors
[2025-07-01 07:24:40,730: INFO/MainProcess] mingle: all alone
[2025-07-01 07:24:40,749: INFO/MainProcess] celery@kemaloktay-MacBook-Pro.local ready.
[2025-07-01 07:24:40,751: INFO/MainProcess] Received task: celery_signal_test.tasks.long_task[5e87fcf7-1f04-4318-8c4f-9d7cec4ef98c]  
[2025-07-01 07:24:40,752: INFO/MainProcess] [TASK START] Task 5e87fcf7-1f04-4318-8c4f-9d7cec4ef98c started.
[2025-07-01 07:24:41,757: INFO/MainProcess] [TASK PROGRESS] 1/30 seconds
[2025-07-01 07:24:42,761: INFO/MainProcess] [TASK PROGRESS] 2/30 seconds
[2025-07-01 07:24:43,765: INFO/MainProcess] [TASK PROGRESS] 3/30 seconds
[2025-07-01 07:24:44,768: INFO/MainProcess] [TASK PROGRESS] 4/30 seconds
[2025-07-01 07:24:45,772: INFO/MainProcess] [TASK PROGRESS] 5/30 seconds
[2025-07-01 07:24:46,775: INFO/MainProcess] [TASK PROGRESS] 6/30 seconds
[2025-07-01 07:24:47,781: INFO/MainProcess] [TASK PROGRESS] 7/30 seconds

worker: Warm shutdown (MainProcess)
[2025-07-01 07:24:48,012: WARNING/MainProcess] Restoring 1 unacknowledged message(s)

((venv) ) ➜ celery_signal_test celery -A celery_signal_test worker --loglevel=INFO --pool=solo

[2025-07-01 07:24:53,388: INFO/MainProcess] Connected to redis://localhost:6379/0
[2025-07-01 07:24:53,394: INFO/MainProcess] mingle: searching for neighbors
[2025-07-01 07:24:54,410: INFO/MainProcess] mingle: all alone
[2025-07-01 07:24:54,428: INFO/MainProcess] celery@kemaloktay-MacBook-Pro.local ready.
[2025-07-01 07:24:54,430: INFO/MainProcess] Received task: celery_signal_test.tasks.long_task[5e87fcf7-1f04-4318-8c4f-9d7cec4ef98c]  
[2025-07-01 07:24:54,431: INFO/MainProcess] [TASK START] Task 5e87fcf7-1f04-4318-8c4f-9d7cec4ef98c started.
[2025-07-01 07:24:55,436: INFO/MainProcess] [TASK PROGRESS] 1/30 seconds
[2025-07-01 07:24:56,440: INFO/MainProcess] [TASK PROGRESS] 2/30 seconds
[2025-07-01 07:24:57,446: INFO/MainProcess] [TASK PROGRESS] 3/30 seconds
[2025-07-01 07:24:58,451: INFO/MainProcess] [TASK PROGRESS] 4/30 seconds
[2025-07-01 07:24:59,454: INFO/MainProcess] [TASK PROGRESS] 5/30 seconds
[2025-07-01 07:25:00,459: INFO/MainProcess] [TASK PROGRESS] 6/30 seconds

worker: Warm shutdown (MainProcess)
[2025-07-01 07:25:01,297: WARNING/MainProcess] Restoring 1 unacknowledged message(s)
