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
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:system-ui,sans-serif;max-width:760px;margin:0 auto;padding:24px 16px;background:#f4f1ea;color:#1d1d1d;line-height:1.5}
h1{border-bottom:3px solid #1d1d1d;padding-bottom:6px}
h2{font-size:1.05em;margin-top:1.6em}
code{background:#fff;padding:1px 5px}
table{border-collapse:collapse;width:100%;font-size:.95em}
td,th{text-align:left;padding:7px 8px;border-bottom:1px solid #d6d0c4;vertical-align:top}
td code{display:inline-block;word-break:break-all}
.note{background:#fff3cd;padding:8px 10px;font-size:.95em}
</style>
<body>
<h1>Service de chiffrement du Bureau</h1>
<p>Le Bureau transmet ses images classifiées chiffrées en <strong>AES-128</strong>.
Vous pouvez récupérer la dernière image transmise, chiffrée avec le mode de votre choix.</p>
<ul>
<li><code>GET /image</code> : mode par défaut (<code>cbc</code>)</li>
<li><code>GET /image?mode=MODE</code> : modes disponibles : <code>cbc</code>, <code>ctr</code>, <code>ecb</code></li>
</ul>
<p>La clé reste au Bureau. L'en-tête du fichier BMP n'est pas chiffré, seuls les pixels le sont.</p>

<h2>Récupérer l'image</h2>
<table>
<tr><th>Depuis</th><th>Commande</th></tr>
<tr><td>la toolbox</td><td><code>curl -o /work/image.bmp http://chiffreur:8000/image</code></td></tr>
<tr><td>macOS, Linux (terminal)</td><td><code>curl -o image.bmp http://localhost:8000/image</code></td></tr>
<tr><td>Windows (PowerShell)</td><td><code>curl.exe -o image.bmp http://localhost:8000/image</code></td></tr>
<tr><td>Windows (invite de commandes)</td><td><code>curl -o image.bmp http://localhost:8000/image</code></td></tr>
</table>
<p class="note">Dans PowerShell, <code>curl</code> seul désigne une autre commande : tapez bien <code>curl.exe</code>
(ou <code>Invoke-WebRequest http://localhost:8000/image -OutFile image.bmp</code>).
Vous pouvez aussi ouvrir <a href="/image">/image</a> dans le navigateur : le fichier se télécharge.</p>
<p>L'image est au format BMP : elle s'ouvre avec Aperçu (macOS), Photos (Windows) ou la visionneuse d'images (Linux).
Récupérée depuis la toolbox, elle apparaît dans <code>./work</code> sur votre poste.</p>
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
