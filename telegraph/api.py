import aiohttp
from io import BytesIO

async def upload(file: BytesIO) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post('https://telegra.ph/upload', data={'file': file}) as response:
            response_json = await response.json()
            return response_json