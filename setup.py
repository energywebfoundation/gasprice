from setuptools import setup

setup(
    name='gasprice',
    version='1.1.5',
    description='predict ethereum gas price',
    url='https://github.com/banteg/gasprice',
    author='banteg',
    py_modules=[
        'gas_price',
    ],
    install_requires=[
        'sanic==20.9.1',
        'pandas==1.1.3',
        'web3==5.12.3',
        'click==7.1.2',
        'retry==0.9.2',
    ],
    entry_points={
        'console_scripts': [
            'gasprice=gas_price:main',
        ]
    }
)
