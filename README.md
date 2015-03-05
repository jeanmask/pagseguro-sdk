=======================
Python Pagseguro SDK
=======================

SDK Python para API de pagamentos do Pagseguro.

Instalação
==========
```
pip install pagseguro-sdk
```


Exemplo de uso
==============

**Listando suas transações dos últimos 30 dias**
```python
from datetime import datetime, timedelta
from pagseguro import PagseguroClient

PAGSEGURO_EMAIL = '' # Seu email ex.: seu@email.com.br
PAGSEGURO_TOKEN = '' # Token de integração gerado pelo PagSeguro
PAGSEGURO_SANDBOX = False

pg = PagseguroClient(email=PAGSEGURO_EMAIL, token=PAGSEGURO_TOKEN, sandbox=PAGSEGURO_SANDBOX)
date_start = datetime.now() - timedelta(days=30)
response = pg.get('/v2/transactions', params={'initialDate': date_start.isoformat()})
print response.xml()
```


**Criando uma transação**

Para criar uma transação siga o código abaixo, levando em consideração as nomclaturas dos nodes XML, que pode ser visto nesse link:

https://pagseguro.uol.com.br/v2/guia-de-integracao/api-de-pagamentos.html#v2-item-api-de-pagamentos-parametros-api

```python
from pagseguro import PagseguroClient

PAGSEGURO_EMAIL = '' # Seu email ex.: seu@email.com.br
PAGSEGURO_TOKEN = '' # Token de integração gerado pelo PagSeguro
PAGSEGURO_SANDBOX = False

pg = PagseguroClient(email=PAGSEGURO_EMAIL, token=PAGSEGURO_TOKEN, sandbox=PAGSEGURO_SANDBOX)

# Produtos / Itens (obrigatório no minimo um item)
items = [
    {'id': '1', 'description': 'Meu produto de teste', 'quantity': 2, 'amount': '20.00'},
    {'id': '2', 'description': 'Meu produto de teste 2', 'quantity': 1, 'amount': '30.00'}
]

# Dados do cliente (opcional)
sender = {'email': 'qualquer@email.com.br'}

# Referencia do sistema no sistema (opcional)
reference = 'A1234'

# Dados de frete (opcional)
shipping = {'type': '2', 'cost': '5.00'}

code, payment_url = pg.checkout(items, sender, reference, shipping)

print code        # C22E7BF08C8C38E334E17F8545FCC752
print payment_url # https://pagseguro.uol.com.br/v2/checkout/payments.html?code=C22E7BF08C8C38E334E17F8545FCC752
```

Documentação do Pagseguro
=========================

https://pagseguro.uol.com.br/v2/guia-de-integracao/visao-geral.html