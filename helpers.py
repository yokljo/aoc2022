import requests, os

dl_headers = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
	"accept-language": "en-US,en;q=0.5",
	"accept-encoding": "gzip, deflate, br",
	"cache-control": "max-age=0",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "same-origin",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
}

def getfile(index):
	filename = f"input{index}"
	if not os.path.exists(filename):
		print("Downloading...")

		with open("cookie.dat", "r") as f:
			cookie = f.read()
		dl_headers["cookie"] = cookie
			
		url = f"https://adventofcode.com/2022/day/{index}/input"
		r = requests.get(url, allow_redirects=True, headers=dl_headers)
		data = r.content
		if r.status_code != 200:
			raise Exception(f"Not available! {r.status_code}")

		with open(filename, 'wb') as f:
			f.write(data)
	return open(filename)

def getlines(index):
	with getfile(index) as f:
		lines = f.readlines()
	striplines = []
	for line in lines:
		if line.endswith("\n"):
			striplines.append(line[:-1])
		else:
			striplines.append(line)
	return striplines

def getparts(line, splitchars = " ,", fmt=None, wrap = False):
	parts = []
	part = ""
	fmt_index = 0
	def next():
		nonlocal part
		nonlocal fmt_index
		if len(part) > 0:
			if fmt is not None and len(fmt) > fmt_index:
				part_fmt = fmt[fmt_index]
				if part_fmt == "i":
					part = int(part)
				if part_fmt == "f":
					part = float(part)
			parts.append(part)
			fmt_index += 1
			if wrap and fmt_index >= len(fmt):
				fmt_index = 0
		part = ""

	for c in line:
		if c in splitchars:
			next()
		else:
			part += c
	next()
	return parts

import re
def rematch(pat, s):
	c = re.compile(pat)
	m = c.match(s)
	if m:
		return m.groups()
	else:
		return None

