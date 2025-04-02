import numpy as np
def test_last_updated_datetime(playstore_df):
    assert playstore_df['Last_Updated'].dtype == np.dtype('<datetime64[ns]')
