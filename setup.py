from setuptools import setup, find_packages

version = '0.2.0.dev1'

setup(
    name='sphinx.themes.plone',
    version=version,
    use_2to3=True,
    description="Collection of Sphinx Themes for Plone Documentations",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Framework :: Plone',
        'Framework :: Sphinx',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Software Development :: Documentation',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
    ],
    keywords='sphinx plone themes',
    author='Alexander Loechel on behalf of Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    maintainer='Alexander Loechel on behalf of Plone Foundation',
    maintainer_email='Alexander.Loechel@lmu.de',
    url='https://github.com/plone/sphinx.themes.plone.git',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['sphinx', 'sphinx.themes'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Sphinx',
        'docutils',
        'Pygments',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
