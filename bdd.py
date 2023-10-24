import sqlite3

def recuperer_eleves_par_nom(nom):
    conn = sqlite3.connect('eleves.db')
    cur = conn.cursor()
    res = cur.execute("SELECT nom, prenom, classe FROM Eleve WHERE nom = ?", (nom, ))
    eleves = res.fetchall()  # on stocke les résultats pour pouvoir les renvoyer
    conn.close()  
    return eleves  # après avoir fermé la connexion

def recuperer_eleves(saisie):
    conn = sqlite3.connect('eleves.db')
    cur = conn.cursor()
    res = cur.execute("""
        SELECT nom, prenom, classe 
        FROM Eleve 
        WHERE nom LIKE ? OR prenom LIKE ?
        """, 
        ('%' + saisie + '%', '%' + saisie + '%')
    )
    eleves = res.fetchall()  # on stocke les résultats pour pouvoir les renvoyer
    conn.close()  
    return eleves  # après avoir fermé la connexion
