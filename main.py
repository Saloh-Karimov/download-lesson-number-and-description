import requests
from bs4 import BeautifulSoup

# specify the website URL
url = "https://www.site.com/lessons"

# send a GET request to the URL
response = requests.get(url)

# parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the lessons in the HTML using a CSS selector
lessons = soup.select('.lessons-item')

# write the lessons and descriptions to a file
with open('lessons.txt', 'w') as f:
    for lesson in lessons:
        # get the lesson number and name
        lesson_number = lesson.select_one('.lessons-title').text.strip()
        lesson_name = lesson.select_one('.lessons-name').text.strip()

        # write the lesson number and name to the file
        f.write(f"{lesson_number}: {lesson_name}\n")
