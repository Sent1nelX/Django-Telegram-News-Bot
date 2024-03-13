import requests
from bs4 import BeautifulSoup
from django.conf import settings
from accounts.models import News


def get_html(url=settings.DOMAIN_NAME_PARS):
    response = requests.get(url, headers=settings.HEADERS)
    
    if response.status_code != 200:
        return None
    
    return response.text


def proccessing(html):
    soup = BeautifulSoup(html, 'lxml').find('div', {'id': 'content-1'}
        ).find_all('div', {'class': 'main-news_top_item'})
    
    for item in soup:
        try:
            title = item.find('span', {'class': 'main-news_top_item_title'}).get_text(strip=True)
            time = item.find('div', {'class': 'main-news_top_item_meta'}).get_text(strip=True)
            url = settings.DOMAIN_NAME_PARS + item.find('a')['href']

            if not News.objects.filter(title=title).exists():
                description = get_detail_news(url)

                new_news = News(
                    title=title,
                    info=description,
                    url=url,
                    time=time,
                )
                new_news.save()
            else:
                continue
        
        except Exception:
            continue


def get_detail_news(url):
    soup = BeautifulSoup(get_html(url), 'lxml').find('div', {'class': 'content_main_text'})
    if soup is None:
        return None
    
    general_text = ""

    for item in soup.find_all('p'):
        try: 
            if item.text.find('Наши новости теперь в WhatsApp!') != -1:
                continue

            general_text += item.get_text().replace('Tengrinews.kz', 'Adik') + '\n'

        except:
            continue
    
    return general_text.strip()


def proccessing_table_2(html):
    
    soup = BeautifulSoup(html, 'lxml').find('div', {'id': 'content-2'}
        ).find_all('div', {'class': 'main-news_top_item'})
    
    for item in soup:
        try:
            time = item.find('div', {'class': 'main-news_top_item_meta'}).get_text(strip=True)
            if time.lower() != 'сегодня':
                continue
            else:
                title = item.find('span', {'class': 'main-news_top_item_title'}).get_text(strip=True)
                url = settings.DOMAIN_NAME_PARS + item.find('a')['href'][1:]


                if not News.objects.filter(title=title).exists():
                    description = get_detail_news(url)
                    new_news = News(
                        popular=True,
                        title=title,
                        info=description,
                        url=url,
                        time=time,
                    )
                    new_news.save()
                else:
                    continue
        except Exception as x:
            print(x)
            continue
