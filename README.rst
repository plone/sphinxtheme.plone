=====================================
 Sphinx Themes for Plone Documentation
=====================================

Introduction
============

This package is a collection of sphinx themes for the plone documentation.


Setup
=====

Installation from PyPI_ is fairly straightforward:

1. Install the package::

	  $ easy_install sphinx.themes.plone

	  or

      $ pip install sphinx.themes.plone

      or using buildout::

            [buildout]
		    parts=
		        sphinx
		    
		    [sphinx]
		    recipe=zc.recipe.egg
		    eggs=
		        Sphinx
		        sphinx.plonetheme

2. Edit the "conf.py" configuration file to point to the plone themes::

      # At the top.
      import sphinx.themes.plone

      # ...

      # Activate the theme.
      html_theme = 'bootstrap'
      html_theme_path = sphinx.themes.plone.get_html_theme_path()


		extensions = ['sphinxjp.themecore']
		html_theme = 'plonetheme'
		# Opensearch support with Plone icon
		html_use_opensearch = 'http://my.site.tld/mydoc'
		...
		# Have a disqus setting for this site to have visitors feedback?
		# (register at http://disqus.com/)
		html_theme_options = {
		  'disqus_name': 'the_disqus_site_shortname'
		}