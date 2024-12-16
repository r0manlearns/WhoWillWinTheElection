import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import urljoin

# Define the base URL
base_url = "https://election.lab.ufl.edu"

# Define the page endpoints
endpoints = [
    "/early-vote/2024-early-voting/2024-general-election-early-vote-alabama/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-alaska/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-arizona/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-arkansas/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-california/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-colorado/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-connecticut/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-delaware/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-district-of-columbia/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-florida/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-georgia/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-hawaii/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-idaho/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-illinois/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-indiana/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-iowa/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-kansas/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-kentucky/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-louisiana/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-maine/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-maryland/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-massachusetts/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-michigan/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-minnesota/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-mississippi/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-missouri/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-montana/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-nebraska/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-nevada/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-new-hampshire/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-new-jersey/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-new-mexico/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-new-york/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-north-carolina/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-north-dakota/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-ohio/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-oklahoma/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-oregon/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-pennsylvania/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-rhode-island/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-south-carolina/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-south-dakota/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-tennessee/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-texas/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-utah/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-vermont/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-virginia/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-washington/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-west-virginia/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-wisconsin/",
    "/early-vote/2024-early-voting/2024-general-election-early-vote-wyoming/",
    "/early-vote/2024-early-voting/",
]

# Define the tabs
tabs = {
    "Total Voted": "us-tab-total",
    "In-Person Early": "us-tab-inperson",
    "Mail Ballots": "us-tab-mailballot"
}

# Directory to save the CSV files
output_dir = r"C:\Users\Admin\OneDrive - Maryville University\Desktop\Data\raw data"
os.makedirs(output_dir, exist_ok=True)

# Function to scrape data from a specific endpoint and tab

def scrape_data(endpoint):
    try:
        response = requests.get(urljoin(base_url, endpoint))
        response.raise_for_status()  # Check for HTTP errors
        print(f"Successfully retrieved {endpoint}")  # Debugging output
    except requests.RequestException as e:
        print(f"Request failed for {endpoint}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the full HTML for inspection
    print(soup.prettify())  # Debugging output to inspect the entire HTML structure

    for tab_name, tab_id in tabs.items():
        # Find the tab content using its ID
        tab_content = soup.find(id=f"us-tab-content-{tab_id.split('-')[-1]}")
        if tab_content:
            print(f"Found content for tab: {tab_name}")  # Debugging output
            # Find all tables within the tab content
            tables = tab_content.find_all("table", class_='table table-sm table-striped')
            if not tables:
                print(f"No tables found for {tab_name} in {endpoint}")  # Debugging output
            for index, table in enumerate(tables):
                # Parse the table header
                header = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]
                # Parse the table rows
                rows = []
                for row in table.find("tbody").find_all("tr"):
                    cells = [td.get_text(strip=True) for td in row.find_all("td")]
                    if cells:
                        rows.append(cells)
                
                if rows:  # Ensure there are rows to create a DataFrame
                    df = pd.DataFrame(rows, columns=header)
                    # Clean filename by replacing special characters
                    filename = f"{endpoint.split('/')[-3]}_{tab_name}_table{index + 1}.csv".replace(' ', '_').replace('/', '_')
                    df.to_csv(os.path.join(output_dir, filename), index=False)
                    print(f"Saved data for {tab_name} from {endpoint}, Table {index + 1}")
                else:
                    print(f"No rows found in table {index + 1} for {tab_name} in {endpoint}")  # Debugging output
        else:
            print(f"No content found for tab: {tab_name} in {endpoint}")  # Debugging output


# Iterate over each endpoint and scrape data
for endpoint in endpoints:
    scrape_data(endpoint)
