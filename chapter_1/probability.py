import pandas as pd

def load_gss_data():
    return pd.read_csv('35478-0001-Data.tsv', sep='\t', index_col=1)

def bankers_probability(gss_dataframe):
    bankers = (gss_dataframe['INDUS10'] == 6870)
    return compute_probability(bankers)
def female_probability(gss_dataframe):
    female = (gss_dataframe['SEX'] == 2)
    return compute_probability(female)
def liberal_probability(gss_dataframe):
    '''
    The values of polviews are on a seven-point scale:
    1   Extremely liberal
    2   Liberal
    3   Slightly liberal
    4   Moderate
    5   Slightly conservative
    6   Conservative
    7   Extremely conservative
    '''

    '''
    I’ll define liberal to be True for anyone whose response is “Extremely liberal”, “Liberal”, or “Slightly liberal”.

    '''
    liberal = (gss_dataframe['POLVIEWS'] <= 3)
    return  compute_probability(liberal)
def compute_probability(A):
    """Computes the probability of a proposition, A."""
    '''
    If we use the sum function on this Series, 
    it treats True as 1 and False as 0, so the total is the number of bankers.
    '''
    #A.sum()
    '''
    To compute the fraction of True values in the series,
     we can use the mean function,which computes the fraction of True 
    values in the Series
    '''
    return A.mean()









if __name__ == '__main__':
    print(liberal_probability(load_gss_data()))