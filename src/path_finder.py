from nltk.corpus import wordnet as wn
from .keyword_extractor import extract_keywords_fixed

def build_word_graph_recursive(graph, word, depth=0, max_depth=2, parent=None, visited=None):
    """build word graph recursively using WordNet definitions."""
    if visited is None:
        visited = set()
    if depth > max_depth or word in visited:
        return
    visited.add(word)    
    graph.add_word(word)
    if parent and parent != word:
        graph.connect_words(parent, word, rel_type="RELATED_TO", strength=1)    
    if depth >= max_depth:
        return    
    synsets = wn.synsets(word)
    if not synsets:
        return
    definition = synsets[0].definition()
    keywords = extract_keywords_fixed(definition)
    for keyword in keywords:
        if len(keyword) > 2:
            build_word_graph_recursive(
                graph, keyword, depth + 1, max_depth, 
                parent=word, visited=visited
            )

def find_path(graph, start_word, end_word, max_attempts=3):
    """find semantic path between two words using WordNet"""
    for depth in range(1, max_attempts + 1):
        print(f"searching with depth={depth}...")
        build_word_graph_recursive(graph, start_word, max_depth=depth)
        build_word_graph_recursive(graph, end_word, max_depth=depth)
        path = graph.find_shortest_path(start_word, end_word)
        if path:
            print(f"path found: {' -> '.join(path)}")
            return path
    print("No path found!")
    return None
