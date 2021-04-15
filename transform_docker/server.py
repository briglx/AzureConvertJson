"""HTTP Server to transform json to json using liquid formatter."""
import json
import logging
import os
import uuid

from aiohttp import web
from liquid import Liquid, filter_manager


def generate_guid():
    """Generate a UUID string."""
    return str(uuid.uuid4())


def convert_quality_filter(quality):
    """Jinja2 Filter to convert quality score."""
    quality_map = {
        "A01": "Poor",
        "A02": "OK",
        "A03": "Moderate",
        "A04": "Good",
    }

    if quality not in quality_map:
        raise ValueError("The quality is not a valid value. It must be A01 - A04")

    return quality_map[quality]


def render(data, template_path, template_name, filters, debug=False):
    """Render data as a string for a given template."""
    file_name = os.path.join(template_path, template_name)

    # Register Filter
    for filter_name, filter_code in filters.items():
        filter_manager.register(filter_name)(filter_code)

    with open(file_name, "r") as template_file:
        template_string = template_file.read()
    template = Liquid(template_string, liquid_config={"debug": debug})

    # Transform
    result_string = template.render(**data)  # Unpack argument lists

    return result_string


def render_dict(data, template_path, template_name, filters):
    """Render data as Json Dictionary for a given template."""
    result_string = render(data, template_path, template_name, filters)

    return json.loads(result_string)


async def post_api_transform(request):
    """Handle transform api call."""
    LOGGER.info("post_api_transform called")

    # Get payload
    data = await request.json()

    # Add tracking guid
    data["system_guid"] = generate_guid()

    # set filters
    filters = {"convert": convert_quality_filter}

    # Transform
    message = render_dict(data, TEMPLATE_PATH, TEMPLATE_NAME, filters)

    return web.json_response(message)


if __name__ == "__main__":
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Starting Python HTTP web server.")

    TEMPLATE_PATH = os.environ.get("TEMPLATE_PATH")
    TEMPLATE_NAME = os.environ.get("TEMPLATE_NAME")

    if not TEMPLATE_PATH:
        raise ValueError(
            "Template path is required." "Have you set the TEMPLATE_PATH env variable?"
        )

    if not TEMPLATE_NAME:
        raise ValueError(
            "Template transform is required."
            "Have you set the TEMPLATE_NAME env variable?"
        )

    app = web.Application()
    app.add_routes([web.post("/api/liquid_json_transform", post_api_transform)])
    web.run_app(app)
