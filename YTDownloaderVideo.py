from pafy import *



def menu_texto(num, resolucao, extensao, tamanho):
    if num < 10:
        print('', num, end='       ')
    if num >= 10:
        print('', num, end='      ')
    if len(resolucao) < 8:
        print(resolucao, end='         ')
    if len(resolucao) == 8:
        print(resolucao, end='        ')
    if len(resolucao) > 8:
        print(resolucao, end='       ')
    if len(extensao) < 4:
        print(extensao, end='         ')
    if len(extensao) >= 4:
        print(extensao, end='        ')
    print(tamanho)


def info_texto(video):
    print('\n============= INFORMAÇÕES ===========')
    print(f'* Título:  {video.title}\n* Autor:   {video.author}\n* Duração: {video.duration}')
    print('=====================================\n')


def link_valido(link):
    try:
        video = new(link)
        return True
    except:
        return False


link = input('\nLink: ').strip()
while link_valido(link) == False:
    print('>>> Link inválido.')
    link = input('\nLink: ').strip()

video = new(link)
info_texto(video)
videostreams = video.videostreams

print(' NUM     RESOLUÇÃO     EXTENSÃO      TAMANHO')
print('=====   ===========   ==========    =========')
num = 0
for s in videostreams:
    num += 1
    resolucao = s.resolution
    extensao = s.extension
    tamanho   = f'{s.get_filesize() / (1024 * 1024):.2f} MB'
    menu_texto(num, resolucao, extensao, tamanho)

opcao = input('\nOpção: ').strip()
while not opcao.isnumeric() or int(opcao) > num - 1:
    print('>>> Digite uma opção válida.')
    opcao = input('\nOpção: ').strip()
opcao = int(opcao)

videostreams[opcao - 1].download()
print('>>> Donwload concluído.')
