from flask import Flask

app=Flask(__name__)


@app.route('/abc')
def hi():
    return '<h1>I am amitava running from Virtual Environment!!!</h1>'


if __name__=='__main__':
    app.run()

    

