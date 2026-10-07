---
package_version: "4.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Publishing Swim KPS on GitHub

## Key takeaway
Create a separate public swim-kps repository, review safety and publication rights, then publish via a reviewed branch and pull request.

## Summary
Create a separate public swim-kps repository, review safety and publication rights, then publish via a reviewed branch and pull request.

## Before publishing
- Review the [proposed MIT license](LICENSE) and copyright attribution. Only license your own material or properly licensed contributions; bibliographic References do not convey the linked publication's copyright.
- Confirm the package contains no private swimming notes, personal videos, identifiers or hidden secrets. Keep all private records outside Git history.
- Review [Safety](SAFETY.md), [Start here](START-HERE.md) and the two stroke Practices for claims that require in-person support.
- Establish a confidential conduct/security reporting route before advertising one.
- Verify the exact contract in [KPS Core AUTHORING.md](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md). This domain declares KPS 9.x and was originally structurally checked against 9.0.0; do not silently rewrite `validated_with`.

## Create an independent repository
Suggested owner and name: `xiongxianfei/swim-kps`. Create the public repository at https://github.com/new without mixing it into KPS Core or REM. If GitHub adds an initial LICENSE/README, preserve those intentional choices during the PR rather than overwriting blindly.

## Publish through review
1. Push this extracted repository as a new publication branch, or have an authorized GitHub integration commit the files to a new branch.
2. Open a PR to `main` labeled as the Swim public release draft.
3. Let `.github/workflows/validate.yml` run structural and regression checks.
4. Review the actual diff, citations, privacy, safety and claimed KPS contract compatibility; remember that CI cannot certify swimming safety or scientific truth.
5. Merge after human review, then tag `v4.0.1` and publish a short release note. Keep Swim versioning independent of KPS Core.

## After publication
Enable Issues and suitable branch rules, verify the [Contributor guide](CONTRIBUTING.md), and add a reciprocal link in the KPS Core README or a domain showcase if desired. Any future personal session study should remain private unless consciously and safely generalized.
