class Website:
    def __init__(self, is_cached: bool, response):
        self.is_cached = is_cached
        self.response = response

    def get_website(self):
        return self
