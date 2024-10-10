import re
import csv
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
staff_list = []
data_list = []
#loop through untill the entire directory has been scraped
for i in range(len(webpages)-1):
    print(webpages[i])
    

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

###CHAT GPT GENERATED (partially)###
email_pattern = re.compile(r"Email:\s*([^\s]+?(\.com|\.edu|\.org))")

# Open a CSV file for writing
with open("emails.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Name", "Email"])

    # Extract emails from each string and write them into the CSV
    for idx, (entry, name) in enumerate(zip(data_list, staff_list)):
        match = email_pattern.search(entry)
        if match:
            email = match.group(1)
            writer.writerow([name, email])  # Write email to the CSV
print('done')
###CHAT GPT GENERATED (partially)###
#prompt: how to seach through a list of strings and collect data after entry: "Email: "


