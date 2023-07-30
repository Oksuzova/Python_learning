from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_score = max(article_upvotes)
article = article_texts[article_upvotes.index(max_score)]
link = article_links[article_upvotes.index(max_score)]

print(article)
print(link)










spotify = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                      client_secret=SPOTIPY_CLIENT_SECRET,
                                      redirect_uri=SPOTIPY_REDIRECT_URI)
access_token = spotify.get_cached_token()




SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")





# with open("website.html") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)
# # print(soup.title.string)
# #
# # print(soup.prettify())
#
# # print(soup.p)
#
# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# # company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)


