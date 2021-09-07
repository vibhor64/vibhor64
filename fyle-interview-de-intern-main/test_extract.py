import os
import json
import logging
import pytest
from extract import extract_amount

logger = logging.getLogger(__name__)

def get_test_dirpaths():
    dirpaths = []
    for dir in os.listdir('./data'):
        dirpaths.append(os.path.join('./data', dir))
    return dirpaths


dirpaths = get_test_dirpaths()
@pytest.mark.parametrize('dirpath', dirpaths)
def test_extract(dirpath):
    expected_filepath = os.path.join(dirpath, 'expected.json')
    with open(expected_filepath, mode='r', encoding="utf-8") as f:
        expected_amount = json.load(f).get('amount')
    extracted_amount = extract_amount(dirpath)
    assert expected_amount == extracted_amount, 'Expected and extracted amounts do not match'