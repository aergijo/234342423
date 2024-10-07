from flask import Flask, render_template
import api.catapi as catp
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',url = catp.getapi() )


if __name__ == "__main__":
    app.run("0.0.0.0",port=8000,debug=True)