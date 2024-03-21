import requests,json,os
os.system('cls')
def api_get_bible(book_name,chapter,verse):
    api_get=requests.get(f'https://bible-api.com/{book_name} {chapter}:{verse}')
    api=json.loads(api_get.content)


    for x in api['verses']:
        return x



def get_api(url):
    api_get=requests.get(url)
    api=json.loads(api_get.content)
    return api