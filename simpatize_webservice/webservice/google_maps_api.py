
class URL:
    def create(self, request):
        if request == "":
            return "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}"
        else:
            return ""