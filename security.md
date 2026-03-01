# Security Documentation

## Intended Users

This repository is intended for use by:
- **Primary user**: The repository owner (student enrolled in CSE 3000: Contemporary Issues in Computer Science and Engineering)
- **Course instructors and teaching assistants**: For grading and educational purposes
- **Authorized collaborators**: Any collaborators explicitly added to the repository for group work or peer review purposes

The repository contains academic assignments, coursework, and associated data files for educational purposes only.

## Risk Assessment

### Security Threats and Concerns

**Low to Moderate Risk Level**: This repository contains academic coursework and educational materials. The primary risks include:

1. **Academic Integrity**: 
   - Unauthorized access could lead to plagiarism or academic dishonesty if assignment solutions are copied
   - Exposure of completed assignments could compromise the integrity of course assessments

2. **Repository Integrity**:
   - Unauthorized modifications could corrupt assignments or introduce malicious code


### Mitigation Factors

- This is an **academic repository** for coursework, not production software
- The risk is primarily academic rather than operational or financial

## Security Measures Implemented

The following security measures have been implemented to protect this repository:

### 1. Code Ownership (CODEOWNERS)
- A `CODEOWNERS` file is configured to designate `@batmandoescalc` and `@Divpath` as code owners
- This ensures that all changes require approval from at least one of the designated owners

### 2. Pull Request Protection Rules
- **Branch protection** is enabled for the default branch
- **Pull request approvals** are required before merging:
  - Code owner review is required (`require_code_owner_review: true`)
  - This prevents unauthorized changes from being merged directly
- Protection rules apply to:
  - Branch deletions
  - Non-fast-forward merges
  - All pull requests targeting the default branch

### 3. Access Control
- Repository access is restricted to authorized users only
- Only the repository owner and explicitly added collaborators have write access
