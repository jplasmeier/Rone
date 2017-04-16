# Rone - A tool for downloading files

import assets

asset_list = assets.get_list_of_assets()

print("FOund the following:")
print(''.join([str(x) for x in asset_list]))

for asset in asset_list:
    asset.download_latest()
    print("Same file?: " + str(asset.compare_cksum()))
