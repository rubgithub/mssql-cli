import os
import platform
import sys

def get_executable_path():
    # 1. Verify if it is running inside PyInstaller
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        mssqltoolsservice_base_path = os.path.join(sys._MEIPASS, 'mssqlcli', 'mssqltoolsservice', 'bin')
    
    # 2. Debug override
    elif 'MSSQLTOOLSSERVICE_PATH' in os.environ:
        mssqltoolsservice_base_path = os.environ['MSSQLTOOLSSERVICE_PATH']
    
    # 3. Default internal path
    else:
        mssqltoolsservice_base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'bin'))

    mssqltoolsservice_name = u'MicrosoftSqlToolsServiceLayer{}'.format(
        u'.exe' if (platform.system() == u'Windows') else u'')

    mssqltoolsservice_full_path = os.path.abspath(os.path.join(mssqltoolsservice_base_path, 
                                                               mssqltoolsservice_name))

    if not os.path.exists(mssqltoolsservice_full_path):
        if not getattr(sys, 'frozen', False):
            print("SqlToolsService not found. Attempting to download binaries...")
            try:
                # AQUI ESTAVA O ERRO: Alterado de 'dev_setup' para 'setup_service'
                from . import setup_service
                setup_service.install()
            except Exception as e:
                error_message = f"Failed to download SqlToolsService: {e}. Please run 'mssql-cli-setup' manually."
                raise EnvironmentError(error_message)
        else:
            error_message = f"{mssqltoolsservice_full_path} does not exist. Packaging error."
            raise EnvironmentError(error_message)

    return mssqltoolsservice_full_path