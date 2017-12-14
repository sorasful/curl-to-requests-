import requests
import click
import re


REGEX_ADDRESS = r"""curl '[\w:\/\.0;9-]+'"""
REGEX_HEADERS = r"""(-H ?(?:'|")[\w\s\\\/\.,;:\-\+=()\*]+)"""
REGEX_DATAS = r"""(-d|--data)( ?'[\w\s{":\.,}]+')"""
REGEX_VERB = r"""-X [\w]+"""

# @click.command()
# @click.argument('command')
def convert_curl_to_requests(command):
    """
    Take a curl as parameter and return the str of the python to implement.
    :param command:
    :return:
    """

    r_address = re.findall(REGEX_ADDRESS, command)
    address = ""
    if r_address:
        address = r_address[0].split(' ')[1].strip("'")

    r_headers = re.findall(REGEX_HEADERS, command)
    headers_k_v = [header.split(': ') for header in r_headers]
    headers = {key.replace('-H ', '').replace('"', '').replace("'", ''): value.replace('"', '').replace("'", '') for key, value in  headers_k_v}

    r_datas = re.findall(REGEX_DATAS, command)
    r_verb = re.findall(REGEX_VERB, command)

    output = "requests.{0}()"
    # requests.get(url='http://google.fr', headers = headers, datas={})


    return output


if __name__ == "__main__":

    TEST_COMMAND = "curl 'https://stackoverflow.com/questions/28568900/django-pagination-object-of-type-nonetype-has-no-len' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'referer: https://www.google.fr/' -H 'authority: stackoverflow.com' -H 'cookie: prov=50b62f78-637f-c6ff-3ad1-a64d03e675db; __qca=P0-1804862972-1508318898660; cc=bce0d12d6dbe4386a29c85993987db2e; _ga=GA1.2.472993284.1508318899; _gid=GA1.2.115529633.1513108052' --compressed"
    # TEST_COMMAND = """curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:3000/data  --data '{"key1":"value1", "key2":"value2"}'"""
    convert_curl_to_requests(TEST_COMMAND)