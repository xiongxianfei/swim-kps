"""Pinned checker and Swim's local Git/manifest adaptations; no safety certification."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate


class PackageTests(unittest.TestCase):
    def test_validator_matches_pin(self):
        pin = json.loads((ROOT / 'upstream-lock.json').read_text())['validator']
        self.assertEqual(pin['sha256'], hashlib.sha256((ROOT / pin['path']).read_bytes()).hexdigest())

    def test_git_metadata_is_not_knowledge(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'package'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.pytest_cache'))
            path = root / '.git' / 'internal.md'
            path.parent.mkdir()
            path.write_text('Git tool state without knowledge metadata.')
            result = validate.validate(root)
            self.assertTrue(result['ok'], result['errors'])

    def test_manifest_detects_content_changes_and_excludes_tool_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'package'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.pytest_cache'))
            payload = validate.manifest_payload_files(root)
            (root / 'MANIFEST.sha256').write_text(''.join(
                validate.sha(p) + '  ' + p.relative_to(root).as_posix() + '\n' for p in payload))
            for name in ('.git/objects/fixture', '__pycache__/fixture.pyc', '.pytest_cache/state'):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('Tool state, not publication content.')
            result = validate.validate(root, manifest=True)
            self.assertTrue(result['ok'], result['errors'])
            readme = root / 'README.md'
            original = readme.read_bytes()
            readme.write_bytes(original + b'\nChanged publication content.\n')
            result = validate.validate(root, manifest=True)
            self.assertIn('manifest-hash', {e['code'] for e in result['errors']})
            readme.write_bytes(original)
            (root / 'unexpected.txt').write_text('Unexpected payload.')
            result = validate.validate(root, manifest=True)
            self.assertIn('manifest-coverage', {e['code'] for e in result['errors']})


if __name__ == '__main__':
    unittest.main(verbosity=2)
