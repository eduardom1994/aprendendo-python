t = "João;TV;3500|Maria;Notebook;4200|Carlos;Celular;2500|Ana;Tablet;3100"

r = t.split('|')
total_vendas = 0
maior_valor = 0
nome_maior_venda = ''

for l in r:
    nome, produto, valor_str = l.split(';')
    valor = float(valor_str)
    total_vendas += valor

    if  valor > maior_valor:
        maior_valor = valor
        nome_maior_venda = nome


print(f"Total de Vendas: {total_vendas}")
print(f"Nome do vendedor com maior venda: {nome_maior_venda} - Total: {maior_valor:.3f}")