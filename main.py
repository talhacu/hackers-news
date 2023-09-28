import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import webbrowser
window = Tk()
window.minsize(800,900)
target_url = "https://news.ycombinator.com/news"
def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def open_url(url):
    webbrowser.open(url, new=2)
def crawl(url):
    news = make_request(url)
    all_news = []
    counter = 1
    with open("haberler.txt", "w") as haberler:
        pass
    for new in news.findAll('a', {'rel': 'noreferrer'}):
        found_new_text = new.text
        haber_linki = new.get('href')
        single_news = f"- {counter}.Haber:    {found_new_text}\n- Link: {haber_linki}\n"

        news_label = Label(text=single_news, fg="blue",cursor="hand2")
        news_label.pack()
        news_label.bind("<Button-1>", lambda e, url = haber_linki: open_url(url))

        all_news.append(news_label)

        with open("haberler.txt", "a") as haberler:
            haberler.write(f"{single_news}\n{haber_linki}\n")
        counter += 1
    messagebox.showinfo(message="haberler.txt oluşturuldu")

haber_label = Label(text="Haberlere ulaşmak için tıklayın")
haber_label.pack()

haber_getir = Button(text="Haberleri Getir", command=lambda: crawl(target_url))
haber_getir.pack(pady=30)

result_label = Label(text="", justify=LEFT)
result_label.pack(pady=10)



window.mainloop()