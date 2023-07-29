from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())

# print(soup.p)

all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
# company_url = soup.select_one(selector="#name")
print(company_url)

headings = soup.select(".heading")
print(headings)

