import os

import requests


class Cdown(object):

    root_url = 'https://www2.census.gov/geo/tiger/'

    state_fips = [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                  26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46,
                  47, 48, 49, 50, 51, 53, 54, 55, 56, 60, 66, 69, 72, 78]

    def __init__(self, year=None, ws=os.curdir):

        self.year = year
        self.ws = ws

    def get(self, var, year=None):
        _year = year or self.year

        assert _year is not None

        def _get(url, fpath):

            _ws = os.path.abspath(os.path.dirname(fpath))
            if not os.path.exists(_ws):
                os.makedirs(_ws)

            _r = requests.get(url)

            with open(fpath, 'wb') as _file:
                _file.write(_r.content)

        def counties():
            _file = f'tl_{_year}_us_county.zip'
            _url = f'{Cdown.root_url}/TIGER{_year}/COUNTY/{_file}'
            _fpath = os.path.join(self.ws, _file)

            _get(_url, fpath=_fpath)

        def places():

            _out_ws = os.path.join(self.ws, 'places')

            if not os.path.exists(_out_ws):
                os.makedirs(_out_ws)

            for fips in Cdown.state_fips:
                _file = f'tl_{_year}_{fips:02}_place.zip'
                _url = f'{Cdown.root_url}/TIGER{_year}/PLACE/{_file}'
                _fpath = os.path.join(_out_ws, _file)

                _get(url=_url, fpath=_fpath)

        def states():
            _file = f'tl_{_year}_us_state.zip'
            _url = f'{Cdown.root_url}/TIGER{_year}/STATE/{_file}'
            _fpath = os.path.join(self.ws, _file)
            _get(url=_url, fpath=_fpath)

        _get_var = {'counties': counties,
                    'places': places,
                    'states': states}

        try:
            _get_var[var]()
        except Exception as e:
            raise e
        else:
            return True
