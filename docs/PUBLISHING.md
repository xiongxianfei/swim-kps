---
language: "KPS 9.x"
package_version: "4.0.1"
---

# Publishing Swim KPS changes

## Key takeaway

Use the existing swim-kps repository and review the actual change before publication.

## Summary

`xiongxianfei/swim-kps` is the repository for this library. Ordinary maintenance uses a branch and a pull request; it does not require creating a repository, applying a ZIP or installing a publication script.

## Prepare a change

1. Read the current repository and preserve local work. Keep personal records outside Git history.
2. Update the owning document and its affected links and summaries. Follow [Swim authoring](AUTHORING.md) and [Contributing](../.github/CONTRIBUTING.md).
3. Run the checks in [Maintenance](MAINTENANCE.md). For a packaged archive, also verify its checksum inventory.
4. Open one PR to `main` when publication is authorized. Report actual local checks and inspect the remote CI result separately.

## Review and authority

Review the actual diff, source scope, privacy and publication rights. Safety-, evidence- and human-experience-related content changes need meaningful human review under [the contribution instructions](../AGENTS.md). CI checks structure; it cannot certify swimming safety or scientific truth.

Preserve the existing license and attribution. Reference records do not license the external publications. Merge according to the owner's authorization and branch protections. Create version tags and official releases only when explicitly requested.

## History and compatibility

Record actual checks and publication status in the change PR. Keep Swim versioning independent of Core and preserve the inspected contract in [Compatibility](COMPATIBILITY.md) until a separate compatibility review justifies an update.
