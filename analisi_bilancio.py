import numpy as np

#Data 
monthlyRevenues = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
monthlyExpenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#Lists
monthlyProfit = [] #monthlyProfit = list([])
taxes = []
profitAfterTaxes = []
monthlyProfitMargin = []
bestMonthlyProfits = []
worstMonthlyProfits = []
bestProfit = []
worstProfit = []

#Profit
for i in range(0, len(monthlyRevenues)):
    monthlyProfit.append(monthlyRevenues[i] - monthlyExpenses[i])

#Taxes
taxes = [round((i * 30)/100, 2) for i in monthlyProfit]

#Profit after Taxes
for i in range(0, len(monthlyProfit)):
    profitAfterTaxes.append(monthlyProfit[i] - taxes[i])

#Monthly Profit Margin
for i in range(0, len(profitAfterTaxes)):
    monthlyProfitMargin.append(round(profitAfterTaxes[i]/monthlyRevenues[i]*100,2))

#Mean, best and worst profits
meanProfitForYear = np.mean(profitAfterTaxes)
bestMonthlyProfits = [ i > meanProfitForYear for i in profitAfterTaxes]
worstMonthlyProfits = [ i < meanProfitForYear for i in profitAfterTaxes]

#Best and worst profit
bestProfit = [i == max(profitAfterTaxes) for i in profitAfterTaxes]
worstProfit = [ i == min(profitAfterTaxes) for i in profitAfterTaxes]

revenuesRounded1000 = [int(round(i/1000, 2)) for i in monthlyRevenues]
expensesRounded1000 = [int(round(i/1000, 2)) for i in monthlyExpenses]
monthlyProfitRounded1000 = [int(round(i/1000, 2)) for i in monthlyProfit]
profitAfterTaxesRounded1000 = [int(round(i/1000, 2)) for i in profitAfterTaxes]

print("Revenues:\n", revenuesRounded1000)
print("Expenses:\n", expensesRounded1000)
print("Monthly Profits:\n", monthlyProfitRounded1000)
print("Taxes:\n", taxes)
print("Profits After Taxes:\n", profitAfterTaxesRounded1000)
print("Profit Margin:\n:", monthlyProfitMargin)
print("Best monthly profits:\n", bestMonthlyProfits)
print("Worst monthly profits:\n", worstMonthlyProfits)
print("Best Profit:\n", bestProfit)
print("Worst Profit:\n", worstProfit)


