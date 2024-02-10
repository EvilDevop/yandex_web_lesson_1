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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 style="text-align:center">Анкета претендента</h1>
                                <h3 style="text-align:center">на участие в миссии</h3>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="name" class="form-control" id="surname"  placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="form-control">Какое у Вас образование?</label>
                                            <select class="form-control" id="degreeSelect" name="degree">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть професиии?</label>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="research-engineer" name="profession">
                                                <label class="form-check-label" for="research-engineer">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="civil-engineer" name="profession">
                                                <label class="form-check-label" for="civil-engineer">Инженер-строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="pilot" name="profession">
                                                <label class="form-check-label" for="pilot">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="meteorologist" name="profession">
                                                <label class="form-check-label" for="meteorologist">Метеоролог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="life_support_engineer" name="profession">
                                                <label class="form-check-label" for="life_support_engineer">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="radiation-protection-engineer" name="profession">
                                                <label class="form-check-label" for="radiation-protection-engineer">Инженер по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="doctor" name="profession">
                                                <label class="form-check-label" for="doctor">Врач</label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')