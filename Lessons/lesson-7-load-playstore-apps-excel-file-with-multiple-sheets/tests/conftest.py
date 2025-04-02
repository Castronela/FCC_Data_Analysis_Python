import pytest
import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

excel_file = pd.ExcelFile(data_url)

@pytest.fixture
def playstore_df():
	return excel_file.parse(sheet_name='Google_playstore', index_col=0)
@pytest.fixture
def content_id_df():
	return excel_file.parse(sheet_name='Content_ID', index_col='Content_ID')

