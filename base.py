import requests
import json
from logic import posts_text

# Парсинг с вк группы с помощью vk_api
def main():
    #https://api.vk.com/method/wall.get?user_id=210700286&v=5.52
    group_id="-54530371" #id группы которую мы парсим
    access_token = "df439f51df439f51df439f51efdf3628e1ddf43df439f5180affe39047548ba50381df8"#Сервисный ключ доступа
    version = 5.52
    offset = 0
    count = 50 #кол-во "парсируемых" постов
    r = requests.get('https://api.vk.com/method/wall.get',params={'owner_id': group_id,
                                                                  'count': count,
                                                                  'offset': offset,
                                                                  'access_token':access_token,
                                                                 'v': version})


    # Выводим инф-ю в удобном формате.Среди всех постов выделяем и выводим только те что имеют тэг '#book@proglib', или же просто выводим только книги
    for post in posts_text(r):
        print(post,end='\n\n\n\n')




if __name__ == '__main__':
    main()