from flask import Flask, render_template,redirect,request,url_for



app = Flask(__name__)


#User will make  a request to the web page ==> receive a login page and
# the User will login with his credentials
#if pasword matches a condition
#display custom welcome
#else display another page!

@app.route('/')
def Welcome():
    return render_template('login.html')

@app.route('/secure/<user>')
def secure(user):
    return render_template('secure.html',user=user)

@app.route('/greet/<user>')
def greet(user):
    return render_template('greet.html',user=user)

@app.route('/main/<name>')
def main(name):
    return render_template('main.html', name=name)

@app.route('/unauthenticated/<user>')
def unauthenticated(user):
    return render_template('login.html',user=user, control= True)

@app.route('/login', methods=['POST','GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin':
        return redirect(url_for('secure', user=username))
    elif password == "Clarusway":
        return redirect(url_for('greet', user=username))
    elif password == "Python":
        return redirect(url_for('main', name=username))
    else:
       return  redirect(url_for('unauthenticated', user=username, control= True))






if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3003)