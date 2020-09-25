from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_ngrok import run_with_ngrok
import test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Baze.db'
#run_with_ngrok(app)
db = SQLAlchemy(app)


class Photos(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Photo = db.Column(db.String())


class GG(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    Name_book = db.Column(db.String())
    Coment = db.Column(db.String())
    Date = db.Column(db.String())
    Photo = db.Column(db.String())
    Photo_2 = db.Column(db.String())
    Photo_3 = db.Column(db.String())
    

@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/event')
def event():
    return render_template('event.html')


@app.route('/our_library')
def our_library():
    tasks = GG.query.all()
    return render_template('our_library.html', tasks=tasks)


@app.route('/gallery')
def gallery():
    tasks = Photos.query.all()
    return render_template('gallery.html', tasks=tasks)


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/authors_opinion')
def contacts1():
    return render_template('authors_opinion.html')

@app.route('/frequent_opinion')
def frequent_opinion():
    return render_template('frequent_opinion.html')


@app.route('/young_voice')
def young_voice():
    return render_template('young_voice.html')






@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/delete/<ID>')
def delete(ID):
    GG.query.filter_by(ID=int(ID)).delete()
    db.session.commit()
    return redirect(url_for('index'))

# Вот тут кидаем в бд данные пользователя


@app.route('/create-task', methods=['POST'])
def create():
    try:
        log = str(test.Map.get_address(request.form['address']))[1:-1]
    except:
        log = '59.14, 37.9http://localhost:8080/our_library'
    new_task = GG(Name=request.form['name'], Address=request.form['address'], Address_log=log, Goods=request.form['goods'],
                  Period=request.form['period'], Coment=request.form['coment'], Photo=request.form['photo'], Condition='In_progress')
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('contacts1'))


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)
    #app.run()
