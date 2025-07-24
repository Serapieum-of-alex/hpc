# Pre-commit Hooks with Pixi

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Overview

Pre-commit hooks are scripts that run automatically before each commit to identify and fix common issues early in the development process. This project uses [pre-commit](https://pre-commit.com/) to manage these hooks, ensuring code quality and consistency.

When integrated with [Pixi](https://prefix.dev/docs/pixi/overview), pre-commit hooks can be easily managed within your project's development environment.

## Benefits of Pre-commit Hooks

- **Catch issues early**: Identify problems before they're committed
- **Consistent code style**: Automatically format code to project standards
- **Prevent security issues**: Detect secrets, vulnerabilities, and other security concerns
- **Save time**: Avoid failed CI/CD pipelines by catching issues locally
- **Improve code quality**: Run tests and linters automatically

## Setting Up Pre-commit with Pixi

### 1. Install Pixi

If you haven't installed Pixi yet, follow the instructions on the [Pixi installation page](https://prefix.dev/docs/pixi/installation):

For Windows:
```powershell
# Using PowerShell
iwr -useb https://pixi.sh/install.ps1 | iex
```

For Linux/macOS:
```bash
# Using curl
curl -fsSL https://pixi.sh/install.sh | bash
```

### 2. Clone the Repository and Install Dependencies

```bash
git clone https://github.com/Serapieum-of-alex/hpc.git
cd hpc
pixi install
```

### 3. Install Pre-commit in the Pixi Environment

The project already has pre-commit as a development dependency in the `pyproject.toml` file. When you run `pixi install`, pre-commit will be installed in the development environment.

To verify that pre-commit is installed:

```bash
pixi run --environment dev pre-commit --version
```

### 4. Install the Pre-commit Hooks

To install the pre-commit hooks into your local git repository:

```bash
pixi run --environment dev pre-commit install
```

This will set up the git hooks script and also install the hook environments.

To install the commit message hook:

```bash
pixi run --environment dev pre-commit install --hook-type commit-msg
```

## Using Pre-commit Hooks

### Running Pre-commit Hooks Manually

To run all pre-commit hooks manually on all files:

```bash
pixi run --environment dev pre-commit run --all-files
```

To run a specific hook:

```bash
pixi run --environment dev pre-commit run <hook-id> --all-files
```

For example, to run just the black formatter:

```bash
pixi run --environment dev pre-commit run black --all-files
```

### Automatic Execution

Once installed, pre-commit hooks will run automatically when you attempt to commit changes. If any hook fails, the commit will be aborted, allowing you to fix the issues before trying again.

### Skipping Hooks

In some cases, you might need to skip pre-commit hooks:

```bash
git commit -m "Your message" --no-verify
```

However, this should be used sparingly, as the hooks are designed to maintain code quality.

## Configured Hooks

This project has the following pre-commit hooks configured:

### Code Formatting

- **black**: Python code formatter
- **isort**: Sorts Python imports
- **beautysh**: Shell script formatter

### Code Quality

- **flake8**: Python linter
- **bandit**: Security linter for Python code

### File Formatting

- **trailing-whitespace**: Removes trailing whitespace
- **end-of-file-fixer**: Ensures files end with a newline
- **mixed-line-ending**: Normalizes line endings
- **pretty-format-json**: Formats JSON files

### Security Checks

- **gitleaks**: Scans for secrets and credentials
- **detect-secrets**: Detects secrets in code
- **checkov**: Scans for security issues
- **truffleHog**: Finds credentials and secrets

### Testing

- **pytest-check**: Runs pytest with coverage
- **notebook-check**: Validates Jupyter notebooks
- **doctest**: Runs doctests in Python modules

## Customizing Pre-commit Configuration

The pre-commit configuration is stored in the `.pre-commit-config.yaml` file at the root of the repository. You can modify this file to add, remove, or configure hooks.

After modifying the configuration, update the installed hooks:

```bash
pixi run --environment dev pre-commit install
```

## Troubleshooting

### Hook Installation Issues

If you encounter issues installing hooks:

```bash
pixi run --environment dev pre-commit clean
pixi run --environment dev pre-commit install
```

### Slow Hooks

Some hooks, particularly those that run tests, can be slow. You can skip these during development:

```bash
SKIP=pytest-check,notebook-check git commit -m "Your message"
```

### Updating Hooks

To update all hooks to their latest versions:

```bash
pixi run --environment dev pre-commit autoupdate
```

## Best Practices

1. **Run hooks before pushing**: Ensure all hooks pass before pushing to remote
2. **Keep hooks updated**: Regularly run `pre-commit autoupdate`
3. **Add custom hooks**: Create local hooks for project-specific checks
4. **Document hook behavior**: Ensure team members understand what each hook does
5. **Use with CI/CD**: Run the same checks in your CI/CD pipeline

!!! note
    This documentation was generated on 2025-07-24.