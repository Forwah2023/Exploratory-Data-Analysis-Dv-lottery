# Exploratory Data Analysis Of Dv-lottery.

This project is a collection of scripts and Jupyter notebooks I used in the data preparation and analysis of the CEAC data. The CEAC data is
information about the annual DV-Lottery program run by the U.S governement. This scraped data was obtained from  the website https://dvcharts.xarthisius.xyz/. The results of my analysis and plots are hosted on my personal website. 

## Table of Contents

- Introduction
- Features
- Installation
- Usage
- License

## Introduction

 Every year, the U.S government publishes information on the selectees of the Dv-lottery program for the current fiscal year. This data is 
 regularly scraped and analysed by the owner of https://dvcharts.xarthisius.xyz/. However, I believe there is more to explore about the data 
 that is currenty hosted on that website. This project's objectives are two-fold: first, I wish to document the steps I used in reproducing 
 all the plots hosted on the aforementioned site, and second, to go beyond the exiting plots and provide more insightful details on the data
 using advanced plotting frameworks and graphs. I mainly use Pnadas for data manipulation and Plotly for graphs.

## Features

- Data scraping Python script (*CEAC_data_scraper.py*) for the website https://dvcharts.xarthisius.xyz/. This script captures all the data (CSV), from 2013 
to the current fiscal year.
- Data scraping Python script for the current fiscal year only (*get_latest_CEAC.py*). 
- Python script to transform or format the downloaded CEAC data into an optimized format (*ceac_cleaner.py*)
- Jupyter notebook documenting the cleaning and tranformation of the CEAC data (*Ceac_Cleaning.ipynb*).
-Jupyter notebook documenting the data analysis of the CEAC data for any given year, including plots (*Ceac_2023_analysis_II.ipynb*)

## Installation
- create virtual environment
pip install virtualenv
-activate virtual environment
virtualenv venv
-Install notebook requirements
pip install -r requirements_notebook.txt
-Install scraping requirements
pip install -r requirements_scraping.txt

## Usage
- Open notebook from folder 
jupyter notebook

- Run scraping scripts
python *script_name.py*

## License
 This project is licensed under the GNU General Public License (GPL) - see the LICENSE file for details.

