from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Retrieve API key from .env file
API_KEY = os.getenv("API_KEY")

# Get the current datetime for file naming
current_datetime = datetime.now().strftime("%m_%d_%Y")


def get_latest_jobs(page_number=1, page_size=10):
    offset = (page_number - 1) * page_size

    # Define the search parameters
    params = {
        "engine": "google_jobs",
        "q": "Data Engineer | Analytics Engineer",
        "hl": "en",
        "chips": "date_posted:week",
        "start": offset,
        "api_key": API_KEY,
    }

    # Execute the search
    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results.get("jobs_results", [])

    # Print results for troubleshooting
    print(f"Jobs Results: {jobs_results}")

    # Define the file path
    file_path = f"../raw_data/latest_jobs_{current_datetime}.json"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        # Save to JSON
        with open(file_path, "w") as f:
            json.dump(jobs_results, f)
        print(f"Saved file to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

    return jobs_results


def main():
    # Calculate the number of searches you can perform weekly within the limit
    searches_per_month = 100
    weeks_per_month = 4  # Approximate
    searches_per_week = searches_per_month // weeks_per_month

    # Default page size returns 10 jobs
    page_size = 10

    # Perform searches up to the weekly limit
    for page_number in range(1, searches_per_week + 1):
        get_latest_jobs(page_number, page_size)


if __name__ == "__main__":
    main()
