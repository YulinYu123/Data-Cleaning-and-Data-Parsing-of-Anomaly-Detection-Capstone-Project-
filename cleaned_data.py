import pandas as pd

# read the csv file into a dataframe
df = pd.read_csv("2023.04.05-13.34.10.csv")

# the columns we want to keep (important columns)
columns_to_keep = ['System Time', 'System Uptime', 'Disk Size', 'Disk Free', 'Disk Usage', 'Connection Available',
'Heading Target', 'Heading Actual', 'Speed Target', 'Speed Actual', 'Load Mass', 'Load Mass Is Stable',
'Error Count', 'EVMS Error Code', 'EVMS Status Code', 'EVMS Amp Hours Remaining', 'EVMS Battery Voltage',
'EVMS Temperature', 'Battery Percentage', 'Battery Current', 'BMS Detected Cells', 'BMS Detected Modules',
'BMS Lowest Cell', 'BMS Highest Cell', 'BMS Average Cell', 'BMS Highest Temperature', 'BMS Lowest Temperature',
'BMS Average Temperature', 'BMS Module 0 Balance Voltage', 'BMS Module 0 Cell 0', 'BMS Module 0 Cell 1',
'BMS Module 0 Cell 2', 'BMS Module 0 Cell 3', 'BMS Module 0 Cell 4', 'BMS Module 0 Cell 5', 'BMS Module 0 Cell 6',
'BMS Module 0 Cell 7', 'BMS Module 0 Cell 8', 'BMS Module 0 Detected Cells', 'BMS Module 0 Lowest Cell',
'BMS Module 0 Highest Cell', 'BMS Module 0 Average Cell', 'BMS Module 0 Temperature', 'BMS Module 1 Balance Voltage',
'BMS Module 1 Cell 0', 'BMS Module 1 Cell 1', 'BMS Module 1 Cell 2', 'BMS Module 1 Cell 3', 'BMS Module 1 Cell 4',
'BMS Module 1 Cell 5', 'BMS Module 1 Cell 6', 'BMS Module 1 Cell 7', 'BMS Module 1 Cell 8', 'BMS Module 1 Detected Cells',
'BMS Module 1 Lowest Cell', 'BMS Module 1 Highest Cell', 'BMS Module 1 Average Cell', 'BMS Module 1 Temperature',
'BMS Module 2 Balance Voltage', 'BMS Module 2 Cell 0', 'BMS Module 2 Cell 1', 'BMS Module 2 Cell 2',
'BMS Module 2 Cell 3', 'BMS Module 2 Cell 4', 'BMS Module 2 Cell 5', 'BMS Module 2 Cell 6', 'BMS Module 2 Cell 7',
'BMS Module 2 Cell 8', 'BMS Module 2 Detected Cells', 'BMS Module 2 Lowest Cell', 'BMS Module 2 Highest Cell',
'BMS Module 2 Average Cell','BMS Module 2 Temperature','BMS Module 3 Balance Voltage','BMS Module 3 Cell 0',
'BMS Module 3 Cell 1','BMS Module 3 Cell 2','BMS Module 3 Cell 3','BMS Module 3 Cell 4','BMS Module 3 Cell 5',
'BMS Module 3 Cell 6','BMS Module 3 Cell 7','BMS Module 3 Cell 8','BMS Module 3 Detected Cells','BMS Module 3 Lowest Cell',
'BMS Module 3 Highest Cell','BMS Module 3 Average Cell','BMS Module 3 Temperature','BMS Module 4 Balance Voltage',
'BMS Module 4 Cell 0','BMS Module 4 Cell 1','BMS Module 4 Cell 2','BMS Module 4 Cell 3','BMS Module 4 Cell 4',
'BMS Module 4 Cell 5','BMS Module 4 Cell 6','BMS Module 4 Cell 7','BMS Module 4 Cell 8','BMS Module 4 Detected Cells',
'BMS Module 4 Lowest Cell','BMS Module 4 Highest Cell','BMS Module 4 Average Cell','BMS Module 4 Temperature',
'BMS Module 5 Balance Voltage','BMS Module 5 Cell 0','BMS Module 5 Cell 1','BMS Module 5 Cell 2','BMS Module 5 Cell 3',
'BMS Module 5 Cell 4','BMS Module 5 Cell 5','BMS Module 5 Cell 6','BMS Module 5 Cell 7','BMS Module 5 Cell 8',
'BMS Module 5 Detected Cells','BMS Module 5 Lowest Cell','BMS Module 5 Highest Cell','BMS Module 5 Average Cell',
'BMS Module 5 Temperature','BMS Module 6 Balance Voltage','BMS Module 6 Cell 0','BMS Module 6 Cell 1','BMS Module 6 Cell 2',
'BMS Module 6 Cell 3','BMS Module 6 Cell 4','BMS Module 6 Cell 5','BMS Module 6 Cell 6','BMS Module 6 Cell 7','BMS Module 6 Cell 8',
'BMS Module 6 Detected Cells','BMS Module 6 Lowest Cell','BMS Module 6 Highest Cell','BMS Module 6 Average Cell','BMS Module 6 Temperature',
'BMS Module 7 Balance Voltage','BMS Module 7 Cell 0','BMS Module 7 Cell 1','BMS Module 7 Cell 2','BMS Module 7 Cell 3','BMS Module 7 Cell 4',
'BMS Module 7 Cell 5','BMS Module 7 Cell 6','BMS Module 7 Cell 7','BMS Module 7 Cell 8','BMS Module 7 Detected Cells','BMS Module 7 Lowest Cell',
'BMS Module 7 Highest Cell','BMS Module 7 Average Cell','BMS Module 7 Temperature','12V Regulator Voltage','Coolant Temperature','GPS Status',
'GPS Satellites','GPS Latitude','GPS Longitude','GPS Altitude','Accelerometer X','Accelerometer Y','Accelerometer Z','G-Force','Tilt Angle',
'G-Force','Tilt Angle','Addio Hand-Controller Inputs','Addio Input States','Addio Output States','Addio Suspended Outputs','Addio Temperature',
'Addio Hook Current','Addio Pump Current','Addio 12V High-Power Current','Addio 12V Standby Current','Addio 12V Safety Current','Addio Standby Switch Current']

# Create a new DataFrame containing only the important columns
df_filtered = df[columns_to_keep]

# Delete lines containing non-values
df_filtered.dropna(inplace=True)

# Reset the index to ensure that the index is continuous
df_filtered.reset_index(drop=True, inplace=True)

# Print the first 5 lines of the DataFrame
print(df_filtered.head())

# print(df_filtered)

