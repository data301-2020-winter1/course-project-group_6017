def load_and_process(url_or_path_to_csv_file):
    
    # Method Chain 1 (Load data and deal with missing data)  
    import numpy as np
    import pandas as pd

    df1 = (pd.read_csv(url_or_path_to_csv_file).dropna()
          .reset_index(drop=True)  
          .rename(columns={" Rocket": "Cost in Millions"})
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(Launch_origin=lambda x: np.where(x['Country of Launch']==x['Companys Country of Origin'], 1, 0))
          .rename(columns={"Launch_origin": "Launch in Country of Company"})
          .drop(['DateTime','Location'], axis=1)
    )

    # Make sure to return the latest dataframe

    return df2 