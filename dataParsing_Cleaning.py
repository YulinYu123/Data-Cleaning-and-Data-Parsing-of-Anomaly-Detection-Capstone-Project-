import pandas as pd

# read the csv file into a dataframe
df = pd.read_csv("2023.04.05-13.34.10.csv")

# the columns we want to keep
columns_to_keep = [
    'System Time', 'System Uptime', 'Disk Size', 'Disk Free', 'Disk Usage', 'Connection Available',
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
    'Addio Hook Current','Addio Pump Current','Addio 12V High-Power Current','Addio 12V Standby Current','Addio 12V Safety Current','Addio Standby Switch Current'
]

# Create a new DataFrame containing only the columns we want to keep
df_filtered = df[columns_to_keep]

# Delete lines containing non-values
df_filtered.dropna(inplace=True)

# Reset the index to ensure that the index is continuous
df_filtered.reset_index(drop=True, inplace=True)

# Create a dictionary for headers
dict_df = df_filtered.to_dict('list')
dict_df_k = dict_df.keys()

# dictionary for the headers
dict_header = dict()
# assign keys and initialise values
dict_header['NameGroup'] = []
dict_header['LengthData'] = len(df_filtered.index)-1
dict_header['NumColumn'] = len(df_filtered.columns)-1

# looping through to assign header values
for keys in dict_df.keys():
    dict_header['NameGroup'].append(keys)

# dictionary for the body data
dict_bodyData = dict()
dict_bodyData['System'] = {}
dict_bodyData['System']['System Time'] = dict_df['System Time']
dict_bodyData['System']['System Uptime'] = dict_df['System Uptime']
dict_bodyData['System']['Disk Size'] = dict_df['Disk Size']
dict_bodyData['System']['Disk Free'] = dict_df['Disk Free']
dict_bodyData['System']['Disk Usage'] = dict_df['Disk Usage']
dict_bodyData['System']['Connection Available'] = dict_df['Connection Available']
dict_bodyData['System']['Heading Target'] = dict_df['Heading Target']
dict_bodyData['System']['Heading Actual'] = dict_df['Heading Actual']
dict_bodyData['System']['Speed Target'] = dict_df['Speed Target']
dict_bodyData['System']['Speed Actual'] = dict_df['Speed Actual']
dict_bodyData['System']['Load Mass'] = dict_df['Load Mass']
dict_bodyData['System']['Load Mass Is Stable'] = dict_df['Load Mass Is Stable']
dict_bodyData['System']['Error Count'] = dict_df['Error Count']

dict_bodyData['EVMS'] = {}
dict_bodyData['EVMS']['EVMS Error Code'] = dict_df['EVMS Error Code']
dict_bodyData['EVMS']['EVMS Status Code'] = dict_df['EVMS Status Code']
dict_bodyData['EVMS']['EVMS Amp Hours Remaining'] = dict_df['EVMS Amp Hours Remaining']
dict_bodyData['EVMS']['EVMS Battery Voltage'] = dict_df['EVMS Battery Voltage']
dict_bodyData['EVMS']['EVMS Temperature'] = dict_df['EVMS Temperature']

dict_bodyData['Battery'] = {}
dict_bodyData['Battery']['Battery Percentage'] = dict_df['Battery Percentage']
dict_bodyData['Battery']['Battery Current'] = dict_df['Battery Current']

