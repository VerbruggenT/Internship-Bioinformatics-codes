f = open('C:\Python27\Doc\permXML/(13) Ens R.txt', 'rU')
ensembllist = []
for line in f:
	ensembllist.append(line[:-2])
g = open('C:\Python27\Doc\permXML/Lijst of Ensemble Identifiers Tim SPARQL.txt', 'w')
g.write('PREFIX wp:      <http://vocabularies.wikipathways.org/wp#>'+'\n'+'PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>'+'\n'+'PREFIX dcterms: <http://purl.org/dc/terms/>'+'\n'+'SELECT DISTINCT ?pathway str(?ensId) as ?geneProduct'+'\n'+'WHERE {'+'\n'+'    ?geneProduct a wp:GeneProduct . '+'\n'+'    #?geneProduct rdfs:label ?label .'+'\n'+'    ?geneProduct wp:bdbEnsembl ?ensId .'+'\n'+'    ?geneProduct dcterms:isPartOf ?pathway .'+'\n'+'    ?pathway a wp:Pathway .'+'\n'+'    FILTER (')
n = 0

for item in ensembllist:
	if not n==0:
		g.write('") || regex(str(?ensId), "'+item)
	else:
		g.write('regex(str(?ensId), "'+item)
	n+=1
g.write('")).' + '\n'+'}')
g.close()
print '\n'