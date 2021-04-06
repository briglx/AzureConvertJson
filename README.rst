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

Development
===========

Setup your dev environment by creating a virtual environment

.. code-block:: bash

    # virtualenv \path\to\.venv -p path\to\specific_version_python.exe
    python -m venv .venv.
    .venv\scripts\activate

    deactivate

Make a copy of local-example.env and rename to local.env. Edit the file with the necessary values.

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

Now that you have all test dependencies installed, you can run tests on the project:

.. code-block:: bash

    isort .
    codespell  --skip="./.*,*.csv,*.json,*.pyc,./docs/_build/*,./htmlcov/*"
    black setup.py script tests
    flake8 setup.py script tests
    pylint setup.py script tests
    pydocstyle setup.py script tests

Build Docker Images
-------------------

Build and run your image.

Run Docker Image locally

.. code-block:: bash

    > docker build --pull --rm -f "dockerfile" -t convertjson:latest "."
    > docker run --rm -it convertjson:latest

    # Run interactive with environment variables
    > docker run --rm -it --env-file local.env convertjson:latest

    #If you want to see STDOUT use 
    > docker run --rm -a STDOUT convertjson:latest


.. |architecture-overview| image:: docs/JsonConvertArchitecture.png


References
----------
- Eventhubs python library https://docs.microsoft.com/en-us/python/api/overview/azure/eventhub-readme?view=azure-python
- Eventhubs python getting started https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send
