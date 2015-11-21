Installation and usage
----------------------

The only requirements are docker and docker-compose(recommended):

https://docs.docker.com/compose/gettingstarted/


First time only:

.. code-block:: bash

   $ ./create_db_users.sh

Start webpage locally:

.. code-block:: bash

   $ docker-compose up

run tests:

.. code-block:: bash

   $ docker-compose run web py.test
