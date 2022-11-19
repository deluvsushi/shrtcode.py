from requests import get

class ShrtCode:
	def __init__(self) -> None:
		self.api = "https://api.shrtco.de/v2"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
		}
	
	def shorten_url(self, url: str) -> dict:
		return get(
			f"{self.api}/shorten?url={url}",
			headers=self.headers).json()
	
	def protect_url(
			self,
			url: str,
			password: str) -> dict:
		return get(
			f"{self.api}/shorten?url={url}&password={password}",
			headers=self.headers).json()
	
	def generate_emoji_url(self, url: str) -> dict:
		return get(
			f"{self.api}/shorten?emoji&url={url}",
			headers=self.headers).json()
			
	def get_url_information(self, code: str) -> dict:
		return get(
			f"{self.api}/info?code={code}",
			headers=self.headers).json()
	
	def get_status(self) -> dict:
		return get(
			f"{self.api}/status",
			headers=self.headers).json()
	
	def generate_custom_url(
			self,
			url: str,
			custom_code: str) -> dict:
		return get(
			f"{self.api}/shorten?url={url}&custom_code={custom_code}",
			headers=self.headers).json()
