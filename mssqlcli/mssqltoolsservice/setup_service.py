import os
import sys
import mssqlcli.mssqltoolsservice.externals as mssqltoolsservice

def install():
    """Download and install binaries when running from an installed package."""
    print('Downloading SqlToolsService binaries...')
    current_plat = mssqltoolsservice.get_current_platform()
    
    if not current_plat:
        print('Error: Could not determine platform.')
        sys.exit(1)

    try:
        mssqltoolsservice.download_sqltoolsservice_binaries()
        mssqltoolsservice.copy_sqltoolsservice(current_plat)
        print(f'Finished setup for {current_plat}.')
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    install()