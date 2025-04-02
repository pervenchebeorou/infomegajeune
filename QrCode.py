import qrcode
from PIL import Image

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


# Ouvrir le logo
logo = Image.open("images/logomegajeune.jpg")  # Remplace par le chemin de ton logo

# Calculer la taille du logo (il doit être plus petit que le QR code)
qr_width, qr_height = img.size
logo_size = int(qr_width / 5)  # Le logo sera 1/5 de la taille du QR code
logo = logo.resize((logo_size, logo_size))

# Calculer la position du logo au centre du QR code
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Ajouter le logo au QR code
img.paste(logo, logo_position, mask=logo)

# Sauvegarder l'image générée avec le logo au centre
img.save("qrcode_with_logo.png")

# Optionnellement, afficher l'image
img.show()
