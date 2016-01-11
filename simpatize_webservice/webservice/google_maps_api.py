EMPTY_STRING = ""
URL_FROM_GOOGLE = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}"


class URL:
    def create(self, request):
        if request == EMPTY_STRING:
            return URL_FROM_GOOGLE
        else:
            return EMPTY_STRING