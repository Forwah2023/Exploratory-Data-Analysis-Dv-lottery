# Exploratory Data Analysis Of Dv-lottery data.

This project is a collection of scripts and Jupyter notebooks I used to prepare and analyse the CEAC data. The CEAC data is
information about the annual DV-Lottery program the U.S. government runs. This scraped data was obtained from  the website https://dvcharts.xarthisius.xyz/. The results of my analysis and plots are hosted on my website. 

## Table of Contents

- Introduction
- Features
- Installation
- Usage
- License

## Introduction

 Every year, the U.S. government publishes information on the selectees of the Dv-lottery program for the current fiscal year. This data is 
 regularly scraped and analysed by the owner of https://dvcharts.xarthisius.xyz/. However, I believe there is more to explore about the data 
 that is currently hosted on that website. This project's objectives are two-fold: first, I wish to document the steps I used in reproducing 
 all the plots hosted on the site mentioned above, and second, to go beyond the existing plots and provide more insightful details on the data
 using advanced plotting frameworks and graphs. I mainly use Pnadas for data manipulation and Plotly for graphs.

## Features

- Data scraping Python script (*CEAC_data_scraper.py*) for the website https://dvcharts.xarthisius.xyz/. This script captures all the data (CSV), from the year 2013 
to the current fiscal year.
- Data scraping Python script for the current fiscal year only (*get_latest_CEAC.py*). 
- Python script to transform or format the downloaded CEAC data into an optimized format (*ceac_cleaner.py*)
- Jupyter notebook documenting the cleaning and transformation of the CEAC data (*Ceac_Cleaning.ipynb*).
-Jupyter notebook documenting the data analysis of the CEAC data for any given year, including plots (*Ceac_2023_analysis_II.ipynb*)
- Geo-data (ISO codes) of the participating embassies in  the DV-Lottery stored at *examples/ISO_ALPHA.csv*, and required to generate the choropleth plot in *Ceac_2023_analysis_II.ipynb*.
- Jupyter notebook documenting the steps required to generate a summary of the CEAC data from the year 2013 to the present year, containing key KPIs. (*Historical_CEAC_analysis.ipynb*)
-Jupyter notebook documenting the steps required to generate an area plot showing the relative distribution of status across case numbers per region. (*preparing_area_region_chart.ipynb*).
-Jupyter notebook documenting the steps required to generate an area plot showing the relative distribution of status across case numbers per consulate (*preparing_embassy_case_area_plot.ipynb*).
-Jupyter notebook documenting the steps required to generate a bar chart showing the proportion of issued visas to cases for each consulate (*preparing_embassy_bar_chart.ipynb*).
-Jupyter notebook documenting the steps required to generate a bar chart showing the relative distribution of various statuses between regions. (*preparing_regional_bar_graph.ipynb*).
-Jupyter notebook documenting the steps required to generate a choropleth chart showing the relative distribution of derivatives (accompanying cases) between regions. (*preparing_global_derivative_chart.ipynb*).
-Jupyter notebook documenting the steps required to generate a bar chart showing the relative distribution of holes (disqualified cases) between regions. (*preparing_regional_holes_graph.ipynb*).

## Installation
- Install a virtual environment manager:
  `pip install virtualenv`
- Create and activate the virtual environment:
 `virtualenv venv`
- Install notebook requirements:
  `pip install -r requirements_notebook.txt`
- Install scraping requirements:
 `pip install -r requirements_scraping.txt`

## Usage
- Open notebook from folder 
jupyter notebook
- The folder *examples* contains sample unprocessed CSV and pickle files; the latter was obtained from cleaning the former.

- Run scraping scripts
python *script_name.py*
The downloaded CEAC data will be saved to the *downloads* folder created at runtime while the cleaned CSV files will be stored to the *ceac_pkl* folder.

## License
 This project is licensed under the GNU General Public License (GPL) - see the LICENSE file for details.

