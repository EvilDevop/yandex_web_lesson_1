from flask import Flask, url_for, request

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
                        <span class="highlighted-text">Человечество вырастает из детства.</span> <br>
                        <span class="highlighted-text">Человечеству мала одна планета.</span> <br>
                        <span class="highlighted-text">Мы сделаем обитаемыми безжизненные пока планеты.</span> <br>
                        <span class="highlighted-text">И начнем с Марса!</span> <br>
                        <span class="highlighted-text">Присоединяйся!</span> <br>
                      </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    mercury = ['Эта планета близка к солнцу;', 'На ней можно быстро загареть;', ['Она не так далеко от Земли;'], ['Она небольшая.']]
    venus = ['Она близка к Земле;', 'На ней тепло;', 'Она больше Земли;', 'Она красивая.']
    mars = ['Она близка к Земле;', 'На ней много необходимых ресурсов;', 'На ней есть вода и атмосфера;', 'Она просто красивая.']
    jupiter = ['Эта планета большая;', 'На ней можно накуриться газа;', 'Это самая большая планета солнечной системы;', 'Она недалеко от Земли.']
    planets = {'Меркурий': mercury, 'Венера': venus, 'Марс': mars, 'Юпитер': jupiter}
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
                    <h1>Мое предложение: {planet_name}</h1> <br>
                    <span class="highlighted-text">{planets[planet_name][0]}</span> <br>
                    <span class="highlighted-text">{planets[planet_name][1]}</span> <br>
                    <span class="highlighted-text">{planets[planet_name][2]}</span> <br>
                    <span class="highlighted-text">{planets[planet_name][3]}</span> <br>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')