
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret_key"

posts = []

@app.route('/')
def main():
    return render_template('main.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id-1]
    return render_template('post.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "password":
            session['logged_in'] = True
            return redirect('/admin')
        else:
            return redirect('/login')
    else:
        return render_template('login.html')

@app.route('/admin')
def admin():
    if 'logged_in' in session:
        return render_template('admin.html')
    else:
        return redirect('/login')

@app.route('/admin/create', methods=['POST'])
def create():
    title = request.form['title']
    body = request.form['body']
    author = "admin"
    date = datetime.now().strftime("%Y-%m-%d")
    new_post = {'title': title, 'body': body, 'author': author, 'date': date}
    posts.append(new_post)
    return redirect('/')

@app.route('/admin/update/<int:post_id>', methods=['POST'])
def update(post_id):
    post = posts[post_id-1]
    post['title'] = request.form['title']
    post['body'] = request.form['body']
    return redirect('/')

@app.route('/admin/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    posts.pop(post_id-1)
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
