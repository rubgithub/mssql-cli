# -*- coding: utf-8 -*-
import os
import platform
import sys

def get_executable_path():
    """
    Find mssqltoolsservice executable relative to this package.
    """
    # 1. Check if running inside a PyInstaller bundle
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        mssqltoolsservice_base_path = os.path.join(sys._MEIPASS, 'mssqlcli', 'mssqltoolsservice', 'bin')
    
    # 2. Check for environment variable override (Debug mode)
    elif 'MSSQLTOOLSSERVICE_PATH' in os.environ:
        mssqltoolsservice_base_path = os.environ['MSSQLTOOLSSERVICE_PATH']
    
    # 3. Default path (bin folder inside the package)
    else:
        mssqltoolsservice_base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'bin'))

    # Set executable name based on platform
    mssqltoolsservice_name = u'MicrosoftSqlToolsServiceLayer{}'.format(
        u'.exe' if (platform.system() == u'Windows') else u'')

    mssqltoolsservice_full_path = os.path.abspath(os.path.join(mssqltoolsservice_base_path, 
                                                               mssqltoolsservice_name))

    # --- AUTOMATIC DOWNLOAD LOGIC ---
    if not os.path.exists(mssqltoolsservice_full_path):
        # Only attempt download if NOT a standalone binary (PyInstaller)
        if not getattr(sys, 'frozen', False):
            print("SqlToolsService not found. Attempting to download binaries...")
            try:
                # Import the setup_service we created
                from . import setup_service
                setup_service.install()
            except Exception as e:
                error_message = f"Failed to download SqlToolsService: {e}. Please run 'mssql-cli-setup' manually."
                raise EnvironmentError(error_message)
        else:
            error_message = f"Critical Error: {mssqltoolsservice_full_path} not found in bundle."
            raise EnvironmentError(error_message)

    return mssqltoolsservice_full_path