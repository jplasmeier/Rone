# Rone Asset Schema
# Asset objects abstract out the operations on a data set

import urllib.request
import datetime

class Asset():
    """
    An asset for Rone to manage downloading and updating for.
    """

    def __init__(self, url, filetype, filename, asset_path):
        self.url = url
        self.filetype = filetype
        self.filename = filename
        self.asset_path = asset_path

    def __str__(self):
        return self.filename

    def download_latest(self, download_name=None):
        """
        Download a fresh copy of the dataset.
        download_path: the temporary destintion of this copy
        """
        print("Downloading: " + self.filename)
        if download_name is None:
            download_name = self.filename + "_TEMP" + str(datetime.datetime.now())
        
        local_filename, headers = urllib.request.urlretrieve(self.url, download_name)

        # Make sure that the returned filename matches the expected name
        assert(local_filename == download_name)

        return local_filename

asset_list = []

college_scorecard = Asset(
    url="https://ed-public-download.apps.cloud.gov/downloads/Most-Recent-Cohorts-All-Data-Elements.csv",
    filetype="csv",
    filename="college_scorecard.csv",
    asset_path="./assets/")

asset_list.append(college_scorecard)

def get_list_of_assets():
    return asset_list
        
