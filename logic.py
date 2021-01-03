import json

def posts_text(request):
    json_output = json.loads(request.text)['response']['items']
    for posts in json_output:
        for elem in posts:
            if elem == 'text' and '#book@proglib' in posts[elem]:
                yield posts[elem]