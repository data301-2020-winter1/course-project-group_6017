import numpy as np
import pandas as pd

 # Method Chain 1
    
def load_and_process(url_or_path_to_csv_file):
    df1 = (pd.read_csv(url_or_path_to_csv_file).dropna()
          .reset_index(drop=True)  
          .rename(columns={" Rocket": "Cost in Millions of Rocket"})
    )

    # Method Chain 2 

    df2 = (
          df1
          .assign(Launch_origin=lambda x: np.where(x['Country of Launch']==x['Companys Country of Origin'], "True", "False"))
          .rename(columns={"Launch_origin": "Launch in Country of Company"})
          .drop(['DateTime','Location', 'Detail'], axis=1)
    )

    # Return the latest dataframe

    return df2