import requests
import os

def validate_gemini_api_key(GEMINI_API_KEY):
    if not GEMINI_API_KEY:
        print(
        "No API key was found"
    )
    elif not GEMINI_API_KEY.startswith("AIzaSy"):
        print(
        "An API key was found, but it doesn't start AIzaSy; please check you're using the right key"
    )
    elif GEMINI_API_KEY.strip() != GEMINI_API_KEY:
        print(
        "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them"
    )
    else:
        print("API key found and looks good so far!")


def validate_scrapin_api_key(SCRAPIN_API_KEY):
    if not SCRAPIN_API_KEY:
        print(
        "No API key was found"
    )
    elif not SCRAPIN_API_KEY.startswith("sk_"):
        print(
        "An API key was found, but it doesn't start sk_; please check you're using the right key"
    )
    elif SCRAPIN_API_KEY.strip() != SCRAPIN_API_KEY:
        print(
        "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them"
    )
    else:
        print("API key found and looks good so far!")


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape a LinkedIn profile using the Scrapin API.
    Args:
        linkedin_profile_url (str): The LinkedIn profile URL to scrape.
    Returns:
        dict: A dictionary containing the scraped profile data.
    Raises:
        ValueError: If the provided URL is invalid or if no data is found.
    """

    if not linkedin_profile_url.startswith("https://www.linkedin.com/in/"):
        raise ValueError("Invalid LinkedIn profile URL. It should start with 'https://www.linkedin.com/in/'")
    
    if not linkedin_profile_url.endswith("/"):
        linkedin_profile_url += "/"

    api_endpoint = "https://api.scrapin.io/enrichment/profile"
    params = {
        "apikey": os.environ["SCRAPIN_API_KEY"],
        "linkedInUrl": linkedin_profile_url,
    }
    response = requests.get(
        api_endpoint,
        params=params,
        timeout=10,
    )

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }
    
    if not data:
        raise ValueError("No data found for the provided LinkedIn profile URL.")
    
    return data
