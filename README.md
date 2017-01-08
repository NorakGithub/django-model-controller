# Django Model Controller

[![Documentation Status](https://readthedocs.org/projects/django-model-controller/badge/?version=latest)](http://django-model-controller.readthedocs.io/en/latest/?badge=latest)
                

**Model instance tracker.**

Full documentation for this project available at [http://django-common-boxset.readthedocs.io/][docs]

---

### Overview

Come to a time that you want to able to keep track on each record of data that was created or updated. 
This project give you the ability to answer these questions: When this record was created? When this record was updated? 
Who created this record? Who updated this record?

These are the classes that you can use to extend your classes:

#### Model
- **AbstractTimeStampMarker** model datetime create and update
- **AbstractModelController** model datetime and who create and update

#### Form
- **ModelControllerForm** form for automatically setup who create and update

#### View
- **CreateViewMixin** view that used form class extended from ModelControllerForm must extend from CreateViewMixin 
- **UpdateViewMixin** similar to CreateViewMixin but for UpdateView

### Requirements

- Python (2.7, 3.2, 3.4, 3.5)
- Django (1.8, 1.9, 1.10)

## Quick start

1. Install via pip
```
$ pip install django-common-boxset
```

[docs]: http://django-common-boxset.readthedocs.io/
