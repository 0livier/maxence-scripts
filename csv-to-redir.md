# Goal
This little script is used to generate htaccess fragment for redirecting 404 pages - mostly because they were not migrated during the v1 -> v2 transition -
to actually working pages.

# Inner workings
You need to feed the script in STDIN a valid CSV with two columns, one for the page that is actually in 404, the other for destination.

# Usage
```bash
python ./csv-to-redir.py < exemple_data/csv-to-redir.csv | sort -u | tee htaccess-fragment
```

