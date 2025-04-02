import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

excel_file = pd.ExcelFile(data_url)
playstore_df = excel_file.parse(sheet_name='Google_playstore', index_col=0)
content_id_df = excel_file.parse(sheet_name='Content_ID', index_col='Content_ID')

print(playstore_df)
print('\n')
print(content_id_df)
