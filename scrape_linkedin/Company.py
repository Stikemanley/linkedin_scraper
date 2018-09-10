from bs4 import BeautifulSoup
from pprint import pprint
from .utils import *
import re


class Company(object):
    """Linkedin Profile object

    Attributes:
        - personal_info
        - experiences
        - skills
        - accomplishments
        - interests
        - to_dict: return dictionary of all properties listed above
    """

    def __init__(self, body):
        """Initializes a profile with beautifulsoup body"""
        self.soup = BeautifulSoup(body, 'html.parser')


    def top_card_info(self):
        """Return dict of personal info about the user"""
        info = {}
        top_card = self.soup.find('div',{'class':'org-top-card-module__container'})
        Employees = top_card.findAll('a',{'class':'org-company-employees-snackbar__details-highlight'})
        if len(Employees) > 1:
            liEmployees = Employees[1]
        else:
            liEmployees = top_card.find('a',{'class':'org-company-employees-snackbar__details-highlight'})
        comp_name = ' '.join(top_card.find('h1',{'class':'org-top-card-module__name'})['title'].split()).encode('ascii', errors='ignore').decode('utf-8', errors='ignore')
        industry = ' '.join(top_card.find('span',{'class':'company-industries'}).text.split()).encode('ascii', errors='ignore').decode('utf-8', errors='ignore')
        city = ' '.join(top_card.find('span',{'class':'org-top-card-module__location'}).text.split(',')[0].split()).encode('ascii', errors='ignore').decode('utf-8', errors='ignore')
        state = ' '.join(top_card.find('span',{'class':'org-top-card-module__location'}).text.split(',')[1].split()).encode('ascii', errors='ignore').decode('utf-8', errors='ignore')
        liEmployees = ''.join(re.findall(r'\d+',liEmployees.text)).encode('ascii', errors='ignore').decode('utf-8', errors='ignore')
        top_card_info = {
            'Company Name':comp_name,
            'Industry': industry,
            'City': city,
            'State': state,
            'LIEmployees': liEmployees
        }


        return top_card_info

    def company_info(self):
        """
        Returns:
            dict of person's professional experiences.  These include:
                - Jobs
                - Education
                - Volunteer Experiences
        """

        other_comp = self.soup.find('div', {'class': 'org-about-company-module__org-info'})
        comp_type = other_comp.find('p', {'class': 'org-about-company-module__company-type'}).text
        desc = other_comp.find('p', {'class': 'org-about-us-organization-description__text'}).text.strip('\n').strip('\t').strip('\r\n').strip('\r\n\r\n')
        web = other_comp.find('a', {'class': 'org-about-us-company-module__website'})['href']
        spec = str(list(other_comp.find('p',{'class':'org-about-company-module__specialities'}).text.strip('\n').strip().split(',')))

        other_comp_info = {
            'Company Type': comp_type,
            'Description': desc,
            'Website': web,
            'Specialties': spec
        }
        return other_comp_info
    def testUS(self):
        states = ["Alaska",
                  "Alabama",
                  "Arkansas",
                  "American Samoa",
                  "Arizona",
                  "California",
                  "Colorado",
                  "Connecticut",
                  "District of Columbia",
                  "Delaware",
                  "Florida",
                  "Georgia",
                  "Guam",
                  "Hawaii",
                  "Iowa",
                  "Idaho",
                  "Illinois",
                  "Indiana",
                  "Kansas",
                  "Kentucky",
                  "Louisiana",
                  "Massachusetts",
                  "Maryland",
                  "Maine",
                  "Michigan",
                  "Minnesota",
                  "Missouri",
                  "Mississippi",
                  "Montana",
                  "North Carolina",
                  "North Dakota",
                  "Nebraska",
                  "New Hampshire",
                  "New Jersey",
                  "New Mexico",
                  "Nevada",
                  "New York",
                  "Ohio",
                  "Oklahoma",
                  "Oregon",
                  "Pennsylvania",
                  "Puerto Rico",
                  "Rhode Island",
                  "South Carolina",
                  "South Dakota",
                  "Tennessee",
                  "Texas",
                  "Utah",
                  "Virginia",
                  "Virgin Islands",
                  "Vermont",
                  "Washington",
                  "Wisconsin",
                  "West Virginia",
                  "Wyoming"]
        Location = self.soup.find('span',{'class':'org-top-card-module__location'}).text.split(',')[1]
        print(Location)
        if Location in states:
            print('YAY')
            return False
        else:
            return True

    def to_dict(self):
        """Return full dict of person's profile
        """
        info = {}
        info['top_card_info'] = self.top_card_info
        info['other_comp_info'] = self.other_comp_info
        print(info)
        return info

    def __dict__(self):
        return self.to_dict()

    def __eq__(self, that):
        return self.to_dict() == that.to_dict()


