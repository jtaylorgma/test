#######################################################################
#Program: stat01.R
#Project: gitTest
#Author: Josh Taylor, Greylock McKinnon Associates
#Last Edited: 6/10/15
#######################################################################


wage <- read.csv("G:/gitTest/Data/wage.csv")

wageReg = lm(wage ~ educ + exper + tenure, data = wage)
summary(wageReg)