import sys
import mssqlcli.mssqltoolsservice.externals as mssqltoolsservice

def install():
    current_plat = mssqltoolsservice.get_current_platform()
    if not current_plat:
        sys.exit(1)
    try:
        mssqltoolsservice.download_sqltoolsservice_binaries()
        mssqltoolsservice.copy_sqltoolsservice(current_plat)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)