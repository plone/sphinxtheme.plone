.. _Sphinx: http://sphinx-doc.org/
.. _Plone: http://plone.org
.. _docs.plone.org: http://docs.plone.org
.. _Bootstrap: http://bootstrap.org

=====================================
Advanced Usage on sphinx.themes.plone
=====================================

---------------------
General Configuration
---------------------

There are two type of configuration parts in the conf.py of the `Sphinx`_ Documentation you are try to apply one of our theme on:

* sphinx-keywords (see )

  - project
  - copyright
  - trademark_name
  - version
  - release
  - html_use_opensearch

* Theme specific configuration done via the html_theme_options dict:

  - rightsidebar
  - doc_languages
  - doc_language
  - trademark_name
  - searchbox
  - use_ga
  - googleanalytics_id
  - googleanalytics_domain
  - googleanalytics_path
  - external_topbar
  - version_switcher
  - always_show_version_switcher
  - always_show_language_switcher
  - show_version_warning


Sphinx-Keyword Settings
.......................

Description and Naming Settings
===============================

project
-------

copyright
---------


trademark_name
--------------

version
-------




Theme specific configuration (html_theme_options)
.................................................


Language Settings
=================


doc_language
------------

Field-Type:
  String

Possible Values:
  any Language Code (see ref)

Default:
  'en'


doc_languages
-------------

Default:
  ``[{'lang_code':'en','lang_name':'English'}]``


Visual Switches
===============

colophon
--------

Switch on or off the Colophon in the Theme, Trademark-Name and Logo and copyright Block at the bottom of the page.

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True


doormat
-------

Switch on or of the rendering of the Doormat block and Template. The doormat is the special Navigation Block at the bottom of the page.

Connected Customization option: :ref:`doormat_template`

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True


external_topbar
---------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  ``False``

show_version_warning
--------------------


Field-Type:
  Boolean

Possible / Useful Values:
  ``True`` / ``False``

Default:
  ``False``

version_switcher
----------------

Field-Type:
  Boolean

Possible / Useful Values:
  ``True`` / ``False``

Default: 
  ``True``


always_show_version_switcher
----------------------------

Field-Type:
  Boolean

Possible / Useful Values:
  ``True`` / ``False``

Default:
  False

language_switcher
-----------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True

always_show_language_switcher
-----------------------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  False



searchbox
---------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True



sticky_navigation
-----------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  ``False``

Logo Customization
==================

logo
----

Logo on the Top of the Page

Field-Type: Path-String

Possible / Useful Values: path to image in static folder

logo_additional_text
--------------------

Additional Text below the Logo, if changes you might want to change the css style for it too.

Field-Type: String

Default: Documentation

trademark_logo
--------------


Field-Type: Path-String

Possible / Useful Values: path to the image in static folder

trademark_name
--------------

Alt tag for the trademark_logo image


Field-Type
  String

Default
  Plone


favicon 
-------

Field-Type:
  Path-String



Google Analytic Settings
========================


use_ga
------

Use and include Google Analytics code which is modified by the following keywords:

  - googleanalytics_id
  - googleanalytics_domain
  - googleanalytics_path

Possible Values: 
  True / False

Default: 
  ``False``

googleanalytics_id
------------------

Field-Type:
  String

Default:
  not set


googleanalytics_domain
----------------------

googleanalytics_path
--------------------

Field-Type:
  String

Default:
  /




------------------------------
Build in Customization Options
------------------------------

sphinx.themes.plone makes it simply possible to modify or customize several parts of the theme by dropping a template overwriter in a _templates directory in your documentation root or by replacing elements like Logo or so in the static folder of the documentation root.

As sphinx.themes.plone uses the `Bootstrap`_ Framework for making the Grid and some of the visual styling easyer some the templates must respect those rules.

templates names
...............

- doormat.html
- version_warning.html

.. _doormat_template:

Structure of doormat
====================


.. code-block:: html+jinja

    {% block doormat%}
        <nav class="row">
          <div class="col-xs-3">
            <ul class="list-unstyled">
              <li><a href="#">doormat</a></li>
            </ul>
          </div>
          <div class="col-xs-3">
            <ul class="list-unstyled">
              <li><a href="#">doormat</a></li>
            </ul>
          </div>
          <div class="col-xs-3">
            <ul class="list-unstyled">
              <li><a href="#">doormat</a></li>
            </ul>
          </div>
          <div class="col-xs-3">
            <ul class="list-unstyled">
              <li><a href="#">doormat</a></li>
            </ul>
          </div>

        </nav>
    {% endblock %}

Structure of version_warning
============================

.. code-block:: html+jinja

    {% block version_warning %}
    {% endblock %}




important static ressources to overwrite
........................................

* logos, favicon and apple-touch-icon
* css

  * admonition.css

* specific icons:

  * dialog-note.png
  * dialog-seealso.png
  * dialog-todo.png
  * dialog-topic.png
  * dialog-warning.png
  * external.png



