from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html', message="Hello World!")

@app.route('/<name>')
def hello_name(name):
    return render_template('hello.html',message="Hello "+name)

if __name__ == '__main__':
    app.run(debug=True)
