import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

#split string on the hidden characters that indicate newlines
data = data.splitlines()

#check data
print "*split string first time*\n"
print data
print "\n"

#split string into list of strings then use list comprehension
#to make list of lists
data = [i.split(', ') for i in data]

#check data
print "*split string again*\n"
print data
print "\n"

#create pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

#check data
print "*show in dataframe*\n"
print df
print "\n"

#convert alcohol and tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "*calculate Alcohol mean, median, mode, range, variance, standard deviation*\n"

#alcohol mean
df['Alcohol'].mean()
print "Alcohol mean is " + str(df['Alcohol'].mean()) 
# 5.4436363636363634

#alcohol median
df['Alcohol'].median() 
print "Alcohol median is " + str(df['Alcohol'].median())
# 5.63

#alcohol mode
# If all numbers occur equally often, stats.mode() will return the smallest number
stats.mode(df['Alcohol'])
print "Alcohol mode is " + str(stats.mode(df['Alcohol'])) 
# 4.02

#alcohol range
range = max(df['Alcohol']) - min(df['Alcohol'])
print "Alcohol range is " + str(range)
# 2.4500000000000002

#alcohol variance
df['Alcohol'].var() 
print "Alcohol variance is " + str(df['Alcohol'].var())
# 0.63642545454546284

#alcohol standard deviation
df['Alcohol'].std() 
print "Alcohol standard deviation is " + str(df['Alcohol'].std())
# 0.79776278087252406

print "\n" + "*calculate Tobacco mean, median, mode, range, variance, standard deviation*\n"
#tobacco mean
df['Tobacco'].mean()
print "Tobacco mean is " + str(df['Tobacco'].mean()) 
# 3.6181818181818186

#tobacco median
df['Tobacco'].median()
print "Tobacco median is " + str(df['Tobacco'].median()) 
# 3.53

#tobacco mode
stats.mode(df['Tobacco'])
print "Tobacco mode is " + str(stats.mode(df['Tobacco']))
# 2.71

#tobacco range
range = max(df['Tobacco']) - min(df['Tobacco'])
print "Tobacco range is " + str(range)
# 1.8499999999999996

#tobacco variance
df['Tobacco'].var()
print "Tobacco variance is " + str(df['Tobacco'].var()) 
# 0.3489363636363606

#tobacco standard deviation
df['Tobacco'].std()
print "Tobacco standard deviation is " + str(df['Tobacco'].std()) 
# 0.59070835751355388

print "\n" + "*calculate mean, median, mode, range, variance, standard deviation for Alcohol AND Tobacco*\n"


data = '''Alcohol/Tobacco
6.47
4.03
6.13
3.76
6.19
3.77
4.89
3.34
5.63
3.47
4.52
2.92
5.89
3.20
4.79
2.71
5.27
3.53
6.08
4.51
4.02
4.56'''

#split string on the hidden characters that indicate newlines
data = data.split('\n')

#split string into list of strings then use list comprehension
#to make list of lists
data = [i.split(', ') for i in data]

#check data
print "*recreating data without distinct columns*\n"
print data
print "\n"

#create pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

#check data
print "*showing in dataframe*\n"
print df
print "\n"

#convert alcohol/tobacco column to float
df['Alcohol/Tobacco'] = df['Alcohol/Tobacco'].astype(float)

#total mean
print "The mean for Alcohol AND Tobacco is " + str(df['Alcohol/Tobacco'].mean()) + "\n"

#total median
print "The median for Alcohol AND Tobacco is " + str(df['Alcohol/Tobacco'].median()) + "\n"

#total mode
stats.mode(df['Alcohol/Tobacco'])
print "The mode of Alcohol AND Tobacco is " + str(stats.mode(df['Alcohol/Tobacco'])) + "\n"

#total range
range = max(df['Alcohol/Tobacco']) - min(df['Alcohol/Tobacco'])
print "The Alcohol AND Tobacco range is " + str(range) + "\n"

#total variance
df['Alcohol/Tobacco'].var()
print "The Alcohol AND Tobacco variance is " + str(df['Alcohol/Tobacco'].var()) + "\n"

#total standard deviation
df['Alcohol/Tobacco'].std()
print "The Alcohol AND Tobacco standard deviation is " + str(df['Alcohol/Tobacco'].std()) + "\n"

