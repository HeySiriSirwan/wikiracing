# wikiracing

a simple tool for discovering semantic connections between words using WordNet and Neo4j graph database

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wordnet-graph.git
   cd wordnet-graph
    ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download NLTK data:
   ```python
   import nltk
   nltk.download('wordnet')
   ```
## Usage
   ```python
   from src.word_graph import WordGraph
   from src.path_finder import find_path
   
   # configure with your Neo4j credentials
   graph = WordGraph(URI, USERNAME, PASSWORD)
   
   path = find_path(graph, 'pizza', 'andromeda')
   ```

## Project Structure
   ```
   wordnet-graph/
   ├── src/
   │   ├── keyword_extractor.py    # text processing with spaCy
   │   ├── word_graph.py          # Neo4j graph operations
   │   └── path_finder.py         # path finding algorithms
   ├── requirements.txt           # dependencies
   ├── README.md                 
   └── example.py               # usage examples
   ```

## Requirements

- Neo4j Database (local or cloud)
- Python 3.8+

## How It Works

1. Extracts keywords from WordNet definitions
2. Builds a graph where words are nodes and semantic relationships are edges
3. Recursively explores connections up to a specified depth
4. Finds the shortest path between any two connected words

## Limitations
- this is a simple implementation and may not find all possible connections
- performance depends on WordNet coverage and graph depth
- results may vary based on the starting words chosen

## Contributing
This is a learning project and contributions are welcome. Feel free to suggest improvements or report issues. :)

