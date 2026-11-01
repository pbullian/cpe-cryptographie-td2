#!/bin/sh
# NEUROLIEN v2.1 - firmware de liaison neurale pour implants NX-7
# Protocole du Consortium Neurolien. Installation par le port de l'avant-bras.
C='\033[1;36m'; Y='\033[1;33m'; G='\033[1;32m'; D='\033[2m'; N='\033[0m'
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
printf "  ${G}+------------------------------------------------------+${N}\n"
printf "  ${G}|  LIAISON NEURALE ETABLIE                             |${N}\n"
printf "  ${G}+------------------------------------------------------+${N}\n"
echo "  Cle d'activation : CPE{neurolien_e51b07}"
