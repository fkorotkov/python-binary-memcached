from setuptools import setup
setup(
    name='python-binary-memcached',
    version='0.27.0',
    author='Jayson Reis',
    author_email='santosdosreis@gmail.com',
    description='A pure python module to access memcached via its binary protocol with SASL auth support',
    url='https://github.com/jaysonsantos/python-binary-memcached',
    packages=['bmemcached', 'bmemcached.client'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'six'
    ]
)
