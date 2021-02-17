# Fundamentus

![scrape](https://github.com/meyer1994/fundamentus/workflows/scrape/badge.svg)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A self updating repository that fetches, parses and stores information from
[Fundamentus][1] every day.

## Table of Contents

- [About](#about)
- [Install](#install)
- [Usage](#usage)
- [Thanks](#thanks)


## About

I've created this as a way to simplify access to information from Fundamentus.
Using this repository people will be able to fetch information in as if they
were using a REST API.

## Install

Run:

```sh
$ pip install -r requirements.txt
```

## Usage

This repository is to be used like a REST service. You can fetch, if available,
information about different stocks from Brazil. For example, if you want to
fetch stock information for PETR3 on 2021-01-17, you can perform a GET request
in the following URL:

```sh
$ curl https://raw.githubusercontent.com/meyer1994/fundamentus/master/data/PETR3/2021-02-17.json
{
    "Cotacao": 28.5,
    "Cresc. Rec.5a": -0.0045,
    "Div.Brut/ Patrim.": 1.81,
    "Div.Yield": 0.0084,
    "EV/EBIT": 8.45,
    "EV/EBITDA": 4.84,
    "Liq. Corr.": 1.08,
    "Liq.2meses": 460013000.0,
    "Mrg Ebit": 0.3271,
    "Mrg. Liq.": -0.1693,
    "P/Ativ Circ.Liq": -0.66,
    "P/Ativo": 0.385,
    "P/Cap.Giro": 33.99,
    "P/EBIT": 4.21,
    "P/L": -8.33,
    "P/VP": 1.5,
    "PSR": 1.378,
    "Patrim. Liq": 247736000000.0,
    "ROE": -0.1801,
    "ROIC": 0.1019
}
```

This repository was created on 2021-01-17, so I only have information from this
day forward. If anyone have historical data from Fundamentus, and is willing
to, share it, I will gladly add it to this repo.

## Thanks

This repository was based on the scrapping utility from [phoemur][2]. It was
adapted to be self updated using GitHub actions.


[1]: https://www.fundamentus.com.br/resultado.php
[2]: https://github.com/phoemur/fundamentus
