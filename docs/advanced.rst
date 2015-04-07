Advanced Usage on sphinx.themes.plone
=====================================



# General information about the project.
project = u'Plone Documentation'
copyright = u'''The text and illustrations in this website are licensed by the Plone Foundation under a Creative Commons Attribution 4.0 International license.
        Plone and the Plone<sup>®</sup> logo are registered trademarks of the Plone Foundation, registered in the United States and other countries.
        For guidelines on the permitted uses of the Plone trademarks, see https://plone.org/foundation/logo
        All other trademarks are owned by their respective owners.
        Hosted by Rackspace.'''

trademark_name = "Plone"

version = [
    #'5.0',
    '4.3',
    #'3.3',
]
# The full version, including alpha/beta/rc tags.
release = '4.3'

# Announce that we have a opensearch plugin
html_use_opensearch = 'http://docs.plone.org'



html_theme = 'plone_org_4'  # for Plone 4 documentation
#html_theme = 'plone_org_5'  # for Plone 5 documentation
import sphinx.themes.plone
html_theme_path = sphinx.themes.plone.get_html_theme_path()


html_theme_options = {
    #"rightsidebar": "false",
    'doc_languages': [
        {'lang_code': 'en', 'lang_name': 'English'},
        #{'lang_code': 'de', 'lang_name': 'German'},
        #{'lang_code': 'it', 'lang_name': 'Italian'},
    ],
    'doc_language': 'en',
    'trademark_name': 'Plone',
    'searchbox': True,
    'use_ga': True,
    'googleanalytics_id': 'UA-1907133-6',
    'googleanalytics_domain': 'plone.org',
    'googleanalytics_path': '/',
    'external_topbar': True,
    'version_switcher': True,
    'always_show_version_switcher': True,
    'always_show_language_switcher': False,
    'show_version_warning': False,
}