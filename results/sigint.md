---
// Sonuç
1 signal atınca çalışmaya devam ediyor (ctrl+C), 2.si olursa terminate ediyor ama elindeki işi yazıyor, workerpooldan bir sn daha iş alabiliyor
---

1 sigint signal sonucu

2025-07-01 06:56:31,449: INFO/MainProcess] Received task: celery_signal_test.tasks.long_task[1b55b388-3f07-4e85-b465-40e84556bab5]  
[2025-07-01 06:56:31,452: INFO/ForkPoolWorker-8] [TASK START] Task 1b55b388-3f07-4e85-b465-40e84556bab5 started.
[2025-07-01 06:56:32,454: INFO/ForkPoolWorker-8] [TASK PROGRESS] 1/30 seconds
[2025-07-01 06:56:33,456: INFO/ForkPoolWorker-8] [TASK PROGRESS] 2/30 seconds
[2025-07-01 06:56:34,458: INFO/ForkPoolWorker-8] [TASK PROGRESS] 3/30 seconds
[2025-07-01 06:56:35,460: INFO/ForkPoolWorker-8] [TASK PROGRESS] 4/30 seconds
[2025-07-01 06:56:36,463: INFO/ForkPoolWorker-8] [TASK PROGRESS] 5/30 seconds
[2025-07-01 06:56:37,465: INFO/ForkPoolWorker-8] [TASK PROGRESS] 6/30 seconds

worker: Hitting Ctrl+C again will terminate all running tasks!

worker: Warm shutdown (MainProcess)
[2025-07-01 06:56:38,469: INFO/ForkPoolWorker-8] [TASK PROGRESS] 7/30 seconds
[2025-07-01 06:56:39,472: INFO/ForkPoolWorker-8] [TASK PROGRESS] 8/30 seconds
[2025-07-01 06:56:40,475: INFO/ForkPoolWorker-8] [TASK PROGRESS] 9/30 seconds
[2025-07-01 06:56:41,477: INFO/ForkPoolWorker-8] [TASK PROGRESS] 10/30 seconds
[2025-07-01 06:56:42,480: INFO/ForkPoolWorker-8] [TASK PROGRESS] 11/30 seconds
[2025-07-01 06:56:43,483: INFO/ForkPoolWorker-8] [TASK PROGRESS] 12/30 seconds
[2025-07-01 06:56:44,486: INFO/ForkPoolWorker-8] [TASK PROGRESS] 13/30 seconds
[2025-07-01 06:56:45,489: INFO/ForkPoolWorker-8] [TASK PROGRESS] 14/30 seconds
[2025-07-01 06:56:46,491: INFO/ForkPoolWorker-8] [TASK PROGRESS] 15/30 seconds
[2025-07-01 06:56:47,495: INFO/ForkPoolWorker-8] [TASK PROGRESS] 16/30 seconds
[2025-07-01 06:56:48,498: INFO/ForkPoolWorker-8] [TASK PROGRESS] 17/30 seconds
[2025-07-01 06:56:49,501: INFO/ForkPoolWorker-8] [TASK PROGRESS] 18/30 seconds
[2025-07-01 06:56:50,511: INFO/ForkPoolWorker-8] [TASK PROGRESS] 19/30 seconds
[2025-07-01 06:56:51,513: INFO/ForkPoolWorker-8] [TASK PROGRESS] 20/30 seconds
[2025-07-01 06:56:52,516: INFO/ForkPoolWorker-8] [TASK PROGRESS] 21/30 seconds
[2025-07-01 06:56:53,518: INFO/ForkPoolWorker-8] [TASK PROGRESS] 22/30 seconds
[2025-07-01 06:56:54,520: INFO/ForkPoolWorker-8] [TASK PROGRESS] 23/30 seconds
[2025-07-01 06:56:55,523: INFO/ForkPoolWorker-8] [TASK PROGRESS] 24/30 seconds
[2025-07-01 06:56:56,526: INFO/ForkPoolWorker-8] [TASK PROGRESS] 25/30 seconds
[2025-07-01 06:56:57,528: INFO/ForkPoolWorker-8] [TASK PROGRESS] 26/30 seconds
[2025-07-01 06:56:58,530: INFO/ForkPoolWorker-8] [TASK PROGRESS] 27/30 seconds
[2025-07-01 06:56:59,533: INFO/ForkPoolWorker-8] [TASK PROGRESS] 28/30 seconds
[2025-07-01 06:57:00,536: INFO/ForkPoolWorker-8] [TASK PROGRESS] 29/30 seconds
[2025-07-01 06:57:01,539: INFO/ForkPoolWorker-8] [TASK PROGRESS] 30/30 seconds
[2025-07-01 06:57:01,540: INFO/ForkPoolWorker-8] [TASK END] Task 1b55b388-3f07-4e85-b465-40e84556bab5 completed.
[2025-07-01 06:57:01,543: INFO/ForkPoolWorker-8] Task celery_signal_test.tasks.long_task[1b55b388-3f07-4e85-b465-40e84556bab5] succeeded in 30.090873792s: None

2 signal sonucu
[2025-07-01 06:57:26,894: INFO/ForkPoolWorker-8] [TASK START] Task a936f76c-2ab6-4564-9409-be02a57af81b started.
[2025-07-01 06:57:27,896: INFO/ForkPoolWorker-8] [TASK PROGRESS] 1/30 seconds
[2025-07-01 06:57:28,899: INFO/ForkPoolWorker-8] [TASK PROGRESS] 2/30 seconds

worker: Hitting Ctrl+C again will terminate all running tasks!

worker: Warm shutdown (MainProcess)
[2025-07-01 06:57:29,902: INFO/ForkPoolWorker-8] [TASK PROGRESS] 3/30 seconds
[2025-07-01 06:57:30,903: INFO/ForkPoolWorker-8] [TASK PROGRESS] 4/30 seconds
[2025-07-01 06:57:31,905: INFO/ForkPoolWorker-8] [TASK PROGRESS] 5/30 seconds
[2025-07-01 06:57:32,908: INFO/ForkPoolWorker-8] [TASK PROGRESS] 6/30 seconds
[2025-07-01 06:57:33,911: INFO/ForkPoolWorker-8] [TASK PROGRESS] 7/30 seconds
[2025-07-01 06:57:34,915: INFO/ForkPoolWorker-8] [TASK PROGRESS] 8/30 seconds
[2025-07-01 06:57:35,918: INFO/ForkPoolWorker-8] [TASK PROGRESS] 9/30 seconds
[2025-07-01 06:57:36,931: INFO/ForkPoolWorker-8] [TASK PROGRESS] 10/30 seconds
[2025-07-01 06:57:37,934: INFO/ForkPoolWorker-8] [TASK PROGRESS] 11/30 seconds

worker: Cold shutdown (MainProcess)
[2025-07-01 06:57:38,936: INFO/ForkPoolWorker-8] [TASK PROGRESS] 12/30 seconds
