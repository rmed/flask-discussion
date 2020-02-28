Flask-Discussion
================

Flask-Discussion is an extension for `Flask`_ that adds support for several
discussion/comment systems to your application. Simply use the provided
*macros* in your templates::

    {% import "flask_discussion/helper.html" as discussion %}

    <html>
        <body>
            {{ discussion.render_comments(title="Page title", identifier="my-page", url="http://mypage.com") }}
        </body>
    </html>

.. _Flask: https://palletsprojects.com/p/flask/


Supported Systems
-----------------

The following comment systems are supported:

- Disqus
- Isso (0.12.2)
- Remark42 (1.5.0)


User Guide
----------

.. toctree::
   :maxdepth: 2

   quickstart
   macros
   config
