# geocode-mapycz

A Python package that uses Selenium to access JavaScript API of Mapy.cz for geocoding.

## Installation
You can either clone this repo and use it as is, or you can pip-install it through:
```sh
pip install git+https://github.com/one-data-cookie/geocode-mapycz
```
## Simple Usage
```py
>>> from geocode_mapycz import geocode_mapycz
>>> places = ['Praha', 'Brno']     
>>> geocode_mapycz(queries=places)

{
  'queries': ['Praha', 'Brno'],
  'locality': '',
  'limit': 1,
  'lang': 'cs',
  'results': {
    'Praha': [{
      'coords': (50.0835493857, 14.4341412988),
      'label': '',
      'address': 'Praha, Česko'
    }],
    'Brno': [{
      'coords': (49.200221, 16.607841),
      'label': '',
      'address': 'Brno, Česko'
    }]
  }
}
```

## Advanced Usage
```py
>>> from geocode_mapycz import geocode_mapycz
>>> places = ['ZŠ Merhautova', 'Gymnázium, Řečkovice']     
>>> geocode_mapycz(queries=places, locality='Brno', limit=2, lang='en')

{
  'queries': ['ZŠ Merhautova', 'Gymnázium, Řečkovice'],
  'locality': 'Brno',
  'limit': 2,
  'lang': 'en',
  'results': {
    'ZŠ Merhautova': [
      {
        'coords': (49.20525360107422, 16.624147415161133),
        'label': 'ZŠ a MŠ Brno, Merhautova',
        'address': 'Merhautova 932/37, Brno - Černá Pole, Czechia'
      },
      {
        'coords': (49.20464324951172, 16.625391006469727),
        'label': 'ZŠ a MŠ Brno, Vranovská',
        'address': 'Vranovská 182/17, Brno - Zábrdovice, Czechia'
      }
    ],
    'Gymnázium, Řečkovice': [
      {
        'coords': (49.24648666381836, 16.578563690185547),
        'label': 'Gymnázium Brno - Řečkovice',
        'address': 'Terezy Novákové 936/2, Brno - Řečkovice, Czechia'
      },
      {
        'coords': (49.2073122813916, 16.589326957226),
        'label': 'Parkoviště Gymnázium Matyáše Lercha',
        'address': 'Žižkova, Brno, Czechia'
      }
    ]
  }
}
```
