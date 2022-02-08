'''The functions provided by the scipy.io package enables us to work around with different formats of files'''

from scipy.io import loadmat
x = loadmat('test.mat')
#save the individual elements as python object
lon = x['lon']
lat = x['lat']
# one-liner to read a single variable
lon = loadmat('test.mat')['lon']
