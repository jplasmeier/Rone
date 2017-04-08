# Rone

Rone is a tool for updating local files periodically. 

Steps (per file):

* Use wget to download the from a URL 
* make sure it’s actually the filetype specified 
* Run cksum on old file
* Run cksum on new file
* Compare - if different, replace and trigger next steps

Config Needed (per file):
* URL
* filetype
* file name (use wget option to standardize)
* asset directory (old file)  

