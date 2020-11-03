#!/usr/bin/env python
# coding: utf-8

# In[4]:


def Queen(nb):
    def _Queen(R,nb,Res):
        if len(R)==nb: Res.append(R)
        else:
            for i0 in set(range(1,nb+1))-set(R):
                liste=[len(R)-j!=abs(i0-i) for j,i in enumerate(R)]
                if not(False in liste): _Queen(R+[i0],nb,Res)
    Res=[]
    _Queen([],nb,Res)
    return Res,('Number of solutions : %d' % len(Res))
Queen(8)

