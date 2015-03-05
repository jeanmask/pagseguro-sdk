# encoding: utf-8

from __future__ import unicode_literals
from functools import wraps

import requests
import xmltodict


class PagseguroApiError(Exception):
    pass


class PagseguroClient(object):
    HTTP_METHODS = ['get', 'post']

    API = 'https://ws.pagseguro.uol.com.br'
    API_SANDBOX = 'https://ws.sandbox.pagseguro.uol.com.br'

    URL = 'https://pagseguro.uol.com.br'
    URL_SANDBOX = 'https://sandbox.pagseguro.uol.com.br'

    CHECKOUT_DEFAULS = {'currency': 'BRL'}

    @staticmethod
    def parse_response(response, *args, **kwargs):
        response.xml = lambda: xmltodict.parse(response.content)

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
        self.url = self.URL_SANDBOX if sandbox else self.URL

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

            kwargs['hooks'] = {'response': self.__class__.parse_response}

            if not url[:4] == "http":
                url = self.api + url

            return request_func(url, **kwargs)

        return caller

    def parse_checkout_params(self, items, sender, reference, shipping):
        params = self.CHECKOUT_DEFAULS or {}

        for ix, item in enumerate(items):
            for k, v in item.items():
                params['item{0}{1}'.format(k.capitalize(), ix + 1)] = v
        if sender:
            for k, v in sender.items():
                params['sender{0}'.format(k.capitalize())] = v
        if shipping:
            for k, v in shipping.items():
                params['shipping{0}'.format(k.capitalize())] = v
        if reference:
            params['reference'] = reference

        return params

    def payment_url(self, code):
        return '{0}/v2/checkout/payment.html?code={1}'.format(self.url, code)

    def checkout(self, items, sender=None, reference=None, shipping=None):
        params = self.parse_checkout_params(items, sender, reference, shipping)

        response = self.post('/v2/checkout', params=params)

        if response.status_code != 200:
            raise PagseguroApiError(response.text)

        response_data = response.xml()

        code = response_data['checkout']['code']

        return (code, self.payment_url(code))
