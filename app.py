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



from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
import os

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

        # /// Salvestame tagasiside faili "tagasiside.txt"
        with open("tagasiside.txt", "a", encoding="utf-8") as f:
            f.write(feedback_message + "\n") # /// Iga kasutaja sisestatud tagasiside salvestatakse uuele reale

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
        q4 = request.form.get("q4", "").lower()
        q5 = request.form.get("q5", "").lower()
        q6 = request.form.get("q6", "").lower()
        q7 = request.form.get("q7", "").lower()
        q8 = request.form.get("q8", "").lower()

        if "matrikkel" in q1 or "matriklinumber" in q1:
            tulemus += 1
        if "isikuandmed" in q2 or "kontonumber" in q2 or "arvelduskonto" or "pangakonto" in q2 or "pangaarve" in q2:
            tulemus += 1
        if "avaleht" in q3 or "avalehel" in q3:
            tulemus += 1
        if "kalender" in q4 or "minu kalender" in q4:
            tulemus += 1
        if "õppetulemused" in q5:
            tulemus += 1
        if "registreeringud" in q6:
            tulemus += 1
        if "õppeained" in q7:
            tulemus += 1
        if "õppekavad" in q8:
            tulemus += 1
    
    return render_template("kontroll.html", tulemus=tulemus)

app.secret_key = "salajane_võti"

ADMIN_PAROOL = "admin" 

KKK_FAIL = "kkk.txt"

def loe_kkk():
    kkk = []
    if os.path.exists(KKK_FAIL):
        with open(KKK_FAIL, "r", encoding="utf-8") as f:
            for rida in f:
                osad = rida.strip().split("||")
                if len(osad) == 4:
                    kkk.append({
                        "küsimus": osad[0],
                        "vastus" : osad[1],
                        "kategooria": osad[2]
                        "kategoorialink": osad[3]
                    })
    return kkk

def lisa_kkk(küsimus, vastus, kategooria, kategoorialink):
    with open(KKK_FAIL, "a", encoding="utf-8") as f:
        f.write(f"{küsimus}||{vastus}||{kategooria}||{kategoorialink}\n")

@app.route("/kkk")
def kkk():
    otsing = request.args.get("q", "").lower()
    kkk_list = loe_kkk()

    if otsing:
        kkk_list = [
            item for item in kkk_list
            if otsing in item["küsimus"].lower()
            or otsing in item["vastus"].lower()
        ]
    return render_template("kkk.html", kkk=kkk_list)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        parool = request.form.get("parool")
        if parool == ADMIN_PAROOL:
            session["admin_logged_in"] = True
            return redirect(url_for("admin_kkk"))
        else:
            flash("Vale parool! Proovi uuesti.")
            return redirect(url_for("admin_login"))
    
    return render_template("admin_login.html")

@app.route("/admin/kkk", methods=["GET", "POST"])
def admin_kkk():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    
    if request.method == "POST":
        küsimus = request.form["küsimus"]
        vastus = request.form["vastus"]
        kategooria = request.form["kategooria"]
        kategoorialink = request.form.get('kategoorialink')
        if kategoorialink and not kategoorialink.startswith("/"):
            kategoorialink = "/" + kategoorialink
        lisa_kkk(küsimus, vastus, kategooria, kategoorialink)
        return redirect(url_for("admin_kkk"))
    
    return render_template("admin_kkk.html", kkk=loe_kkk())

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("Oled välja logitud.")
    return redirect(url_for("kkk"))

# /// Flask route kustutamiseks
@app.route("/admin/kkk/delete/<int:index>", methods=["POST"])
def admin_kkk_delete(index):
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    kkk_list = loe_kkk()
    if 0 <= index < len(kkk_list):
        kkk_list.pop(index)
        # Salvesta uuesti faili
        with open(KKK_FAIL, "w", encoding="utf-8") as f:
            for item in kkk_list:
                f.write(f"{item['küsimus']}||{item['vastus']}||{item['kategooria']}||{item['kategoorialink']}\n")
    return redirect(url_for("admin_kkk"))





if __name__ == '__main__':
    app.run(debug=True)
