import base64
import json

import requests
from Crypto.Cipher import DES3


class Util:
    def __init__(self, settings):
        self.settings = settings
        self.__get_auth()

    def __get_auth(self):
        headers = {"Accept": "application/json"}
        response = requests.post(self.resolve_url(self.settings.access_token),
                                 headers=headers,
                                 params={"apiKey": self.settings.api_key,
                                         'secret': self.settings.secret_key}
                                 )
        if response.status_code == 200:
            body = response.json()
            if 'token' in body:
                self.token = body.get('token')
        else:
            self.token = None

            raise Exception(self.settings.get_error_msg(response.status_code),
                            response.json())

    def resolve_url(self, endpoint):
        return self.settings.url + endpoint

    def send_request(self, endpoint, data, method="post"):
        headers = {"Accept": "application/json",
                   "Authorization": self.token}
        if method == "get":
            req = requests.get(self.resolve_url(endpoint), headers=headers)
        else:
            req = requests.post(self.resolve_url(endpoint), data=data,
                                headers=headers)
        if req.status_code == 200:
            body = req.json()
            if 'status' in body:
                if body.get('status') == "success":
                    return body
                else:
                    return {'status': 'error',
                            'message': self.settings.get_error_msg(
                                body.get('code')),
                            "response": req.json()}
            return
        else:
            return {"status": "error",
                    "message": self.settings.get_error_msg(req.status_code),
                    "response": req.json()}

    def encrypt(self, message):

        block_size = 8
        padding_size = block_size - (len(message) % block_size)

        if padding_size > 0:
            message += chr(padding_size) * padding_size
        cipher = DES3.new(message, DES3.MODE_ECB)
        ciphered = cipher.encrypt(message.encode('utf-8'))
        return base64.b64encode(ciphered).decode('utf-8')
