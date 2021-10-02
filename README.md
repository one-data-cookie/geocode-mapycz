# geocode-mapycz
[![GitHub license](https://img.shields.io/github/license/one-data-cookie/geocode-mapycz?style=flat-square)](https://github.com/one-data-cookie/geocode-mapycz/blob/main/LICENSE)

A Python script for accessing JavaScript API of Mapy.cz for geocoding.

## Installation
You can either clone this repo and use it as is, or you can pip install it with the following command:
```sh
pip install git+https://github.com/one-data-cookie/geocode-mapycz
```
## Usage

```py
>>> from geocode_mapycz import geocode_mapycz
>>> places = ['Praha', 'Brno']     
>>> geocode_mapycz(queries=places)
```
