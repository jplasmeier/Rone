# Rone Asset Schema

class Asset():
    """
    An asset for Rone to manage downloading and updating for.
    """

    def __init__(self, url, filetype, filename, asset_path):
        self.url = url
        self.filetype = filetype
        self.filename = filename
        self.asset_path = asset_path

asset_list = []

college_scorecard = Asset(
    url="https://ed-public-download.apps.cloud.gov/downloads/Most-Recent-Cohorts-All-Data-Elements.csv",
    filetype="csv",
    filename="college_scorecard.csv",
    asset_path="./assets/")

asset_list.append(college_scorecard)

def get_list_of_assets():
    return asset_list
        
