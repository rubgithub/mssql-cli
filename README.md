[![Custom Version](https://img.shields.io/badge/version-1.1.0.dev2601181416-orange)](https://github.com/seu-usuario/mssql-cli)
[![Python versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

# mssql-cli (Python 3.10+ Fork)

> **FORK NOTE:** This is a community-maintained fork updated to support **Python 3.10, 3.11, and 3.12**. It includes patches for legacy dependencies (e.g., `collections.abc`) and integrates modern `.NET` binaries for the SqlToolsService to ensure compatibility with current environments.

> **DISCLAIMER:** This project is provided "as is", without warranty of any kind, express or implied. Use it at your own risk. This fork is not officially affiliated with Microsoft or the original dbcli maintainers.

> **DEPRECATION NOTICE (Original Project):** mssql-cli is on the path to deprecation, and will be fully replaced by the new [go-sqlcmd](https://learn.microsoft.com/sql/tools/sqlcmd/go-sqlcmd-utility) utility once it becomes generally available.

[**mssql-cli**](https://github.com/dbcli/mssql-cli) is an interactive command line query tool for SQL Server. This open source tool works cross-platform and proud to be a part of the [dbcli](https://github.com/dbcli) community. 

![mssql-cli Autocomplete](https://github.com/dbcli/mssql-cli/raw/main/screenshots/mssql-cli-autocomplete.gif)

## Key Features
- **Auto-completion**: fewer keystrokes needed to complete complicated queries.
- **Syntax highlighting**: highlights T-SQL keywords.
- **Query history**: easily complete an auto-suggested query that was previously executed.
- **Configuration file support**: customize the mssql-cli experience for your needs.
- **Multi-line queries**: execute multiple queries at once using the multi-line edit mode.
- **Modern Python Support**: Fully compatible with Python 3.10+.

## Quick Start

### Install from this Fork

```sh
To install global, run:
uv tool install --force git+https://github.com/rubgithub/mssql-cli.git@py311-fix

Run:
mssql-cli -S localhost -U sa -C
```
