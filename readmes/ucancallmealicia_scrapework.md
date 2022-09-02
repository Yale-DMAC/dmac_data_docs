# scrapework

A Python framework for scraping web pages.

### Requirements

* Python 3.4+
* [`requests`](https://pypi.org/project/requests/) module
* [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) module

### Getting Started

To run:

```
$ cd git/scrapework
$ python
Python 3.6.2 |Anaconda custom (x86_64)| (default, Sep 21 2017, 18:29:43) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import scrapework
>>> s = scrapework.Scrape(vars)
>>> s.get_pages()
>>> s.parse_files()
>>>
``` 

Scrape class takes the following as arguments:

* Base URL of website to scrape - i.e. 'https://archivesgig.com'
* Path to output directory - i.e. '/Users/username/path/to/folder or 'folder'
* Desired filename for output files - i.e. 'archivesgig'
* Pagination data (optional): URL structure for paginated pages (i.e. '/pages/'), begin page number (i.e. 1), end page number (i.e. 200), step (i.e. 1) 