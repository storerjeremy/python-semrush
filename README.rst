==============
python-semrush
==============

Python-Semrush is a wrapper around the `SEMrush API`_ version 3.0.

Thanks to `tomlinton`_ for the basis of this package.

.. _`SEMrush API`: http://www.semrush.com/api-documentation/
.. _`tomlinton`: https://github.com/tomlinton

Installation
============

You can install python-semrush from github.

From github;

.. code-block:: bash

    $ pip install git+https://github.com/sishinami/python-semrush.git

Usage
=====
.. code-block:: python

    from python_semrush.semrush import SemrushClient
    client = SemrushClient(key='your_semrush_api_key')
    result = client.domain_ranks(domain='example.com')

Todo
====

- Implement projects API http://www.semrush.com/api-projects/
- Implement accounts API http://www.semrush.com/api-accounts/
- Implement specific errors

License
=======

This software is licensed under the `MIT License`. See the ``LICENSE``
file in the top distribution directory for the full license text.


Author
======

Jeremy Storer <storerjeremy@gmail.com>

@2021 sishinami <git@mail.hazime.net>
