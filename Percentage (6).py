f=open('C:\Python27\Doc\permXML\(6) ZOOMAWP.txt', 'rU')
PWs1=[]
for line in f:
	if not line.split('\t')[0] in PWs1:
		PWs1.append(line.split('\t')[0])
print len(PWs1) , 'pathways in ZOOMA'
f.close()

f=open('C:\Python27\Doc\permXML\(6) MiningWP.txt', 'rU')
PWs2=[]
for line in f:
	if not line.split('\t')[0] in PWs2:
		PWs2.append(line.split('\t')[0])
print len(PWs2), 'pathways in Description'
f.close()

f=open('C:\Python27\Doc\permXML\(6) Ens RWP.txt', 'rU')
PWs3=[]
for line in f:
	if not line.split('\t')[0] in PWs3:
		PWs3.append(line.split('\t')[0])
print len(PWs3), 'pathways from All genes'
f.close()

f=open('C:\Python27\Doc\permXML\(6) Cytoscape.txt', 'rU')
PWs4=[]
for line in f:
	if not line.split('\t')[0] in PWs4:
		PWs4.append(line.split('\t')[0])
print len(PWs4), 'pathways from Cytoscape'
f.close()

f=open('C:\Python27\Doc\permXML\(6) Manual.txt', 'rU')
PWs5=[]
for line in f:
	if not line.split('\t')[0] in PWs5:
		PWs5.append(line.split('\t')[0])
print len(PWs5), 'pathways from Manual'
f.close()

print '\n'

a=0
for item in PWs1:
	if item in PWs2:
		a+=1		
print a, '', 'pathways overlap in ZOOMA and Description'

b=0
for item in PWs1:
	if item in PWs3:
		b+=1
print b, '', 'pathways overlap in ZOOMA and All genes'

c=0
for item in PWs1:
	if item in PWs4:
		c+=1
print c, '', 'pathways overlap in ZOOMA and Cytoscape'

d=0
for item in PWs2:
	if item in PWs3:
		d+=1
print d , '', 'pathways overlap in Description and All genes' 

e=0
for item in PWs2:
	if item in PWs4:
		e+=1
print e, '', 'pathways overlap in Description and Cytoscape'

f=0
for item in PWs3:
	if item in PWs4:
		f+=1
print f, '', 'pathways overlap in Cytoscape and All genes'

print '\n'

h=0
for item in PWs1:
	if item in PWs2:
		if item in PWs3:
			h+=1
print h, '', 'pathways overlap in ZOOMA, Description and All genes'

i=0
for item in PWs1:
	if item in PWs2:
		if item in PWs4:
			i+=1
print i, '', 'pathways overlap in ZOOMA, Description and Cytoscape'

j=0
for item in PWs1:
	if item in PWs3:
		if item in PWs4:
			j+=1
print j, '', 'pathways overlap in ZOOMA, All genes and Cytoscape'

k=0
for item in PWs2:
	if item in PWs3:
		if item in PWs4:
			k+=1
print k, '', 'pathways overlap in Description, All genes and Cytoscape'

print '\n'

g=0
for item in PWs1:
	if item in PWs2:
		if item in PWs3:
			if item in PWs4:
				g+=1
print g, '', 'pathways overlap in ZOOMA, Description, All genes and Cytoscape'

for item in PWs1:
	if item in PWs2:
		if item in PWs3:
			if item in PWs4:
				print item

print '\n'

l=0
for item in PWs1:
	if item in PWs5:
		l+=1		
print l, '', 'pathways overlap in ZOOMA and Manual'

m=0
for item in PWs2:
	if item in PWs5:
		m+=1		
print m, '', 'pathways overlap in Description and Manual'

n=0
for item in PWs3:
	if item in PWs5:
		n+=1		
print n, '', 'pathways overlap in All genes and Manual'

o=0
for item in PWs4:
	if item in PWs5:
		o+=1		
print o, '', 'pathways overlap in Cytoscape and Manual'