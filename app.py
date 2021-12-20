from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/assignment8')
def assignment_8():  # put application's code here
    return render_template('assignment8.html', profile={'first_name': '', 'second_name': ''}, genre='',
                           hobbies=('soccer', 'basketball', 'hanging out', 'traveling'))


@app.route('/cv')
@app.route('/')
def my_cv():  # put application's code here
    return render_template('cv.html')


if __name__ == '__main__':
    app.run(debug=True)
