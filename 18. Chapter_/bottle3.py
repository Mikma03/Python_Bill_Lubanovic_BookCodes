from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Cześć, %s!" % thing

run(host='localhost', port=9999)
