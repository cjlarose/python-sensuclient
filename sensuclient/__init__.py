import requests

class Client(object):
    def __init__(self, host):
        self.host = host
        self.clients = ClientManager(self.host + '/clients')
        self.checks = CheckManager(self.host + '/checks')

class ResourceManager(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def _get(self, endpoint, *args, **kwargs):
        r = requests.get(self.prefix + endpoint, *args, **kwargs)
        #print self.prefix + endpoint
        #print r.status_code
        r.raise_for_status()
        #print r.headers
        #print r.text
        return r.json()

    def _post(self, endpoint, *args, **kwargs):
        r = requests.post(self.prefix + endpoint, *args, **kwargs)
        r.raise_for_status()
        return r

    def _delete(self, endpoint, *args, **kwargs):
        r = requests.delete(self.prefix + endpoint, *args, **kwargs)
        r.raise_for_status()
        return r

class ClientManager(ResourceManager):
    def list(self):
        return self._get('')
    
    def get(self, name):
        return self._get('/%s' % name)

    def delete(self, name):
        return self._delete('/%s' % name)

class CheckManager(ResourceManager):
    def list(self):
        return self._get('')

    def get(self, name):
        return self._get('/%s' % name)

    def request(self, name, subscribers):
        payload = {
            'name': name,
            'subscribers': subscribers,
        }
        return self._post('/request', data=payload)
