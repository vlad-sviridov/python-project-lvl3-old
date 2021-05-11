import os
import re
import requests
from urllib import parse


def get_response(url: str) -> object:
    """Get response object.

    Args:
        url (string): URL which get as a respones.

    Returns:
        object: Response object.
    """

    response = requests.get(url)

    if response.encoding is None:
        response.iter_content = 'utf-8'

    return response.text


def url_to_file_name(url: str, extention='.html') -> str:
    parsed = parse.urlparse(url)
    file_name = re.sub("[^0-9a-zA-Z]", '-', parsed.netloc + parsed.path)
    return file_name + extention


def save_page(content: object, path: str):
    with open(path, 'w') as file:
        file.write(content)


def download(output_dir: str, url: str) -> str:
    """Download web page to a file

    Args:
        output_dir (string): the directory where a page will saved
        url (string): URL from which to download a page

    Returns:
        string: Path to a downloaded page
    """

    page = get_response(url)
    file_name = url_to_file_name(url)
    path = os.path.join(output_dir, file_name)
    save_page(page, path)

    return path
