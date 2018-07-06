import xml.etree.ElementTree as ET
tree = ET.parse('C:\Python27\Doc/aop-wiki-xml-2018-04-01')
root = tree.getroot()


#To find all elements to make matches, use the following for-loop
#for child in root:
#    print child.tag
#for item in root.iter():
#    print item.tag


#To write to file, open file and add 'w' to make writing possible. For loop go through all chemicals, which are defined as '{http://www.aopwiki.org/aop-xml}chemical' where the casrn is defined as '{http://www.aop-xml}casrn'.
g = open('C:\Python27\Doc\permXML/LijstmetCasrns.txt', 'w')
for chemical in root.findall('{http://www.aopkb.org/aop-xml}chemical'):
    g.write(chemical.find('{http://www.aopkb.org/aop-xml}casrn').text + '\n')
g.close()

#for jchem-inchi-keys
g = open('C:\Python27\Doc\permXML/LijstmetJchemInchikeys.txt', 'w')
for chemical in root.findall('{http://www.aopkb.org/aop-xml}chemical'):
    inchi = chemical.find('{http://www.aopkb.org/aop-xml}jchem-inchi-key').text 
    g.write(str(inchi) + '\n')
g.close()

#for indigo-inchi-keys. These already have a \n in their text so no need to write that.
g = open('C:\Python27\Doc\permXML/LijstmetIndigoInchikeys.txt', 'w')
for chemical in root.findall('{http://www.aopkb.org/aop-xml}chemical'):
    inchi = chemical.find('{http://www.aopkb.org/aop-xml}indigo-inchi-key').text 
    g.write(str(inchi))
g.close()

#for dsstox-ids
g = open('C:\Python27\Doc\permXML/Lijstmetdsstoxids.txt', 'w')
for chemical in root.findall('{http://www.aopkb.org/aop-xml}chemical'):
    inchi = chemical.find('{http://www.aopkb.org/aop-xml}dsstox-id').text 
    g.write(str(inchi) + '\n')
g.close()


g = open('C:\Python27\Doc\permXML/LijstmetBiologicalObjects.txt', 'w')
for biologicalobject in root.findall('{http://www.aopkb.org/aop-xml}biological-object'):
    biologicalobjectID = biologicalobject.find('{http://www.aopkb.org/aop-xml}source-id').text 
    g.write(str(biologicalobjectID) + '\n')
g.close()

g = open('C:\Python27\Doc\permXML/LijstmetBiologicalprocess.txt', 'w')
for biologicalprocess in root.findall('{http://www.aopkb.org/aop-xml}biological-process'):
    biologicalsourceID = biologicalprocess.find('{http://www.aopkb.org/aop-xml}source-id').text 
    g.write(str(biologicalsourceID) + '\n')
g.close()

IDs = []
g = open('C:\Python27\Doc\permXML/KeyEvents.txt', 'w')
for KE in root.findall('{http://www.aopkb.org/aop-xml}key-event'):
    level = KE.find('{http://www.aopkb.org/aop-xml}biological-organization-level').text
    if level == 'Cellular' or level == 'Molecular':
        IDs.append(KE.get('id'))

for KEref in root.findall('{http://www.aopkb.org/aop-xml}vendor-specific'):
    for KEref2 in KEref.findall('{http://www.aopkb.org/aop-xml}key-event-reference'):
        ID = KEref2.get('id')
        if ID in IDs:
            g.write('https://aopwiki.org/events/'+KEref2.get('aop-wiki-id')+'\n')
g.close()


list = ['Molecular','Cellular','Tissue','Organ','Individual','Population']
godict = {}
bpfdict = {}
for bpf in root.findall('{http://www.aopkb.org/aop-xml}biological-process'):
    bpfdict[bpf.get('id')] = bpf.find('{http://www.aopkb.org/aop-xml}source').text
    if bpf.find('{http://www.aopkb.org/aop-xml}source').text == 'GO':
        godict[bpf.get('id')]=bpf.find('{http://www.aopkb.org/aop-xml}source-id').text
GOquery = open('C:\Python27\Doc\permXML/GOsforKEsquery.txt', 'w')
GOquery.write('SELECT * FROM term \n WHERE ')
gonumber=0
for key in godict:
    if not gonumber==0:
        GOquery.write("or acc='"+godict[key]+"';")
    else:
        GOquery.write("acc='"+godict[key]+"';")
        gonumber+=1
