.. _macros:

Macros
======

Flask-Discussion exposes a set of Jinja macros for use in Flask application
templates. Note that macros for each system will require specific configuration
values.

----


Helper macro
------------

The **helper macro** renders the appropriate comment system depending on your
configuration. Internally, it calls the system-specific macros in a transparent
way. This is useful in case you want to support several comment systems by just
modifying the configuration of your application instead of its code.

Available in the ``flask_discussion/helper.html`` template.

.. function:: helper.render_comments()

    Render the comment system specified in the ``DISCUSSION_SYSTEM``
    configuration key. If no valid value is provided, an error will be
    shown.

    Note that this macro **accepts any keyword argument** and forwards the
    appropriate values to the system-specific macro called underneath.
    Therefore, if you intend to support several systems, you should specify all
    the values that would be required.


Example usage::

    {% import "flask_discussion/helper.html" as discussion %}

    <html>
        <body>
            {# Specify values used by several comment systems #}
            {{ discussion.render_comments(title="Page title", identifier="my-page", url="http://mypage.com") }}
        </body>
    </html>


----


Disqus macros
-------------

These macros integrate `Disqus`_ comments into an application.

.. _Disqus: https://disqus.com/

Available in the ``flask_discussion/disqus.html`` template.


.. function:: disqus.render_comments(identifier, url, title)

    Render Disqus comments using the provided parameters and embed the JS client.

    :param identifier: Unique page identifier (e.g. blog post ID)
    :param url: URL of the page
    :param title: Title of the page


Example usage::

    {% import "flask_discussion/disqus.html" as disqus %}

    <html>
        <body>
            {{ disqus.render_comments("my-page", "http://mypage.com", "Page title") }}
        </body>
    </html>


.. function:: disqus.render_comment_count()

    Render Disqus comment count.

    This should be called before the closing ``</body>`` tag. Make sure to
    include ``#disqus_thread`` in the ``href`` attribute of the link for which
    to show the comment count.


Example usage::

    {% import "flask_discussion/disqus.html" as disqus %}

    <html>
        <body>
            <a href="http://mypage.com#disqus_thread">Comments</a>
            {{ disqus.render_comment_count() }}
        </body>
    </html>


----


Isso macros
-----------

These macros integrate `Isso`_ comments into an application.

.. _Isso: https://github.com/posativ/isso/

Available in the ``flask_discussion/isso.html`` template.


.. function:: isso.embed_client()

    Embed Isso script.

    This can either be used to globally include the script (e.g. in the head of
    the page) or called as part of  the ``isso.render_comments()`` macro.


Example usage::

    {% import "flask_discussion/isso.html" as isso %}

    <html>
        <body>
            <a href="http://mypage.com">Visit my page</a>

            {{ isso.embed_client() }}
        </body>
    </html>


.. function:: isso.render_comments(identifier="", title="", include_script=true)

    Render Isso comments.

    :param identifier: Optional identifier of the page
    :param title: Optional title of the page
    :param include_script: Set to ``false`` to not call the
        ``isso.embed_client()`` macro (e.g. for cases in which the client is
        embeded globally).

Example usage::

    {% import "flask_discussion/isso.html" as isso %}

    <html>
        <body>
            {{ isso.render_comments("my-page", "Page title") }}
        </body>
    </html>



.. function:: isso.render_comment_count()

    Render Isso comment count.

    This **cannot be use at the same time as the full Isso client**. Make sure
    to include ``#isso_thread`` in the ``href`` attribute of the link for which
    to show the comment count.


Example usage::

    {% import "flask_discussion/isso.html" as isso %}

    <html>
        <body>
            <a href="http://mypage.com#isso_thread">Comments</a>
            {{ isso.render_comment_count() }}
        </body>
    </html>
