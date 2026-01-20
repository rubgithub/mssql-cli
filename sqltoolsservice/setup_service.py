#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys

# Get the directory where this script is located (mssqltoolsservice folder)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Get the project root directory
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))

# Add directories to path to ensure imports work regardless of execution context
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import utility
import mssqlcli.mssqltoolsservice.externals as mssqltoolsservice

def install():
    """
    Downloads and installs the appropriate .NET SqlToolsService binaries.
    This is called during 'uv tool install' or via 'mssql-cli-setup'.
    """
    print('Running SQL engine setup...')
    
    # 1. Identify the current platform
    current_plat = mssqltoolsservice.get_current_platform()
    
    if not current_plat:
        print('Error: Could not determine the current platform.')
        sys.exit(1)

    print('Current platform identified: {}'.format(current_plat))

    # 2. Download the .NET 8 binary for the specific architecture
    print('Downloading SqlToolsService binaries for {}...'.format(current_plat))
    try:
        mssqltoolsservice.download_sqltoolsservice_binaries()
    except Exception as e:
        print('Error downloading binaries: {}'.format(e))
        sys.exit(1)

    # 3. Extract binaries into the package's bin directory
    print('Installing SqlToolsService for {}...'.format(current_plat))
    try:
        mssqltoolsservice.copy_sqltoolsservice(current_plat)
    except Exception as e:
        print('Error extracting binaries: {}'.format(e))
        sys.exit(1)

    print('Finished engine setup for {}.'.format(current_plat))

if __name__ == '__main__':
    install()