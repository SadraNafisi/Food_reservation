#############
Food_Reservation
#############
This webapp is developed by *django* and make online reservation service available , also service provider(**server**) can also interact with the website and make the foods menu and details in its admin webpage.

Requirement
============
``python`` 3.6 or more

Feature
============
* Different Webapps: customer and server have divided webapp. ``reservation/`` directory is for customer side and ``service/`` is for server side.

* Dynamic Website: server can make menu editable by just some click from its pc or smartphone via internet such as : add food , delete food , change food availablity , ... .

* Easy-to-Install: The installation process is really convenient, although for using it on a online server there would be need a admin .

Installation
============

1- Clone this repo into your server(pc):

.. code-block:: bash

  git clone https://github.com/SadraNafisi/Food_reservation.git:

  cd Food_reservation

2- Create python virtual enviornment(*virtenv*) in project directory and include that with ``source`` command:

.. code-block:: bash

  python -m venv .venv

  source .venv/bin/activate

3- Install dependencies of project for python:

.. code-block:: bash

  pip install -r requirement.txt

4- Begin project by running ``manage.py runserver``:

.. code-block:: bash

  python manage.py runserver

Roles
=================
Admin ==> Name: **admin** , Password: **admin**

Customer ==> Name: **sadra** , Password: **sadra**

**NOTE**: By signing up in website , a new customer role would be created.

Example
=============
.. raw:: html

   <div style="display: flex; justify-content: space-around;">
       <img src="screenshots/Login.png" alt="Login page" style="width: 850px;height:600px;">
       <img src="screenshots/Order_menu.png" alt="Food Menu" style="width: 850px;height:600px;">
       <img src="screenshots/SignUp.png" alt="SignUp page" style="width: 850px;height:600px;">
       <img src="screenshots/dashboard_view.png" alt="Dashboard page" style="width: 850px;height:600px;">
   </div>


