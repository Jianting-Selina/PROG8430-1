import pandas as pd

class ExcelDataFrameStyler:
    def __init__(self, file_path):
        """
        Initializes the ExcelDataFrameStyler with the path to the Excel file.
        """
        self.file_path = file_path
        self.df = self.read_excel_file()
    
    def read_excel_file(self):
        """
        Reads the Excel file into a pandas DataFrame.
        """
        return pd.read_excel(self.file_path)
    
    def style_dataframe(self):
        """
        Applies basic styling to the DataFrame.
        """
        return self.df.style\
            .set_table_styles(
                [{'selector': 'thead th',
                  'props': [('background-color', '#4CAF50'),  # Green header background
                            ('color', 'white'),  # White text color in headers
                            ('font-weight', 'bold'),  # Bold font in headers
                            ('text-align', 'center')]}]  # Center-align headers
            )
    
    def display_styled_dataframe(self):
        """
        Displays the styled DataFrame.
        """
        styled_df = self.style_dataframe()
        return styled_df

def main():
    file_path = 'News_release_chart_data_August_2024.xlsx'
    styler = ExcelDataFrameStyler(file_path)
    styled_df = styler.display_styled_dataframe()
    
    # Display the styled DataFrame in Jupyter
    return styled_df

