import pandas as pd

excel_file = 'Customer.xlsx'


def open_excel(filename):
    df = pd.read_excel(filename)
    return df


def split_data(raw_data):
    df_processed = pd.DataFrame(raw_data)
    headers = list(df_processed.columns.values)
    customer_list = df_processed['Customer'].unique()

    for index, row in df_processed.iterrows():
        for i in customer_list:
            df_edit = pd.DataFrame(row)
            df_transposed = df_edit.T
            df_transposed.to_excel(f'Output_Customer_{i}.xlsx', index=False, columns=headers)


customer_data = open_excel(excel_file)
split_data(customer_data)

