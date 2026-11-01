"""Service de chiffrement du Bureau : transmet l'image classifiée, chiffrée en AES-128 avec le mode demandé.

L'en-tête BMP reste en clair pour que le fichier s'ouvre dans une visionneuse ; seuls les pixels sont chiffrés.
"""
import hashlib, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from flask import Flask, Response, request

app = Flask(__name__)
KEY = os.urandom(16)


def _archive():
    # l'image dort chiffrée dans les archives du Bureau ; on la ressort au démarrage
    k = hashlib.sha256(b'Le Bureau nie toute implication.').digest()[:16]
    n = hashlib.sha256(b'TEMPEST').digest()[:16]
    d = Cipher(algorithms.AES(k), modes.CTR(n)).decryptor()
    return d.update(open(os.path.join(os.path.dirname(__file__), 'classified.dat'), 'rb').read()) + d.finalize()


RAW = _archive()
OFF = int.from_bytes(RAW[10:14], 'little')        # start of pixel data
HEAD, PIX = RAW[:OFF], RAW[OFF:]

MODES = {
    'cbc': lambda: modes.CBC(os.urandom(16)),
    'ctr': lambda: modes.CTR(os.urandom(16)),
    'ecb': lambda: modes.ECB(),
}

PAGE = """<!doctype html><html lang="fr"><meta charset="utf-8"><title>Service de chiffrement du Bureau</title>
<body style="font-family:system-ui,sans-serif;max-width:720px;margin:0 auto;padding:24px 16px;background:#f4f1ea">
<h1>Service de chiffrement du Bureau</h1>
<p>Le Bureau transmet ses images classifiees chiffrees en <strong>AES-128</strong>.
Vous pouvez recuperer la derniere image transmise, chiffree avec le mode de votre choix.</p>
<ul>
<li><code>GET /image</code> &mdash; mode par defaut (<code>cbc</code>)</li>
<li><code>GET /image?mode=MODE</code> &mdash; modes disponibles : <code>cbc</code>, <code>ctr</code>, <code>ecb</code></li>
</ul>
<p>La cle reste au Bureau. L'en-tete du fichier BMP n'est pas chiffre, seuls les pixels le sont.</p>
</body></html>"""


@app.get('/')
def index():
    return PAGE


@app.get('/image')
def image():
    mode = request.args.get('mode', 'cbc').lower()
    if mode not in MODES:
        return f'mode inconnu : {mode} (modes : cbc, ctr, ecb)\n', 400
    enc = Cipher(algorithms.AES(KEY), MODES[mode]()).encryptor()
    body = HEAD + enc.update(PIX) + enc.finalize()
    return Response(body, mimetype='image/bmp',
                    headers={'Content-Disposition': f'attachment; filename=image-{mode}.bmp'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)), threaded=True)
