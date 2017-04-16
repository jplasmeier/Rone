# Rone

Rone is a tool for updating local files periodically. 

Steps (per file):

* Use urllib to download the from a URL 
* make sure it’s actually the filetype specified 
* Run cksum on old file
* Run cksum on new file
* Compare - if different, replace and trigger next steps

Config Needed (per file):
* URL
* filetype
* file name (used to standardize in case the incoming name changes)
* asset directory (old file)  

### Future Work:

We could use the Etag field in the header to possibly avoid running cksum. That is, if the Etags match then we are sure that the file hasn't changed. Thus we only run cksum on the files if there is a cache miss. 
