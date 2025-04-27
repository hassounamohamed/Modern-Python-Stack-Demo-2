#Make an HTTP request
def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  print(f"Scraping: {url}")
import keywords
if __name__ == "__main__":
  main()


#Parse the HTTP response with “Beautifulsoup”
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

#  soup = BeautifulSoup(response.content, "html.parser")
# find all elements with class="comment"
#  elements = soup.find_all(class_="comment")

  # Show the number of elementd found
#  print(f"Elements: {len(elements)}")


if __name__ == "__main__":
  main()

#Extract individual comments
import requests
from bs4 import BeautifulSoup

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")
  # find all elements with class="ind" and indent level = 0
  elements = soup.find_all(class_="ind" , indent=0)
  # for each of this elements, find the next element
  comments = [e.find_next(class_="comment") for e in elements]

  # Show the number of comments found
  print(f"Comments: {len(comments)}")

if __name__ == "__main__":
  main()

#Clean up the response text
import requests
from bs4 import BeautifulSoup

def main():
 url = "https://news.ycombinator.com/item?id=42919502"
 response = requests.get(url)

 soup = BeautifulSoup(response.content, "html.parser")
 #  find all elements with class="ind" and indent level = 0
#  elements = soup.find_all(class_="ind" , indent=0)
  # for each of this elements, find the next element
#  comments = [e.find_next(class_="comment") for e in elements]

  # show each comment (job post)
#for comment in comments:
#    comment_text = comment.get_text()
#    print(comment_text)

if __name__ == "__main__":
  main()

#Process the scraped content for useful data
import requests
from bs4 import BeautifulSoup

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")
  # find all elements with class="ind" and indent level = 0
  elements = soup.find_all(class_="ind" , indent=0)
  # for each of this elements, find the next element
  comments = [e.find_next(class_="comment") for e in elements]

  # Map of technologies keyword to search for
  # and the occurence initialized at 0
  keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0 }

  # show each comment (job post)
  for comment in comments:
    # get the comment text and lower case it
    comment_text = comment.get_text().lower()

    # split comment by space which create an array of words
    words = comment_text.split(" ")

    print(words)

if __name__ == "__main__":
  main()
#Visualizing the data with “matplotlib”
import matplotlib.pyplot as plt
# plot a bar graph
plt.bar(keywords.keys(), keywords.values())
# Add labels
plt.xlabel("Language")
plt.ylabel("# of Mentions")
plt.show()
