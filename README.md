# 🔍 LinkedIn Candidate

An automated Python script that uses Selenium to log into LinkedIn and search for candidate profiles based on keywords and location filters.

This tool is useful for recruiters, analysts, or developers who want to automate the discovery of potential candidates for job opportunities or networking.

## ✨ Features

- Logs into LinkedIn using your credentials
- Searches for people based on keywords and optional location
- Collects the first 10 profiles for each keyword
- Displays name, job title, location, and profile link
- Includes a 5-minute delay between searches to allow viewing results before the next one

## ⚙️ Technologies Used

- Python 3
- Selenium
- Chrome WebDriver (managed automatically by `webdriver_manager`)

## 🛠️ How to Open the Project

```bash
# Clone the repository
git clone https://github.com/bruno-moura-2804/LinkedIn-Candidate.git
cd LinkedIn-Candidate

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate.bat    # On Windows

# Install the dependencies
pip install -r requirements.txt

# Run the script
python linkedin_candidate.py
