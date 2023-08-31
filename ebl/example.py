import json
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



def get_some_fragments_and_parse(url):
    url_string = url(0)
    resp = requests.get(url_string)
    data = resp.json()
    fragments = data["fragments"]
    for fragment in tqdm(fragments):
        atf = fragment["atf"]
        parsed_atf = parse_atf_lark(atf)
        fragment["text"] = parsed_atf
    return fragments



if __name__ == "__main__":
    url = lambda skip: f"http://0.0.0.0:8000/fragments/retrieve-all?skip={skip}"
    fragments = get_all_fragments(url)
    #fragments = get_first_batch_fragments(url)
    with open(Path(__file__).parent / "fragments.json", "w") as f:
        json.dump(fragments, f)
