import csv
import json
import math
import random
import sys


# Finding Jaccard distance
def compute_sse(Y, point):
    length = 0
    asd = 0
    for j in point:
        for i in Y:
            if (Y[j][1] != j): continue
            asd = 1 - float(len((Y[i][0]).intersection(Y[j][0]))) / len((Y[i][0]).union(Y[j][0]))
            length += math.pow(asd, 2)
    print 'sse: ', (length/100), ' k = ', len(point)


def cluster_make(pt):
    a = 0
    for i in pt:
        a += math.pow(i, 2)
    return a

no_of_clusters, seedValues, filein, fileout = sys.argv[1:]

cluster_count = int(no_of_clusters)
fout = open(fileout, 'w')
storeOut = sys.stdout
sys.stdout = fout

fin = open(filein)
# f2 = open('Tweets.json')
inpMat = {}

a = fin.readline()
i = 0
while (a != ''):
    info = json.loads(a)
    info['text'] = set((info['text']).split(' '))
    inpMat.update({info['id']: [info['text'], -1]})
    a = fin.readline()


fseed = open(seedValues, 'rt')
headerInfo = csv.Sniffer().has_header(fseed.read(1024))
fseed.seek(0)
in_csv = csv.reader(fseed)
if headerInfo:
    Attr_names = next(in_csv)
K = [int(i[0]) for i in in_csv]

# getting centroids  randomly for k
temp = random.sample(K, cluster_count)
points = {}
len_k_pt = len(temp)
for i in temp:
    points.update({i: inpMat[i]})
# print 'Debug point 1'
# pdb.set_trace()



Xlength = len(inpMat)
fin.close()
fseed.close()

#Code Base ....

dmeasure = {}
count = 0
subtr = []
previous = []

for i in xrange(cluster_count):
    subtr.append([-1])
# pdb.set_trace()
print 'Iterations : ',
while (count < 25 and any(tem != 0 for tem in subtr)):
    print count,
   
    previous = []
    temp = inpMat.iterkeys()
	
    for j in xrange(Xlength):
        previous.append(temp.next())

    for i in inpMat:
        # put each element into nearest centroid cluster.
        dmeasure = 1
        mini = 2
        idAllocate = 0
        for k_i in points:
            dmeasure = 1 - float(len((inpMat[i][0]).intersection(points[k_i][0]))) / len((inpMat[i][0]).union(points[k_i][0]))
            if (dmeasure < mini):
                mini = dmeasure
                idAllocate = k_i
        inpMat[i][1] = idAllocate
    
	
	##base 2
	
    points_temp = {}
    for each_i in points:
        dmeasure = 1
        sse_min = 999999999
        idAllot = 0

        for i in inpMat:
            if (inpMat[i][1] != each_i): continue
            temp_set = []
            for j in inpMat:
                if (inpMat[j][1] != each_i): continue
                if (i == j): continue
                temp_set.append(1 - float(len((inpMat[i][0]).intersection(inpMat[j][0]))) / len((inpMat[i][0]).union(inpMat[j][0])))
            dmeasure = cluster_make(temp_set)
            if (dmeasure < sse_min):
                # pdb.set_trace()
                sse_min = dmeasure
                idAllot = i
    
        points_temp.update({idAllot: inpMat[idAllot]})

    points_len = len(points)
    points_temp_ptr = points_temp.__iter__()
    subtr = []
    for j in points:
        subtr.append(j - points_temp_ptr.next())
    points = points_temp
    count += 1

print "\n"
for pt in points:
    print  i,
    print '\t',
    for j in inpMat:
        if (pt == inpMat[j][1]):
            print j, ',',
    print '\n\n'
compute_sse(inpMat, points)
sys.stdout = storeOut
fseed.close()
print 'Outputting to file:', fileout
