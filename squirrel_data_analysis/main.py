import pandas as pd

data = pd.read_csv(r"C:\Users\mahar\OneDrive\Documents\GitHub\pandas_python\squirrel_data_analysis\data.csv")
# print(data)

# fur color coloumn
fur_coloumn = data["Primary Fur Color"]
# print(fur_coloumn)
gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
black_fur_count = len(data[data["Primary Fur Color"] == "Black"])
red_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

# construct the dataframe
data_dict = {
    "Fur color": ["Gray","Cinnamon","Black"],
    "count": [gray_fur_count,red_fur_count,black_fur_count]
}

squirrel_df = pd.DataFrame(data_dict)
squirrel_df.to_csv(r"C:\Users\mahar\OneDrive\Documents\GitHub\pandas_python\squirrel_data_analysis\squirrel_count.csv")
# print(gray_fur_count)
# print(black_fur_count)
# print(red_fur_count)
