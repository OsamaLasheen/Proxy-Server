from filter_result import FilterResult


class Filter:

    def is_blocked(self, website_url: str) -> FilterResult:

        url_found_flag = False
        f = open("URLs.txt", "r")

        for x in f:
            x = x.replace("\n", "")
            if x.__eq__(website_url):
                url_found_flag = True
                break

        f.close()

        if url_found_flag:
            data = "This URL is blocked!!!!!"
            return FilterResult(is_blocked=True, message=data)

        else:
            data = "This URL is not blocked."
            return FilterResult(is_blocked=False, message=data)
