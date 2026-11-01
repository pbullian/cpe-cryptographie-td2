# TD2 — Missions du Bureau : crypto moderne

**CPE Lyon · 3IRC · Cryptographie et protocoles pour la sécurité informatique**
Travaux dirigés de Pablo Bullian.

Cinq missions courtes, au format CTF : chiffrement symétrique (AES), RSA, signatures numériques et échange de clés Diffie-Hellman.

> **Niveau :** découverte · **Durée :** ~1h30 · **Drapeau :** `CPE{...}`
> Chaque drapeau s'obtient en lançant des outils sur les données fournies.

## Mise en route (tout tourne dans Docker)

```bash
docker compose -f docker-compose.student.yml up -d --build
docker compose -f docker-compose.student.yml run --rm toolbox bash
# fichiers des missions : /files (lecture seule) · dossier de travail : /work (= ./work sur votre poste)
```

- **Site du Bureau** : <http://localhost:8080> depuis votre navigateur, `http://site` depuis la toolbox.
- **Service de chiffrement du Bureau** : adresse donnée en cours.
- Pour tout arrêter : `docker compose -f docker-compose.student.yml down`.

---

## S1 — Quel mode ? · *symétrique*

Le Bureau a intercepté `/files/s1/message.enc`. Un informateur nous a remis la clé (`cle.hex`) et l'IV (`iv.hex`) : c'est de l'AES-128. Le mode opératoire, lui, reste inconnu.

## S2 — L'image qui fuit · *symétrique*

Le service de chiffrement du Bureau transmet une image classifiée, chiffrée en AES-128. La clé ne quitte jamais le Bureau. Le service est documenté sur sa page d'accueil.

## A1 — RSA à la main · *asymétrique*

`/files/a1/rsa_a_la_main.txt` : la clé publique de Bob et un message d'Alice.

## A3 — Le bon logiciel · *signature*

Le site du Bureau propose l'outil d'activation sur trois miroirs. Chaque version donne une clé d'activation différente ; une seule est authentique.

## A5 — Diffie-Hellman écouté · *échange de clés*

`/files/a5/capture_dh.txt` : un échange Diffie-Hellman intercepté entre Alice et Bob, suivi d'un message chiffré.

---

## Rendu

Pour chaque mission : le **drapeau** `CPE{...}` + **2–3 phrases** : quelle faiblesse avez-vous exploitée, et qu'aurait dû faire le Bureau ?
