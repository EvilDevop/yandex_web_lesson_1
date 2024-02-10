from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return '''
    И на Марсе будут яблони цвести!
    '''

@app.route('/')
def main_page():
    return '''
    Миссия Колонизация Марса
    '''

@app.route('/promotion')
def promotion():
    return '''
    Человечество вырастает из детства. <br>
    Человечеству мала одна планета. <br>
    Мы сделаем обитаемыми безжизненные пока планеты. <br>
    И начнем с Марса! <br>
    Присоединяйся! <br>
    '''

@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                              filename='css/style.css')}" />
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1> <br>
                        <img src="{url_for('static', filename='img/MARS.png')}" 
                               alt="здесь должна была быть картинка, но не нашлась"> <br>
                        <div class="p-3 mb-2 bg-secondary text-white">Человечество вырастает из детства.</div> <br>
                        <div class="p-3 mb-2 bg-success text-white">Человечеству мала одна планета.</div> <br>
                        <div class="p-3 mb-2 bg-secondary text-white">Мы сделаем обитаемыми безжизненные пока планеты.</div> <br>
                        <div class="p-3 mb-2 bg-warning text-dark">И начнем с Марса!</div> <br>
                        <div class="p-3 mb-2 bg-danger text-white">Присоединяйся!</div> <br>
                      </body>
                    </html>"""

if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')