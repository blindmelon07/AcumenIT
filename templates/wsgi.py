from flask import Flask, url_for, request, render_template
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def show_the_login_form():
    kwargs = {'login_url': url_for("login")}
    return render_template('login.html', **kwargs)
    #return render_template('login.html', login_url=url_for("login"))

def do_the_login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "admin":
        return "login success"
    else:
        return "login fail"
    
    return "login"