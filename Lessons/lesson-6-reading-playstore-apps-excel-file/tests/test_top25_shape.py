def test_top25_shape(playstore_df):
    assert playstore_df.shape == (25, 5)
