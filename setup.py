from setuptools import setup

setup(
    name='geocode_mapycz',
    version='0.0.1',
    author='Michal Kolacek',
    author_email='kolacek.m@gmail.com',
    description='Geocode using Mapy.cz',
    url='https://github.com/one-data-cookie/geocode-mapycz',
    license='MIT',
    packages=['geocode_mapycz'],
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=['selenium'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
