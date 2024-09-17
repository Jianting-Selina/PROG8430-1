import pandas as pd
from IPython.display import display

def read_excel_file(file_path):
    """
    Reads an Excel file into a pandas DataFrame.
    """
    return pd.read_excel(file_path)

def style_dataframe(df):
    """
    Applies basic styling to the DataFrame.
    """
    return df.style.set_table_styles(
            [{'selector': 'thead th',
              'props': [('background-color', '#4CAF50'),  # Green header background
                        ('color', 'white'),  # White text color in headers
                        ('font-weight', 'bold'),  # Bold font in headers
                        ('text-align', 'center')]}]  # Center-align headers
        )

def main():
    file_path = 'News_release_chart_data_August_2024.xlsx'
    df = read_excel_file(file_path)
    styled_df = style_dataframe(df)
    
    return styled_df


