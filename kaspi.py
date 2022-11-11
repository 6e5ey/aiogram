import requests


def kaspi_shop_get_info(sku):

    headers_price_competition = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Accept': 'application/json, text/*',
        'Accept-Language': 'en-US,en;q=0.8,ru;q=0.5,ru-RU;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json; charset=utf-8',
        'Origin': 'https://kaspi.kz',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-chernyi-102298404/?c=750000000',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    pre_data = {"cityId": "750000000", "id": sku, "merchantUID": "", "limit": 5, "page": 0, "sort": True}
    data_price_competition = json.dumps(pre_data, indent=4)  # TURN dict INTO json

    url_price_competition = "https://kaspi.kz/yml/offer-view/offers/" + sku + "?PageSpeed=noscript"
    response_price_competition = requests.post(url_price_competition, headers=headers_price_competition,
                                               # cookies=cookies_merchant,
                                               data=data_price_competition)


    info_competition = response_price_competition.json()['offers']
    top_store = info_competition[0]['merchantName']  # ТОП 1 МАГАЗИН
    price_store = int(info_competition[0]['price'])  # ТОП 1 ЦЕНА
    two_store = info_competition[1]['merchantName']  # ТОП 2 МАГАЗИН
    two_price_store = int(info_competition[1]['price'])  # ТОП 2 ЦЕНА
    three_store = info_competition[2]['merchantName']  # ТОП 3 МАГАЗИН
    three_price_store = int(info_competition[2]['price'])  # ТОП 3 ЦЕНА
    four_store = info_competition[3]['merchantName']  # ТОП 4 МАГАЗИН
    four_price_store = int(info_competition[3]['price'])  # ТОП 4 ЦЕНА
    five_store = info_competition[4]['merchantName']  # ТОП 5 МАГАЗИН
    five_price_store = int(info_competition[4]['price'])  # ТОП 5 ЦЕНА
    return str(price_store) + " - " + top_store + "\n" + \
           str(two_price_store) + " - " + two_store + "\n" + \
           str(three_price_store) + " - " + three_store + "\n" + \
           str(four_price_store) + " - " + four_store + "\n" + \
           str(five_price_store) + " - " + five_store
