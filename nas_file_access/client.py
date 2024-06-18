# client.py

import requests
from urllib.parse import urljoin

class NASFileAccess:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.sid = None

    def login(self):
        login_url = urljoin(self.base_url, "webapi/auth.cgi")
        login_payload = {
            "api": "SYNO.API.Auth",
            "version": "6",
            "method": "login",
            "account": self.username,
            "passwd": self.password,
            "session": "FileStation",
            "format": "sid"
        }
        response = self.session.post(login_url, data=login_payload, verify=False)
        response_data = response.json()
        self.sid = response_data['data']['sid']

    def list_files(self, folder_path):
        if not self.sid:
            self.login()
        file_list_url = urljoin(self.base_url, "webapi/entry.cgi")
        file_list_payload = {
            "api": "SYNO.FileStation.List",
            "version": "2",
            "method": "list",
            "folder_path": folder_path,
            "_sid": self.sid
        }
        response = self.session.post(file_list_url, data=file_list_payload, verify=False)
        return response.json()['data']['files']

    def count_file(self, folder_path, filename):
        files = self.list_files(folder_path)
        return sum(1 for file in files if file['name'] == filename)

    def logout(self):
        if not self.sid:
            return
        logout_url = urljoin(self.base_url, "webapi/auth.cgi")
        logout_payload = {
            "api": "SYNO.API.Auth",
            "version": "6",
            "method": "logout",
            "session": "FileStation",
            "_sid": self.sid
        }
        self.session.post(logout_url, data=logout_payload, verify=False)
        self.sid = None
