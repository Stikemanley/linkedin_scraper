from scrape_linkedin.Scraper import  Scraper
from scrape_linkedin.Search import Search
import pandas as pd
import time
import os
import sys

links = []
industries = []
page = 0
results = 0
input = pd.read_csv('OutputDF.csv')
if os.path.exists('./results.csv'):
    results = pd.read_csv('./results.csv')
else:
    results = pd.DataFrame(columns=['Company Name','Industry','City','State','LIEmployees','Company Type','Description','Website','Specialties'])
json = []
jsonDF = pd.DataFrame(columns=['Company Name','Industry','City','State','LIEmployees','Company Type','Description','Website','Specialties'])




with Scraper(cookie='AQEDASc-uNgEkbW3AAABY4EZkPMAAAFjpSYU800AR86mqoTSbTbsTiNkRtwDxrrdJp9O9R0B5zxS6IdFOjTWp8Tvvet_OVTuLzmW7Sk6r_y3yYHnLNDdNfz9z3cxX_pVCC0r9HDT7oX1kGP8f-iJrY7r') as scraper:
    for i in range(len(input['link'])):
        try:
            print(i)
            url = 'https://www.linkedin.com' + str(input.ix[i,'link'])
            company = scraper.get_company(url)

            try:

                top = company.top_card_info()
                bot = company.company_info()
                top.update(bot)
                json.append(top)


                print('***')
                result = pd.DataFrame([top],columns=top.keys())
                print(result)
                print('***')
                results = pd.concat([results,result], axis=0, ignore_index=True)
                #results = results.drop(columns=['index'])
                print(results)
                results.to_csv('./results.csv', index='ignore')



            except:
                print(sys.exec_info()[0])
                print('not making it')
                print(top)
                continue
        except:
            continue
    for i in range(len(json)):
        row = pd.DataFrame(json[i],columns = json[i].keys90)
        jsonDF = pd.concat([jsonDF,row], axis=0, ignore_index=True)

    jsonDF.to_csv('./jsonDF_results.csv')



