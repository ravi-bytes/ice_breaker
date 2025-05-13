import os
import requests
from dotenv import load_dotenv


load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """scrape information from a LinkedIn profile
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        print("Using profile data from a gist")
        linkedin_profile_url = "https://gist.githubusercontent.com/ravi-bytes/13359a482fd5ee3dd68b3fa437bce755/raw/0417a10cc396d73fb6706f4fec8a9a2b1f4cdb73/ravi-proxycurl.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        print("Using ProxyCurl API to scrape LinkedIn profile")
        api_key = "2-AVwoxbhQQIB9vTxCHXPA"
        headers = {"Authorization": "Bearer " + api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_profile_url,
            # "extra": "include",
            # "github_profile_id": "include",
            # "personal_contact_number": "include",
            "personal_email": "include",
            # "inferred_salary": "include",
            "skills": "include",
            "use_cache": "if-present",
            "fallback_to_cache": "on-error",
        }
        response = requests.get(
            api_endpoint, params=params, headers=headers, timeout=10
        )
    data = response.json()
    # print(data)
    return data


if __name__ == "__main__":
    # Example usage
    linkedin_profile_url = "https://www.linkedin.com/in/raviiyer/"
    mock = False  # Set to True to use mock data
    profile_data = scrape_linkedin_profile(linkedin_profile_url, mock)
    # print(profile_data)
