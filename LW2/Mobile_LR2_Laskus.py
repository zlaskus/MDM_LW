import pandas as pd

data = pd.read_csv('NetTraffic.csv')

class tariff_11(object):
	def __init__(self):
		self.ip = str(input())
		self.price = .5

print('Enter IP address')
user = tariff_11()

rate = data['Rate(MB)'].loc[(data['Src'] == user.ip) | (data['Dest'] == user.ip)].sum()
bill = rate*user.price

print('\nCLIENT IP ADDRESS: %s\n' % user.ip)
print('USED DATA RATE: %.4f MB' % rate, end='')
print('\tPRICE: %.2f RUB/MB\n' % user.price)
print('TOTAL AMOUNT: %.4f RUB' % bill)