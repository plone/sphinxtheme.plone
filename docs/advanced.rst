.. _Sphinx: http://sphinx-doc.org/
.. _Plone: http://plone.org
.. _docs.plone.org: http://docs.plone.org

=====================================
Advanced Usage on sphinx.themes.plone
=====================================

---------------------
General Configuration
---------------------

There are two type of configuration parts in the conf.py of the `Sphinx`_ Documentation you are try to apply one of our theme on:

* sphinx-keywords (see )

  - ``project``
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

project
-------

copyright
---------


trademark_name
--------------

version
-------







Language Settings
=================


doc_language
------------

Possible Values: any Language Code (see ref)

Default: 'en'


doc_languages
-------------

Default: ``[{'lang_code':'en','lang_name':'English'}]``

colophon = True
doormat = True
external_topbar = False

favicon = img/favicon.ico
logo = /img/plone.svg
logo_additional_text = Documentation
trademark_logo = /img/plone-invers.svg
trademark_name = Plone

searchbox = True
sticky_navigation = False

show_version_warning = False

# Version and language switcher setting
version_switcher = True
language_switcher = True
always_show_version_switcher = False
always_show_language_switcher = False

Google Analytic Settings
========================


use_ga
------

Use and include Google Analytics code which is modified by the following keywords:

  - googleanalytics_id
  - googleanalytics_domain
  - googleanalytics_path

Possible Values: True / False

Default: ``False``

googleanalytics_id
------------------

Default: not set


googleanalytics_domain
----------------------

googleanalytics_path
--------------------

Default: /




------------------------------
Build in Customization Options
------------------------------

sphinx.themes.plone makes it simply possible to modify or customize several parts of the theme by dropping a template overwriter in a _templates directory in your documentation root or by replacing elements like Logo or so in the static folder of the documentation root.

templates names


- doormat.html






