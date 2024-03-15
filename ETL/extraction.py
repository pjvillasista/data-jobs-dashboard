from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_latest_jobs():
    # Define the search parameters
    params = {
        "engine": "google_jobs",
        "q": "Data Analyst",  # Make sure to use the function's query parameter
        "hl": "en",
        "chips": "date_posted:week",
        "api_key": API_KEY,
    }

    # Execute the search
    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results.get("jobs_results", [])

    # Print results for troubleshooting
    print(f"Jobs Results: {jobs_results}")

    # Define the file path
    file_path = "./raw_data/latest_jobs.json"

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
