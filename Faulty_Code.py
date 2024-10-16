import pandas as pd

''' 
Define a funtion - process_faulty_codes.
input_csv is the csv file containing the data to be processed 
and sevon_csv is the csv file containing the fault related information
'''
def process_faulty_codes(input_csv, sevcon_csv):
    # Read the csv file containing the data to be processed and stored it in a DataFrame called the_checked_unit:
    df_the_checked_unit = pd.read_csv(input_csv)

    # Read the csv file containing the fault related information and stored it in a DataFrame called df_faults_information:
    df_faults_information = pd.read_csv(sevcon_csv)

    # Filter out the non-empty and non-zero values in the Sevcon Fault column of the_checked_unit, and stored it in a new DataFrame called filtered_df:
    filtered_df = df_the_checked_unit[(df_the_checked_unit['Sevcon Fault'].notna()) & (df_the_checked_unit['Sevcon Fault'] != 0)]

    # According to the requirement, Converting the decimal Sevcon Fault codes(19907) to hexadecimal(0x4DC3):
    filtered_df.loc[:,'Sevcon Fault'] = filtered_df['Sevcon Fault'].apply(lambda x: f'0x{int(x):X}')

    # Merge filtered_df and df_sevcon_faults Dataframe to a new Dataframe by a left join. 
    # The join is based on the matching relationship between the 'Sevcon Fault' column (from filtered_df) and the 'FID' column (from df_sevcon_faults). 
    # This associates Sevcon Fault codes with Sevcon fault information.
    merged_df = pd.merge(filtered_df, df_faults_information, left_on='Sevcon Fault', right_on='FID', how='left')

    # Extract the columns we need from merged_df DataFrame and return the result:
    result_df = merged_df[['System Time', 'Sevcon Fault', 'Type', 'Message', 'Description', 'Recommended Action']]

    return result_df

# Call the function and pass in the input file and Sevcon file:
result = process_faulty_codes('2023.02.21-01.05.47.csv', 'Sevcon_motor_faults.csv')

# These are just some functions to make sure show all columns and rows for clearer display:
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(result)

