from fuzzywuzzy import process
from fuzzysearch import find_near_matches
import math
import pickle

from typing import List

def fuzzy_extract(query_string: str, match_string: str, threshold: int, max_dist: int):
    matches = []
    for word, _ in process.extractBests(query_string, (match_string,), score_cutoff=threshold):
        for match in find_near_matches(query_string, word, max_l_dist=max_dist):
            word = word[match.start:match.end]
            matches.append({"kw": query_string, "word": word, "dist": match.dist})
    return matches

def get_match(text: str, keywords: List[str], threshold: int):
    keywords = [keyword.lower() for keyword in keywords]
    text = text.lower()

    canidates = []
    extracted = [fuzzy_extract(query_string, text, 0, 1) for query_string in keywords if len(query_string) > 0]
    for item in extracted:
        for di in item:
            if di["dist"] <= math.ceil(len(di["word"]) / threshold):
                canidates.append(di)

    if not canidates:
        return []

    result = str(canidates[0]["kw"])
    return result

keywords = ["happy"]
with open('data/greetings_newyear.pickle', 'rb') as f:
    list_text = pickle.load(f)

for i in list_text:
    text = i
    print(get_match(text, keywords, 10))