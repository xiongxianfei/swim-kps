---
language: "KPS 9.x"
package_version: "4.0.1"
---

# Maintaining Swim KPS

## Key takeaway

Use the pinned checker and focused package tests when maintaining the repository. Reading the knowledge requires no script or sibling checkout.

## Summary

This guide covers structural validation, reviewed dependency fingerprints and optional archive checks. [Contributing](../.github/CONTRIBUTING.md) covers authoring and review. Check results belong in the current PR; they do not establish swimming safety or scientific validity.

## Repository checks

Run from the repository root with Python 3 and its standard library:

```bash
python3 validate.py .
python3 -m unittest discover -s tests -v
```

The validator checks metadata, local links, structure and declared dependencies. The focused tests cover the actual package, checker integrity, Git-metadata exclusion and manifest behavior. Both commands run in CI. Common validator regression coverage stays at the pinned Core revision rather than being copied into this project.

[upstream-lock.json](../upstream-lock.json) records the checker revision, digest and local adaptations. Replacing it requires compatibility review; a documentation cleanup does not upgrade the authoring contract.

## Dependency fingerprints

Review changed source meanings and their receiving summaries before running:

```bash
python3 validate.py . --accept-reviewed-summaries
```

Ordinary validation never accepts changes automatically. Preserve LF under `.gitattributes`; resolve line-ending differences before treating changed hashes as knowledge changes.

## Packaged archive checks

The Git source tree does not keep `MANIFEST.sha256`. When an archive is requested, generate its inventory inside a clean staging copy, then verify the extracted archive:

```bash
python3 - <<'PYMANIFEST'
from pathlib import Path
import validate
root = Path('.')
Path('MANIFEST.sha256').write_text(''.join(
    validate.sha(path) + '  ' + path.relative_to(root).as_posix() + '\n'
    for path in validate.manifest_payload_files(root)
), encoding='utf-8')
PYMANIFEST
python3 validate.py . --manifest
```

The payload helper excludes Git metadata and caches while detecting changed or unexpected files. Repeat the manifest check after extraction. This checks archive bytes and coverage, not the evidence behind the content.
