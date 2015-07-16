########################################################################################################################
#Program: stat01.py
#Project: gitTest
#Author: Josh Taylor, Greylock Mckinnon Associates
#Last Edited: 6/11/2015
########################################################################################################################


import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#path to this file: "C:\Users\jtaylor\Projects\Git\Code\test\stat01.py"

df = pd.read_csv("G:\gitTest\Data\wage.csv")

y = df['wage']
x = df[['educ', 'exper', 'tenure']]

wageReg = sm.OLS(y,x).fit()
print wageReg.summary()

###I want to add more changes to this file###

plt.scatter(df['educ'], df['wage'])
plt.ylabel("Wage in Dollars")
plt.xlabel("Education in Years")
plt.show()

print "Hello World!"

#making a comment