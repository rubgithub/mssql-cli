import os
import sys
import platform
import tarfile
import zipfile
import requests
import utility

# SQLTOOLSSERVICE_RELEASE version
SQLTOOLSSERVICE_RELEASE = "5.0.20251227.1"
SQLTOOLSSERVICE_BASE = os.path.join(utility.ROOT_DIR, 'sqltoolsservice')

# Map platforms
SUPPORTED_PLATFORMS = {
    'manylinux1_x86_64': 'Microsoft.SqlTools.ServiceLayer-linux-x64-net8.0.tar.gz',
    'macosx_arm64': 'Microsoft.SqlTools.ServiceLayer-osx-arm64-net8.0.tar.gz',
    'macosx_x64': 'Microsoft.SqlTools.ServiceLayer-osx-x64-net8.0.tar.gz',
    'win_amd64': 'Microsoft.SqlTools.ServiceLayer-win-x64-net8.0.zip',
    'win32': 'Microsoft.SqlTools.ServiceLayer-win-x86-net8.0.zip'
}

TARGET_DIRECTORY = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', 'bin'))

def get_current_platform():
    """Identify the platform to download"""
    plat = sys.platform
    arch = platform.machine().lower()
    if plat == 'win32':
        return 'win_amd64' if '64' in arch else 'win32'
    elif plat == 'linux':
        return 'manylinux1_x86_64'
    elif plat == 'darwin':
        return 'macosx_arm64' if 'arm' in arch or 'aarch64' in arch else 'macosx_x64'
    return None

def download_sqltoolsservice_binaries():
    """Download the specific binary"""
    current_plat = get_current_platform()
    if not current_plat:
        print("Platform not supported")
        return

    packageFileName = SUPPORTED_PLATFORMS[current_plat]
    packageFilePath = os.path.join(SQLTOOLSSERVICE_BASE, current_plat, packageFileName)
    
    dir_name = os.path.dirname(packageFilePath)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    githubUrl = 'https://github.com/microsoft/sqltoolsservice/releases/download/{}/{}'.format(SQLTOOLSSERVICE_RELEASE, packageFileName)
    print('Downloading {}'.format(githubUrl))
    r = requests.get(githubUrl)
    with open(packageFilePath, 'wb') as f:
        f.write(r.content)

def copy_sqltoolsservice(platform_key):
    """Extract the binary to bin folder"""
    utility.clean_up(directory=TARGET_DIRECTORY)
    
    packageFileName = SUPPORTED_PLATFORMS[platform_key]
    copy_file_path = os.path.join(SQLTOOLSSERVICE_BASE, platform_key, packageFileName)

    print('Extracting from {}'.format(copy_file_path))
    if copy_file_path.endswith('tar.gz'):
        compressed_file = tarfile.open(name=copy_file_path, mode='r:gz')
    else:
        compressed_file = zipfile.ZipFile(copy_file_path)

    if not os.path.exists(TARGET_DIRECTORY):
        os.makedirs(TARGET_DIRECTORY)
    compressed_file.extractall(TARGET_DIRECTORY)