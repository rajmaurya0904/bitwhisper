# Bitwhisper

Terminal tool that loads a binary file and finds headers or structures by field constraints (e.g. 'u32 length between 10 and 100 following magic PNG'), using a small declarative schema. For reverse engineers and file-format hackers.

## Installation

You can install Bitwhisper in the following ways:

### From source (editable mode)

For development, install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

This installs the package and the optional `dev` dependencies (testing and linting tools).

### From source (production)

If you only want the runtime dependencies (currently none), you can install without the dev extras:

```bash
pip install -e .
```

### From PyPI (when available)

Once published, you can install from PyPI:

```bash
pip install bitwhisper
```

To get the development dependencies when installing from PyPI:

```bash
pip install "bitwhisper[dev]"
```

However, note that the package is not yet on PyPI, so the above may not work until the first release.

## Usage

TODO: fill in as the build loop lands the core feature.

## Example

TODO.

## FAQ

TODO.

## License

MIT -- see [LICENSE](LICENSE).