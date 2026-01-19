#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys

# Ensure the root directory is in the path so local imports (utility, mssqlcli) work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import utility
import mssqlcli.mssqltoolsservice.externals as mssqltoolsservice

def run_setup():
    """
    Performs the development setup by downloading and installing the 
    appropriate .NET SqlToolsService binaries for the current platform.
    """
    print('Running dev setup...')
    print('Root directory: \'%s\'\n' % utility.ROOT_DIR)

    # 1. Identify the current platform (Windows, Linux, or macOS ARM64/Intel)
    # This uses the improved logic in externals.py to detect Apple Silicon
    current_plat = mssqltoolsservice.get_current_platform()
    
    if not current_plat:
        print('Error: Could not determine the current platform.')
        sys.exit(1)

    print('Current platform identified: {}'.format(current_plat))

    # 2. Download ONLY the .NET 8 binary required for this specific runner/machine
    # This fixes the "FileNotFoundError" by targeting the correct architecture
    print('Downloading SqlToolsService binaries for {}...'.format(current_plat))
    try:
        mssqltoolsservice.download_sqltoolsservice_binaries()
    except Exception as e:
        print('Error downloading binaries: {}'.format(e))
        sys.exit(1)

    # 3. Extract/Install the SqlToolsService into the package's bin directory
    # This prepares the environment for PyInstaller to bundle the application
    print('Installing SqlToolsService for {}...'.format(current_plat))
    try:
        mssqltoolsservice.copy_sqltoolsservice(current_plat)
    except Exception as e:
        print('Error extracting binaries: {}'.format(e))
        sys.exit(1)

    print('Finished dev setup for {}.'.format(current_plat))

if __name__ == '__main__':
    run_setup()