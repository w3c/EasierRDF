Simple template for a Docker Compose setup based on [Virtuoso](https://github.com/openlink/virtuoso-opensource/), providing an RDF store, SPARQL Endpoint, and RDF browser (among other available features) for a quick knowledge base deployment.

# Localize

1. Replace `rdf/example.ttl` with your knowledge base
2. Add your namespaces to `initdb.d/setup.sql`
3. Adapt `docker-compose.yml`
4. Copy `.env.dist` to `.env` and change `DBA_PASSWORD`

# Start to use

1. Run `docker compose up --build`
2. Test the SPARQL endpoint at [`http://localhost:8890/sparql`](http://localhost:8890/sparql)
2. Test the RDF browser at [`http://localhost:8080/`](http://localhost:8080/)
