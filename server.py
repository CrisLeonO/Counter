from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")


@app.route('/new_count')
def new_counter():
    if "count" in session:
        session['count'] += 2
    return render_template("index.html")


@app.route('/destroySession')
def reset():
    session.clear()
    return redirect('/' )


@app.route('/add', methods=['POST'])
def add():
    increment = int(request.form['increment'])
    session['count'] += increment
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