GOquery.close()
bolist = open('C:\Python27\Doc\permXML/BOlist.txt', 'w')
bodict = {}
for bpf in root.findall('{http://www.aopkb.org/aop-xml}biological-object'):
    bodict[bpf.get('id')] = bpf.find('{http://www.aopkb.org/aop-xml}source').text
justGOs=open('C:\Python27\Doc\permXML/GOlist.txt', 'w')
fileforGOs = open('C:\Python27\Doc\permXML/GOsforKEs.txt', 'w')

HGNC= open('C:\Python27\Doc/HGNC list.txt', 'rU')
genedict = {}

for line in HGNC:
    if not 'HGNC ID    Approved Symbol    Approved Name    Previous Symbols    Synonyms    Ensembl ID(supplied by Ensembl)'in line:
        a = line.split('\t')
        genedict[a[0]]=[]
        genedict[a[0]].append(a[1])
        genedict[a[0]].append(a[2])
        if not a[5][:-1] == '':
            genedict[a[0]].append(a[5][:-1])
        for item in a[3].split(', '):
            if not item == '':
                genedict[a[0]].append(a[3])
        for item in a[4].split(', '):
            if not item == '':
                genedict[a[0]].append(a[4])
HGNC.close()

var=['201','52','195','381','382','383','385','386','55']
var2=[]
dictvar={}
for item in var:
	for KeyID in root.findall('{http://www.aopkb.org/aop-xml}vendor-specific'):
		for id in KeyID.findall ('{http://www.aopkb.org/aop-xml}key-event-reference'):
			if id.get('aop-wiki-id')==item:
				var2.append(id.get('id'))
				dictvar[id.get('id')]=item
print dictvar

titles = open('C:\Python27\Doc\permXML/KETitles.txt', 'w')

