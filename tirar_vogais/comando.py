texto = open('cancao_do_exilio.txt', 'r')
cripto = open('cancao_criptografada.txt', 'w')

for linha in texto.readlines():
        for letra in linha:
            if letra in 'aeiouãõáíàê':
                cripto.write('*')
            else:
                cripto.write(letra)

print('Cripto concluído com sucesso!')
texto.close()
cripto.close()
