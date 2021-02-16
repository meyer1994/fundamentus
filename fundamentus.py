from collections import defaultdict

import httpx
from bs4 import BeautifulSoup

URL = 'http://www.fundamentus.com.br/resultado.php'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
PARAMS = {
    'pl_min': '',
    'pl_max': '',
    'pvp_min': '',
    'pvp_max': '',
    'psr_min': '',
    'psr_max': '',
    'divy_min': '',
    'divy_max': '',
    'pativos_min': '',
    'pativos_max': '',
    'pcapgiro_min': '',
    'pcapgiro_max': '',
    'pebit_min': '',
    'pebit_max': '',
    'fgrah_min': '',
    'fgrah_max': '',
    'firma_ebit_min': '',
    'firma_ebit_max': '',
    'margemebit_min': '',
    'margemebit_max': '',
    'margemliq_min': '',
    'margemliq_max': '',
    'liqcorr_min': '',
    'liqcorr_max': '',
    'roic_min': '',
    'roic_max': '',
    'roe_min': '',
    'roe_max': '',
    'liq_min': '',
    'liq_max': '',
    'patrim_min': '',
    'patrim_max': '',
    'divbruta_min': '',
    'divbruta_max': '',
    'tx_cresc_rec_min': '',
    'tx_cresc_rec_max': '',
    'setor': '',
    'negociada': 'ON',
    'ordem': '1',
    'x': '28',
    'y': '16'
}


def load():
    res = httpx.get(URL, headers=HEADERS, params=PARAMS)
    bs = BeautifulSoup(res.text, features='lxml')

    table = bs.find('table', {'id': 'resultado'})

    head = table.find('thead')
    body = table.find('tbody')

    keys = [key.text for key in head.find_all('th')]

    rows = []
    for tr in body.find_all('tr'):
        row = [r.text for r in tr.find_all('td')]
        rows.append(row)

    result = defaultdict(dict)
    for ticker, *data in rows:
        for key, dat in zip(keys[1:], data):
            result[ticker][key] = dat

    return result
