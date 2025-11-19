# AlaweinOS Shared Scripts

This directory contains utility scripts that work across the AlaweinOS monorepo.

---

## Available Scripts

### Development Setup
Scripts to set up development environment across systems.

### Testing
Scripts to run tests across multiple systems.

### Quality Checks
Scripts for linting, formatting, and type checking.

---

## Usage

All scripts should be run from the repository root:

```bash
# From repository root
./scripts/script-name.sh
```

---

## Script Guidelines

### Creating New Scripts

1. **Place in this directory** if it applies to multiple systems
2. **Make executable:**
   ```bash
   chmod +x scripts/your-script.sh
   ```
3. **Add documentation:**
   - Script purpose at top
   - Usage examples
   - Requirements

4. **Update this README:**
   - Add script to appropriate section
   - Document parameters and options

### Script Template

```bash
#!/usr/bin/env bash
# Script: script-name.sh
# Purpose: Brief description of what this script does
# Usage: ./scripts/script-name.sh [options]

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Script implementation
```

---

## System-Specific Scripts

For scripts specific to a single system, place them in that system's directory:
- **MEZAN**: `/MEZAN/scripts/`
- **TalAI**: Module-specific scripts
- **optilibria**: `/optilibria/scripts/`
- **SimCore**: `/SimCore/scripts/`
- **qmlab**: `/qmlab/scripts/`

---

## Contributing

When adding scripts:
1. Follow the script template
2. Test thoroughly
3. Document clearly
4. Update this README

See [CONTRIBUTING.md](../CONTRIBUTING.md) for general guidelines.

---

## Contact

For questions about scripts:
- Open an issue on GitHub
- Contact: meshal@berkeley.edu

---

**Last Updated:** 2025-11-19
