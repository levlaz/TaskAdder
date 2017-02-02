from setuptools import setup

setup(
    name='TaskAdder',
    packages=['taskadder'],
    include_package_data=True,
    install_requires=[
        'kanboard',
    ],
)
