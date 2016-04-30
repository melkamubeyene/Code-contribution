import numpy as np
import scipy as sc
from scipy import stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import euclidean_distances
from sympy import *
from sympy.abc import x, y
#Agregating the two evidences by determining weight in the form of distance
def agregation(Entity_struc, Entity_Tex):
    while(not(Entity_struc==Entity_Tex).all()):
        w1_1=x/(0.01+euclidean_distances(Entity_struc,Entity_struc))
        w1_2=x/(0.01+euclidean_distances(Entity_struc,Entity_Tex))
        f=solve((w1_1+w1_2)-1, x)
        p1_1=f/(0.01+euclidean_distances(Entity_struc,Entity_struc))
        p1_2=f/(0.01+euclidean_distances(Entity_struc,Entity_Tex))
        Entity_struc=(p1_1*Entity_struc)+(p1_2*Entity_Tex)
        Entity_Tex=(p1_2*Entity_struc)+((p1_1)*Entity_Tex)
        Agregated_evidence=Entity_Tex
    return Agregated_evidence
doc1=agregation(np.array([0.03020719446058235, 0.7750055302251238, 0.05641601788291324, 0.02487732341572901, 0.06815030851749641, 0.045343625498155175]), np.array([0.1292574635498672, 0.09444838014197174, 0.09080899741404197, 0.09447550915527418, 0.44633318113786247, 0.14467646860098238]))
doc2=agregation(np.array([0.5648483876143109, 0.12468348691048348, 0.10343264113170432, 0.10347379655271033, 0.10356168779079096]), np.array([0.4049811871394113, 0.07655070372040285, 0.0033070433279001744, 0.3852412625532274, 0.12991980325905825]))
