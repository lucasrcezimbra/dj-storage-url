# GitHub Copilot Instructions for dj-storage-url

This document provides Copilot-specific guidelines and best practices for contributing to the `dj-storage-url` repository.

## Repository Overview

`dj-storage-url` is a Python library that enables configuring Django storage backends from URL strings. It supports various storage types including file system, memory, and S3 storage, providing a simple and consistent way to configure Django storage through URLs.

## Code Style and Formatting

### Python Code Standards
- **Line Length**: 88 characters (Black default)
- **Formatter**: Black is used for automatic code formatting
- **Linter**: Ruff with the following configuration:
  - Selected rules: `["E", "F", "I"]` (pycodestyle errors, pyflakes, isort)
  - Ignored rules: `["E501"]` (line too long, handled by Black)
- **Import Sorting**: Use isort-compatible import organization (part of Ruff configuration)

### Code Quality Guidelines
- Write clear, descriptive function and variable names
- Avoid type hints
- Add docstrings for public functions and classes
- Follow PEP 8 conventions (enforced by Ruff and Black)
- Keep functions small and focused on a single responsibility

## Development Workflow

### Prerequisites
- Python 3.9 or higher
- Poetry for dependency management

### Setup Commands
```bash
git clone https://github.com/lucasrcezimbra/dj-storage-url
cd dj-storage-url
make install  # Installs dependencies and pre-commit hooks
```

### Common Development Tasks
```bash
make lint      # Run linting (pre-commit hooks)
make test      # Run tests with pytest
make test-cov  # Run tests with coverage
make build     # Build the package
```

### Pre-commit Hooks
The repository uses pre-commit hooks that automatically run:
- Code formatting (Black)
- Linting (Ruff)
- YAML formatting
- JSON formatting
- Various file checks (trailing whitespace, file size, etc.)

## Testing Practices

### Test Framework
- **Framework**: pytest
- **Location**: `tests/` directory
- **Naming**: Test files should follow the pattern `test_*.py`
- **Configuration**: Tests are configured in `pyproject.toml`

### Test Guidelines
- Write descriptive test names that explain what is being tested
- Use class-based organization for related tests (e.g., `TestFileSystemStorage`)
- Include both positive and negative test cases
- Test edge cases and error conditions
- Use pytest fixtures for common test data setup
- Follow the Arrange-Act-Assert pattern

### Test Example Structure
```python
class TestStorageType:
    def test_basic_functionality(self):
        # Arrange
        url = "scheme://example"

        # Act
        result = parse(url)

        # Assert
        assert result == expected_output
```

## Copilot-Specific Prompts and Guidelines

### Repository-Specific Context

When asking Copilot for help, provide this context:

- "This is a Django storage configuration library"
- "URLs follow the pattern: `scheme://netloc/path?query`"
- "Output should be Django storage backend configuration dictionaries"
- "Use existing helper functions like `strtobool` for boolean conversion"
- "Follow the existing pattern in `SCHEME_TO_CONFIG` mapping"

## Contributing Guidelines

### Pull Request Checklist
- [ ] Code follows Black formatting (automatic via pre-commit)
- [ ] All Ruff linting rules pass
- [ ] Tests are included for new functionality
- [ ] Existing tests still pass
- [ ] Documentation is updated if needed
- [ ] Pre-commit hooks pass

### Code Review Focus Areas
- URL parsing correctness and edge cases
- Django storage backend compatibility
- Test coverage for new features
- Error handling and validation
- Code maintainability and readability

## Additional Resources

- [Django Storage Documentation](https://docs.djangoproject.com/en/stable/ref/files/storage/)
- [Project Documentation](https://dj-storage-url.readthedocs.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Black Code Style](https://black.readthedocs.io/)
- [Ruff Linter](https://docs.astral.sh/ruff/)

---

*This document is maintained by the project maintainers. Please update it when project conventions change.*
