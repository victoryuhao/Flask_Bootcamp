#!c:\users\vjiang\documents\github\flask_bootcamp\responsive_bar_charts\myproject\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==0.12.5','console_scripts','bokeh'
__requires__ = 'bokeh==0.12.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==0.12.5', 'console_scripts', 'bokeh')()
    )
