{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "# Method Chain 1 (Load data and deal with missing data)\n",
    "    \n",
    "    import pandas as pd\n",
    "    import numpy as np\n",
    "\n",
    "    df1 = (pd.read_csv('/Users/anastasiachignon/dropbox/course-project-group_6017/data/raw/Global Space Launches.csv').dropna()\n",
    "          .reset_index(drop=True)  \n",
    "          .rename(columns={\" Rocket\": \"Cost of the Rocket in Millions\"})\n",
    "           .sort_values(\"Year\", ascending=True)\n",
    "    )\n",
    "    \n",
    "# Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "    df2 = (\n",
    "          df1\n",
    "          .assign(Launch_origin=lambda x: np.where(x['Country of Launch']==x['Companys Country of Origin'], 1, 0))\n",
    "          .rename(columns={\"Launch_origin\": \"Launch in Same Country of Company origin\"})\n",
    "          .drop(['DateTime','Location'], axis=1)\n",
    "    )\n",
    "    \n",
    "# Make sure to return the latest dataframe\n",
    "\n",
    "    return df2\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
