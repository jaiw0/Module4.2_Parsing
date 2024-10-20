import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()

Job_title = []
Company_Name = []
City = []
Category = []

for title in root.iter('job_title'):
    Job_title.append(title.text)


for company in root.iter('company_name'):
    Company_Name.append(company.text)

for city in root.iter('city'):
    City.append(city.text)

for category in root.iter('category'):
    Category.append(category.text)

print("Job Title:",Job_title)
print('')
print("Company name:",Company_Name)
print('')
print("City:",City)
print('')
print("Category:",Category)
