# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `gh-ec2`, a GitHub CLI extension that provides simple helper commands to interact with AWS EC2 instances. The extension is written in Python and uses bash as the entry point.

## Architecture

- **gh-ec2** (bash script): Entry point that validates dependencies (Python, AWS CLI) and handles SSH authentication before invoking the Python script
- **main.py**: Core Python application using argparse that manages EC2 instances through AWS CLI subprocess calls
- **Configuration**: Stores instance configurations in `~/.instance_list.json` with instance names, IDs, AWS profiles, and SSH key paths

## Key Components

### main.py Structure
- Uses `subprocess.run()` to execute AWS CLI commands with shell=True
- Stores instance configurations as JSON array with fields: instance_name, instance_id, profile, path_key
- Supports actions: config, list, status, start, stop, ssh, nautilus, ip
- `get_ip()` function queries AWS for public IP addresses

### Entry Point (gh-ec2)
- Validates Python and AWS CLI availability
- Ensures SSH agent is running and keys are loaded
- Passes all arguments to main.py

## Development Commands

This is a simple Python script with no build system or test framework. The project uses:
- No package manager (no requirements.txt, package.json, or pyproject.toml)
- No testing framework
- No linting or formatting tools configured
- Direct execution via `python main.py` or through the bash wrapper

## Usage Patterns

The extension follows GitHub CLI extension conventions and expects to be installed via `gh extension install matsui528/gh-ec2`. It manages AWS EC2 instances through a simple JSON configuration file and provides commands for common operations like starting, stopping, and SSH access.