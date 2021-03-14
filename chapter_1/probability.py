import pandas as pd



def compute_probability(A):
    """Computes the probability of a proposition, A."""
    return A.mean()

gss = pd.read_csv('35478-0001-Data.tsv', sep='\t', index_col=1)
#print(gss.head())
#indus10 column represents industry code. 6870 is for banker
bankers = (gss['INDUS10'] == 6870)
#print(bankers.head())
'''
If we use the sum function on this Series, 
it treats True as 1 and False as 0, so the total is the number of bankers.
'''
print(bankers.sum())
'''
To compute the fraction of bankers, we can use the mean function,which computes the fraction of True 
values in the Series
'''



print(compute_probability(bankers))
female = (gss['SEX'] == 2)
print(compute_probability(female))




