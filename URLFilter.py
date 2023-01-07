class Filter:

    def isBlocked(self,website_url: str):

        URL_found_flag = False
        f = open("URLs.txt", "r")

        for x in f:
            x = x.replace("\n", "")
            if (x.__eq__(website_url)):
                URL_found_flag = True
                break

        f.close()

        if (URL_found_flag):
            data = "This URL is blocked!!!!!"
            return (True,data)

        else:
            data = "This URL is not blocked."
            return (False,data)
