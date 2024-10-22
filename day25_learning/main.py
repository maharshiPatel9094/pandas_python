import pandas as pd
 
data = pd.read_csv("./weather_data.csv")
print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)














# import csv
# with open("./weather_data.csv") as data:
#     data = csv.reader(data)
#     print(data)
#     for row in data:
#         print(row)





# with open("./weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

