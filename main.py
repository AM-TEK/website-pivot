from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure this file exists in a `templates` folder

if __name__ == '__main__':
    app.run(debug=True)
