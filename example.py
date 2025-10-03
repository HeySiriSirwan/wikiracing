from src.word_graph import WordGraph
from src.path_finder import find_path

URI = "your_neo4j_uri"
USERNAME = "your_username"
PASSWORD = "your_password"

graph = WordGraph(URI, USERNAME, PASSWORD)
graph.clear_graph()

start_word = 'pizza'
end_word = 'andromeda'
find_path(graph, start_word, end_word)
graph.close()
