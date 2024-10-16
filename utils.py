import pandas as pd

# Function to process the CSV data before displaying and before downloading
def process_csv_data(df):
    # 1. Remove the column "Custom text"
    if 'Custom text' in df.columns:
        df.drop(columns=['Custom text'], inplace=True)

    # 2. Remove quotation marks from strings in the DataFrame
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)

    # 3. Add a new column 'Parcel Size' and populate it with the value 'Parcel'
    df['Parcel Size'] = 'Parcel'

    # 4. Modify the 'Delivery method' column
    if 'Delivery method' in df.columns:
        df['Delivery method'] = df['Delivery method'].replace({
            'Tracked 48': '2 - 4 Business Days',
            'Tracked 24': 'Next Day - Tracked 24'
        })

    # 5. Add a new column 'Service Code' and populate based on 'Delivery method'
    if 'Delivery method' in df.columns:
        df['Service Code'] = df['Delivery method'].map({
            '2 - 4 Business Days': 'TPS48',
            'Next Day - Tracked 24': 'TPN24'
        }).fillna('')  # Fill NaN values with an empty string


    if 'Delivery zip/postal code' in df.columns:
        df.rename(columns={'Delivery zip/postal code': 'Delivery ZIP/postal code'}, inplace=True)

    return df

def adjust_all_columns_to_string(df):
    # Replace NaN values with empty strings
    df = df.where(pd.notnull(df), '')
    # Convert all columns to string
    return df.astype(str)


# Function to convert DataFrame to CSV
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')
