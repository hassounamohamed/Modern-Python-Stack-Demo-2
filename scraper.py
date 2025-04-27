#Make an HTTP request
#def main():
#    print('Hello world!')
import requests

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)
  print(f"Scraping: {url}")
  print(response)

if __name__ == "__main__":
  main()