#!/usr/bin/python
"""Main script for json convert."""
import argparse
import asyncio
import logging
import os
from string import Template

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient


def create_sample_data():
    return {
        "m_rid": "3bd56d4a8acb43f6a748231d534710e1",
        "create_datetime": "2020-11-17T06:25:12Z",
        "period_start_time": "2019-07-23T22:00:00Z",
        "period_end_time": "2020-09-30T22:00:00",
        "quantity": 25.93,
        "quality": "A04",
    }

def create_message(path, data):
    """Create message from template."""
    with open(path, "r") as template_file:
        src = Template(template_file.read())
        result = src.substitute(data)
        return result


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

        data = create_sample_data()
        message = create_message(os.path.join(TEMPLATE_PATH, 'from_template.txt'), data)

        # Add events to the batch.
        event_data_batch.add(EventData(message))
        event_data_batch.add(EventData("Second event"))
        event_data_batch.add(EventData("Third event"))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)


if __name__ == "__main__":
    logging.info("Starting script")

    parser = argparse.ArgumentParser(
        description="Provision Analytics Workspaces.",
        add_help=True,
    )
    parser.add_argument(
        "--connection_string",
        "-c",
        help="Eventhubs Connection String",
    )
    parser.add_argument(
        "--eventhubs_name",
        "-n",
        help="EventHubs Name",
    )
    parser.add_argument(
        "--template_path",
        "-t",
        help="Template Path",
    )

    args = parser.parse_args()

    CONNECTION_STRING = args.connection_string or os.environ.get(
        "EVENT_HUB_CONNECTION_STRING"
    )
    EVENT_HUB_NAME = args.eventhubs_name or os.environ.get(
        "EVENT_HUB_NAME"
    )
    TEMPLATE_PATH = args.template_path or os.environ.get(
        "TEMPLATE_PATH"
    )

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

    if not TEMPLATE_PATH:
        raise ValueError(
            "Template path is required."
            "Have you set the TEMPLATE_PATH env variable?"
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