dict_bodyData['BMS'] = {}
dict_bodyData['BMS']['BMS Detected Cells'] = dict_df['BMS Detected Cells']
dict_bodyData['BMS']['BMS Detected Modules'] = dict_df['BMS Detected Modules']
dict_bodyData['BMS']['BMS Lowest Cell'] = dict_df['BMS Lowest Cell']
dict_bodyData['BMS']['BMS Highest Cell'] = dict_df['BMS Highest Cell']
dict_bodyData['BMS']['BMS Average Cell'] = dict_df['BMS Average Cell']
dict_bodyData['BMS']['BMS Highest Temperature'] = dict_df['BMS Highest Temperature']
dict_bodyData['BMS']['BMS Lowest Temperature'] = dict_df['BMS Lowest Temperature']
dict_bodyData['BMS']['BMS Average Temperature'] = dict_df['BMS Average Temperature']
dict_bodyData['BMS']['BMS Module 0 Balance Voltage'] = dict_df['BMS Module 0 Balance Voltage']
dict_bodyData['BMS']['BMS Module 0 Cell 0'] = dict_df['BMS Module 0 Cell 0']
dict_bodyData['BMS']['BMS Module 0 Cell 1'] = dict_df['BMS Module 0 Cell 1']
dict_bodyData['BMS']['BMS Module 0 Cell 2'] = dict_df['BMS Module 0 Cell 2']
dict_bodyData['BMS']['BMS Module 0 Cell 3'] = dict_df['BMS Module 0 Cell 3']
dict_bodyData['BMS']['BMS Module 0 Cell 4'] = dict_df['BMS Module 0 Cell 4']
dict_bodyData['BMS']['BMS Module 0 Cell 5'] = dict_df['BMS Module 0 Cell 5']
dict_bodyData['BMS']['BMS Module 0 Cell 6'] = dict_df['BMS Module 0 Cell 6']
dict_bodyData['BMS']['BMS Module 0 Cell 7'] = dict_df['BMS Module 0 Cell 7']
dict_bodyData['BMS']['BMS Module 0 Cell 8'] = dict_df['BMS Module 0 Cell 8']
dict_bodyData['BMS']['BMS Module 0 Detected Cells'] = dict_df['BMS Module 0 Detected Cells']
dict_bodyData['BMS']['BMS Module 0 Lowest Cell'] = dict_df['BMS Module 0 Lowest Cell']
dict_bodyData['BMS']['BMS Module 0 Highest Cell'] = dict_df['BMS Module 0 Highest Cell']
dict_bodyData['BMS']['BMS Module 0 Average Cell'] = dict_df['BMS Module 0 Average Cell']
dict_bodyData['BMS']['BMS Module 0 Temperature'] = dict_df['BMS Module 0 Temperature']
dict_bodyData['BMS']['BMS Module 1 Balance Voltage'] = dict_df['BMS Module 1 Balance Voltage']
dict_bodyData['BMS']['BMS Module 1 Cell 0'] = dict_df['BMS Module 1 Cell 0']
dict_bodyData['BMS']['BMS Module 1 Cell 1'] = dict_df['BMS Module 1 Cell 1']
dict_bodyData['BMS']['BMS Module 1 Cell 2'] = dict_df['BMS Module 1 Cell 2']
dict_bodyData['BMS']['BMS Module 1 Cell 3'] = dict_df['BMS Module 1 Cell 3']
dict_bodyData['BMS']['BMS Module 1 Cell 4'] = dict_df['BMS Module 1 Cell 4']
dict_bodyData['BMS']['BMS Module 1 Cell 5'] = dict_df['BMS Module 1 Cell 5']
dict_bodyData['BMS']['BMS Module 1 Cell 6'] = dict_df['BMS Module 1 Cell 6']
dict_bodyData['BMS']['BMS Module 1 Cell 7'] = dict_df['BMS Module 1 Cell 7']
dict_bodyData['BMS']['BMS Module 1 Cell 8'] = dict_df['BMS Module 1 Cell 8']
dict_bodyData['BMS']['BMS Module 1 Detected Cells'] = dict_df['BMS Module 1 Detected Cells']
dict_bodyData['BMS']['BMS Module 1 Lowest Cell'] = dict_df['BMS Module 1 Lowest Cell']
dict_bodyData['BMS']['BMS Module 1 Highest Cell'] = dict_df['BMS Module 1 Highest Cell']
dict_bodyData['BMS']['BMS Module 1 Average Cell'] = dict_df['BMS Module 1 Average Cell']
dict_bodyData['BMS']['BMS Module 1 Temperature'] = dict_df['BMS Module 1 Temperature']
dict_bodyData['BMS']['BMS Module 2 Balance Voltage'] = dict_df['BMS Module 2 Balance Voltage']
dict_bodyData['BMS']['BMS Module 2 Cell 0'] = dict_df['BMS Module 2 Cell 0']
dict_bodyData['BMS']['BMS Module 2 Cell 1'] = dict_df['BMS Module 2 Cell 1']
dict_bodyData['BMS']['BMS Module 2 Cell 2'] = dict_df['BMS Module 2 Cell 2']
dict_bodyData['BMS']['BMS Module 2 Cell 3'] = dict_df['BMS Module 2 Cell 3']
dict_bodyData['BMS']['BMS Module 2 Cell 4'] = dict_df['BMS Module 2 Cell 4']
dict_bodyData['BMS']['BMS Module 2 Cell 5'] = dict_df['BMS Module 2 Cell 5']
dict_bodyData['BMS']['BMS Module 2 Cell 6'] = dict_df['BMS Module 2 Cell 6']
dict_bodyData['BMS']['BMS Module 2 Cell 7'] = dict_df['BMS Module 2 Cell 7']
dict_bodyData['BMS']['BMS Module 2 Cell 8'] = dict_df['BMS Module 2 Cell 8']
dict_bodyData['BMS']['BMS Module 2 Detected Cells'] = dict_df['BMS Module 2 Detected Cells']
dict_bodyData['BMS']['BMS Module 2 Detected Cells'] = dict_df['BMS Module 2 Detected Cells']
dict_bodyData['BMS']['BMS Module 2 Lowest Cell'] = dict_df['BMS Module 2 Lowest Cell']
dict_bodyData['BMS']['BMS Module 2 Highest Cell'] = dict_df['BMS Module 2 Highest Cell']
dict_bodyData['BMS']['BMS Module 2 Average Cell'] = dict_df['BMS Module 2 Average Cell']
dict_bodyData['BMS']['BMS Module 2 Temperature'] = dict_df['BMS Module 2 Temperature']
dict_bodyData['BMS']['BMS Module 3 Balance Voltage'] = dict_df['BMS Module 3 Balance Voltage']
dict_bodyData['BMS']['BMS Module 3 Cell 0'] = dict_df['BMS Module 3 Cell 0']
dict_bodyData['BMS']['BMS Module 3 Cell 1'] = dict_df['BMS Module 3 Cell 1']
dict_bodyData['BMS']['BMS Module 3 Cell 2'] = dict_df['BMS Module 3 Cell 2']
dict_bodyData['BMS']['BMS Module 3 Cell 3'] = dict_df['BMS Module 3 Cell 3']
dict_bodyData['BMS']['BMS Module 3 Cell 4'] = dict_df['BMS Module 3 Cell 4']
dict_bodyData['BMS']['BMS Module 3 Cell 5'] = dict_df['BMS Module 3 Cell 5']
dict_bodyData['BMS']['BMS Module 3 Cell 6'] = dict_df['BMS Module 3 Cell 6']
dict_bodyData['BMS']['BMS Module 3 Cell 7'] = dict_df['BMS Module 3 Cell 7']
dict_bodyData['BMS']['BMS Module 3 Cell 8'] = dict_df['BMS Module 3 Cell 8']
dict_bodyData['BMS']['BMS Module 3 Detected Cells'] = dict_df['BMS Module 3 Detected Cells']
dict_bodyData['BMS']['BMS Module 3 Lowest Cell'] = dict_df['BMS Module 3 Lowest Cell']
dict_bodyData['BMS']['BMS Module 3 Highest Cell'] = dict_df['BMS Module 3 Highest Cell']
dict_bodyData['BMS']['BMS Module 3 Average Cell'] = dict_df['BMS Module 3 Average Cell']
dict_bodyData['BMS']['BMS Module 3 Temperature'] = dict_df['BMS Module 3 Temperature']
dict_bodyData['BMS']['BMS Module 4 Balance Voltage'] = dict_df['BMS Module 4 Balance Voltage']
dict_bodyData['BMS']['BMS Module 4 Cell 0'] = dict_df['BMS Module 4 Cell 0']
dict_bodyData['BMS']['BMS Module 4 Cell 1'] = dict_df['BMS Module 4 Cell 1']
dict_bodyData['BMS']['BMS Module 4 Cell 2'] = dict_df['BMS Module 4 Cell 2']
dict_bodyData['BMS']['BMS Module 4 Cell 3'] = dict_df['BMS Module 4 Cell 3']
dict_bodyData['BMS']['BMS Module 4 Cell 4'] = dict_df['BMS Module 4 Cell 4']
dict_bodyData['BMS']['BMS Module 4 Cell 5'] = dict_df['BMS Module 4 Cell 5']
dict_bodyData['BMS']['BMS Module 4 Cell 6'] = dict_df['BMS Module 4 Cell 6']
dict_bodyData['BMS']['BMS Module 4 Cell 7'] = dict_df['BMS Module 4 Cell 7']
dict_bodyData['BMS']['BMS Module 4 Cell 8'] = dict_df['BMS Module 4 Cell 8']
dict_bodyData['BMS']['BMS Module 4 Detected Cells'] = dict_df['BMS Module 4 Detected Cells']
dict_bodyData['BMS']['BMS Module 4 Lowest Cell'] = dict_df['BMS Module 4 Lowest Cell']
dict_bodyData['BMS']['BMS Module 4 Highest Cell'] = dict_df['BMS Module 4 Highest Cell']
dict_bodyData['BMS']['BMS Module 4 Average Cell'] = dict_df['BMS Module 4 Average Cell']
dict_bodyData['BMS']['BMS Module 4 Temperature'] = dict_df['BMS Module 4 Temperature']
dict_bodyData['BMS']['BMS Module 5 Balance Voltage'] = dict_df['BMS Module 5 Balance Voltage']
dict_bodyData['BMS']['BMS Module 5 Cell 0'] = dict_df['BMS Module 5 Cell 0']
dict_bodyData['BMS']['BMS Module 5 Cell 1'] = dict_df['BMS Module 5 Cell 1']
dict_bodyData['BMS']['BMS Module 5 Cell 2'] = dict_df['BMS Module 5 Cell 2']
dict_bodyData['BMS']['BMS Module 5 Cell 3'] = dict_df['BMS Module 5 Cell 3']
dict_bodyData['BMS']['BMS Module 5 Cell 4'] = dict_df['BMS Module 5 Cell 4']
dict_bodyData['BMS']['BMS Module 5 Cell 5'] = dict_df['BMS Module 5 Cell 5']
dict_bodyData['BMS']['BMS Module 5 Cell 6'] = dict_df['BMS Module 5 Cell 6']
dict_bodyData['BMS']['BMS Module 5 Cell 7'] = dict_df['BMS Module 5 Cell 7']
dict_bodyData['BMS']['BMS Module 5 Cell 8'] = dict_df['BMS Module 5 Cell 8']
dict_bodyData['BMS']['BMS Module 5 Detected Cells'] = dict_df['BMS Module 5 Detected Cells']
dict_bodyData['BMS']['BMS Module 5 Lowest Cell'] = dict_df['BMS Module 5 Lowest Cell']
dict_bodyData['BMS']['BMS Module 5 Highest Cell'] = dict_df['BMS Module 5 Highest Cell']
dict_bodyData['BMS']['BMS Module 5 Average Cell'] = dict_df['BMS Module 5 Average Cell']
dict_bodyData['BMS']['BMS Module 5 Temperature'] = dict_df['BMS Module 5 Temperature']
dict_bodyData['BMS']['BMS Module 6 Balance Voltage'] = dict_df['BMS Module 6 Balance Voltage']
dict_bodyData['BMS']['BMS Module 6 Cell 0'] = dict_df['BMS Module 6 Cell 0']
dict_bodyData['BMS']['BMS Module 6 Cell 1'] = dict_df['BMS Module 6 Cell 1']
dict_bodyData['BMS']['BMS Module 6 Cell 2'] = dict_df['BMS Module 6 Cell 2']
dict_bodyData['BMS']['BMS Module 6 Cell 3'] = dict_df['BMS Module 6 Cell 3']
dict_bodyData['BMS']['BMS Module 6 Cell 4'] = dict_df['BMS Module 6 Cell 4']
dict_bodyData['BMS']['BMS Module 6 Cell 5'] = dict_df['BMS Module 6 Cell 5']
dict_bodyData['BMS']['BMS Module 6 Cell 6'] = dict_df['BMS Module 6 Cell 6']
dict_bodyData['BMS']['BMS Module 6 Cell 7'] = dict_df['BMS Module 6 Cell 7']
dict_bodyData['BMS']['BMS Module 6 Cell 8'] = dict_df['BMS Module 6 Cell 8']
dict_bodyData['BMS']['BMS Module 6 Detected Cells'] = dict_df['BMS Module 6 Detected Cells']
dict_bodyData['BMS']['BMS Module 6 Lowest Cell'] = dict_df['BMS Module 6 Lowest Cell']
dict_bodyData['BMS']['BMS Module 6 Highest Cell'] = dict_df['BMS Module 6 Highest Cell']
dict_bodyData['BMS']['BMS Module 6 Average Cell'] = dict_df['BMS Module 6 Average Cell']
dict_bodyData['BMS']['BMS Module 6 Temperature'] = dict_df['BMS Module 6 Temperature']
dict_bodyData['BMS']['BMS Module 7 Balance Voltage'] = dict_df['BMS Module 7 Balance Voltage']
dict_bodyData['BMS']['BMS Module 7 Cell 0'] = dict_df['BMS Module 7 Cell 0']
dict_bodyData['BMS']['BMS Module 7 Cell 1'] = dict_df['BMS Module 7 Cell 1']
dict_bodyData['BMS']['BMS Module 7 Cell 2'] = dict_df['BMS Module 7 Cell 2']
dict_bodyData['BMS']['BMS Module 7 Cell 3'] = dict_df['BMS Module 7 Cell 3']
dict_bodyData['BMS']['BMS Module 7 Cell 4'] = dict_df['BMS Module 7 Cell 4']
dict_bodyData['BMS']['BMS Module 7 Cell 5'] = dict_df['BMS Module 7 Cell 5']
dict_bodyData['BMS']['BMS Module 7 Cell 6'] = dict_df['BMS Module 7 Cell 6']
dict_bodyData['BMS']['BMS Module 7 Cell 7'] = dict_df['BMS Module 7 Cell 7']
dict_bodyData['BMS']['BMS Module 7 Cell 8'] = dict_df['BMS Module 7 Cell 8']
dict_bodyData['BMS']['BMS Module 7 Detected Cells'] = dict_df['BMS Module 7 Detected Cells']
dict_bodyData['BMS']['BMS Module 7 Lowest Cell'] = dict_df['BMS Module 7 Lowest Cell']
dict_bodyData['BMS']['BMS Module 7 Highest Cell'] = dict_df['BMS Module 7 Highest Cell']
dict_bodyData['BMS']['BMS Module 7 Average Cell'] = dict_df['BMS Module 7 Average Cell']
dict_bodyData['BMS']['BMS Module 7 Temperature'] = dict_df['BMS Module 7 Temperature']
                                                   
