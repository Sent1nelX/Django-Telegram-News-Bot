from bs4 import BeautifulSoup
from requests import get
from os import system
system('clear')





def get_html(url):
    response = get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'})
    if response.status_code != 200:
        return None
    
    with open('index.html', 'w') as file:
        file.write(response.text)
    return response.text


def proccessing(html):
    soup = BeautifulSoup(html, 'lxml').find('div', {'class': 'tab-content'}).find_all('div', {'class': 'main-news_top_item'})
    a  = []
    for item in soup:
        title = item.find('span', {'class': 'main-news_top_item_title'}).get_text(strip=True)
        date = item.find('div', {'class': 'main-news_top_item_meta'}).get_text(strip=True)
        url = 'https://tengrinews.kz/' + item.find('a')['href']
        try:
            html = get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/000000000 Safari/537.36 Edg/000000000'})
            item_soup = BeautifulSoup(html.text, 'lxml').find('div', {'class': 'content_main_text'}).find('p').text

            info = item_soup.replace('Tengrinews.kz', 'MarselleNaz')
        except:
            continue
        
        a.append({
            'title': title,
            'info': info if info else None,
            'url': url,
            'date': date,
        })
        
    return a


def main():
    url = 'https://tengrinews.kz/'
    html = get_html(url)
    soup = proccessing(html)
    import json 


    with open('data.json', 'w') as file:
        json.dump(soup, file, indent=4, ensure_ascii=False)
    return len(soup)


if __name__ == '__main__':
    print(main())

