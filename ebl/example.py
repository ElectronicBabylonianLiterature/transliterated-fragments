import json
from multiprocessing import Pool
from pathlib import Path

import requests
from tqdm import tqdm

from ebl.transliteration.domain.lark_parser import parse_atf_lark


def get_all_fragments(url):
    url_string = url(0)
    resp = requests.get(url_string)
    data = resp.json()
    fragments = data["fragments"]
    limit = len(fragments)
    total_count = data["totalCount"]
    try:
        for skip in tqdm(range(limit + 1, total_count, limit)):
            url_string = url(skip)
            resp = requests.get(url_string)
            data = resp.json()
            fragments.extend(data["fragments"])
    except Exception as e:
        print(e)
        print(f"Failed collected {len(fragments)} fragments with skip {skip}. Restart with skip={skip}")
    return fragments


def get_first_batch_fragments(url):
    url_string = url(0)
    resp = requests.get(url_string)
    data = resp.json()
    fragments = data["fragments"]
    return fragments

def parse_fragment(fragment):
    atf = fragment["atf"]
    parsed_atf = parse_atf_lark(atf)
    fragment["text"] = parsed_atf
    return fragment
def parse_fragments(fragments):
    with Pool(processes=None) as p:
        fragments = list(tqdm(p.imap(parse_fragment, fragments), total=len(fragments)))
    return fragments



if __name__ == "__main__":
    URL = "http://0.0.0.0:8000/fragments/retrieve-all"
    url = lambda skip: f"{URL}?skip={skip}"
    #fragments = get_all_fragments(url)
    fragments = get_first_batch_fragments(url)
    fragments = parse_fragments(fragments)
    with open(Path(__file__).parent / "fragments.json", "w") as f:
        json.dump(fragments, f)
