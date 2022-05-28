from pprint import pprint
import requests

TOKEN = 'AQAAAAAvIZ_GAADLW_Vk2SWxFU9ItGqmX6ehB4U'
file_path = ''
disk_file_path = 'test/netology/test.txt'
filename = 'test.txt'

class YaUploader:
    
    def __init__(self, token: str=TOKEN):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_href(self, disk_file_path:str=disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_file_path, "overwrite": "true"}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href', '')
        return href
    
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()            

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_file_to_disk(disk_file_path, filename)  
