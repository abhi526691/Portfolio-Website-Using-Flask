from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/blogs')
def blog():
    return render_template('blogs.html')

@app.route('/timeline')
def achivement():
    return render_template('timeline.html')


if __name__ == '__main__':
    app.run(debug=True)