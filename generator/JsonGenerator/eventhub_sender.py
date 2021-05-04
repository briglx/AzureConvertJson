"""Send events to Eventhub."""
import datetime
import json
import random
import uuid
import os

from azure.eventhub import EventData, EventHubProducerClient

CONNECTION_STRING = os.environ.get("EVENT_HUB_CONNECTION_STRING")
EVENT_HUB_NAME = os.environ.get("EVENT_HUB_NAME")

# This script simulates the production of events for 10 devices.
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

# Create a producer client to produce and publish events to the event hub.
producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING,
    eventhub_name=EVENT_HUB_NAME,
)

for y in range(0, 20):  # For each device, produce 20 events.
    event_data_batch = (
        producer.create_batch()
    )  # Create a batch. You will add events to the batch later.
    for dev in devices:
        # Create a dummy reading.
        reading = {
            "id": dev,
            "timestamp": str(datetime.datetime.utcnow()),
            "uv": random.random(),
            "temperature": random.randint(70, 100),
            "humidity": random.randint(70, 100),
        }
        s = json.dumps(reading)  # Convert the reading into a JSON string.
        event_data_batch.add(EventData(s))  # Add event data to the batch.
    producer.send_batch(event_data_batch)  # Send the batch of events to the event hub.

# Close the producer.
producer.close()
