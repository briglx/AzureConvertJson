#!/usr/bin/python
"""Main script for json convert."""
import asyncio
import logging
import os

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient


async def run():
    """Create sample messages."""
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData("First event "))
        event_data_batch.add(EventData("Second event"))
        event_data_batch.add(EventData("Third event"))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)


if __name__ == "__main__":
    logging.info("Starting script")

    # Retrieve the IDs and secret to use with ClientSecretCredential
    CONNECTION_STRING = os.environ["EVENT_HUB_CONNECTION_STRING"]

    EVENT_HUB_NAME = os.environ["EVENT_HUB_NAME"]

    if not CONNECTION_STRING:
        raise ValueError(
            "Event hub connection string is required."
            "Have you set the EVENT_HUB_CONNECTION_STRING env variable?"
        )

    if not EVENT_HUB_NAME:
        raise ValueError(
            "Event hub name is required."
            "Have you set the EVENT_HUB_NAME env variable?"
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
