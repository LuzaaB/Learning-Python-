# Manga Downloader

A manga downloader program using MangaDex API.

## Table of Contents
- Modules Used
- Description of each file

### Modules Used :
- requests
- json
- dataclasses
- img2pdf
- typing(Dict, List)
- pathlib(Path)
- tqdm

### Description of each file
- ***chapList.json*** : example of how the json data is sent from the website
- ***chapterlist.json*** : example of how the json data is sent from the website
- ***JSON_CHAP_LIST.json*** : example of extracted contents of chapters ie. images of the chapters
- ***manga_id.py*** : main program
- ***manga_id_two.py*** : program downloads image by image (before volume wise sorting and pdf downloading)
- ***mangadl.py*** : first program (before using data_classes)
- ***pdf_converter.py*** : uses PIL to download pdf
- ***temp_manga.py*** : main program for testing and updating (making the program better)
- ***temporary.py*** : volume sorting
- ***After_the_Rain.json*** : example of all the useful data extracted from the data sent by the website  
  (contains everything needed for downloading)
- ***After the Rain.json*** : same as above but doesn't contain chapter pages (images) data
- ***volsplit.py*** : program to test new things before adding it to temp_manga.py