# encoding: utf-8

from __future__ import unicode_literals
from functools import wraps

import requests
import xmltodict


def xml_parser(r, *args, **kwargs):
    r.xml = lambda: xmltodict.parse(r.text)


class PagseguroClient(object):
    HTTP_METHODS = ['get', 'post']
    API = 'https://ws.pagseguro.uol.com.br/'
    API_SANDBOX = 'https://ws.sandbox.pagseguro.uol.com.br'

    def __init__(self, email, token, sandbox=False, charset='utf-8'):
        """
        Inicia uma nova instancia da API

        Args:
        - email: Seu email de autenticação do Pagseguro
        - token: Token gerado pela conta do email informado
        """
        self.email = email
        self.token = token
        self.charset = charset
        self.api = self.API_SANDBOX if sandbox else self.API

    def __getattr__(self, name):
        if name not in self.HTTP_METHODS:
            raise AttributeError("%r is not an HTTP method" % name)

        # Get the Requests based function to use to preserve their defaults.
        request_func = getattr(requests, name, None)
        if request_func is None:
            raise AttributeError("%r could not be found in the backing lib"
                                 % name)

        @wraps(request_func)
        def caller(url, **kwargs):
            """Hand off the call to Requests."""
            headers = kwargs.get('headers', {})
            headers['Content-Type'] = 'application/x-www-form-urlencoded; {0}'
            headers['Content-Type'] = headers['Content-Type'].format(
                self.charset)

            params = kwargs.get('params', {})
            params['email'] = self.email
            params['token'] = self.token

            kwargs['timeout'] = kwargs.get('timeout', (1, 30))
            kwargs['headers'] = headers
            kwargs['params'] = params

            kwargs['hooks'] = {'response': xml_parser}

            if not url[:4] == "http":
                url = self.api + url

            return request_func(url, **kwargs)

        return caller
