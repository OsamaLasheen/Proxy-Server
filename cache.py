from website import Website


class Cache:
    cached_websites = dict()

    def add_website(self, website_url: str, response):
        self.cached_websites[website_url] = response

    def get_website(self, website_url: str):
        return self.cached_websites[website_url]

    def is_cached(self, website_url: str) -> Website:
        return Website(is_cached=True, response=self.get_website(website_url=website_url)) if website_url in self.cached_websites else Website(is_cached=False, response=None)
