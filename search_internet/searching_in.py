import numpy as np;
import pandas as pd;
from googlesearch import search
from bs4 import BeautifulSoup
import requests

def get_software_description(software_name):
    try:
        query = f"{software_name} software description"
        for result in search(query, num_results=1):
            response = requests.get(result)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extracting meta description
            description = soup.find('meta', attrs={'name': 'description'})
            if description and 'content' in description.attrs:
                return description['content']
            # Fall back to extracting the first paragraph
            p_tag = soup.find('p')
            if p_tag:
                return p_tag.get_text()
    except Exception as e:
        return str(e)
    return "Description not found"


df = pd.read_csv('/Users/AmitBhatia/repo/learn_python/search_internet/sw_list.csv')

count =0
for name in df["Software Name"]:
    count = count +1 
print(count)
search_software_name = df["Software Name"][0]
print("Searching for {}".format(search_software_name))
return_software_result = get_software_description(search_software_name)
print(return_software_result)

