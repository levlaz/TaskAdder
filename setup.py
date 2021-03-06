from setuptools import setup, find_packages

setup(
    name='TaskAdder',
    version='1.0.0',
    description='Desktop Utility to add Tasks to a Kanboard',
    url='https://github.com/levlaz/TaskAdder',
    author='Lev Lazinskiy',
    author_email='lev@levlaz.org',
    license='GPL v3',
    classifiers=[
        'Development Status :: 5 - Production',
        'Intended Audience :: End Users',
        'Topic :: Desktop Utilities :: Productivity',
        'License :: OSI Approved :: GPL v3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='productivity, tasks, desktop',
    packages=find_packages(),
    install_requires=['kanboard'],
    entry_points={
        'console_scripts': [
            'taskadder=taskadder:main',
        ],
    },
    include_package_data=True,
    package_data={'taskadder': ['icon.png']}
)

