class Website:
    def __init__(self, is_cached, response):
        self.is_cached = is_cached
        self.response = response

    def get_website(self):
        return self
