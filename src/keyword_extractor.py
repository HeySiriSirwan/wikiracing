import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords_fixed(text: str) -> list[str]:
    """extract keywords from text using spaCy with entity recognition."""
    doc = nlp(text)
    keep_pos = {"ADJ", "NOUN", "PROPN"}
    ent_spans = [(ent.start, ent.end, ent.text) for ent in doc.ents]
    ent_token_index = set()
    ent_map = {}
    for start, end, ent_text in ent_spans:
        for i in range(start, end):
            ent_token_index.add(i)
        ent_map[start] = ent_text
    result = []
    seen = set()
    i = 0
    while i < len(doc):
        token = doc[i]
        if i in ent_map:
            ent_text = ent_map[i].strip()
            key = ent_text.lower()
            if key not in seen and any(ch.isalpha() for ch in ent_text):
                result.append(ent_text)
                seen.add(key)
            while i < len(doc) and i in ent_token_index:
                i += 1
            continue
        if token.is_punct or token.is_space or not any(ch.isalpha() for ch in token.text):
            i += 1
            continue
        if token.is_stop or token.pos_ not in keep_pos:
            i += 1
            continue
        if token.pos_ == "PROPN":
            token_out = token.text
        else:
            token_out = token.lemma_.lower()
        key = token_out.lower()
        if key not in seen:
            result.append(token_out)
            seen.add(key)
        i += 1
    return result
