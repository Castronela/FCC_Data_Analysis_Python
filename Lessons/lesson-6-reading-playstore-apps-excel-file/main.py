import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

excel_file = pd.ExcelFile(data_url)
playstore_df = excel_file.parse(usecols=['App', 'Rating', 'Installs', 'Genres', 'Last_Updated'], parse_dates=['Last_Updated'])
playstore_df = playstore_df.sort_values('Rating', ascending=False).head(25)
print(playstore_df)
