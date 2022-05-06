import pandas as pd

dic={"class":['i',' ii', 'iii', 'iv'], 
     'branch': ['it', 'cse', 'ece', 'ce'], 
     'strength': [97,240,256,58], 
     'faculty':[25,55,56,32]}

x=pd.DataFrame(dic)
x.index=['B.Tech-1','B.Tech-2','B.Tech-3','B.Tech-4']
print(x)