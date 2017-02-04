from flask import Flask


app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hi, I\'m appA. Slides at <a href=\"https://mesosphere.github.io/presentations\">https://mesosphere.github.io/presentations</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
