try:
    from babel.messages import frontend as babel
except ImportError:
    pass
from setuptools import setup, find_packages

version = '0.5.9.dev0'

setup(
    name='sphinxtheme.plone',
    version=version,
    description="Collection of Sphinx Themes for Plone Documentations",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Framework :: Sphinx',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
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
    },
    entry_points="""
    # -*- Entry points: -*-
    """,
    cmdclass = {
        'compile_catalog': babel.compile_catalog,
        'extract_messages': babel.extract_messages,
        'init_catalog': babel.init_catalog,
        'update_catalog': babel.update_catalog
    },
)
