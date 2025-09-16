import os
import sys
import time
import numpy as np
path = r'network-embeddings'
prone = r'proNE.py'

methods = ['node2vec', 'deepWalk', 'line', 'grarep', 'hope']
# methods = ['node2vec', 'deepWalk']

f = open('Subjectp.dict')
lines = f.readlines()
tim=np.zeros((10,6))
EMB_SIZE = sys.argv[1]

if (not os.path.exists(f'emb{EMB_SIZE}')):
    os.mkdir(f'emb{EMB_SIZE}')
i=0
for line in lines:
    dir, csv = line.split(',')
    # emb = os.path.join(path, dir) + os.sep + 'emb'
    # if (not os.path.exists(emb)):
    #     os.mkdir(emb)
    if (not os.path.exists(f'emb{EMB_SIZE}/{dir}')):
        os.mkdir(f'emb{EMB_SIZE}/{dir}')
    j=0
    for method in methods:
        start_time = time.time()
        cmd = f'python -m openne --method {method} --input {dir}/edgelist --graph-format edgelist --output emb{EMB_SIZE}/{dir}/{dir.lower()}-{method.lower()}.emd --representation-size {EMB_SIZE}'
        os.system(cmd)
        print(cmd)
        tim[i,j]=time.time() - start_time
        j=j+1
    start_time = time.time()
    cmd = f'python {prone} -graph {dir}/edgelist -emb1 emb{EMB_SIZE}/{dir}/{dir.lower()}-prone-sparse.emd -emb2 emb{EMB_SIZE}/{dir}/{dir.lower()}-prone-spectral.emd -dimension {EMB_SIZE} -step 10 -theta 0.5 -mu 0.2'
    print(cmd)
    os.system(cmd)
    tim[i,5]=time.time() - start_time
    i=i+1
np.savetxt(str(EMB_SIZE)+'_time.csv',tim, delimiter=',', fmt='%f')