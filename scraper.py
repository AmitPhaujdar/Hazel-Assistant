import requests
from bs4 import BeautifulSoup
import json
interests = [
    'Content Writing',
    'Digital Marketing',
    'UI/UX Design',
    'SEO',
    'Social Media Marketing',
    'Web Development',
    'Data Analytics',
    'Mobile App Development',
    'Full Stack Development',
    'Front End Development'
]
'''
threshold = int(input('Enter stipend threshold :'))
'''


def scraper(threshold):
    for i in range(1, 7):
        URL = 'https://internshala.com/internships/page-{}'.format(i)

        header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
                  }

        page = requests.get(URL, headers=header)

        soup = BeautifulSoup(page.content, 'html.parser')
        headers = json.load(open('headers.json'))
        containers = soup.findAll(
            "div", {"class": "container-fluid individual_internship"})
        for container in containers:
            row = dict.fromkeys(headers)
            row['title'] = container.a.text
            row['applylink'] = 'https://internshala.com' + container.a["href"]
            company_container = container.findAll(
                "a", {"class": "link_display_like_text"})
            row['companyname'] = company_container[0].text

            stipend_container = container.findAll(
                "td", {"class": "stipend_container_table_cell"})
            row['salary'] = stipend_container[0].text
            start_container = container.findAll(
                "div", {"id": "start-date-first"})
            row['startdate'] = start_container[0].text
            apply_by_container = container.findAll(
                "div", {"class": "table-responsive"})
            apply_by = apply_by_container[0].findAll("td")
            row['enddate'] = apply_by[4].text
            for i in interests:
                if i in row['title']:
                    '''
                    print('Category :', row['title'])
                    '''
                    '''
                    print('company name :', row['companyname'].strip())
                    '''
                    if 'Unpaid' not in row['salary'].strip():
                        if '-' in row['salary'].strip() and 'lump' not in row['salary'].strip():
                            stipend2 = row['salary'].strip().split(
                                '-')[1].split('/')[0]
                            if(int(stipend2) > threshold):
                                print('Category :', row['title'])
                                print('company name :',
                                      row['companyname'].strip())
                                print('stipend2 :', row['salary'].strip())
                                print('start date :', row['startdate'])
                                print('end date :', row['enddate'])
                                print('apply link :', row['applylink'])
                                print('\n')
                        elif 'lump' in row['salary'].strip():
                            if '-' in row['salary'].split('l')[0]:
                                stipend2 = row['salary'].split(
                                    'l')[0].split('-')[1]
                                if(int(stipend2) > threshold):
                                    print('Category :', row['title'])
                                    print('company name :',
                                          row['companyname'].strip())
                                    print('stipend2 :', row['salary'].strip())
                                    print('start date :', row['startdate'])
                                    print('end date :', row['enddate'])
                                    print('apply link :', row['applylink'])
                                    print('\n')
                            else:
                                stipend2 = row['salary'].split('l')[0]
                                if(int(stipend2) > threshold):
                                    print('Category :', row['title'])
                                    print('company name :',
                                          row['companyname'].strip())
                                    print('stipend2 :', row['salary'].strip())
                                    print('start date :', row['startdate'])
                                    print('end date :', row['enddate'])
                                    print('apply link :', row['applylink'])
                                    print('\n')

                        elif 'lump' not in row['salary'].strip():
                            stipend2 = row['salary'].strip().split('/')[0]

                            if(int(stipend2) > threshold):
                                print('Category :', row['title'])
                                print('company name :',
                                      row['companyname'].strip())
                                print('stipend2 :', row['salary'].strip())
                                print('start date :', row['startdate'])
                                print('end date :', row['enddate'])
                                print('apply link :', row['applylink'])
                                print('\n')
                        else:
                            stipend2 = row['salary'].strip()
                            if(int(stipend2) > threshold):
                                print('Category :', row['title'])
                                print('company name :',
                                      row['companyname'].strip())
                                print('stipend2 :', row['salary'].strip())
                                print('start date :', row['startdate'])
                                print('end date :', row['enddate'])
                                print('apply link :', row['applylink'])
                                print('\n')
                    '''
                    print('start date :', row['startdate'])
                    print('end date :', row['enddate'])
                    print('apply link :', row['applylink'])
                    '''
                    print('\n')


'''
scraper(threshold)
'''
