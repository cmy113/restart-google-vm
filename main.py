import googleapiclient.discovery
import time
import logging

# Define variables
PROJECT = "my-blog-345711"
ZONE = "us-west1-b"
INSTANCE = "test"

def restart_vm(event, context):
    compute = googleapiclient.discovery.build('compute', 'v1')

    # Stop VM
    logging.info(f"Stopping instance: {INSTANCE} in project: {PROJECT} in zone: {ZONE} ")
    result = compute.instances().stop(project=PROJECT, zone=ZONE, instance=INSTANCE).execute()

    # Sleep for 90s for it to fully stop
    logging.info("Sleep for 90s")
    time.sleep(90)

    # Start VM
    logging.info(f"Starting instance: {INSTANCE} in project: {PROJECT} in zone: {ZONE} ")
    result = compute.instances().start(project=PROJECT, zone=ZONE, instance=INSTANCE).execute()