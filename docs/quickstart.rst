.. _quickstart:

Quickstart
==========

First install the extension::

    pip install Flask-Discussion


And then initialize it in your application::

    from flask import Flask
    from flask_discussion import Discussion

    discussion = Discussion()

    def init_app():
        app = Flask(__name__)

        # Set config values
        # .....

        discussion.init_app(app)


This will register the extension templates (which contain the macros for each
comment system) with your application, making them available in your own
templates.

If you want to be able to swap comment systems through the configuration of
your application, you may use the macro defined in
``flask_discussion/helper.html``::

    {% import "flask_discussion/helper.html" as discussion %}

    <html>
        <body>
            {{ discussion.render_comments(title="Page title", identifier="my-page", url="http://mypage.com") }}
        </body>
    </html>

Note that the macro **receives any keyword argument and will relay the
appropriate information to the corresponding system-specific macro** (i.e. each
comment system may use only specific information, therefore you should provide
all possible values for all comment systems).

However, if you only want to use a specific comment system, you may import its
macros directly. For instance, for Disqus::

    {% import "flask_discussion/disqus.html" as disqus %}

    <html>
        <body>
            {{ disqus.render_comments(identifier="my-page", url="http://mypage.com", title="Page title") }}
        </body>
    </html>


Check the next sections to see configuration variables available for each
supported comment system.
