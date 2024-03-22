import requests


def fetch_bank(url, params):
    print(url)
    headers = params.get("headers")
    body = params.get("body")
    method = params.get("method")
    if method == "POST":
        return requests.post(url, headers=headers)
    elif method == "GET":
        return requests.get(url, headers=headers)


def check_1():
    stock = fetch_bank("https://www.elkor.lv/api/ext/kt-api-extensions/catalog/leasing/loadBanks?storeCode=lat", {
        "headers": {
            "accept": "*/*",
            "accept-language": "en,en-US;q=0.9,ru-RU;q=0.8,ru;q=0.7,my;q=0.6",
            "content-type": "application/json",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "cookie": "CookieConsent={stamp:%27SyoTFSswaxFOPgSIohtpmO2aUFSoRWqYCk5uT3RPywB5l+D/oAyOtQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:2%2Cutc:1711127990944%2Cregion:%27lv%27}; rrpvid=895080624633282; _gcl_au=1.1.1898179312.1711127991; rcuid=65e49da02878efb2880524da; _ga=GA1.1.238686052.1711127991; _ga=GA1.3.238686052.1711127991; _gid=GA1.3.1440231463.1711127991; _hjSession_2183454=eyJpZCI6IjcyOTI1MjE2LTMyMTItNGRjZi1iY2ViLWNhMmQyM2ZiZWNmNCIsImMiOjE3MTExMjc5OTE1NzcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1711127991674.1314065884; lp_vid_1982=8ccd4df0-5917-40cb-b081-d8bdbd4e0409; lp_session_start_1982=1711127992101; lp_session_1982=778416; lp_abtests_1982=[]; _hjSessionUser_2183454=eyJpZCI6IjNjMWVjZTkyLTAyM2MtNWViNi1iNDg1LTg4NGQyYTdkNDE2ZCIsImNyZWF0ZWQiOjE3MTExMjc5OTE1NzYsImV4aXN0aW5nIjp0cnVlfQ==; lp_pageview_1982=4; rr-testCookie=testvalue; _ga_Q0BV0F68N5=GS1.1.1711127991.1.1.1711129678.59.0.0; _ga_QEEFYT2NV9=GS1.1.1711127991.1.1.1711129678.0.0.1102940303; _dc_gtm_UA-11178667-1=1",
            "Referer": "https://www.elkor.lv/",
            "Referrer-Policy": "origin"
        },
        "body": "{\"isCacheOnServer\":true}",
        "method": "POST"
    })
    print(stock.status_code)
    item = stock.json()["result"]["items"]
    print(item)
    for i in item:
        print(i)


def fetch_auto(url, params):
    headers = params.get("headers")
    body = params.get("body")
    method = params.get("method")
    if method == "POST":
        return requests.post(url, headers=headers)
    elif method == "GET":
        return requests.get(url, headers=headers)


def check_2():
    item = fetch_auto("https://auto.ru/-/ajax/desktop-search/listingSpecial/", {
        "headers": {
            "accept": "*/*",
            "accept-language": "en,en-US;q=0.9,ru-RU;q=0.8,ru;q=0.7,my;q=0.6",
            "content-type": "application/json",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "same-origin",
            "sec-fetch-site": "same-origin",
            "x-client-app-version": "50.0.13693690",
            "x-client-date": "1711130663342",
            "x-csrf-token": "c3c3c894c6ff99d6cd3dd1ab7112e5f6c2e8a5cd99d4c47c",
            "x-page-request-id": "cc43ace1b011758935aed750ecdbb3a6",
            "x-requested-with": "XMLHttpRequest",
            "x-retpath-y": "https://auto.ru/cars/kia/all/",
            "cookie": "autoru_gdpr=1; suid=d4e9810aeea7131eea54f4565bddb798.1ccd6c087929e363e9fa93c2f55bb5e2; _csrf_token=c3c3c894c6ff99d6cd3dd1ab7112e5f6c2e8a5cd99d4c47c; autoru_sid=a%3Ag65fdb87d2d05mud8opgie9viuc061gj.7c7db5ffc3d2f2f012aaec9af072cd03%7C1711126653037.604800.iSbE9Hlrr2ietm5uxfdiZg.Gyzhn2JIq5fZrW0ph4dxWSo_v7L6-u4rAjMrc0r8uPA; autoruuid=g65fdb87d2d05mud8opgie9viuc061gj.7c7db5ffc3d2f2f012aaec9af072cd03; fp=5c6d115abfc68d7ea5dfc94a7174a2ec%7C1711126663133; Session_id=noauth:1711126664; sessar=1.1188.CiDFwerWmEhz0l1wNGf7n6cQQ0OPMWhuaAOYXw9JmtuSoQ.Icgnanilp-5VcxGRRVbQoRu9r0_gEF731OvT9Oqhog8; yandex_login=; ys=c_chck.2878046013; i=SbM2gdUIduRk1HdIVm+ECHmA5kwEyGIk5egrlN4F09eqgWJiB5KGA2jMME0rOi6BMrClnew2I1V7g4yEak8G7OhS0rs=; yandexuid=6534457931689088238; mda2_beacon=1711126664195; sso_status=sso.passport.yandex.ru:synchronized; yaPassportTryAutologin=1; los=1; bltsr=1; coockoos=1; spravka=dD0xNzExMTMwNTQ2O2k9ODUuMjU0Ljc1LjM0O0Q9RENGMEY1MTAyNjBDODIxNDc4OEVBQjdEOUY3OTU5NUQ0M0ZFRDYxREFGMDQ3RDhDOTM2OUZGMkJCM0IzRTRBRDUwRDI1OEFGMjJEMDc4MUU1RDAzNjRGRTBCMzAxODc3OERBOTEzMUQzQjYxRDhGOUQwMUQ3QzRCQkUzMTZCOTkxRUFFOTdBRENGNzNBOUJEMUUzRTt1PTE3MTExMzA1NDYyNjE2ODM0Mzk7aD1jZWZmMTNjYTk3ZGIwMTNhODI3MjdhMDk4ZGMxMTJiYQ==; from=direct; _yasc=/l3ITKzoyeJNt0F21+oFmvGYESGq9S4auCzU4G8oRhCZEFYYbJU7ifOWR5OY6XrfMOJwlCaqvbR6; layout-config={\"screen_height\":627,\"screen_width\":1114,\"win_width\":799.275390625,\"win_height\":630.434814453125}; count-visits=11; from_lifetime=1711130608635",
            "Referer": "https://auto.ru/cars/kia/all/",
            "Referrer-Policy": "no-referrer-when-downgrade"
        },
        "body": "{\"catalog_filter\":[{\"mark\":\"KIA\"}],\"section\":\"all\",\"category\":\"cars\",\"geo_id\":[]}",
        "method": "POST"
    })
    print(item.json())


check_2()
