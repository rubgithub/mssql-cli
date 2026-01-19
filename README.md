# mssql-cli (Modernized Fork)

[![Build and Release](https://github.com/rubgithub/mssql-cli/actions/workflows/release.yml/badge.svg?branch=py311-fix)](https://github.com/rubgithub/mssql-cli/actions/workflows/release.yml)

> [!IMPORTANT]
> **Active Development:** The updated version of this tool, including support for **Python 3.12+**, **.NET 8.0**, and **macOS Apple Silicon**, is located in the `py311-fix` branch.

## 🚀 Get the Working Version

The original `mssql-cli` is currently unmaintained. This fork fixes critical issues with modern Python versions and modern operating systems.

### 1. Browse the Updated Code
Check out the active branch here:
👉 **[mssql-cli (branch: py311-fix)](https://github.com/rubgithub/mssql-cli/tree/py311-fix)**

### 2. Download Standalone Binaries
If you don't want to manage Python environments, we provide pre-compiled binaries for:
* 🪟 **Windows** (x64)
* 🐧 **Linux** (x64)
* 🍎 **macOS** (ARM64 - M1/M2/M3)

Download them from the **[Releases Section](https://github.com/rubgithub/mssql-cli/releases)**.

---

## ✨ Improvements in this Fork

* **Python Compatibility:** Fixed for 3.10, 3.11, and 3.12.
* **Modern Engine:** Upgraded `SqlToolsService` to **.NET 8.0**.
* **Privacy Focused**: Microsoft telemetry collection has been removed to avoid execution errors.
* **Native macOS:** First version to support Apple Silicon natively (no Rosetta required).
* **Automated CI/CD:** Fully automated builds using GitHub Actions.

## 📦 Installation via uv

You can install this fork directly using `uv`:

```bash
uv tool install git+[https://github.com/rubgithub/mssql-cli.git@py311-fix](https://github.com/rubgithub/mssql-cli.git@py311-fix)
