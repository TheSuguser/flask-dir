"""flask_dir - Generate flask project 

Usage:
    flask_dir [Options] [<name>]

Arguments:
    <name>      The name of the flask application

Options:

"""
from __future__ import absolute_import
import sys
import os

from docopt import docopt
try:
    from flask_dir import __version__
except:
    __version__ = "flask_dir 0.0.1"

from flask_dir.template_handle import Template


def main():
    args = docopt(__doc__,version=__version__)
    
    template = Template()
    template.handle(args)

    # try:
    #     init(args)
    # except KeyboardInterrupt:
    #     sys.exit(0)
        
if __name__ == "__main__":
    main()