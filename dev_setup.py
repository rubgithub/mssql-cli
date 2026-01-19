#!/usr/bin/env python
from __future__ import print_function

import os
import sys
import utility
import mssqlcli.mssqltoolsservice.externals as mssqltoolsservice

print('Running dev setup...')
print('Root directory \'%s\'\n' % utility.ROOT_DIR)

# 1. Identify the platform (Windows, Linux or macOS ARM64/Intel)
current_plat = mssqltoolsservice.get_current_platform()

if not current_plat:
    print('Error: Could not determine current platform.')
    sys.exit(1)

print('Current platform identified: {}'.format(current_plat))

# 2. Download binaries for the specific platform 
mssqltoolsservice.download_sqltoolsservice_binaries()

# 3. Clean bin folder
print('Installing sqltoolsservice for {}...'.format(current_plat))
mssqltoolsservice.copy_sqltoolsservice(current_plat)

print('Finished dev setup.')