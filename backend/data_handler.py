import pandas as pd
import requests
from io import StringIO

# --- THESE ARE THE REAL, STABLE LINKS ---
AGRI_DATA_URL = "https://data.gov.in/files/data/csv/Stat-wise_Production_of_Foodgrains_from_2011-12_to_2020-21_%28in_000_tonnes%29.csv"
CLIMATE_DATA_URL = "https://data.gov.in/files/data/csv/Annual_Rainfall_%28State-wise%29_from_2011-2020.csv"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_agriculture_data():
    """
    Fetches and cleans the agriculture production data.
    Now includes headers AND skiprows to fix the tokenizing error.
    """
    print("Fetching Agriculture Data with headers...")
    
    response = requests.get(AGRI_DATA_URL, headers=HEADERS)
    response.raise_for_status()
    
    csv_data = StringIO(response.text)
    
    
    df = pd.read_csv(csv_data, skiprows=3) 
    

    df.rename(columns={"State/UTs": "State"}, inplace=True)
    df_melted = df.melt(id_vars=["State"], var_name="Year", value_name="Production")
    df_melted['Year'] = df_melted['Year'].str.slice(0, 4).astype(int)
    df_melted['Production'] = pd.to_numeric(df_melted['Production'], errors='coerce')
    df_melted.dropna(subset=['Production'], inplace=True)
    
    df_melted['State'] = df_melted['State'].str.strip().str.upper()
    
    print("Loaded and Cleaned Agriculture Data")
    return df_melted, AGRI_DATA_URL


def get_climate_data():
    """
    Fetches and cleans the climate (rainfall) data.
    Now includes headers AND skiprows to fix the tokenizing error.
    """
    print("Fetching Climate Data with headers...")
    
    response = requests.get(CLIMATE_DATA_URL, headers=HEADERS)
    response.raise_for_status()
    
    csv_data = StringIO(response.text)
    

    df = pd.read_csv(csv_data, skiprows=3) 

   
    df.rename(columns={"STATE ": "State"}, inplace=True)
    df_melted = df.melt(id_vars=["State"], var_name="Year", value_name="Rainfall")
    df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')
    df_melted['Rainfall'] = pd.to_numeric(df_melted['Rainfall'], errors='coerce')
    df_melted.dropna(subset=['Rainfall', 'Year'], inplace=True)
    
    df_melted['State'] = df_melted['State'].str.strip().str.upper()
    
    print("Loaded and Cleaned Climate Data")
    return df_melted, CLIMATE_DATA_URL