'''
Projekt:
Interaktiivne ÕIS-i kasutamist toetav rakendus veebilehe kujul.

Töö autorid:
Mihkel Tomson
Artjom Tšerkassov

Juhend:
Programmi käivitamiseks "python app.py"
Veebilehele on hetkel lisatud tagasiside funktsionaalsus, teised funktsioonid lisanduvad
järgneva töö käigus. 

'''



from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# /// Avaleht (avaleht.html)
@app.route('/')
def avaleht():
    return render_template('avaleht.html')

# /// Tagasiside leht (tagasiside.html)
@app.route('/tagasiside', methods=['GET', 'POST'])
def tagasiside():
    if request.method == 'POST':
        feedback_message = request.form['feedback']
        print('Kasutaja tagasiside:', feedback_message)
        return redirect(url_for('aitah'))
    return render_template('tagasiside.html')

# /// Tänuleht
@app.route('/aitah')
def aitah():
    return '<h2>Aitäh tagasiside eest!</h2><a href="/">Tagasi avalehele</a>'

# /// profiili leht (profiil.html)
@app.route ('/profiil')
def profiil():
    return render_template('profiil.html')

# /// Postkasti leht (postkast.html)
@app.route ('/postkast')
def postkast():
    return render_template('postkast.html')

@app.route ('/kalender')
def kalender():
    return render_template('kalender.html')

@app.route('/õppetulemused')
def õppetulemused():
    return render_template('õppetulemused.html')

@app.route('/valikud')
def valikud():
    return render_template('valikud.html')

@app.route('/registreeringud')
def registreeringud():
    return render_template('registreeringud.html')

@app.route('/avaldused')
def avaldused():
    return render_template('avaldused.html')

@app.route('/tunniplaanid')
def tunniplaanid():
    return render_template('tunniplaanid.html')

@app.route('/õppeained')
def õppeained():
    return render_template('õppeained.html')

@app.route('/õppekavad')
def õppekavad():
    return render_template('õppekavad.html')

@app.route('/akadeemiline_kalender')
def akadeemiline_kalender():
    return render_template('akadeemiline_kalender.html')

    
# /// Kontrolli leht

@app.route("/kontroll", methods=["GET", "POST"])
def kontroll():
    tulemus = None

    if request.method == "POST":
        tulemus = 0

        q1 = request.form.get("q1", "").lower()
        q2 = request.form.get("q2", "").lower()
        q3 = request.form.get("q3", "").lower()

        if "martikkel" in q1:
            tulemus += 1
        if "isikuandmed" in q2 or "kontonumber" in q2:
            tulemus += 1
        if "avaleht" in q3:
            tulemus += 1

    return render_template("kontroll.html", tulemus=tulemus)
    
        
if __name__ == '__main__':
    app.run(debug=True)
