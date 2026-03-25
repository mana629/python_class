from flask import Flask, request, redirect, url_for, session, Response, render_template_string

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def home():
    # Landing page with links
    return render_template_string("""
        <h1>Welcome to My Flask App</h1>
        <p>This is the landing page.</p>
        <a href="{{ url_for('login') }}">Go to Login</a>
    """)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if  password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again.", mimetype="text/plain")

    return render_template_string("""
        <h2>Login Page</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    """)

@app.route('/welcome')
def welcome():
    if "user" in session:
        return render_template_string(f"""
            <h2>Welcome, {session['user']}!</h2>
            <p>You are successfully logged in.</p>
            <a href="{{ url_for('logout') }}">Logout</a>
        """)
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
 
 


             