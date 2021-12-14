from webhooks import parse_github_event
from bottle import post, run, request
import messages


@post('/test')
def test():
    name = request.json['name']
    response = 'This server is working, and to prove it to you, ' \
               f"I'll guess your name!\nYour name is... {name}!"
    print(response)
    return response


@post('/github/events')
def manage_github_events():
    parse_github_event(request.json)


run(host='', port=5556, debug=True)
