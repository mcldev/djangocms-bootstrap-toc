from setuptools import find_packages, setup


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Framework :: Django',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Framework :: Django',
    'Framework :: Django :: 2.2',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

REQUIREMENTS = [
    'django>=2.2',
    'django-cms>=3.4.3',
    'django-sekizai>=1.0.0',
]

VERSION='1.0.0'

setup(
    name='djangocms-bootstrap-toc',
    packages=find_packages(exclude=('test_app', 'docs')),
    include_package_data=True,
    version=VERSION,
    description='Bootstrap Table of Contents Plugin for Django CMS',
    author='Michael Carder',
    url='https://github.com/mcldev/djangocms-bootstrap-toc',
    install_requires=REQUIREMENTS,
    keywords=['django', 'Django CMS', 'table of contents', 'CMS', ],
    classifiers=CLASSIFIERS,
)
