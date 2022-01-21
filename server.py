from flask import Flask, render_template

app = Flask( __name__ )

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def index():
    return render_template("index.html")


@app.route( '/hello/<string:banana>/<int:num>', methods=['GET'])

def hello(banana, num):

    return render_template("hello.html", banana=banana, num=num )


if __name__ == "__main__":
    app.run( debug=True )
