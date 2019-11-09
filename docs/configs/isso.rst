.. _configs/isso:

Isso Configuration
==================

The following configuration keys are available for Disqus comments. Note that
all the keys correspond to the data attributes used to `configure the Isso
client`_:

.. _configure the Isso client: https://posativ.org/isso/docs/configuration/client/

+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_URL``                 | URL where the Isso server resides. **Required**.                    |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_CSS``                 | Set to ``False`` to prevent Isso from automatically                 |
|                                         | appending the stylesheet. **Defaults to** ``True``.                 |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_LANG``                | Override useragent's preferred language with one of                 |
|                                         | the languages available in Isso (two letter code).                  |
|                                         | **Defaults to** ``en``.                                             |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_REPLY_TO_SELF``       | Set to ``True`` when server spam guard is configured                |
|                                         | with ``reply-to-self = true``.                                      |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_REQUIRE_AUTHOR``      | Set to ``True`` when server spam guard is configured                |
|                                         | with ``require-author = true``.                                     |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_REQUIRE_EMAIL``       | Set to ``True`` when server spam guard is configured                |
|                                         | with ``require-email = true``.                                      |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_REPLY_NOTIFICATIONS`` | Set to ``True`` when reply notifications is configured              |
|                                         | in the server with ``reply-notifications = true``.                  |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_MAX_COMMENTS_TOP``    | Number of top level comments to show by default. If some            |
|                                         | comments are not shown, an ``"X Hidden"`` link is shown.            |
|                                         | Set to ``"inf"`` to show all or ``"0"`` to hide all.                |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_MAX_COMMENTS_NESTED`` | Number of nested comments to show by default. If some               |
|                                         | comments are not shown, an ``"X Hidden"`` link is shown.            |
|                                         | Set to ``"inf"`` to show all or ``"0"`` to hide all.                |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_REVEAL_ON_CLICK``     | Number of comments to reveal upon clicking the ``"X                 |
|                                         | Hidden"`` link.                                                     |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_AVATAR``              | Set to ``True`` to enable avatar generation or ``False``            |
|                                         | to disable it.                                                      |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_AVATAR_BG``           | Set avatar background color. Any valid CSS color will do.           |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_AVATAR_FG``           | Set avatar foreground color. Up to 8 colors are possible.           |
|                                         | The default color scheme is based on `this color palette`_.         |
|                                         | Multiple colors must be separated by space. If you use less         |
|                                         | than eight colors and not a multiple of 2, the color                |
|                                         | distribution is not event.                                          |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_GRAVATAR``            | Set to ``True`` to use gravatar images instead of generating        |
|                                         | svg images. You have to set ``DISCUSSION_ISSO_AVATAR`` to           |
|                                         | ``False`` if you want to use this. Otherwise both the gravatar      |
|                                         | and avatar svg image will show up. This requires setting the        |
|                                         | ``gravatar = true`` configuration in the server.                    |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_VOTE``                | Set to ``True`` to enable voting feature on the client side.        |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_VOTE_LEVELS``         | List of vote levels used to customize comment appearance based      |
|                                         | on score. Provide comma-separated values (e.g. ``"0,5,10,25,100"``) |
|                                         | or a JSON array (e.g. ``"[-5,5,15]"``).                             |
|                                         |                                                                     |
|                                         | For example, the value ``"-5,5"`` will cause each ``isso-comment``  |
|                                         | to be given one of these 3 classes:                                 |
|                                         |                                                                     |
|                                         | - ``isso-vote-level-0`` for scores lower than -5                    |
|                                         | - ``isso-vote-level-1`` for scores between -5 and 4                 |
|                                         | - ``isso-vote-level-2`` for scores of 5 and greater                 |
|                                         |                                                                     |
|                                         | These classes can then be used to customize the appearance of       |
|                                         | comments (e.g. put a star on popular comments).                     |
+-----------------------------------------+---------------------------------------------------------------------+
| ``DISCUSSION_ISSO_FEED``                | Set to ``True`` to enable the addition of a link to the feed for    |
|                                         | the comment thread. The link will only be valid if the appropriate  |
|                                         | setting, in ``[rss]`` section, is also enabled server-side.         |
+-----------------------------------------+---------------------------------------------------------------------+


.. _this color palette: http://colrd.com/palette/19308/

