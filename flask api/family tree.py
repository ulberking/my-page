from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')

@app.route('/Minho')
def showMinho():
    return render_template('minho.html',name='Minho',age='15')
@app.route('/Family')
def showYena():
    return render_template('family.html',name='Family',age='15')
@app.route('/Yena')
def showFamily():
    return render_template('yena.html',name='Yena',age='18')
app.run(debug=True)