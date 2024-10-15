#!/bin/python3

import subprocess
import asyncio
import requests
import json
import os

DEV_MODE = False

base_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(base_dir, ".config.json" if DEV_MODE else "config.json")

with open(config_path, "r") as f:
	config = json.load(f)

async def main():
	url = "https://forty-two-helper-6ec37292ad42.herokuapp.com/"
	params = {
		'user_id': config['user_id']
	}
	requests.post(url + 'lock', params=params)

	subprocess.run(config['lock_cmd'],shell=True, capture_output=True, executable="/bin/bash")

	requests.post(url + 'unlock', params=params)




if __name__ == "__main__":
	asyncio.run(main())
