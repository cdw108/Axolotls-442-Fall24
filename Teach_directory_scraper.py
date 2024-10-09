import requests
from bs4 import BeautifulSoup

#make a list of all the webpages to scrape
webpages = ['https://www.latech.edu/faculty-staff/single-entry/cat/administration_facilities/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/chief-information-officer/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/chief_innovation_officer/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/college-of-business/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/college-of-education/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/college-of-engineering-and-science/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/college-of-liberal-arts/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/finance/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/provost/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/research-partnerships/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/student_advancement/',
            'https://www.latech.edu/faculty-staff/single-entry/cat/university_advancement/']

#loop through untill the entire directory has been scraped
for i in range(len(webpages)-1):
    print(webpages[i])
    staff_list = []
    data_list = []

#sructure for beautiful soup requests found from: https://www.youtube.com/watch?v=JlHdv4Dfjq4, and adapted to the tech directory website
    current_webpage = requests.get(webpages[i])
    s = BeautifulSoup(current_webpage.text, 'html.parser')

#find the name of the staff member and add it too the list
    staff_member = s.find_all('div', class_= 'listing-left')
    for element in staff_member:
        staff_list.append(element.find('a').get_text() + ", ")

#find data associated with the staff member and add it to the repective index
    data = s.find_all('div', class_= 'listing-right')
    for element in data:
        data_list.append(element.find('p').get_text())
      
    for i in range(len(data_list)):
        print(staff_list[i], data_list[i])


