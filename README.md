# TUTORIAL - Configuração e execução do experimento de packet padding utilizando MININET

Este documento descreve o passo a passo para configurar e executar o experimento.

## Requisitos
- Python 3
- Mininet
- Bibliotecas Matplotlib e Pandas
- Permissão para executar comandos como `sudo`

## Passo a Passo para Execução

### 1. Crie um ambiente virtual
Para garantir um ambiente isolado e evitar conflitos com outras dependências, siga os passos abaixo para criar um ambiente virtual em Python:

```bash
# Crie o ambiente virtual
python -m venv suavenv

# Ative o ambiente virtual:
# No Linux/macOS:
source suavenv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 2. Instale o MININET na sua máquina

```bash
sudo apt-get install mininet
```

### 3. Execute o script para criar o ambiente de testes
O script `experimento.sh` automatiza a criação do ambiente de testes. Para executá-lo, utilize o seguinte comando:

```bash
sudo ./experimento.sh
```

Esse script configurará os componentes necessários para o experimento.

### 4. Gerando os gráficos do experimento
Agora dentro da pasta experimento/

Execute:
```bash
python3 gera.py
```


## Observações
- Caso encontre problemas de permissão, verifique se o script possui permissão:

```bash
chmod +x experimento.sh
```

