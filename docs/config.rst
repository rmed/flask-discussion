.. _config:

Configuration
=============

Flask-Discussion supports several comment systems, as well as configuring
individual aspects of each of them through the configuration of your
application. Each of these configuration keys follows the naming convention
``DISCUSSION_X_Y`` where ``X`` is the name of the comment system and ``Y`` the
name of the configuration parameter (usually being the same name as specified
in the documentation of said system).

In order to use the helper macro ``render_comments()`` you need to set the
value of the ``DISCUSSION_SYSTEM`` key to one of the supported systems:

- ``"disqus"``
- ``"isso"``

Below is a list of specific configuration keys for all supported comment
systems:

.. toctree::
   :maxdepth: 2

   configs/disqus
   configs/isso
