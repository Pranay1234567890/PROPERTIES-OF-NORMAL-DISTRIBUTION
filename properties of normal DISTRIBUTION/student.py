import pandas as pd
import statistics


df = pd.read_csv("StudentsPerformance.csv")
result = df["reading score"].to_list()
mean  = statistics.mean(result)
meadian = statistics.median(result)
mode =statistics.mode(result)
standard = statistics.stdev(result)

print("The mean of the result = " + str(mean))
print("The median of the result  = " + str(meadian))
print("The mode of the result  = " + str(mode))
print("The standard deviation of the result  = {}".format (standard))
standardpositive1 = mean+standard
standardnegative1 = mean-standard
standardpositive2 = mean+(2*standard)
standardnegative2 = mean-(2*standard)
standardpositive3 = mean+(3*standard)
standardnegative3 = mean-(3*standard)

standiv1 = [i for i in result if i<standardpositive1 and i > standardnegative1]
standiv2 = [i for i in result if i<standardpositive2 and i > standardnegative2]
standiv3 = [i for i in result if i<standardpositive3 and i > standardnegative3]
percentage1  = len(standiv1)*100/len(result)
percentage2  = len(standiv2)*100/len(result)
percentage3  = len(standiv3)*100/len(result)
print("{}% of data lies within standiv1".format(percentage1))
print("{}% of data lies within standiv2".format(percentage2))
print("{}% of data lies within standiv3".format(percentage3))