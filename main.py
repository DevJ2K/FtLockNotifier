import subprocess
import asyncio
from datetime import datetime
import requests
import json

with open("config.json", "r") as f:
	config = json.load(f)

async def main():
	url = "http://127.0.0.1:8000/"
	params = {
		'user_id': config['user_id']
	}
	requests.post(url + 'lock', params=params)

	subprocess.run(config['lock_cmd'],shell=True, capture_output=True, executable="/bin/bash")

	requests.post(url + 'unlock', params=params)




if __name__ == "__main__":
	asyncio.run(main())
