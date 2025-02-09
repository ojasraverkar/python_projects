import requests
import time
import pandas as pd

# Read all districts from the text file. Each line should contain one district name.
with open("all_districts_india.txt", "r", encoding="utf-8") as f:
    districts = [line.strip() for line in f if line.strip()]

results = []

# Loop over each district and query the Nominatim API.
for district in districts:
    # Build the query string: district name plus ", India" to focus the search.
    query = f"{district}, India"
    params = {
        "q": query,
        "format": "json",
        "limit": 1  # Only take the top result
    }
    headers = {
        "User-Agent": "AllDistrictsCSVGenerator/1.0 (your_email@example.com)"  # Replace with your contact info
    }
    
    try:
        response = requests.get("https://nominatim.openstreetmap.org/search", params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        if data:
            lat = data[0].get("lat", None)
            lon = data[0].get("lon", None)
            print(f"Found {district}: lat {lat}, lon {lon}")
        else:
            print(f"No data found for {district}")
            lat, lon = None, None
    except Exception as e:
        print(f"Error retrieving data for {district}: {e}")
        lat, lon = None, None

    results.append({
        "District": district,
        "Latitude": lat,
        "Longitude": lon
    })
    
    # Pause for 1 second to respect Nominatim's usage policy.
    time.sleep(1)

# Convert the results to a DataFrame and save to a CSV file.
df = pd.DataFrame(results)
df.to_csv("all_indian_districts.csv", index=False)
print("CSV file 'all_indian_districts.csv' has been created.")
