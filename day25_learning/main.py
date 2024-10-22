import pandas as pd 

# Reading the CSV file with an explicit header
try:
    data = pd.read_csv(r"C:\Users\mahar\OneDrive\Documents\GitHub\pandas_python\day25_learning\weather_data.csv", header=0)  # Ensure first row is header
    # print("DataFrame contents:\n", data)  # Print the entire DataFrame
except FileNotFoundError:
    print("File not found. Check the path.")



# creating a dataframe from scratch
data_dict = {
    "students" : ["Amy","james","angela"],
    "scores" : [76,56,65]
}

data_student = pd.DataFrame(data_dict)
# print(data_student)
# creating a new csv file
data_student.to_csv(r"C:\Users\mahar\OneDrive\Documents\GitHub\pandas_python\day25_learning\new_data.csv")






# data_dict = data.to_dict()
# # print(data_dict)


# # getting data in row
# days = data[data.day == "Monday"]
# # print(days)

# # get the row with maximum temperature
# max_row_temp = data[data.temp == data.temp.max()]
# # print(max_row_temp )
# # we can also get access to this row
# # print(max_row_temp.temp * 9/5 + 32)



# # series is a coloumn 
# # data_temp = data["temp"]
# # data_temp = data.temp
# data_temp_list = data.temp.to_list()
# # print(data_temp_list)

# # -----max
# max_temp = data.temp.max()
# # print(max_temp)
# # ---------------avg
# # print(data.temp.mean())

# # -----------avg
# # total = 0
# # for temp in data_temp_list:
# #     total += temp
# # print(f"average  temperature is: {total/len(data_temp_list)}")