[![Custom Version](https://img.shields.io/badge/version-1.1.0.dev2601181416-orange)](https://github.com/rubgithub/mssql-cli)
[![Python versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![Build and Release EXE](https://github.com/rubgithub/mssql-cli/actions/workflows/release.yml/badge.svg)](https://github.com/rubgithub/mssql-cli/actions/workflows/release.yml)

# mssql-cli (3.10+ Fork)

> **DEPRECATION NOTICE (Original Project):** mssql-cli is on the path to deprecation, and will be fully replaced by the new [go-sqlcmd](https://learn.microsoft.com/sql/tools/sqlcmd/go-sqlcmd-utility) utility once it becomes generally available.

> **FORK NOTE:** This is a community-maintained fork updated to support **Python 3.10, 3.11, and 3.12**. It includes patches for legacy dependencies and integrates updated binaries for the SqlToolsService to ensure compatibility with current environments. **Telemetry has been completely disabled in this fork for better stability and privacy.**

> **DISCLAIMER:** This project is provided "as is", without warranty of any kind. This fork is not officially affiliated with Microsoft or the original dbcli maintainers.

## ⚠️ Maintenance Policy
**This fork is strictly for compatibility.** The primary goal of this repository is to ensure `mssql-cli` remains functional and installable on modern Python versions (3.10+). 
- **No New Features:** There is no intention to add new functionalities or support for new database technologies.
- **Limited Support:** Support is limited to fixing installation issues and ensuring the tool runs on current Python environments.
- **Legacy Focus:** This is a "maintenance-only" project to keep a classic tool alive.

[**mssql-cli**](https://github.com/dbcli/mssql-cli) is an interactive command line query tool for SQL Server.

![mssql-cli Autocomplete](https://github.com/dbcli/mssql-cli/raw/main/screenshots/mssql-cli-autocomplete.gif)

## Key Features
- **Auto-completion**: Fewer keystrokes needed to complete complicated queries.
- **Syntax highlighting**: Highlights T-SQL keywords.
- **Modern Python Support**: Fully compatible with Python 3.10, 3.11, and 3.12.
- **Standalone Binary**: Available as a single executable for Windows (no Python required).
- **Privacy Focused**: Microsoft telemetry collection has been removed to avoid execution errors.

---

## Installation and Usage

### Option 1: Standalone Executable (Recommended for Windows)
Download the latest `mssql-cli-windows.exe` from our [Releases Page](https://github.com/rubgithub/mssql-cli/releases). 
No Python installation is required. Just download and run:
```powershell
.\mssql-cli-windows.exe -S localhost -U sa -C
```

### Option 2: Managed Installation via uv
If you use uv, you can install the tool globally:
```powershell
uv tool install git+https://github.com/rubgithub/mssql-cli.git@py311-fix
```

### Option 3: Building from Source

```powershell
git clone https://github.com/rubgithub/mssql-cli.git
cd mssql-cli
git checkout py311-fix

uv pip compile pyproject.toml -o requirements.txt
uv pip sync requirements.txt

uv pip install pyinstaller
uv run pyinstaller --onefile --name "mssql-cli" `
    --collect-all "mssqlcli" `
    --add-data "mssqlcli/mssqltoolsservice/bin;mssqlcli/mssqltoolsservice/bin" `
    --add-data "mssqlcli/packages/mssqlliterals/*.json;mssqlcli/packages/mssqlliterals" `
    --hidden-import "pyodbc" `
    mssqlcli/main.py
```


_The resulting binary will be available in the dist/ folder._	