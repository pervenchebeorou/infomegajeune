import qrcode

# L'URL ou le texte que tu veux encoder dans le QR code
data = "https://pervenchebeorou.github.io/infomegajeune/"  # Remplace par l'URL ou le texte

# Créer un objet QRCode
qr = qrcode.QRCode(
    version=1,  # Version de QR code (1 est le plus petit)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
    box_size=10,  # Taille des "cases" du QR code
    border=4,  # Taille du bord du QR code
)

# Ajouter les données au QR code
qr.add_data(data)
qr.make(fit=True)

# Créer une image du QR code
img = qr.make_image(fill='black', back_color='white')

# Sauvegarder l'image générée
img.save("qrcode.png")
