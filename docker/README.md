Simple template for a Docker Compose setup with a SPARQL Endpoint and RDF browser for a small knowledge base.

# Run

1. `docker compose up --build`
2. test the SPARQL endpoint http://localhost:8890/sparql and the RDF browser at http://localhost:8080/

# Adapt

1. replace rdf/example.ttl with your knowledge base
2. add your namespaces to initdb.d/setup.sql
3. adapt docker-compose.yml
4. copy .env.dist to .env and change DBA\_PASSWORD
