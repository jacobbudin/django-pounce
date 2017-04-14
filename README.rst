Pounce
======

Pounce allows you to suggest web browsers preload resources using the HTTP `Link` header. This technique optimizes web performance by allowing clients to begin downloading resources before they're referenced in your response's HTML source code. (For more information, see the `W3C's Preload document <https://w3c.github.io/preload/>`_.).


Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install django-pounce


Integration
~~~~~~~~~~~~

#. In your app's settings (``settings.py``), add ``pounce.middleware.PounceMiddleware`` to your ``MIDDLEWARE`` list.
#. Also in your app's settings, add a ``POUNCE_RESOURCES`` iterable like so:

   .. code-block:: python3

      POUNCE_RESOURCES = (('img/logo.png', 'img'), ('js/main.js', 'script'))

That's it. Once complete, you should see a `Link` header referencing these resources with each request.


Compatibility
~~~~~~~~~~~~~

* Django 1.11
* Python 3.5


F.A.Q.
~~~~~~~~~~~~~

**Does Pounce push resources (over HTTP2)?**

No. Why? Per the `W3C Preload document <https://w3c.github.io/preload/>`_:

   Initiating server push for a preload link is an optional optimization. For example, the server might omit initiating push if it believes that the response is available in the client's cache: the client will process the preload directive, check the relevant caches, and initiate the request to the server if the resource is missing.

Since you don't know which resources are in your requestor's cache, pushing these resources preemptively may consume unnecessary bandwidth and defeat your overall caching strategy.

**Will Pounce support Python 2?**

No.
