log_message('Setup: Activate CORS');
update DB.DBA.HTTP_PATH set HP_OPTIONS = serialize(vector('browse_sheet', '', 'noinherit', 'yes', 'cors', '*', 'cors_restricted', 0))  where HP_LPATH = '/sparql';
log_message('Setup: Declare namespaces');
DB.DBA.XML_SET_NS_DECL ('ex', 'http://example.org/', 2);
log_message('Setup: Load data');
ld_dir_all ('/rdf/', '*.ttl', 'http://example.org');
rdf_loader_run();
log_message('Setup: Finished');

