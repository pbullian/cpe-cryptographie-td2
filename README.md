# TD2 — Missions du Bureau : crypto moderne

**CPE Lyon · 3IRC · Cryptographie et protocoles pour la sécurité informatique**
Travaux dirigés de Pablo Bullian.

Cinq missions courtes, au format CTF : chiffrement symétrique (AES), RSA, signatures numériques et échange de clés Diffie-Hellman.


> **Niveau :** découverte · **Durée :** ~1h30 · **Drapeau :** `CPE{...}`
> Chaque drapeau s'obtient en lançant des outils sur les données fournies.

## Prologue

Au sous-sol d'un immeuble sans plaque, quai Saint-Antoine à Lyon, le **Bureau Central du Chiffre** forme ses nouvelles recrues d'une manière bien à lui : il rejoue les grandes affaires de la **guerre froide**, transposées avec les outils d'aujourd'hui. Les décors ont changé, les erreurs sont restées les mêmes.

Cinq dossiers sont posés sur la table. Quatre sont des affaires déclassifiées, **inspirées de faits réels**. Le cinquième porte un tampon que personne n'a jamais vu au Bureau : il est daté de **2045**.

Pas de nom de code, pas d'arme : un terminal et une boîte à outils. Cinq missions, cinq drapeaux. *Le Bureau nie toute implication.*

## Mise en route (tout tourne dans Docker)

```bash
docker compose -f docker-compose.student.yml up -d --build      # lance la toolbox et les services des missions
docker compose -f docker-compose.student.yml run --rm toolbox bash
```

Dans la toolbox, les fichiers des missions sont dans `/files` (lecture seule) et votre dossier de travail est `/work` (= `./work` sur votre poste). Les adresses à utiliser sont indiquées dans chaque mission.

Pour tout arrêter : `docker compose -f docker-compose.student.yml down`.

---

## S1 — Quel mode ? · *symétrique*

> **Dossier PIMLICO.** *Juillet 1985.* Oleg Gordievsky, colonel du KGB et agent secret du MI6 depuis onze ans, se sait démasqué. Un sac de supermarché à la main, il se poste au coin d'une rue de Moscou : c'est le signal. Quelques jours plus tard, il franchit la frontière finlandaise caché dans le coffre d'une voiture diplomatique britannique.
>
> *Version du Bureau.* Au poste-frontière, notre informateur n'a que quelques secondes. Il glisse au douanier un ticket de métro griffonné et disparaît. Au dos : une clé et un IV. Le même soir, nos antennes captent une transmission chiffrée.

Le message intercepté est dans `/files/s1/message.enc`, avec la clé (`cle.hex`) et l'IV (`iv.hex`) du ticket. C'est de l'AES-128. Le mode opératoire, lui, est parti avec l'informateur.

## S2 — L'image qui fuit · *symétrique*

> **Dossier TEMPEST.** *1943, laboratoires Bell.* La machine de chiffrement 131-B2 de l'armée américaine est réputée inviolable. Jusqu'au jour où un ingénieur remarque, à l'autre bout de la pièce, un oscilloscope dont les pics suivent chaque lettre tapée : on peut lire le message en clair sans toucher à la machine. Pendant toute la guerre froide, les deux blocs traqueront ces fuites sous le nom de code TEMPEST. Le chiffrement était parfait ; c'est le reste qui parlait.
>
> *Version du Bureau.* Le Bureau vient d'installer un service pour transmettre ses images classifiées à nos ambassades. Le directeur en est très fier : « AES-128, la clé ne sort jamais d'ici. » Avant de lui confier les plans de défense, il vous demande de jouer l'espion adverse. Une image classée **TOP SECRET** vient d'être transmise.

**Service de chiffrement du Bureau** : son adresse est donnée par l'enseignant en début de séance. Il est documenté sur sa page d'accueil. La clé ne quitte jamais le Bureau.

## A1 — RSA à la main · *asymétrique*

> **Dossier NICKEL.** *Brooklyn, 1953.* Un jeune livreur de journaux laisse tomber une pièce de cinq cents : elle s'ouvre en deux. À l'intérieur, un microfilm couvert de chiffres. Le FBI mettra quatre ans à le lire : il faudra qu'un espion soviétique passe à l'Ouest pour expliquer son chiffre, entièrement fait au crayon. *Août 1977* : dans sa rubrique du *Scientific American*, Martin Gardner présente au grand public un chiffre révolutionnaire « qui demanderait des millions d'années à casser » : RSA.
>
> *Version du Bureau.* Nom de code **BOB** : un diplomate de l'Est qui veut passer à l'Ouest. Il a découpé l'article de Gardner et fabriqué sa paire de clés RSA au crayon, sur un carnet à spirale. Il a publié sa clé publique dans les petites annonces d'un journal genevois. Notre agent **ALICE** vient de lui répondre. Si nous pouvons lire ce message, le contre-espionnage adverse le peut aussi.

`/files/a1/rsa_a_la_main.txt` : la clé publique de Bob et le message d'Alice.

## A3 — Le bon firmware · *signature*

> **Dossier NEUROLIEN.** *Lyon, 2045.* Les implants neuronaux sont devenus aussi banals que les téléphones l'étaient au début du siècle. Le vôtre, un **NX-7** logé dans l'avant-bras gauche, réclame la mise à jour **Neurolien v2.1**. Trois corporations rivales la distribuent et se disputent votre cortex : **Amadrone**, **SpaceY** et **Looker**. Depuis cette nuit, la rumeur parle de serveurs piratés. Un mauvais firmware, et votre cerveau travaille pour quelqu'un d'autre.

Les trois corporations proposent le firmware. Chaque version donne une clé d'activation différente ; une seule est authentique.

| Corporation | Depuis votre navigateur | Depuis la toolbox |
|---|---|---|
| Amadrone | <http://localhost:8081> | `http://amadrone` |
| SpaceY | <http://localhost:8082> | `http://spacey` |
| Looker | <http://localhost:8083> | `http://looker` |

## A5 — Diffie-Hellman écouté · *échange de clés*

> **Dossier IVY BELLS.** *Années 1970, mer d'Okhotsk.* Un sous-marin américain se pose par 120 mètres de fond et pose une bretelle d'écoute sur un câble sous-marin soviétique. Persuadée que personne ne pourrait jamais l'atteindre, la marine soviétique y faisait passer ses communications presque sans protection. L'écoute durera des années, jusqu'à ce qu'un ancien analyste de la NSA vende le secret au KGB.
>
> *Version du Bureau.* Deux sous-marins adverses, l'*Amiral Korsakov* et le *Volna*, remontent vers le détroit de Gibraltar. Pour se parler, ils commencent par un échange de clés Diffie-Hellman, puis chiffrent leurs ordres. Leur matériel de bord date de l'époque d'Ivy Bells. Le capitaine de corvette Morel pose le relevé de la station d'écoute de Toulon sur votre bureau : « S'ils préparent une attaque, je veux le savoir avant l'aube. »

`/files/a5/capture_dh.txt` : l'échange intercepté entre les deux sous-marins, suivi de leur message chiffré.

---

## Rendu

Pour chaque mission : le **drapeau** `CPE{...}` + **2–3 phrases** : quelle faiblesse avez-vous exploitée, et qu'aurait dû faire celui qui l'a commise ?
