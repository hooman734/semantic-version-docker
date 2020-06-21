from urllib.request import urlopen
from json import loads
import semver


def resolve_version(__package_name__, __v_type__):
    max_version = '0.0.0'
    url_address = "https://api.nuget.org/v3-flatcontainer/{}/index.json".format(__package_name__)
    try:
        with urlopen(url_address) as web_content:
            data = web_content.read()
            encoding = web_content.info().get_content_charset('utf-8')
            version_list = loads(data.decode(encoding))['versions']
            for version in version_list:
                if semver.compare(version, max_version) == 1:
                    max_version = version

            if __v_type__ == 'major':
                max_version = semver.VersionInfo.parse(max_version)
                max_version = max_version.bump_major()

            if __v_type__ == 'minor':
                max_version = semver.VersionInfo.parse(max_version)
                max_version = max_version.bump_minor()

            if __v_type__ == 'patch':
                max_version = semver.VersionInfo.parse(max_version)
                max_version = max_version.bump_patch()

    except:
        return (), '404'
    return (max_version.major, max_version.minor, max_version.patch), '200'
