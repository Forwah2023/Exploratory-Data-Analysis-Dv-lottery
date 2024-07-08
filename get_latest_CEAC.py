from CEAC_data_scraper import download_pdf,download
from datetime import datetime
import os
import urllib.request
from urllib.parse import urljoin

#Get html of recent CEAC page
current_year = datetime.today().strftime("%Y") 
base_url="https://dvcharts.xarthisius.xyz/"
current_url="{}ceacFY{}.html".format(base_url,current_year[-2:])

# get the html page
html=download(current_url)

if html:
    #Define folder parameters
    folder_name = "downloads"
    current_directory = os.getcwd()
    new_folder_path = os.path.join(current_directory, folder_name)
    # Create the folder if it does not exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
             
    # Download recent file
    download_pdf(current_url,html,folder=new_folder_path)
else:
    print("Web page not available")