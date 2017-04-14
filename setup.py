from setuptools import setup
from pounce import __version__

setup(
    name='django-pounce',
    version=__version__,
    author="Jacob Budin",
    author_email='self@jacobbudin.com',
    description=("Django middleware for preloading resources using the HTTP Link header"),
    install_requires=[],
    license='BSD',
    keywords='django preload performance',
    url='https://github.com/jacobbudin/django-pounce',
    packages=[
        'pounce',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities',
    ],
)
