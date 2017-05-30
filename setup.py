from setuptools import setup, find_packages

version = '0.3.0.dev1'

setup(
    name='sphinxtheme.plone',
    version=version,
    use_2to3=True,
    description="Collection of Sphinx Themes for Plone Documentations",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Framework :: Sphinx',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Software Development :: Documentation',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
    ],
    keywords='sphinxtheme sphinx plone themes',
    author='Alexander Loechel on behalf of Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    maintainer='Alexander Loechel on behalf of Plone Foundation',
    maintainer_email='Alexander.Loechel@lmu.de',
    url='https://github.com/plone/sphinxtheme.plone.git',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['sphinxtheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Sphinx',
        'docutils',
        'Pygments',
    ],
    extras_require={
        'release': [
            'zest.releaser',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    """,
)
