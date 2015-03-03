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