for l in var2:
    q = 'KE'+l+'dict'
    q = {}
    q['nodescription'] = 0
    q['hasdescription'] = 0
    q['nomeasurement'] = 0
    q['hasmeasurement'] = 0
    q['nocelterm'] = 0
    q['hascelterm'] = 0
    q['noorganterm'] = 0
    q['hasorganterm'] = 0
    q['noapplicabilitytax'] = 0
    q['hasapplicabilitytax'] = 0
    q['nobepr'] = 0
    #be = biological event, pr = biological process
    q['hasbepr'] = 0
    q['nobeob'] = 0
    #ob = biological object
    q['hasbeob'] = 0
    q['nobeac'] = 0
    #ac = biological action
    q['hasbeac'] = 0

    amountofKEs = 0
    for KE in root.findall('{http://www.aopkb.org/aop-xml}key-event'):
        level = KE.find('{http://www.aopkb.org/aop-xml}biological-organization-level').text
        if KE.get('id') == l:
            titles.write(KE.find('{http://www.aopkb.org/aop-xml}title').text + '\n')
            amountofKEs +=1
            if KE.find('{http://www.aopkb.org/aop-xml}description').text == None:
                q['nodescription'] += 1
            else:
                q['hasdescription'] += 1
            if KE.find('{http://www.aopkb.org/aop-xml}measurement-methodology').text == None:
                q['nomeasurement'] += 1
            else:
                q['hasmeasurement'] += 1
            if KE.find('{http://www.aopkb.org/aop-xml}cell-term') == None:
                q['nocelterm'] += 1
            else:
                q['hascelterm'] += 1
            if KE.find('{http://www.aopkb.org/aop-xml}organ-term') == None:
                q['noorganterm'] += 1
            else:
                q['hasorganterm'] += 1

            if not KE.find('{http://www.aopkb.org/aop-xml}biological-events') == None:
                if KE.find('{http://www.aopkb.org/aop-xml}biological-events').find('{http://www.aopkb.org/aop-xml}biological-event').get('process-id') == None:
                    q['nobepr'] += 1
                else:
                    q['hasbepr'] += 1
                if KE.find('{http://www.aopkb.org/aop-xml}biological-events').find('{http://www.aopkb.org/aop-xml}biological-event').get('object-id') == None:
                    q['nobeob'] += 1
                else:
                    q['hasbeob'] += 1
                if KE.find('{http://www.aopkb.org/aop-xml}biological-events').find('{http://www.aopkb.org/aop-xml}biological-event').get('action-id') == None:
                    q['nobeac'] += 1
                else:
                    q['hasbeac'] += 1
            else:
                q['nobepr'] += 1
                q['nobeob'] += 1
                q['nobeac'] += 1

    print '\n'
    print q['nodescription'],'no description'
    print q['hasdescription'],'has description'
    print q['nomeasurement'],'no measurement'
    print q['hasmeasurement'],'has measurement'
    print q['nocelterm'],'no celterm'
    print q['hascelterm'],'has celterm'
    print q['noorganterm'],'no organterm'
    print q['hasorganterm'],'has organterm'
    print q['nobepr'] ,'no biological process'
    print q['hasbepr'],'has biological process'
    print q['nobeob'],'no biological object'
    print q['hasbeob'],'has biological object'
    print q['nobeac'],'no biological action'
    print q['hasbeac'],'has biological action'
    print q['noapplicabilitytax'] ,'no taxonomy'
    print q['hasapplicabilitytax'] ,'has taxonomy'

    print '\n'

    total=0
    kebp = {}
    kebp['GO'] =0
    kebp['MI'] = 0
    kebp['MESH']=0
    kebp['MP'] = 0
    kebp['MI'] = 0
    kebp['VT'] = 0
    kebp['HP'] = 0
    kebp['NBO'] = 0
    kebp['PCO'] = 0
    kebo = {}
    kebo['CL'] =0
    kebo['GO'] =0
    kebo['FMA'] = 0
    kebo['MESH']=0
    kebo['MP'] = 0
    kebo['PR'] = 0
    kebo['CHEBI'] = 0
    kebo['UBERON'] = 0
    kebo['PCO'] = 0

    kect={}
    kect['CL']=0
    kect['WIKI']=0
    keot={}
    keot['UBERON']=0
    keot['WIKI']=0

    for KE in root.findall('{http://www.aopkb.org/aop-xml}key-event'):
        level = KE.find('{http://www.aopkb.org/aop-xml}biological-organization-level').text
        if KE.get('id') == l:
            if not KE.find('{http://www.aopkb.org/aop-xml}biological-events') == None:
                if not KE.find('{http://www.aopkb.org/aop-xml}biological-events').find('{http://www.aopkb.org/aop-xml}biological-event').get('process-id') == None:
                    for gotag in KE.find('{http://www.aopkb.org/aop-xml}biological-events').findall('{http://www.aopkb.org/aop-xml}biological-event'):
                        if not gotag.get('process-id') == None:
                            kebp[bpfdict[gotag.get('process-id')]]+=1
                            total += 1
                            if godict.has_key(gotag.get('process-id')):
                                fileforGOs.write(str(KE.find('{http://www.aopkb.org/aop-xml}title').text))
                                fileforGOs.write( '\t'+l+'\t')
                                fileforGOs.write(str(godict[gotag.get('process-id')])+'\n')
                                justGOs.write(str(godict[gotag.get('process-id')])+'\n')
                if not KE.find('{http://www.aopkb.org/aop-xml}biological-events').find('{http://www.aopkb.org/aop-xml}biological-event').get('object-id') == None:
					for botag in KE.find('{http://www.aopkb.org/aop-xml}biological-events').findall('{http://www.aopkb.org/aop-xml}biological-event'):
						if not botag.get('object-id')==None:
							kebo[bodict[botag.get('object-id')]]+=1
							if bodict.has_key(botag.get('object-id')):
								bolist.write(str(bodict[botag.get('object-id')])+'\n')
            if not KE.find('{http://www.aopkb.org/aop-xml}cell-term') == None:
                kect[KE.find('{http://www.aopkb.org/aop-xml}cell-term').find('{http://www.aopkb.org/aop-xml}source').text]+=1
            if not KE.find('{http://www.aopkb.org/aop-xml}organ-term') == None:
                keot[KE.find('{http://www.aopkb.org/aop-xml}organ-term').find('{http://www.aopkb.org/aop-xml}source').text]+=1
    print 'Ontologies for Biological Process'
    print kebp
    print 'Ontologies for Biological Object'
    print kebo
    print 'Ontologies for cell-term'
    print kect
    print 'Ontologies for Organ-term'
    print keot
    print '\n'
    print 'total biological process:',total
    for key in kebp:
        if kebp[key] != 0:
            percentage = float(100*kebp[key])/float(total)
            print key,' present for ',percentage
            
            
            
    ensembllist = []
    n=0
    o=0
    overlapdict = {}
    ode = {}
    for KE in root.findall('{http://www.aopkb.org/aop-xml}key-event'):
        level = KE.find('{http://www.aopkb.org/aop-xml}biological-organization-level').text
        if KE.get('id') == l:
            n+=1
            if not KE.find('{http://www.aopkb.org/aop-xml}description').text == None:
                overlapdict[KE.get('id')]=[]
                ode[KE.get('id')]=[]
                o+=1
                for key in genedict:
                    for item in genedict[key]:
                        item1 = ' '+item+' '
                        item2 = '('+item+','
                        item3 = ' '+item+','
                        item4 = '('+item+')'
                        item5 = ' '+item+')'
                        item6 = '['+item+']'
                        item7 = '['+item+','
                        item8 = ' '+item+']'
                        item9 = ' '+item+'.'
                        item10 = '('+item+' '
                        item11 = '['+item+' '
                        if item1 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item2 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item3 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item4 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item5 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item6 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item7 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item8 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item9 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item10 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])
                        if item11 in KE.find('{http://www.aopkb.org/aop-xml}description').text:
                            overlapdict[KE.get('id')].append(item)
                            ode[KE.get('id')].append(genedict[key][2])
                            if not genedict[key][2] in ensembllist:
                                ensembllist.append(genedict[key][2])

    print l
    print 'Total KEs'
    print n
    print 'Total with description'
    print o
    print 'Total amount of unique genes:'
    print len(ensembllist)
    
    g = open('C:\Python27\Doc\permXML/HGNCmappedgenesonKEs'+dictvar[l]+'.txt', 'w')
    for item in overlapdict:
        g.write(item )
        for gene in overlapdict[item]:
            g.write( '\t'+gene)
        g.write('\n')
    g.close()
    g = open('C:\Python27\Doc\permXML/HGNCmappedgenesonKEse'+dictvar[l]+'.txt', 'w')
    for item in ode:
        g.write(item )
        for a in item[1:]:
            g.write('\t')
            g.write(str(ode[item]))
        g.write('\n')
    g.close()

    g = open('C:\Python27\Doc\permXML/SPARQLqueryENSIDsafterHGNCmap'+dictvar[l]+'.txt', 'w')
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
            
            
            
            
titles.close()           
            
