# Release checklist

This checklist covers an `xfh` release. CI modernization is intentionally
deferred to `example-python-project` so it can be back-ported consistently
across repositories.

## Prepare

- Confirm the intended version and supported Python versions.
- Confirm the `xfh` distribution name is still available on PyPI. A missing
  project page does not reserve a name; only a successful upload does.
- Create the PyPI project/account configuration, enable two-factor
  authentication, and prefer a narrowly scoped trusted publisher or project
  token.
- Update `project.version` in `pyproject.toml`.
- Check that the codec support table and recovery limitations match the code.
- Review `git diff`, `git status`, and the commits included since the previous
  release.

## Validate

Run the repository checks from a clean checkout:

```console
make all
```

Then verify the built artifacts rather than the source checkout:

```console
python -m venv ~/tmp/xfh-release-venv
~/tmp/xfh-release-venv/bin/python -m pip install dist/xfh-*.whl
~/tmp/xfh-release-venv/bin/xfh --help
~/tmp/xfh-release-venv/bin/python -c "import xfh; print(xfh.__file__)"
```

- Inspect the wheel and source archive file lists for missing or private data.
- Confirm `twine check dist/*` passes.
- Exercise `info`, `verify`, and `unpack` against a known fixture with the
  installed wheel.
- Confirm strict failure, output-size limiting, overwrite refusal, and salvage
  exit status/reporting still behave as documented.

## Publish

- Upload to TestPyPI first when changing packaging or publishing credentials.
- Install the exact TestPyPI artifact in a fresh environment and repeat the
  smoke test.
- Tag the reviewed release commit with the exact project version, such as
  `0.1.0`, and push the tag.
- Upload exactly the already-reviewed artifacts to PyPI; do not rebuild between
  TestPyPI and PyPI.
- Create a GitHub release from the tag with concise release notes.

The first PyPI upload bootstraps the project and therefore needs a temporary
account-wide token:

```console
read -rsp "PyPI token: " PYPI_TOKEN && echo
export PYPI_TOKEN
make release
unset PYPI_TOKEN
```

After that upload, replace it with a token scoped to the new `xfh` project.
For a TestPyPI upload, additionally set `PYPI_REPOSITORY_URL` to the TestPyPI
legacy upload endpoint.

## Verify

- Confirm the PyPI metadata, project links, license, Python requirement, wheel,
  and source archive render correctly.
- Install from PyPI in a fresh environment and repeat the fixture smoke test.
- Confirm the GitHub tag and release point to the published source.
- Announce material recovery limitations alongside the release.
