from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

'''
@app.route('/brainslice')
def brainslice():
    return render_template('brainslice.html')
'''
if __name__ == '__main__':
    app.run(debug=True)