bolist.close()
            
justGOs.close()
fileforGOs.close()

KRd = {}
KRd['nodescription'] = 0
KRd['hasdescription'] =0
KRd['nowoev'] = 0
KRd['haswoev'] =0
KRd['nowoeb'] = 0
KRd['haswoeb'] =0
KRd['nowoee'] = 0
KRd['haswoee'] =0
KRd['nowoeu'] = 0
KRd['haswoeu'] =0
KRd['noquan'] = 0
KRd['hasquan'] =0
KRd['notaxapp'] = 0
KRd['hastaxapp'] =0
KRd['notaxappev'] = 0
KRd['hastaxappev'] =0
KRd['noref'] = 0
KRd['hasref'] =0



amountofKERs = 0
for KER in root.findall('{http://www.aopkb.org/aop-xml}key-event-relationship'):
    amountofKERs += 1
    if KER.find('{http://www.aopkb.org/aop-xml}description').text == None:
        KRd['nodescription'] += 1
    else:
        KRd['hasdescription'] += 1
    if not KER.find('{http://www.aopkb.org/aop-xml}weight-of-evidence').find('{http://www.aopkb.org/aop-xml}value').text == None:
        KRd['haswoev'] += 1
    else:
        KRd['nowoev'] += 1
    if not KER.find('{http://www.aopkb.org/aop-xml}weight-of-evidence').find('{http://www.aopkb.org/aop-xml}biological-plausibility').text == None:
        KRd['haswoeb'] += 1
    else:
        KRd['nowoeb'] += 1
    if not KER.find('{http://www.aopkb.org/aop-xml}weight-of-evidence').find('{http://www.aopkb.org/aop-xml}emperical-support-linkage').text == None:
        KRd['haswoee'] += 1
    else:
        KRd['nowoee'] += 1
    if not KER.find('{http://www.aopkb.org/aop-xml}weight-of-evidence').find('{http://www.aopkb.org/aop-xml}uncertainties-or-inconsistencies').text == None:
        KRd['haswoeu'] += 1
    else:
        KRd['nowoeu'] += 1
    if not KER.find('{http://www.aopkb.org/aop-xml}quantitative-understanding').find('{http://www.aopkb.org/aop-xml}description').text == None:
        KRd['hasquan'] += 1
    else:
        KRd['noquan'] += 1
    if KER.find('{http://www.aopkb.org/aop-xml}taxonomic-applicability').text == None or KER.find('{http://www.aopkb.org/aop-xml}taxonomic-applicability').text == '\n    ':
        KRd['notaxapp'] += 1
    else:
        KRd['hastaxapp'] += 1
    if KER.find('{http://www.aopkb.org/aop-xml}evidence-supporting-taxonomic-applicability').text == None or KER.find('{http://www.aopkb.org/aop-xml}evidence-supporting-taxonomic-applicability').text == '\n    ':
        KRd['notaxappev'] += 1
    else:
        KRd['hastaxappev'] += 1
    if KER.find('{http://www.aopkb.org/aop-xml}references').text == None:
        KRd['noref'] += 1
    else:
        KRd['hasref'] += 1

        
