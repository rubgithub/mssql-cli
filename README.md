[![Custom Version](https://img.shields.io/badge/version-1.1.0.dev2601181416-orange)](https://github.com/rubgithub/mssql-cli)
[![Python versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

# mssql-cli (Fork Python 3.10+)

> **FORK NOTE:** This is a community-maintained fork updated to support **Python 3.10, 3.11, and 3.12**. It includes patches for legacy dependencies (e.g., `collections.abc`) and integrates binaries for the SqlToolsService 
compatibility with current environments.

> **DISCLAIMER:** This project is provided "as is", without warranty of any kind, express or implied. Use it at your own risk. This fork is not officially affiliated with Microsoft or the original dbcli maintainers.

> **DEPRECATION NOTICE (Original Project):** mssql-cli is on the path to deprecation, and will be fully replaced by the new [go-sqlcmd](https://learn.microsoft.com/sql/tools/sqlcmd/go-sqlcmd-utility) utility once it becomes generally available.

[**mssql-cli**](https://github.com/dbcli/mssql-cli) is an interactive command line query tool for SQL Server.

![mssql-cli Autocomplete](https://github.com/dbcli/mssql-cli/raw/main/screenshots/mssql-cli-autocomplete.gif)

## Key Features
- **Auto-completion**: Fewer keystrokes needed to complete complicated queries.
- **Syntax highlighting**: Highlights T-SQL keywords.
- **Query history**: Easily complete an auto-suggested query that was previously executed.
- **Configuration file support**: Customize the experience for your needs.
- **Multi-line queries**: Execute multiple queries at once.
- **Modern Python Support**: Fully compatible with Python 3.10+.

## Installation and Usage

We recommend using [uv](https://github.com/astral-sh/uv) to manage `mssql-cli`. This ensures the tool runs in an isolated environment with the correct dependencies and binaries.

### 1. Global Installation
To install globally:
```powershell
uv tool uninstall mssql-cli
uv tool install git+https://github.com/rubgithub/mssql-cli.git@py311-fix
```

### 2. Run
```powershell
mssql-cli -S localhost -U sa -C