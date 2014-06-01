======================================
 Sphinx Themes for Plone Documentation
======================================

Introduction
============

This package is a collection of sphinx themes for the plone documentation.


Setup
=====



#. Install the package:

    #. using easy_install::

        $ easy_install sphinx.themes.plone

    #. using pip::

        $ pip install sphinx.themes.plone

    #. using buildout::

        [buildout]
        parts=
            sphinx
        
        [sphinx]
        recipe=zc.recipe.egg
        eggs=
            Sphinx
            sphinx.themes.plone


#. Edit the "conf.py" configuration file to point to the plone themes::

    # At the top.
    import sphinx.themes.plone

    # ...

    # Activate the theme path:
    html_theme_path = sphinx.themes.plone.get_html_theme_path()


#. Select a Plone theme::

      # Activate the theme like this:
      html_theme = 'plone_org_4'

Avaliable Themes:
-----------------

* plone_org_4
* plone_org_5 (TODO: to be finialized)
* plone_classic (TODO: to be implemented)
* plone_sunburst (TODO: to be implemented)
