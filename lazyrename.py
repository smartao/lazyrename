#!/usr/bin/python3
# lazyrename.py - Renomeia arquivos a baseado em um regex
# Utilizacao: python3 lazyrename.py t stringxpto /diretorio/dos/arquivos
#             python3 lazyrename.py r stringxpto /diretorio/dos/arquivos
#

import errno
import sys
import shutil
import os
import re

# Validando quantidade de argumentos necessários
if len(sys.argv) < 4:  # Se o numero de argumentos for menor que 4
    print('Informe 3 argumentos: execucao regex diretorio, Ex:')
    print('python3 {} (r/t) strremover /home/dir/files'.format(sys.argv[0]))
    print('r = Remover t = Testar')
    sys.exit(errno.EPERM)  # saindo do programa com mensagem

if not os.path.exists(sys.argv[3]):
    print('Diretorio nao existe!')
    sys.exit(errno.EPERM)
else:
    execucao = sys.argv[1]
    regex = sys.argv[2]
    dir = sys.argv[3]
    os.chdir(dir)  # Atualizando diretorio de trabalho

datePattern = re.compile(r"""^(.*?) # todo o texto antes da string (1)
    ((_)?{})        # String que desejamos remover (2 e 3)
    (.*?)$          # Todo o texto apos a string para remover (4)
    """.format(regex), re.IGNORECASE | re. VERBOSE)

# Andando por todos os diretorios e subdiretorios
for folderName, subfolders, filenames in os.walk(dir):
    # Atribindo o nome dos arquivos por uma variavel
    for wrongFilename in filenames:
        # Verificando se arquivo bate com a regex
        mo = datePattern.search(wrongFilename)

        # Ignora os arquivos que nao batem com a regex
        if mo is None:
            continue  # Faz o Loop volta para o inicio

        # Obetendo as diferentes partes do nome do arquivo
        beforePart = mo.group(1)
        afterPart = mo.group(4)

        correctFilename = beforePart + afterPart

        # Obtem os paths absolutos completo do arquivos
        absWorkingDir = os.path.abspath(folderName)
        wrongFilename = os.path.join(absWorkingDir, wrongFilename)
        correctFilename = os.path.join(absWorkingDir, correctFilename)

        if execucao == 'r':
            print('Renomeando: \n"%s" para\n"%s"' %
                  (wrongFilename, correctFilename))
            shutil.move(wrongFilename, correctFilename)
        else:
            print('Sera renomeado: \n"%s" para\n"%s"' %
                  (wrongFilename, correctFilename))
