# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:20:51 2026

@author: syeda
"""

import pandas as pd
from bs4 import BeautifulSoup
import re

# Read the HTML file
with open('indeed.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize lists to store data
jobs_data = {
    'Job_Title': [],
    'Company_Name': [],
    'Location': [],
    'Salary': [],
    'Job_URL': []
}

# Find all job cards - look for the main job result containers
job_cards = soup.find_all('div', class_='cardOutline')

print(f"Found {len(job_cards)} job cards\n")

for card in job_cards:
    try:
        # 1. Extract Job Title
        job_title_element = card.find('a', class_='jcs-JobTitle')
        job_title = job_title_element.get_text(strip=True) if job_title_element else 'N/A'
        
        # 2. Extract Job URL (from the href attribute)
        job_url = job_title_element['href'] if job_title_element and job_title_element.get('href') else 'N/A'
        # Make relative URLs absolute if needed
        if job_url.startswith('/'):
            job_url = 'https://in.indeed.com' + job_url
        
        # 3. Extract Company Name
        # Look for company name in the job card
        company_element = card.find('div', {'data-company-name': 'true'})
        if company_element:
            company_name = company_element.get_text(strip=True)
        else:
            # Alternative selector if above doesn't work
            company_element = card.find('a', class_=re.compile('.*company.*'))
            company_name = company_element.get_text(strip=True) if company_element else 'N/A'
        
        # 4. Extract Location
        # Location typically appears near company, often in a separate span
        location_element = None
        # Try to find location in the job metadata section
        for span in card.find_all('span', class_=re.compile('.*location.*', re.I)):
            location_element = span
            break
        
        # Alternative: look for comma-separated location pattern near company
        if not location_element:
            text_content = card.get_text()
            # Try to extract location after company name
            location_match = re.search(r'(\w+(?:\s*,\s*\w+)*)\s*(?:Remote|jobs)', text_content)
            location = location_match.group(1) if location_match else 'N/A'
        else:
            location = location_element.get_text(strip=True)
        
        # 5. Extract Salary
        # Salary appears in a specific pattern in the HTML
        salary_element = None
        # Look for salary pattern in the snippet/summary
        snippet = card.find('div', class_=re.compile('.*snippet.*'))
        
        salary = 'N/A'
        if card:
            # Search entire card text for salary pattern
            card_text = card.get_text()
            # Pattern: ₹XXX,XXX - ₹XXX,XXX or per hour/year
            salary_match = re.search(r'[₹$]\s*[\d,]+(?:\s*-\s*[₹$]\s*[\d,]+)?\s*(?:per\s+(?:hour|year|month|day))?', card_text)
            if salary_match:
                salary = salary_match.group(0).strip()
        
        # Add to dictionary
        jobs_data['Job_Title'].append(job_title)
        jobs_data['Company_Name'].append(company_name)
        jobs_data['Location'].append(location)
        jobs_data['Salary'].append(salary)
        jobs_data['Job_URL'].append(job_url)
        
        print(f"Title: {job_title}")
        print(f"Company: {company_name}")
        print(f"Location: {location}")
        print(f"Salary: {salary}")
        print(f"URL: {job_url}")
        print("-" * 80)
        
    except Exception as e:
        print(f"Error processing card: {str(e)}")
        continue

# Create DataFrame
df = pd.DataFrame(jobs_data)

# Display the DataFrame
print("\n\nFinal DataFrame:")
print(df.to_string())

# Save to CSV
df.to_csv('indeed_jobs.csv', index=False)
print("\n\nData saved to 'indeed_jobs.csv'")

# Display summary
print(f"\nTotal jobs extracted: {len(df)}")
print(f"\nDataFrame Info:")
print(df.info())
print(f"\nFirst few rows:")
print(df.head())
