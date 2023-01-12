https://stackoverflow.com/questions/59344917/cant-open-file-demo-py-errno-2-no-such-file-or-directory-when-running-thro



# Steps that worked

1. add this as the first line in your Python file — this tells Unix which interpreter to use when running this file:
`#!/usr/bin/env python3`

2. make your Python file executable so it can be run directly:

`chmod +x demo.py`

3. in crontab file (`sudo crontab -e`), include:
`sudo python executable.py`