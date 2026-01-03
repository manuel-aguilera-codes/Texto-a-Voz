'''1. Texto a Voz . La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de herramientas de lenguaje natural), 
newspaper3k y gtts (puedes seguir las instrucciones de instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz.'''

from newspaper import Article
from gtts import gTTS
from yaspin import yaspin
from tqdm import tqdm
import time

def url_to_audio(url, output="articulo.mp3"):

    # 1. Cargar Artículo:
    article = Article(url)
    

    with yaspin(text="Procesando artículo...", color="cyan") as spinner:
        article.download()
        article.parse()
        spinner.ok("✔")

    # 2. Obtener el texto:
    text = article.text

    # 3. Convertir a voz:
    txt_speech = gTTS(text, lang='es')

    # Barra de progreso antes de guardar MP3
    print("Generando audio...")
    for _ in tqdm(range(200)):
        time.sleep(0.1)  # solo para mostrar avance
    txt_speech.save(output)

    print(f'Archivo generado: {output}')

# Use Case
url = input('Ingresa la url del articulo: ')
url_to_audio(url)