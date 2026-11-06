tasklib
=======

.. image:: https://github.com/GothenburgBitFactory/tasklib/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/GothenburgBitFactory/tasklib/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/robgolding/tasklib/badge.png?branch=develop
    :target: https://coveralls.io/r/robgolding/tasklib?branch=develop

tasklib is a Python library for interacting with taskwarrior_ databases, using
a queryset API similar to that of Django's ORM.

Requirements
------------

* Python 3.5 or above
* taskwarrior_ v3.0.0 or above.

Taskwarrior 2.x is not supported. tasklib 3.x uses the Taskwarrior 3 storage
backend; existing 2.x data can be migrated with ``task import-v2``.

Installation
------------

Install via pip::

    pip install tasklib

Usage
-----

tasklib has a similar API to that of Django's ORM::

    >>> from tasklib import TaskWarrior

    >>> tw = TaskWarrior('~/.task')
    >>> tasks = tw.tasks.pending()
    >>> tasks
    ['Tidy the house', 'Learn German']
    >>> tasks.filter(tags__contain='chores')
    ['Tidy the house']
    >>> type(tasks[0])
    <class 'tasklib.task.Task'>
    >>> tasks[0].done()
    >>> tasks = tw.tasks.pending()
    >>> tasks
    ['Learn German']
    >>> tasks[0]['tags'] = ['languages']
    >>> tasks[0].save()

For more advanced usage, see the documentation_.

.. _taskwarrior: http://taskwarrior.org
.. _documentation: http://tasklib.readthedocs.org/en/latest/
