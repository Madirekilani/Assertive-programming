 def assert_df_dimensions_equal(df,height, width):
    """
     Asserts that the dimensions (number of rows and columns) of a DataFrame match the specifiied height and width.

     Parameters:
        df (DataFrame): The DataFrame to be checked.
        height (int): The expected number of rows.
        width (int): The expected number of columns.
    """
     assert len(df) == height and len(df.columns) == width, f"DataFrame dimensions do not match. Expected ({height}, {width}), got ({len(df)}, {len(df.columns)})"
 
 def assert_df_columns_equal(df, column_names):
    """
    Asserts that the column names of a DataFrame match the specified list of column names.

    Parameters:
        df (DataFrame): The DataFrame to be checked.
        column_names (list): The expected list of column names.
    """
    assert list(df.columns) == column_names, f"DataFrame column names do not match. Expected {column_names}, got {list(df.columns)}"
 
 def assert_no_duplicate_rows(df):  
    """
    Asserts that there are no duplicate rows in a DataFrame.

    Parameters:
        df (DataFrame): The DataFrame to be checked.
    """
    assert len(df) == len(df.drop_duplicates()), "Duplicate rows found in DataFrame"

def assert_no_null_values (df):
    """
    Asserts that there are no null (NaN) values in a DataFrame.
    
    Parameteres:
        df (DataFrame): The DataFrame to be checked.
    """
    assert not df.isnull().values.any(), "Null values found in DataFrame"

def assert_all_values_positive(df):
    """
     Asserts that all values in a DataFrame are positive.

     Parameters:
        df (Dataframe): The DataFrame to be checked.
     """
     assert (df >= 0).all().all(), "Negative values found in DataFrame" 