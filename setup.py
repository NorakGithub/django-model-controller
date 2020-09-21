import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-model-controller',
    version='0.4.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',  # example license
    description='A model tracking field',
    long_description=README,
    url='https://github.com/NorakGithub/django-model-controller',
    author='Khemanorak Khath',
    author_email='khath.khemanorak@google.com',
    keywords='django model controller tracking',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django>=1.7',
        'django-braces>=1.8.1',
        'django-crispy-forms>=1.6.1',
    ]
)
