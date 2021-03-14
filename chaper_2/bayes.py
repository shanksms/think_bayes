'''
Suppose there are two bowls of cookies.
Bowl 1 contains 30 vanilla cookies and 10 chocolate cookies.
Bowl 2 contains 20 vanilla cookies and 20 chocolate cookies.
Now suppose you choose one of the bowls at random and, without looking, choose a cookie at random.
If the cookie is vanilla, what is the probability that it came from Bowl 1?
'''

import pandas as pd

table = pd.DataFrame(index=['Bowl 1', 'Bowl 1'])
table['prior'] = 1/2, 1/2
'''
The chance of getting a vanilla cookie from Bowl 1 is 3/4.

The chance of getting a vanilla cookie from Bowl 2 is 1/2.
'''
table['likelihood'] = 3/4, 1/2
'''
The next step is similar to what we did with Bayes’s Theorem; we multiply the priors by the likelihoods:
'''
table['unnorm'] = table['prior'] * table['likelihood']
'''
I call the result unnorm because these values are the “unnormalized posteriors”.
 Each of them is the product of a prior and a likelihood:

P(Bi)P(D|Bi)
which is the numerator of Bayes’s Theorem. If we add them up, we have

P(B1)P(D|B1)+P(B2)P(D|B2)
which is the denominator of Bayes’s Theorem, P(D).
'''
'''
So we can compute the total probability of the data like this:
'''
prob_data = table['unnorm'].sum()
table['posterior'] = table['unnorm'] / prob_data

print(table)