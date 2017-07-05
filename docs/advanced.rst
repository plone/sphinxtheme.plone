.. _Sphinx: http://sphinx-doc.org/
.. _Plone: http://plone.org
.. _docs.plone.org: http://docs.plone.org
.. _Bootstrap: http://bootstrap.org

===================================
Advanced Usage on sphinxtheme.plone
===================================

---------------------
General Configuration
---------------------

There are two type of configuration parts in the conf.py of the `Sphinx`_ Documentation you are try to apply one of our theme on:

.. toctree::

  advanced

* sphinx-keywords (see )

  - :ref:`project`
  - :ref:`copyright`
  - :ref:`trademark_name`
  - :ref:`version`
  - :ref:`release`
  - :ref:`html_use_opensearch`

* Theme specific configuration done via the html_theme_options dict:

  - rightsidebar
  - doc_languages
  - doc_language
  - :ref:`html_trademark_name`
  - searchbox
  - :ref:`google_analytic_settings`

    - :ref:`use_ga`
    - :ref:`googleanalytics_id`
    - :ref:`googleanalytics_domain`
    - :ref:`googleanalytics_path`

  - external_topbar
  - version_switcher
  - always_show_version_switcher
  - always_show_language_switcher
  - show_version_warning
  - 'contributing_link': '$URL'
  - 'use_gitter': True
  - 'use_freshdesk': True


Sphinx-Keyword Settings
.......................

Description and Naming Settings
===============================


.. _project:

project
-------


.. _copyright:

copyright
---------


.. _trademark_name:

trademark_name
--------------


.. _version:

version
-------


.. _release:

release:
--------

.. _html_use_opensearch:

html_use_opensearch
-------------------

.. _html_theme_options:

Theme specific configuration (html_theme_options)
.................................................


.. _languages_settings:

Language Settings
=================


.. _doc_language:

doc_language
------------

Field-Type:
  String

Possible Values:
  any Language Code (see ref)

Default:
  'en'


.. _doc_languages:

doc_languages
-------------

Default:
  ``[{'lang_code':'en','lang_name':'English'}]``



.. _visual_switches:

Visual Switches
===============

.. _colophon:

colophon
--------

Switch on or off the Colophon in the Theme, Trademark-Name and Logo and copyright Block at the bottom of the page.

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True


.. _doormat:

doormat
-------

Switch on or off the rendering of the doormat block and template. The doormat is the special navigation block at the bottom of the page.

Connected customization option: :ref:`doormat_template`

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True


.. _external_topbar:

external_topbar
---------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  ``False``


.. _show_version_warning:

show_version_warning
--------------------


Field-Type:
  Boolean

Possible / Useful Values:
  ``True`` / ``False``

Default:
  ``False``

.. _version_switcher:

version_switcher
----------------

Field-Type:
  Boolean

Possible / Useful Values:
  ``True`` / ``False``

Default:
  ``True``


.. _always_show_version_switcher:

always_show_version_switcher
----------------------------

Field-Type:
  Boolean

Possible / Useful Values:
  ``True`` / ``False``

Default:
  False


.. _language_switcher:

language_switcher
-----------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True


.. _always_show_language_switcher:

always_show_language_switcher
-----------------------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  False


.. _searchbox:

searchbox
---------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  True



.. _sticky_navigation:

sticky_navigation
-----------------

Field-Type:
  Boolean

Possible / Useful Values:
  True / False

Default:
  ``False``


.. _custom_logo:

Logo Customization
==================


.. _logo:

logo
----

Logo on the Top of the Page

Field-Type: Path-String

Possible / Useful Values: path to image in static folder


.. _logo_additional_text:

logo_additional_text
--------------------

Additional Text below the Logo, if changes you might want to change the css style for it too.

Field-Type: String

Default: Documentation

.. _trademark_logo:

trademark_logo
--------------


Field-Type: Path-String

Possible / Useful Values: path to the image in static folder

.. _html_trademark_name:

trademark_name
--------------

Alt tag for the trademark_logo image


Field-Type
  String

Default
  Plone


.. _favicon:

favicon
-------

Field-Type:
  Path-String



.. _google_analytic_settings:

Google Analytic Settings
========================


.. _use_ga:

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


.. _googleanalytics_id:

googleanalytics_id
------------------

Field-Type:
  String

Default:
  not set


.. _googleanalytics_domain:

googleanalytics_domain
----------------------

.. _googleanalytics_path:

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
