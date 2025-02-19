#!/bin/bash

HOSTS_LIST=(10 15 20)
PADDING_LIST=(500 1000 2000 3500 5000)

for HOSTS in "${HOSTS_LIST[@]}"; do
    for PADDING in "${PADDING_LIST[@]}"; do
        echo -e "Iniciando experimento com $HOSTS hosts e $PADDING bytes de padding.\n"
        python3 carga.py --hosts $HOSTS --padding $PADDING
        echo -e "Experimento com $HOSTS hosts e $PADDING bytes de padding concluído.\n"
    done
done

for HOSTS in "${HOSTS_LIST[@]}"; do
    echo -e "Iniciando experimento sem padding com $HOSTS hosts.\n"
    python3 sem_carga.py --hosts $HOSTS
    echo -e "Experimento sem padding com $HOSTS hosts concluído.\n"
done

echo -e "Todos os experimentos foram concluídos.\n"

cp extract_delay.sh extract_jitter.sh ijitters.sh pjitters.sh pdelays.sh experimento/

cd experimento/
mkdir -p dados/iperf_jitter dados/ping_jitter dados/ping_delay
chmod +x *.sh

echo -e "Iniciando processamento dos dados.\n"

./extract_delay.sh
./extract_jitter.sh
./pdelays.sh
./pjitters.sh
./ijitters.sh

echo -e "Processamento dos dados concluído.\n"

echo -e "Experimento finalizado.\n"

exit 0