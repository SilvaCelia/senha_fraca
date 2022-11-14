#O programa deve fazer o primeiro passo: dada uma linha, eliminar todos as vogais e todos os espaços que fazem parte da linha, e informar o resultado.


senha = str(input())
senha1 = str(" aeiou ")
resultado = ' '

for i in senha:
    if i not in senha1:
      resultado += i
print(resultado)
