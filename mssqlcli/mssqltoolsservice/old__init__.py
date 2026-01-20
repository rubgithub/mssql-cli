# Template package that stores native sql tools service binaries during wheel compilation.
# Files will be dynamically created here and cleaned up after each run. 

import os
import platform
import sys

def get_executable_path():
    """
        Find mssqltoolsservice executable relative to this package.
    """
    # 1. Verify if it is running inside PyInstaller' executable
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # No PyInstaller, os arquivos são extraídos para sys._MEIPASS
        # O caminho será: temp/_MEIxxx/mssqlcli/mssqltoolsservice/bin
        mssqltoolsservice_base_path = os.path.join(sys._MEIPASS, 'mssqlcli', 'mssqltoolsservice', 'bin')
    
    # 2. Keeps the original Debug
    elif 'MSSQLTOOLSSERVICE_PATH' in os.environ:
        mssqltoolsservice_base_path = os.environ['MSSQLTOOLSSERVICE_PATH']
    
    # 3. Keep the original Logic
    else:
        mssqltoolsservice_base_path = os.path.abspath(
            os.path.join(
                os.path.abspath(__file__),
                '..',
                'bin'))

    # Format name based on platform (Mantendo sua lógica original)
    mssqltoolsservice_name = u'MicrosoftSqlToolsServiceLayer{}'.format(
        u'.exe' if (platform.system() == u'Windows') else u'')

    mssqltoolsservice_full_path = os.path.abspath(os.path.join(mssqltoolsservice_base_path, 
                                                               mssqltoolsservice_name))

    if not os.path.exists(mssqltoolsservice_full_path):
        # Only attempt automatic download if NOT running as a frozen PyInstaller binary
        if not getattr(sys, 'frozen', False):
            print("SqlToolsService not found. Attempting to download binaries...")
            try:
                from . import dev_setup
                dev_setup.install()
            except Exception as e:
                error_message = f"Failed to download SqlToolsService: {e}. Please re-install the mssql-cli package."
                raise EnvironmentError(error_message)
        else:
            # If frozen, it's a packaging error
            error_message = f"{mssqltoolsservice_full_path} does not exist in the standalone bundle."
            raise EnvironmentError(error_message)

    return mssqltoolsservice_full_path
