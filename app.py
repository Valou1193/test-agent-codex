from flask import Flask, send_file
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/call')
def simulate_call():
    """Simulate a phone call using Google Text-to-Speech."""
    text = (
        "Bonjour, merci d'avoir appelé notre restaurant. "
        "Nous sommes ouverts de midi à 22 heures tous les jours "
        "et nous proposons des options végétariennes."
    )
    tts = gTTS(text, lang='fr')
    audio = BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    return send_file(audio, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
