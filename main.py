from normal import FilaNormal
from prioritario import FilaPrioritaria

fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(10))
print(fila_teste.chama_cliente(5))

fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(17))
print(fila_teste2.chama_cliente(1))
print(fila_teste2.chama_cliente(3))
print(fila_teste2.estatistica("10/01/2020",'198','detail'))