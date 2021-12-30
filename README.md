# Instruções - msfvenom_generator

### Clonar o repositório
git clone https://github.com/mickets/msfvenom_generator

### Mover para o repositório
cd msfvenom_generator

### Criar pastas "generated", "x64" e "x86"
mkdir generated
mkdir x64
mkdir x86

### Inserir os executáveis originais nas respetivas pastas "x86" ou "x64"

### Para correr o programa, correr o script com "./venom.py" ou "python3 venom.py"


## Notas:
- Para alterar o lhost, alterar o script venom.py na função "get_lhost()", linha 129 (por defeito tem o IP que estava a utilizar em testes)
- Pode-se alterar o nº de sequências raw e o nº de iterações por raw, linhas 389 e 392
- Cada scan do virustotal leva por volta de 3-4 minutos
- Terminal deve ter no mínimo 80 de largura


## Limitações:
- Apenas faz scan no VirusTotal um ficheiro de cada vez.
- Ficheiros executáveis de 64bits não fazem a reverse shell.
