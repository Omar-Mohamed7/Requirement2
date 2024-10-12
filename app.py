from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    age = request.form['age']
    nationality = request.form['nationality']
    return render_template('results.html', name = name, age = age,
                            nationality = nationality)

if __name__ == '__main__':
    app.run(debug=True)