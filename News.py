import json
from requests import get
from Speak import Bol

def news(ref):
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a495576f2b4a427aa293884206b21cff"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            if ref is not None:
                ref.gui.speaker.setText(f"todays {seq[i]} news is: {headings[i]}")
            Bol(f"todays {seq[i]} news is: {headings[i]}")
        Bol("Boss I am done, I have read most of the latest news")

if __name__ == "__main__":
    news()