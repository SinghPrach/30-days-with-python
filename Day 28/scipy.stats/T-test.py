from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print stats.ttest_1samp(rvs,5.0)

''' Output:
Ttest_1sampResult(statistic = array([-1.40184894, 2.70158009]),
pvalue = array([ 0.16726344, 0.00945234]))
'''

