# AlaweinOS Shared Documentation

This directory contains documentation that applies across the entire AlaweinOS monorepo.

---

## Contents

### Getting Started
- [Quick Start Guide](getting-started.md) - Get up and running with AlaweinOS
- [Architecture Overview](architecture.md) - High-level system architecture
- [Integration Guide](integration-guide.md) - How systems integrate with each other

### Development
- See root `CONTRIBUTING.md` for contribution guidelines
- See root `PROJECT.md` for comprehensive project overview
- See root `STRUCTURE.md` for repository navigation

### System-Specific Documentation

Each system has its own `docs/` directory:
- **MEZAN**: `/MEZAN/docs/`
- **TalAI**: Module-specific documentation
- **optilibria**: `/optilibria/docs/`
- **SimCore**: `/SimCore/docs/`
- **qmlab**: `/qmlab/docs/`

---

## Documentation Organization

**Monorepo-wide (this directory):**
- Cross-system concepts
- Integration patterns
- Shared conventions
- General development guides

**System-specific (`{system}/docs/`):**
- System architecture
- API documentation
- Implementation details
- Usage examples

---

## Quick Links

- [Root README](../README.md) - Organization overview
- [PROJECT.md](../PROJECT.md) - Comprehensive project documentation
- [CLAUDE.md](../CLAUDE.md) - AI assistant comprehensive guide
- [STRUCTURE.md](../STRUCTURE.md) - Repository navigation
- [CONTRIBUTING.md](../CONTRIBUTING.md) - How to contribute

---

## Adding Documentation

1. **Determine scope:**
   - Monorepo-wide? → Add here
   - System-specific? → Add to `{system}/docs/`

2. **Create markdown file:**
   - Use clear, descriptive names
   - Follow existing formatting
   - Include table of contents for long docs

3. **Update this README:**
   - Add link to new document
   - Categorize appropriately

4. **Cross-reference:**
   - Link from related documents
   - Update navigation files

---

## Contact

For questions about documentation:
- Open an issue on GitHub
- Contact: meshal@berkeley.edu

---

**Last Updated:** 2025-11-19
