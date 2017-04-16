# Rone Asset Schema
# Asset objects abstract out the operations on a data set

from subprocess import getoutput, CalledProcessError, call

import datetime
import os
import urllib.request

def get_cksum(filepath):
    """
    Returns the cksum of a file.
    """
    try:
        return getoutput('cksum ' + filepath).split(' ')[0]
    except CalledProcessError as Err:
        print("Error calling cksum: " + Err)
        sys.exit(1)

class Asset():
    """
    An asset for Rone to manage downloading and updating for.
    """

    def __init__(self, url, filetype, filename, asset_path):
        self.url = url
        # This must correspond with the 'Content-Type' field in the request header.
        # e.g. 'text/csv' for .csv files
        self.filetype = filetype
        self.filename = filename
        self.asset_path = asset_path
        self.logfile = filename[:-4] + '_log.txt'

    def __str__(self):
        return self.filename

    def download_latest(self, download_name=None):
        """
        Download a fresh copy of the dataset.
        download_path: the temporary destintion of this copy
        """
        print("Downloading: " + self.filename)
        if download_name is None:
            temp_name = "_TEMP" + str(datetime.datetime.now()).replace(" ","")
            download_name = self.filename + temp_name        
        self.local_filename, self.headers = urllib.request.urlretrieve(self.url, download_name)

        # Make sure that the returned filename matches the expected name
        assert(self.local_filename == download_name)

        # Make sure that the filetypes match
        assert(self.filetype == self.headers.get('Content-Type'))

        return self.local_filename

    def compare_cksum(self):
        """
        Compares the cksum of the new and old file.
        Returns a boolean such that
        False -> cksums differ
        True -> cksums same
        """
        print("Old file: " + os.path.join(self.asset_path, self.filename))
        old_cksum = get_cksum(os.path.join(self.asset_path, self.filename))
        print("New file: " + self.local_filename)
        new_cksum = get_cksum(self.local_filename)
        print("Old cksum: " + old_cksum)
        print("New cksum: " + new_cksum)
        return old_cksum==new_cksum

asset_list = []

college_scorecard = Asset(
    url="https://ed-public-download.apps.cloud.gov/downloads/Most-Recent-Cohorts-All-Data-Elements.csv",
    filetype="text/csv",
    filename="college_scorecard.csv",
    asset_path="./assets/")

asset_list.append(college_scorecard)

def get_list_of_assets():
    return asset_list
        
