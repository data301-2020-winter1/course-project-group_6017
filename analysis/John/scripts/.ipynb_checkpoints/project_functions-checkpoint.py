import numpy as np
import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    df1 = (pd.read_csv(url_or_path_to_csv_file).dropna()
          .reset_index(drop=True)  
          .rename(columns={" Rocket": "Cost in Millions"})
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(Launch_origin=lambda x: np.where(x['Country of Launch']==x['Companys Country of Origin'], 'true', 'false'))
          .rename(columns={"Launch_origin": "Home Country"})
    )

    # Make sure to return the latest dataframe

    return df2;

