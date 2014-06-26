======================================
Sphinx Themes for Plone Documentation
======================================

sphinx.themes.plone is a collection of `Sphinx`_ themes for the `Plone`_ documentation project.


Features
--------

- sphinx.themes.plone comes with own themes for Plone 3, Plone4 and Plone 5

Installation
------------

Install sphinx.themes.plone with pip::

    pip install sphinx.themes.plone

Install sphinx.themes.plone with buildout::

    [buildout]
    parts=
        sphinx

    [sphinx]
    recipe=zc.recipe.egg
    eggs=
        Sphinx
        sphinx.themes.plone

Configuration
-------------

Edit the "conf.py" configuration file to point to the plone themes::

    # At the top.
    import sphinx.themes.plone

    # ...

    # Activate the theme path:
    html_theme_path = sphinx.themes.plone.get_html_theme_path()

    # Activate the theme like this:
    html_theme = 'plone_org_4'

Available Themes
----------------

- plone_classic (TODO: to be implemented)
- plone_sunburst (TODO: to be implemented)
- plone_org_4
- plone_org_5 (TODO: to be finalized)

Contribute
----------

- Issue Tracker: https://github.com/plone/sphinx.themes.plone/issues
- Source Code: https://github.com/plone/sphinx.themes.plone



License
-------

The project is licensed under the GPLv2 license.

.. _Sphinx: http://sphinx-doc.org/
.. _Plone: http://plone.org
