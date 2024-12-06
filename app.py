from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/careers')
def careers():
    return render_template('Careers.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

