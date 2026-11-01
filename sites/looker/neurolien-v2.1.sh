#!/bin/sh
# NEUROLIEN v2.1 - firmware de liaison neurale pour implants NX-7
# Protocole du Consortium Neurolien. Installation par le port de l'avant-bras.
# Le firmware verifie sa signature avant de s'ecrire dans le cortex :
# neurolien-v2.1.sh.sig et consortium_pub.pem doivent etre dans le meme dossier.
C='\033[1;36m'; Y='\033[1;33m'; G='\033[1;32m'; R='\033[1;31m'; D='\033[2m'; N='\033[0m'
SELF="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"; DIR=$(dirname "$SELF")
brain() {
  printf "$1"
  cat <<'ART'
                                   .-~~~~~~~-.
                                .'  _  _  _  '.
                               /  (  )(  )(  ) \
                              |  (_ ._)(_._ _)  |      C O R T E X
                               \   '-'  '-'    /
                                '._    __    _.'
                                   '-.|  |.-'
                                      |  |
ART
  printf "$N"
}
step() { printf "  %s " "$1"; sleep 0.5; }
box() { printf "  $1+------------------------------------------------------+$N\n  $1|  %-52s|$N\n  $1+------------------------------------------------------+$N\n" "$2"; }

printf '\033[2J\033[H'
printf "  ${C}NEUROLIEN v2.1${N}  ${D}installation sur implant NX-7${N}\n\n"
step 'empreinte SHA-256 du firmware ...........'
printf "${Y}%s...${N}\n" "$(openssl dgst -sha256 -r "$SELF" | cut -c1-24)"
step 'cle publique du Consortium ..............'
if [ -f "$DIR/consortium_pub.pem" ] && [ -f "$SELF.sig" ]; then
  printf "${G}presente${N}\n"
else
  printf "${R}absente${N}\n\n  Placez neurolien-v2.1.sh.sig et consortium_pub.pem a cote du firmware.\n"; exit 2
fi
step 'verification de la signature ............'
if openssl dgst -sha256 -verify "$DIR/consortium_pub.pem" -signature "$SELF.sig" "$SELF" >/dev/null 2>&1; then
  printf "${G}VALIDE${N}\n"; sleep 1
else
  printf "${R}INVALIDE${N}\n\n"; box "$R" 'FIRMWARE ALTERE : LIAISON NEURALE REFUSEE'; exit 1
fi

W=34; i=0
printf '\033[2J'
while [ $i -le $W ]; do
  printf '\033[H'
  brain "$C"
  done_=$(printf '%*s' "$i" '' | tr ' ' '=')
  left_=$(printf '%*s' "$((W - i))" '' | tr ' ' '.')
  printf "  ${D}[NEUROJACK]${N}--${C}[PORT NX-7]${N} ${Y}%s>>${N}${D}%s${N} ${C}[NERF MEDIAN]${N}\n" "$done_" "$left_"
  printf "  ${D}  avant-bras gauche${N}\n\n"
  printf "  NEUROLIEN v2.1  |  synchronisation synaptique : ${Y}%3d%%${N}   \n" $((i * 100 / W))
  i=$((i + 1)); sleep 0.08
done
for m in 'cartographie du cortex prefrontal .........' 'calibration de l hippocampe ...............' 'ecriture du firmware ......................'; do
  printf "  %s ${G}OK${N}\n" "$m"; sleep 0.4
done
printf '\033[H'; brain "$G"; printf '\033[7B\n'
box "$G" 'LIAISON NEURALE ETABLIE - signature VALIDE'
echo "  Cle d'activation : CPE{neurolien_7f3a91}"
