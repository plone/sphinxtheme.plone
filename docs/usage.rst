Usage of sphinx.themes.plone
============================

The three steps for use sphinx.themes.plone ist to install it,
configure your `Sphinx`_ documentation to use it 
and adjust the theme config to fulfill your needs.


Installation
------------

Install sphinx.themes.plone with pip

.. code:: python

    pip install sphinx.themes.plone

Install sphinx.themes.plone with buildout::

.. code-block:: ini

    [buildout]
    parts=
        sphinx

    [sphinx]
    recipe=zc.recipe.egg
    eggs=
        Sphinx
        sphinx.themes.plone

**Warning:** *You should never use a checkout of the theme package for just appling a theme to your documentations.*

Basic Configuration
-------------------

Edit the "conf.py" configuration file to point to the plone themes::

    # At the top.
    import sphinx.themes.plone

    ...

    # Activate the theme path:
    html_theme_path = sphinx.themes.plone.get_html_theme_path()

    # Activate the theme like this:
    html_theme = 'plone_org_4'


Available Themes
----------------

- plone_classic
- plone_sunburst
- plone_barceloneta
- plone_org_4
- plone_org_5
