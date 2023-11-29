def afficher_heure(h, m, s, mode):
    if mode == "12h":
        if h > 12:
            h = h - 12
            return "{:02d}:{:02d}:{:02d} PM".format(h, m, s)
        else:
            return "{:02d}:{:02d}:{:02d} AM".format(h, m, s)
    elif mode == "24h":
        return "{:02d}:{:02d}:{:02d}".format(h, m, s)

# Test de la fonction
print(afficher_heure(16, 30, 0, "12h"))  # Affiche 04:30:00 PM
print(afficher_heure(16, 30, 0, "24h"))  # Affiche 16:30:00
