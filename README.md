# Celery Signal Test

This project helps you understand how a Celery worker reacts to different shutdown signals: `SIGINT`, `SIGTERM`, and `SIGKILL`.  
It runs a long task and lets you test how the worker handles it when you send each signal.

---

# Setup for non-containerized test

### 1. Clone the project or create the files

### 2. Create and activate a virtual environment

### 3. Install dependencies

### 4. Start Redis

Make sure Redis is installed on your system.  
Then, start and check it:

```bash
redis-server
redis-cli ping
```

---

## 🚀 How to Use for non-containerized test

### 1. Start the Celery worker

Check 'app broker config' on celery file first.

```bash
celery -A celery_signal_test worker --loglevel=INFO
```

You will see logs from the worker in your terminal.

### 2. Run the task

Open a new terminal and activate the virtual environment again.

```bash
python run_task.py
```

This task takes 30 seconds and prints a log every second.

---

## Send Signals to the Worker

You can send signals to the Celery worker to test how it responds.

```bash
chmod +x send_signal.sh # To make commands runnable, run,

./send_signal.sh SIGINT   # Like pressing Ctrl+C
./send_signal.sh SIGTERM  # Common in production systems
./send_signal.sh SIGKILL  # Force kill immediately
```

> The script automatically finds the worker's PID and sends the signal.

---

## Watch For

- "[TASK START]" and "[TASK END]" show when the task begins and ends.
- If "[TASK END]" does not appear, the task was stopped before it finished.
- The worker log may also show messages like "Warm shutdown" or "Cold shutdown".

---

## 🧼 Clean Up

To clear Redis data after testing:

```bash
redis-cli FLUSHALL
```

## Setup for Docker Container Test

## 🐳 Docker Usage (Optional)

This project can also run in Docker. Celery and Redis are started in separate containers, allowing you to test signal behavior (`SIGTERM`, `SIGKILL`, etc.) in a containerized environment.

---

### 1. Docker Requirements

Make sure Docker and Docker Compose are installed on your system:  
👉 https://docs.docker.com/get-docker/

---

### 2. Start the Containers

Check 'app broker config' on celery file first.

In the project root directory:

```bash
docker-compose up --build
```

- Redis and Celery containers will start.
- You can watch the Celery worker logs in the terminal.

---

### 3. Trigger the Task

In the project root directory:

```bash
docker exec -it celery_worker python run_tasks.py
```

---

### 4. Sending Signals

#### Graceful shutdown (SIGTERM):

```bash
docker stop celery_worker
```

#### Force kill (SIGKILL):

```bash
docker kill celery_worker
```

---

### 5. Clean Up

To stop and remove the containers:

```bash
docker-compose down
```