print 'KEY EVENT RELATIONSHIPS'
print 'The total amount of KERs:'
print amountofKERs
print '\n'
        
        
print KRd['nodescription'], 'no description'
print KRd['hasdescription'], 'has description'
print KRd['nowoev'], 'no WoE value'
print KRd['haswoev'], 'has WoE value'
print KRd['nowoeb'] , 'no WoE biological plausibility'
print KRd['haswoeb'], 'has WoE biological plausibility'
print KRd['nowoee'] , 'no WoE emperical-support-linkage'
print KRd['haswoee'], 'has WoE emperical-support-linkage'
print KRd['nowoeu'] , 'no WoE uncertainties-or-inconsistencies'
print KRd['haswoeu'], 'has WoE uncertainties-or-inconsistencies'
print KRd['noquan'] , 'no quantitative-understanding'
print KRd['hasquan'], 'has quantitative-understanding'
print KRd['notaxapp'] ,'no taxonomic-applicability'
print KRd['hastaxapp'], 'has taxonomic-applicability'
print KRd['notaxappev'] ,'no evidence-supporting-taxonomic-applicability'
print KRd['hastaxappev'], 'has evidence-supporting-taxonomic-applicability'
print KRd['noref'] ,'no references'
print KRd['hasref'], 'has references'
print '\n'



strd = {}
strd['nodescription'] = 0
strd['hasdescription'] = 0
strd['nochem'] = 0
strd['haschem'] = 0
strd['noexp']=0
strd['hasexp'] =0

amountofStressors = 0
for st in root.findall('{http://www.aopkb.org/aop-xml}stressor'):
    amountofStressors += 1
    if st.find('{http://www.aopkb.org/aop-xml}description').text == None:
        strd['nodescription'] += 1
    else:
        strd['hasdescription'] += 1
    if st.find('{http://www.aopkb.org/aop-xml}chemicals') == None:
        strd['nochem'] += 1
    else:
        strd['haschem'] += 1
    if st.find('{http://www.aopkb.org/aop-xml}exposure-characterization').text == None:
        strd['noexp'] += 1
    else:
        strd['hasexp'] += 1
        
print 'STRESSORS'
print 'Total amount:', amountofStressors
print strd['nodescription'], 'no description'
print strd['hasdescription'], 'has description'
print strd['nochem'], 'no chem'
print strd['haschem'], 'has chem'
print strd['noexp'], 'no exp'
print strd['hasexp'], 'has exp'

total = 0
no = 0
for chemical in root.findall('{http://www.aopkb.org/aop-xml}chemical'):
    total+= 1
    if chemical.find('{http://www.aopkb.org/aop-xml}jchem-inchi-key').text == None:
        no += 1

a=total-no

percenthasinchi = a*100/total
print percenthasinchi, '% has inchi'








