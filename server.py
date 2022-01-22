from flask import Flask, render_template

app = Flask( __name__ )


@app.route('/play', methods=['GET'])
def play():

    return render_template( "box.html" ) 

@app.route('/play/<int:num>', methods=['GET'])
def playDiv( num ):

    return render_template( "number.html", num=num )

@app.route('/play/<int:num>/<colorBox>', methods=['GET'])
def playDivColor( num, colorBox):

    return render_template( "index.html", num=num, colorBox=colorBox )

if __name__ == "__main__":
    app.run( debug=True )