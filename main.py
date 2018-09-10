from scrape_linkedin.Scraper import  Scraper
from scrape_linkedin.Search import Search
import pandas as pd
import time

links = []
industries = []
page = 0
results = 0
output_df = pd.DataFrame(columns=['link','industry'])



with Scraper(cookie='AQEDAQiEKJ8FMn6dAAABZZBg5zkAAAFl2KtRbE0AdkO3BAPtxerBi99Q9oKAVO5xQld4Gha6p32ab4GqSNLUEnlfJFZd8WS2FrgBz1e5QUtXenSu0opMyq2SwgFCHuGe6sCuwoZZNlm-C2zfNcAxPVe0') as scraper:

    while results <= 900:
        try:
            # if scraper.driver.find_element_by_css_selector('.search-no-results'):
            #     output_df = pd.DataFrame({'link': links, 'industries': industries})
            #     output_df.to_csv('./outputDF2.csv')
            url = 'https://www.linkedin.com/search/results/companies/?keywords=Data%20Analytics&origin=GLOBAL_SEARCH_HEADER'
            if page > 0:
                url = url + '&page=' + str(page)
            search = scraper.get_search(url)
            new_links = search.get_links()
            print(new_links[0])
            print(new_links[1])
            links = links + new_links[0]
            industries = industries + new_links[1]


            page += 1
            results += 10
            print(results)
        except:
            page += 1
    output_df = pd.DataFrame({'link': links, 'industries': industries})
    output_df.to_csv('./outputDF5.csv')





