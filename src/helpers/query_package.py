from urllib.request import urlopen
from json import loads


def fetch_data(__package_name__):
    url_address = "https://azuresearch-usnc.nuget.org/query?q={}".format(__package_name__)
    pkg_list = list()

    try:
        with urlopen(url_address) as web_content:
            data = web_content.read()
            encoding = web_content.info().get_content_charset('utf-8')
            response = loads(data.decode(encoding))
            for pkg in response["data"]:
                pkg_list.append(pkg["title"])

    except:
        print("Error to fetch")

    return pkg_list

