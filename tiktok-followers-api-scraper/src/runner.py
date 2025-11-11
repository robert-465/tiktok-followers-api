thonimport json
import requests
from tiktok_parser import TikTokParser
from exporters import Exporter

class TikTokFollowerScraper:
    def __init__(self, username=None, user_id=None, url=None):
        self.username = username
        self.user_id = user_id
        self.url = url

    def scrape_followers(self):
        if not self.username and not self.user_id and not self.url:
            raise ValueError("You must provide a username, user_id, or url.")
        
        tiktok_parser = TikTokParser(self.username, self.user_id, self.url)
        followers_data = tiktok_parser.get_followers()

        exporter = Exporter(followers_data)
        exporter.export_to_json('followers_data.json')

if __name__ == '__main__':
    scraper = TikTokFollowerScraper(username="sample_username")
    scraper.scrape_followers()