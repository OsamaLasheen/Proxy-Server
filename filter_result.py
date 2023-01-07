class FilterResult:
    def __init__(self, is_blocked: bool, message: str):
        self.is_blocked = is_blocked
        self.message = message

    def get_result(self):
        return self
