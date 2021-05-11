import os
from page_loader.loader import download


def test_download_page(requests_mock, tmpdir):
    path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'page.html')
    page_url = 'https://ru.hexlet.io/courses'

    with open(path, 'r') as file:
        content = file.read()

    requests_mock.get(page_url, text=content)

    page_file_path = tmpdir / 'ru-hexlet-io-courses.html'
    assert download(tmpdir, page_url) == page_file_path

    with open(page_file_path) as file:
        assert sorted(file.read()) == sorted(content)
