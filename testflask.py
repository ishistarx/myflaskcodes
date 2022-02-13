from flask import Flask

app=Flask(__name__)


@app.route('/amitava')
def hi():
    return '<h1>I am amitava</h1>'


if __name__=='__main__':
    app.run()

    