dict_bodyData['Voltage and Temperature'] = {}
dict_bodyData['Voltage and Temperature']['12V Regulator Voltage'] = dict_df['12V Regulator Voltage']
dict_bodyData['Voltage and Temperature']['Coolant Temperature'] = dict_df['Coolant Temperature']

dict_bodyData['GPS'] = {}
dict_bodyData['GPS']['GPS Status'] = dict_df['GPS Status']
dict_bodyData['GPS']['GPS Satellites'] = dict_df['GPS Satellites']
dict_bodyData['GPS']['GPS Latitude'] = dict_df['GPS Latitude']
dict_bodyData['GPS']['GPS Longitude'] = dict_df['GPS Longitude']
dict_bodyData['GPS']['GPS Altitude'] = dict_df['GPS Altitude']

dict_bodyData['Accelerometer'] = {}
dict_bodyData['Accelerometer']['Accelerometer X'] = dict_df['Accelerometer X']
dict_bodyData['Accelerometer']['Accelerometer Y'] = dict_df['Accelerometer Y']
dict_bodyData['Accelerometer']['Accelerometer Z'] = dict_df['Accelerometer Z']

dict_bodyData['G-Force and Tilt Angle'] = {}
dict_bodyData['G-Force and Tilt Angle']['G-Force'] = dict_df['G-Force']
dict_bodyData['G-Force and Tilt Angle']['Tilt Angle'] = dict_df['Tilt Angle']
dict_bodyData['G-Force and Tilt Angle']['G-Force'] = dict_df['G-Force']
dict_bodyData['G-Force and Tilt Angle']['Tilt Angle'] = dict_df['Tilt Angle']

dict_bodyData['Addio'] = {}
dict_bodyData['Addio']['Addio Hand-Controller Inputs'] = dict_df['Addio Hand-Controller Inputs']
dict_bodyData['Addio']['Addio Input States'] = dict_df['Addio Input States']
dict_bodyData['Addio']['Addio Output States'] = dict_df['Addio Output States']
dict_bodyData['Addio']['Addio Suspended Outputs'] = dict_df['Addio Suspended Outputs']
dict_bodyData['Addio']['Addio Temperature'] = dict_df['Addio Temperature']
dict_bodyData['Addio']['Addio Hook Current'] = dict_df['Addio Hook Current']
dict_bodyData['Addio']['Addio Pump Current'] = dict_df['Addio Pump Current']
dict_bodyData['Addio']['Addio 12V High-Power Current'] = dict_df['Addio 12V High-Power Current']
dict_bodyData['Addio']['Addio 12V Standby Current'] = dict_df['Addio 12V Standby Current']
dict_bodyData['Addio']['Addio 12V Safety Current'] = dict_df['Addio 12V Safety Current']
dict_bodyData['Addio']['Addio Standby Switch Current'] = dict_df['Addio Standby Switch Current']

print(dict_bodyData)