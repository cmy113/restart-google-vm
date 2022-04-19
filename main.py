import googleapiclient.discovery
import time

# Prerequisite
# 1. set timeout for cloud functions to 540s or at least 120s
# 2. Trigger point to be restart_vm
# 3. Python 3.9
# 4. Go to your Pub/Sub topic, add principal for Pub/Sub Publisher for service-xxxx@gcp-sa-monitoring-notification.iam.gserviceaccount.com


# Define variables
PROJECT = "xyz"
ZONE = "us-west1-b"
INSTANCE = "ghost"

def restart_vm(event, context):
    compute = googleapiclient.discovery.build('compute', 'v1')

    # Stop VM
    print(f"Stopping instance: {INSTANCE} in project: {PROJECT} in zone: {ZONE}")

    result = compute.instances().stop(project=PROJECT, zone=ZONE, instance=INSTANCE).execute()

    # Sleep for 90s for it to fully stop
    print("Sleep for 90s")
    time.sleep(90)

    # Start VM
    print(f"Starting instance: {INSTANCE} in project: {PROJECT} in zone: {ZONE}")
    result = compute.instances().start(project=PROJECT, zone=ZONE, instance=INSTANCE).execute()