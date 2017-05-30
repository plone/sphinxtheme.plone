
.. _Sphinx: http://sphinx-doc.org/
.. _Plone: http://plone.org
.. _docs.plone.org: http://docs.plone.org

Usage of sphinxtheme.plone
==========================

The three steps for use sphinx.themes.plone ist to install it,
configure your `Sphinx`_ documentation to use it
and adjust the theme config to fulfill your needs.


Installation
------------

Install sphinx.themes.plone with pip

.. code:: python

    pip install sphinxtheme.plone

Install sphinx.themes.plone with buildout

.. code-block:: ini

    [buildout]
    parts=
        sphinx

    [sphinx]
    recipe=zc.recipe.egg
    eggs=
        Sphinx
        sphinxtheme.plone

.. CAUTION::
    *You should never use a checkout of the theme package for applying a theme to your documentations.*
    Never touch this package to adjust configuration or customize parts, there is no need for that.

Basic Configuration
-------------------

Configure your `Sphinx`_ based Documentation as described by http://sphinx-doc.org/config.html

For just using one of the sphinxtheme.plone designs edit the "conf.py" configuration file to point to the plone themes

.. code-block:: python

    # At the top.
    import sphinxtheme.plone

    ...

    # Activate the theme path:
    html_theme_path = sphinxtheme.plone.get_html_theme_path()

    # Activate the theme like this:
    html_theme = 'plone_org_4'

Additional configuration and custiomzation options are described in the ":doc:`advanced`" section.


Available Themes
----------------

- plone_classic
- plone_sunburst
- plone_barceloneta
- plone_org_4
- plone_org_5

for a preview how they look see ":doc:`theme_preview`"
