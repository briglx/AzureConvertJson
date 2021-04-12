************
Convert Json
************

This is an example project on using Azure Logic apps to convert Json

This project demonstrates how to convert Json using several Azure technologies:

- Python Azure API
- Docker Images
- Azure Eventhubs
- Azure Logic Apps

|architecture-overview|

Workflow:

- Generator App sents message to Eventhubs
- LogicApp converts the message to a new format
- LogicApp publish new message to receiving Eventhubs
  
Setup
=====
This setup will deploy the core infrastructure needed to run the the solution:

- Core infrastructure

  - Resource Group
  - Eventhubs

Core infrastructure
-------------------

**Global Variables**

Configure the global variables

.. code-block:: bash

    RG_NAME = jsonconvert
    RG_REGION = westus
    EH_NAMESPACE = jsconvonvert_ehn
    EH_NAME = jsonconvert_eh



**Resource Group**

Create a resource group for this project

.. code-block:: bash

    az group create --name $RG_NAME --location $RG_REGION

**Evenhubs**

.. code-block:: bash

    # Create an Event Hubs namespace. Specify a name for the Event Hubs namespace.
    az eventhubs namespace create --name $EH_NAMESPACE --resource-group $RG_NAME -l $RG_REGION   

    # Create an event hub. Specify a name for the event hub. 
    az eventhubs eventhub create --name $EH_NAME --resource-group $RG_NAME --namespace-name $EH_NAMESPACE

    # Create Read Policy and Connection string
    #TBD 

**Logic App**

- Create Logic App
- Create Integration Account
- Add Map to Integraton Account


Generator
---------

The generator is a python application that runs in a docker container. The container expects the following environment variables stored in a `local.env` file.

Make a copy of `local-example.env` and rename to `local.env`. Edit the file with the necessary values.

- The `EVENT_HUB_CONNECTION_STRING` is in the format `Endpoint=sb://<yournamespace>.servicebus.windows.net/;SharedAccessKeyName=<yoursharedaccesskeyname>;SharedAccessKey=<yoursharedaccesskey>`
- The `EVENT_HUB_NAME` is the name of your eventhub.
- The `TEMPLATE_PATH` is the path to your message template file `/path/to/templates/`

Run generator in docker

.. code-block:: bash

    # Build and run image
    > docker build --pull --rm -f "dockerfile" -t jsonconvert:latest "."
    > docker run --rm -it --env-file local.env jsonconvert:latest

    #Run app
    > python generator/python_generator/main.py --template_path /path/to/templates/

.. code-block:: bash

    # Build and Run Docker
    > docker build --pull --rm -f "dockerfile" -t jsonconvert:latest "."
    > docker run --rm -it --env-file local.env jsonconvert:latest

    #Run app
    > python generator/python_generator/main.py --template_path /path/to/templates/

Transform
---------
This project shows three different ways to transform Json to Json documents from a Logic App:

- Liquid Transform Action
- Call Azure Function
- Call Container Instance

+------------------------------+-------------------------+-----------------+--------------------+
| Feature                      | Liquid Transform Action | Azure Function  | Container Instance |
+==============================+=========================+=================+====================+
| Use Liquid Template Language | ✅                       | ✅               | ✅                  |
+------------------------------+-------------------------+-----------------+--------------------+
| Use Jinja Template Language  |                         | ✅               | ✅                  |
+------------------------------+-------------------------+-----------------+--------------------+
| Use Custom Filters           |                         | ✅               | ✅                  |
+------------------------------+-------------------------+-----------------+--------------------+
| Need Integration Account     | ✅                       |                 |                    |
+------------------------------+-------------------------+-----------------+--------------------+

✅ 
❌

Development
===========

Setup your dev environment by creating a virtual environment

.. code-block:: bash

    # virtualenv \path\to\.venv -p path\to\specific_version_python.exe
    python -m venv .venv.
    .venv\scripts\activate

    deactivate

Make a copy of local-example.env and rename to local.env. Edit the file with the necessary values.

 - The `EVENT_HUB_CONNECTION_STRING` is in the format `Endpoint=sb://<yournamespace>.servicebus.windows.net/;SharedAccessKeyName=<yoursharedaccesskeyname>;SharedAccessKey=<yoursharedaccesskey>`
 - The `EVENT_HUB_NAME` is the name of your eventhub.
 - The `TEMPLATE_PATH` is the path to your message template file `/path/to/templates/`

Style Guidelines
----------------

This project enforces quite strict `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ and `PEP257 (Docstring Conventions) <https://www.python.org/dev/peps/pep-0257/>`_ compliance on all code submitted.

We use `Black <https://github.com/psf/black>`_ for uncompromised code formatting.

Summary of the most relevant points:

- Comments should be full sentences and end with a period.
- `Imports <https://www.python.org/dev/peps/pep-0008/#imports>`_  should be ordered.
- Constants and the content of lists and dictionaries should be in alphabetical order.
- It is advisable to adjust IDE or editor settings to match those requirements.

Ordering of imports
-------------------

Instead of ordering the imports manually, use `isort <https://github.com/timothycrosley/isort>`_.

.. code-block:: bash

    pip3 install isort
    isort -rc .

Use new style string formatting
-------------------------------

Prefer `f-strings <https://docs.python.org/3/reference/lexical_analysis.html#f-strings>`_ over ``%`` or ``str.format``.

.. code-block:: python

    #New
    f"{some_value} {some_other_value}"
    # Old, wrong
    "{} {}".format("New", "style")
    "%s %s" % ("Old", "style")

One exception is for logging which uses the percentage formatting. This is to avoid formatting the log message when it is suppressed.

.. code-block:: python

    _LOGGER.info("Can't connect to the webservice %s at %s", string1, string2)


Testing
--------
You'll need to install the test dependencies into your Python environment:

.. code-block:: bash

    pip3 install -r requirements_dev.txt

Now that you have all test dependencies installed, you can run linting and tests on the project:

.. code-block:: bash

    isort .
    codespell  --skip="./.*,*.csv,*.json,*.pyc,./docs/_build/*,./htmlcov/*"
    black setup.py generator tests
    flake8 setup.py generator tests
    pylint setup.py generator tests
    pydocstyle setup.py generator tests
    pytest tests

.. |architecture-overview| image:: docs/JsonConvertArchitecture.png


References
----------
- Eventhubs python library https://docs.microsoft.com/en-us/python/api/overview/azure/eventhub-readme?view=azure-python
- Eventhubs python getting started https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send
- Liquid template https://shopify.github.io/liquid/basics/introduction/
- Liquid in Logic App https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-enterprise-integration-liquid-transform
- Create Logic App Integration Account https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-enterprise-integration-create-integration-account?tabs=azure-portal
- Azure Fuctions on Docker https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=bash%2Cportal&pivots=programming-language-python