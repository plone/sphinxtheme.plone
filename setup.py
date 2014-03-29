from setuptools import setup, find_packages
import os

version = '0.0.1dev'

setup(
  name='sphinx.themes.plone',
  version=version,
  use_2to3=True,
  description="Collection of Sphinx Themes for Plone Documentations",
  long_description=open("README.rst").read() + "\n" +
                   open(os.path.join("docs", "HISTORY.rst")).read(),
  # Get more strings from
  # http://pypi.python.org/pypi?:action=list_classifiers
  classifiers=[
    'Programming Language :: Python',
    'Framework :: Sphinx', 
    'Framework :: Plone',       
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Topic :: Software Development :: Documentation',
    'Operating System :: OS Independent',
    #'Development Status :: 5 - Production/Stable',
    'Development Status :: 1 - Planning',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    ],
  keywords='sphinx plone themes',
  #author='Alexander Loechel on behalf of Plone Foundation',
  #author_email='Alexander.Loechel@lmu.de',
  author='Plone Foundation',
  author_email='plone-developers@lists.sourceforge.net',
  url='https://github.com/plone/sphinx.themes.plone.git',
  license='GPL',
  packages=find_packages('src',exclude=['ez_setup']),
  package_dir={'': 'src'},
  namespace_packages=['sphinx', 'sphinx.themes'],
  include_package_data=True,
  zip_safe=False,
  install_requires=[
      'setuptools',
      # -*- Extra requirements: -*-
      'docutils',
      'Pygments',
      'roman',
      'collective.sphinx.autoatschema',
      'sphinxcontrib.contributors',
  ],
  entry_points="""
  # -*- Entry points: -*-
  """,
  )
