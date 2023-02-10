from pandas import *

a = [1, 7, 2]
my_var = Series(a)
print(my_var)

data = {
    "Calories": [10, 50, 60],
    "Duration": [30, 40, 45]
}
print("\n------------------------------------")
df = DataFrame(data)
print(df)
print("\n------------------------------------")

print(df["Calories"])  # => shows only Calories data


print("\n--------------------------------------------")
data_csv = read_csv("./example-eight/df.csv")

data_frame = DataFrame(data_csv)
print(data_frame)

print("\n--------------------------------------------------------------------")
print(data_frame.head())

print("\n--------------------------------------------------------------------")
print(data_frame.tail())

print("\n--------------------------------------------------------------------")
print(data_frame.info())


print("\n--------------------------------------------------------------------")
print(data_frame.describe())

print("\n--------------------------------------------------------------------")
print(data_frame.dropna())

print("\n--------------------------------------------------------------------")
# data_frame["Duration"] = data_frame["Duration"].fillna(130)
# print(data_frame["Duration"])

print("\n--------------------------------------------------------------------")
x = data_frame["Duration"].median()
print("median =>", x)

data_frame["Duration"] = data_frame["Duration"].fillna(
    data_frame["Duration"].median())

# data_frame["Duration"] = data_frame["Duration"].fillna(
#     data_frame["Duration"].mean()) ==> for mean

print(data_frame["Duration"])

print("\n******************************************************************")
data_frame.info()

print("\n******************************************************************")
data_frame["Duration"] = data_frame["Duration"].astype(int)
data_frame.info()

print("\n******************************************************************")
print(data_frame.columns)

print("\n******************************************************************")
data_frame["Date"] = data_frame["Date"].astype("string")
# data_frame["Pulse"] = data_frame["Pulse"].astype(str)
print(data_frame.info())

print("\n******************************************************************")
print(data_frame.loc[:2])  # => not index wise, key can pass like string etc
print("\n******************************************************************")
print(data_frame.iloc[:3])  # => index wise only numerical value

print("\n******************************************************************")
for i in range(len(data_frame)):
    print("\n", data_frame.iloc[i])

print("\n******************************************************************")
print(data_frame.index)

data_frame["Month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

data_frame.index = data_frame["Month"]

print("\n******************************************************************")
for i in range(len(data_frame)):
    print("\n", data_frame.iloc[i])

print("\n\tDuplicate value\n******************************************************************\n")
print(data_frame.duplicated())
