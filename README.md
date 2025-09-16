To run the file:

import networkx as nx
from math import *
!python Driver.py
!python embed.py 128
python proNE.py -graph Ant/edgelist -emb1 emb128/Ant/ant-prone-sparse.emd -emb2 emb128/Ant/ant-prone-spectral.emd -dimension 128 -step 10 -theta 0.5 -mu 0.2
