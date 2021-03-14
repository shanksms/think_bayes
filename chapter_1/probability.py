import pandas as pd

def load_gss_data():
    return pd.read_csv('35478-0001-Data.tsv', sep='\t', index_col=1)

def bankers_boolean_series(gss_dataframe):
    return (gss_dataframe['INDUS10'] == 6870)
def democrat_boolean_series(gss_dataframe):
    return (gss_dataframe['PARTYID'] <= 1)
def liberal_boolean_series(gss_dataframe):
    return (gss_dataframe['POLVIEWS'] <= 3)
def female_boolean_series(gss_dataframe):
    return  (gss_dataframe['SEX'] == 2)
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
def political_affiliations(gss_dataframe):
    '''

    :param gss_dataframe:
    :return:
    '''
    '''
    0   Strong democrat
    1   Not strong democrat
    2   Independent, near democrat
    3   Independent
    4   Independent, near republican
    5   Not strong republican
    6   Strong republican
    7   Other party
    I’ll define democrat to include respondents who chose “Strong democrat” or “Not strong democrat”:
    '''
    return compute_probability((gss_dataframe['PARTYID'] <= 1))

def democrat_and_banker(gss_dataframe):
    '''

    :param gss_dataframe:
    :return:
    Now that we have a definition of probability and a function that computes it, let’s move on to conjunction.

“Conjunction” is another name for the logical and operation. If you have two propositions, A and B,
 the conjunction A and B is True if both A and B are True, and False otherwise.
 If we have two Boolean series, we can use the & operator to compute their conjunction. For example,
  we have already computed the probability that a respondent is a banker.
    '''
    return compute_probability(bankers_boolean_series(gss_dataframe) & democrat_boolean_series(gss_dataframe))
def given_female_probaility_of_liberal(gss_dataframe):
    liberal = liberal_boolean_series(gss_dataframe)
    female = female_boolean_series(gss_dataframe)
    return compute_conditional_probability(liberal, given=female)
def compute_conditional_probability(proposition, given):
    """Probability of A conditioned on given."""
    return compute_probability(proposition[given])
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
    print(given_female_probaility_of_liberal(load_gss_data()))