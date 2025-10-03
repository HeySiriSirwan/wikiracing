from neo4j import GraphDatabase

class WordGraph:    
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def add_word(self, word):
        """add a word node to the graph"""
        with self.driver.session() as session:
            result = session.run(
                "MERGE (w:Word {name: $word}) RETURN elementId(w) AS element_id",
                word=word)
            return result.single()["element_id"]
    
    def connect_words(self, word1, word2, rel_type="related_to", strength=1):
        """create relationship between two words"""
        with self.driver.session() as session:
            result = session.run(
                f"""
                MATCH (a:Word {{name: $word1}})
                MATCH (b:Word {{name: $word2}})
                MERGE (a)-[r:{rel_type}]->(b)
                SET r.strength = $strength
                RETURN id(r)
                """,
                word1=word1, word2=word2, strength=strength
            )
            return result.single()["id(r)"]

    def clear_graph(self):
        """Remove all nodes and relationships from the graph."""
        query = "MATCH (n) DETACH DELETE n"
        with self.driver.session() as session:
            session.run(query)
    
    def word_exists(self, word):
        """Check if word exists in the graph."""
        with self.driver.session() as session:
            result = session.run(
                "MATCH (w:Word {name: $word}) RETURN count(w) AS count",
                word=word
            )
            return result.single()["count"] > 0
            
    def find_shortest_path(self, start_word, end_word):
        """Find shortest path between two words."""
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (start:Word {name: $start_word})
                MATCH (end:Word {name: $end_word})
                MATCH p=shortestPath((start)-[*]-(end))
                RETURN [node in nodes(p) | node.name] AS path
                """,
                start_word=start_word, end_word=end_word
            )
            record = result.single()
            return record["path"] if record else None

    def close(self):
        self.driver.close()
