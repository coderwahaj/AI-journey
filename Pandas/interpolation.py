# Interpolation is the process of estimating unknown data points within the range of a set of known data points.

#    values  interpolated
# 0     1.0           1.0
# 1     2.0           2.0
# 2     NaN           3.0  # Filled linearly between 2 and 4
# 3     4.0           4.0
# 4     5.0           5.0
# 5     NaN           6.0  # Filled between 5 and 7
# 6     7.0           7.0

# linear ,Polynomial,Time
# 1- Perserve Data Integrity
# 2- Smooth Trends
# 3- Avoid Data loss

# Use when time series data,numeric data with trends,avoid dropping  data

import pandas as pd

data = {
    "Time": [1, 2, 3, 4, 5, 6, 7],
    "Values": [10, None, 25, 30, None, None, 75]
}

df = pd.DataFrame(data)
print('Before Interpolation : ' )
print(df)

# Linear interpolation
df['Linear'] = df['Values'].interpolate(method="linear")

# Polynomial interpolation (order 2)
df['Polynomial'] = df['Values'].interpolate(method="polynomial", order=2)

# Time interpolation (requires DatetimeIndex)
df_time = df.copy()
df_time.index = pd.to_datetime(df_time['Time'], unit='D')
df_time['Time_Interp'] = df_time['Values'].interpolate(method="time")

print('After Interpolation :')
print(df_time)