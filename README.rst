Django Model Controller
=======================

.. image:: https://readthedocs.org/projects/django-model-controller/badge/?version=latest

**Model instance tracker.**

Full documentation for this project available at `http://django-model-controller.readthedocs.io <http://django-model-controller.readthedocs.io>`_

----

Overview
--------
Come to a time that you want to able to keep track on each record of data that was created or updated. 
This project give you the ability to answer these questions: When this record was created? When this record was updated? 
Who created this record? Who updated this record?

These are the classes that you can use to extend your classes:

Model
-----
- **AbstractTimeStampMarker** model datetime create and update
- **AbstractModelController** model datetime and who create and update

Form
----
- **ModelControllerForm** form for automatically setup who create and update

View
----
- **CreateViewMixin** view that used form class extended from ModelControllerForm must extend from CreateViewMixin 
- **UpdateViewMixin** similar to CreateViewMixin but for UpdateView

Requirements
------------

- Python (2.7, 3.2, 3.4, 3.5)
- Django (1.8, 1.9, 1.10)

Quick start
-----------

Install using pip:

.. code-block:: sh

    pip install django-model-controller
