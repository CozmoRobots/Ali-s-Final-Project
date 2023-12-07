# Professor If I used Python 3.9.13 for this code. I used the following libraries:
import qrcode # pip install qrcode.
import os # pip install os-sys.

# This is the list of art names.
art_names = [
    "Cheap AI art mountain lake trees",
    "Cheap AI art street lights and trees",
    "Edvard Munch The Scream 1893",
    "Georges Seurat A Sunday Afternoon on the Island of La Grande Jatte 1884–1886",
    "Georgia O’Keeffe Red Canna 1924",
    "Johanne Vermeer The Girl With a Pearl Earring 1632-1675",
    "René Magritte The Son of Man 1964"
]

# This is the relative path for my QR codes.
qr_code_dir = 'Cozmo-The-Art-Evaluator\QR-CODES-FOR-ART'
os.makedirs(qr_code_dir, exist_ok=True)

# I will use this function to create and save QR codes.
def create_qr_code(text, file_path):
    img = qrcode.make(text)
    img.save(file_path)

# This is the loop that will create and save the QR codes.
for art_name in art_names:
    file_name = art_name.replace(' ', '_').replace(',', '') + '.png'
    file_path = os.path.join(qr_code_dir, file_name)
    create_qr_code(art_name, file_path)
