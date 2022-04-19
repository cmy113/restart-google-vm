import googleapiclient.discovery
import time
# Remember to set timeout to 540s or at least 120s
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