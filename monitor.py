import psutil
import subprocess
import time
import logging
import datetime

# Logging setup
logging.basicConfig(
    filename='autoscale.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

THRESHOLD = 75.0
scaled = False

def get_cpu():
    return psutil.cpu_percent(interval=2)

def get_instance_name():
    return "autoscaled-vm-" + datetime.datetime.now().strftime("%H%M%S")

def create_gcp_vm():
    instance_name = get_instance_name()

    cmd = [
        "gcloud", "compute", "instances", "create", instance_name,
        "--zone=asia-south1-a",
        "--machine-type=e2-micro",
        "--image-family=ubuntu-2204-lts",
        "--image-project=ubuntu-os-cloud",
        "--tags=autoscaled"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"GCP VM created: {instance_name}")
        logging.info(f"VM created: {instance_name}")
    else:
        print("Error:", result.stderr)
        logging.error(result.stderr)

print("Monitoring started... Press Ctrl+C to stop.")

while True:
    cpu = get_cpu()
    print(f"CPU Usage: {cpu:.1f}%")
    logging.info(f"CPU: {cpu:.1f}%")

    if cpu > THRESHOLD and not scaled:
        print("Threshold exceeded! Creating VM...")
        logging.info("Threshold exceeded. Creating VM...")
        create_gcp_vm()
        scaled = True

    time.sleep(5)