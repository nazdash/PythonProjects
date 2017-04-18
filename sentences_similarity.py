
# coding: utf-8

import numpy as np
import scipy.spatial
import re

t = []
s = {}
wl = []
w = {}
i = 0
j = 0

with open('sentences.txt', 'r') as file_obj:
    for line in file_obj:
        t.append(line)
        if line not in s.values():
            s[i] = line
            i += 1
        line = line.lower()
        line = re.split('[^a-z]', line)
        line = filter(None, line)
        wl.append(line)
        for word in line:
            if word not in w.values():
                w[j] = word
                j += 1

wc = {}

for line in wl:
    for word in line:
        if word not in wc:
            wc[word] = 0
        wc[word] += 1

print max(s), max(w)

print len(s), len(w)

print "Sentences:", s.keys()
print 'Words:', w.keys()


m = np.zeros((len(s), len(w)))

for n in s.keys():
    for d in w.keys():
        count = 0
        for word in wl[n]:
            if word == w[d]:
                count += 1
        m[n, d] = count

d = []

for vector in range(0, m.shape[0]):
    x = scipy.spatial.distance.cosine(m[0], m[vector])
    d.append(x)

for i in (0, 1, 2):
    print d.index(sorted(d)[i]), sorted(d)[i], s[i]


k = 2
result_file_obj = open('submission-1.txt', 'w')
for i in range(1, k + 1):
    result_file_obj.write(str(d.index(sorted(d)[i])))
    if i < k:
            result_file_obj.write(" ")
result_file_obj.close()

#get_ipython().system(u'cat submission-1.txt')

