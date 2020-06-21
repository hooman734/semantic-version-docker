from urllib.request import urlopen
from json import loads
from re import split


def resolve_version(__package_name__, __v_type__):
    max_major = 0
    max_version = tuple()
    url_address = "https://api.nuget.org/v3-flatcontainer/{}/index.json".format(__package_name__)
    try:
        with urlopen(url_address) as web_content:
            data = web_content.read()
            encoding = web_content.info().get_content_charset('utf-8')
            version_list = loads(data.decode(encoding))['versions']
            for version in version_list:
                (major, minor, *patch_prefix, patch) = split('\.', version)
                if int(major) >= int(max_major):
                    max_major = major
                    p_prefix = ''
                    if len(patch_prefix) != 0:
                        for p in patch_prefix:
                            p_prefix += str(p)

            if __v_type__ == 'major':
                max_version = (str(int(major) + 1), minor, patch), '200'

            if __v_type__ == 'minor':
                max_version = (major, str(int(minor) + 1), patch), '200'

            if __v_type__ == 'patch':
                patch = str(int(patch) + 1) + patch
                max_version = (major, minor, patch), '200'
    except:
        return (), '404'

    return max_version
