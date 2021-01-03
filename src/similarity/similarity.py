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

def get_match_score(text: str, keywords: List[str], threshold: int):
    keywords = [keyword.lower() for keyword in keywords]
    text = text.lower()

    candidates = []
    extracted = [fuzzy_extract(query_string, text, 0, 1) for query_string in keywords if len(query_string) > 0]
    for item in extracted:
        for di in item:
            if di["dist"] <= math.ceil(len(di["word"]) / threshold):
                candidates.append(di)

    if not candidates:
        return 0
    
    return len(candidates)

def get_high_score_text(keywords, filename):
    with open(filename, 'rb') as f:
        list_text = pickle.load(f)

    count = 0
    scores = [0]*len(list_text)
    max_score = 0
    result = 0

    for text in list_text:
        score = get_match_score(text, keywords, 10)
        scores[count] = score
        if score > max_score:
            max_score = score
            result = count
        count += 1
    
    return list_text[result]

def main():
    print(get_high_score_text(['smile','friend', 'newyear'], 'data/greetings_newyear.pickle'))

if __name__ == "__main__":
    main()