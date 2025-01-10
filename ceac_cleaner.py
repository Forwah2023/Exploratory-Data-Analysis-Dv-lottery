import pandas as pd
import numpy as np
import os
import re

save_to="ceac_pkl"
folder_name = "downloads"
current_directory = os.getcwd()

year_pattern = re.compile(r"(\d{4})")
#save folder setup
save_folder_path = os.path.join(current_directory,save_to)
# Create the folder if it does not exist
if not os.path.exists(save_folder_path):
    os.makedirs(save_folder_path)
    
full_dir_path = os.path.join(current_directory, folder_name)

# target columns for cleaning
numeric_cols=['Issued','AP','Ready','Refused','Refused221g','NVC'] # Excluded columns ['InTransit','Transfer']

for entry in os.scandir(full_dir_path):
    if entry.name.endswith('.csv') and not entry.name.startswith('.') and entry.is_file():
        ceac=pd.read_csv(entry.path)
        # Reduce memory occuspied by numeric columns, 8 bits instead of 64bits
        if 'Refused221g' in ceac.columns:
            ceac[numeric_cols]=ceac[numeric_cols].astype(np.int8)
        else:
            ceac['Refused221g']=0
            ceac[numeric_cols]=ceac[numeric_cols].astype(np.int8)
        # Category columns
        category_cols=['region','status']
        ceac[category_cols]=ceac[category_cols].astype('category')
        # remove duplicate entries
        ceac.drop_duplicates(inplace=True)
        # Drop unused columns
        ceac.drop(columns=['InTransit','Transfer'], axis=1, inplace=True)
        #Save cleaned df
        year=year_pattern.search(entry.name).group(1)
        save_file_name=os.path.join(save_folder_path ,f'cleaned_Ceac_{year}.pkl')
        ceac.to_pickle(save_file_name)
        print("cleaned:",entry.name)