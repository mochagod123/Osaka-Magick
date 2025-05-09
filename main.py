import requests
import aiohttp
import json

# 大阪弁
class OsakaMagick():
    def __init__(self):
        pass

    def convert(self, text: str):
        json_data = {
            'text': text,
            'action': 'encode',
            'lang_type': 'osaka',
        }

        response = requests.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data)

        return response.json()["data"]
    
    async def async_convert(self, text: str):
        async with aiohttp.ClientSession() as session:
            json_data = {
                'text': text,
                'action': 'encode',
                'lang_type': 'osaka',
            }
            async with session.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data) as response:
                resp = json.loads(await response.text())
                return resp["data"]

# 京都弁
class KyotoMagick():
    def __init__(self):
        pass

    def convert(self, text: str):
        json_data = {
            'text': text,
            'action': 'encode',
            'lang_type': 'kyoto',
        }

        response = requests.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data)

        return response.json()["data"]
    
    async def async_convert(self, text: str):
        async with aiohttp.ClientSession() as session:
            json_data = {
                'text': text,
                'action': 'encode',
                'lang_type': 'kyoto',
            }
            async with session.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data) as response:
                resp = json.loads(await response.text())
                return resp["data"]

# 広島弁
class HiroshimaMagick():
    def __init__(self):
        pass

    def convert(self, text: str):
        json_data = {
            'text': text,
            'action': 'encode',
            'lang_type': 'hiroshima',
        }

        response = requests.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data)

        return response.json()["data"]
    
    async def async_convert(self, text: str):
        async with aiohttp.ClientSession() as session:
            json_data = {
                'text': text,
                'action': 'encode',
                'lang_type': 'hiroshima',
            }
            async with session.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data) as response:
                resp = json.loads(await response.text())
                return resp["data"]
            
# 秋田弁
class AkitaMagick():
    def __init__(self):
        pass

    def convert(self, text: str):
        json_data = {
            'text': text,
            'action': 'encode',
            'lang_type': 'akita',
        }

        response = requests.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data)

        return response.json()["data"]
    
    async def async_convert(self, text: str):
        async with aiohttp.ClientSession() as session:
            json_data = {
                'text': text,
                'action': 'encode',
                'lang_type': 'akita',
            }
            async with session.post('https://xn--urss5w6nbnz8e.com/action_text', json=json_data) as response:
                resp = json.loads(await response.text())
                return resp["data"]

# 秋田弁
# 同期処理            
# print(OsakaMagick().convert("私は山田です。\nよろしくお願いします。"))
# 非同期処理
# print(asyncio.run(OsakaMagick().async_convert("私は山田です。\nよろしくお願いします。")))

# 京都弁
# 同期処理
# print(KyotoMagick().convert("こんにちは。名前は中島です。"))
# 非同期処理
# print(asyncio.run(KyotoMagick().async_convert("私は山田です。\nよろしくお願いします。")))

# ..