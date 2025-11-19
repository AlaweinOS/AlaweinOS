# SimCore: Interactive Scientific Computing Laboratory

*Modular scientific computing platform for physics, mathematics, and scientific machine learning*

[![Live Platform](https://img.shields.io/badge/Live%20Platform-SimCore%20Lab-blue?style=for-the-badge)](https://lovable.dev/projects/f5c4348e-aff9-4eb4-bf03-0c2e06c7822a)
[![React](https://img.shields.io/badge/React-18.3-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.5-green.svg)](https://www.typescriptlang.org/)
[![WebGPU](https://img.shields.io/badge/WebGPU-Enabled-orange.svg)](#performance)

---

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/alaweimm90/SimCore.git
cd SimCore
npm install

# Start development
npm run dev
# → http://localhost:5173

# Build for production
npm run build
```

## 🧬 Scientific Modules

**25+ Interactive Scientific Simulations**

### Quantum Mechanics & Electronic Structure
- **Graphene Band Structure**: Tight-binding calculations with Dirac cone physics
- **MoS₂ Valley Physics**: Berry curvature and valley Hall effects
- **TDSE Solver**: Time-dependent Schrödinger equation with wave packet dynamics
- **Quantum Tunneling**: Real-time barrier penetration analysis

### Statistical Physics & Magnetism
- **2D Ising Model**: Monte Carlo phase transitions with critical phenomena
- **Boltzmann Distribution**: Energy level population analysis
- **LLG Dynamics**: Magnetization switching and spin torque dynamics

### Advanced Computational Methods
- **Physics-Informed Neural Networks**: PINN-based PDE solvers
- **Machine Learning Analysis**: Pattern recognition in scientific data
- **WebGPU Accelerated Simulations**: Real-time parallelized calculations

### Mathematical Modeling & Scientific ML
- **Advanced Mathematical Methods**: Computational mathematics for scientific applications
- **Scientific Machine Learning**: ML-driven discovery and neural simulation
- **Numerical Analysis**: Modern algorithms for complex mathematical systems

> SimCore refers to the platform's core computational engine—a modular, high-performance system designed to enable research-grade, interactive simulations across physics, mathematics, and scientific machine learning.

## 🔬 Key Features

### Research-Grade Accuracy
- **Literature-verified implementations** with built-in validation
- **Publication-quality visualizations** using plotly.js and WebGL
- **Comprehensive theory integration** with LaTeX equations and references

### Performance & Technology
- **WebGPU acceleration** for intensive calculations
- **Progressive Web App** with offline capability
- **Real-time simulations** at 60fps with hardware acceleration
- **Responsive design** optimized for all devices

### Educational Excellence
- **Interactive tutorials** from beginner to research level
- **Step-by-step theory explanations** with mathematical derivations
- **Scientific validation tools** for physics, mathematics, and ML

### Collaboration & Sharing
- **Shareable URLs** to load exact simulation states
- **Local save/load** of sessions with metadata
- **Import/Export** JSON for reproducible research
- **Collaboration sessions** (public/private) setup from the Share dialog

## 🎯 Use Cases

### For Researchers
- **Band structure and material property calculations**
- **Monte Carlo and ML-driven analysis**
- **Real-time quantum and statistical modeling**
- **Mathematical modeling and computational analysis**
- **Data export** for publication and further simulation

### For Educators
- **Interactive STEM lectures** with live demos in physics, math, and ML
- **Assignments with validation and feedback**
- **Visualization of complex theoretical and mathematical systems**
- **Theory references** linked to primary literature

### For Students
- **Self-paced learning** in physics, mathematics, and scientific machine learning
- **Conceptual clarity** via exploration
- **Immediate feedback** on problem-solving
- **Advanced tools** to prepare for interdisciplinary research

## 🛠️ Technology Stack

**Frontend Architecture**
- React 18.3 + TypeScript + Vite
- shadcn/ui components with Tailwind CSS
- Modular theming system for scientific domains

**Scientific Computing**
- Custom numerical solvers with WebGPU acceleration
- plotly.js for interactive visualization
- KaTeX for mathematical typesetting
- Three.js for 3D graphics and scientific visualization
- Advanced mathematical libraries and ML frameworks

**Performance & State**
- Zustand for simulation state control
- Service workers with offline caching
- Lazy-loaded modules with code splitting
- Memory-optimized GPU algorithms

## 🔍 Quality Assurance & Auditing

Comprehensive automated audits ensure performance, accessibility, and code quality on every push.

### Run Audits Locally

```bash
# First time: install Playwright browsers
npx playwright install --with-deps

# Run full audit suite (Lighthouse + axe + Playwright + CSS stats + Pa11y)
npm run audit:full
```

### Audit Tools

- **Lighthouse CI**: Performance, accessibility, SEO, best practices
- **axe-core**: WCAG 2.1 A/AA compliance
- **Playwright**: Visual regression, reduced-motion tests, smoke tests
- **CSS Analyzer**: Style consistency and optimization metrics
- **Pa11y**: Automated accessibility crawling

### View Results

After running `npm run audit:full`, check:
- `.audit/lhci/` - Lighthouse HTML reports
- `.audit/axe/axe.json` - Accessibility violations
- `.audit/playwright/` - Screenshots, traces, test reports
- `.audit/css.json` - CSS statistics
- `.audit/pa11y.json` - Accessibility audit results

### CI Integration

- Audits run automatically on:
  - Every push to `main`
  - Pull requests (quick audit)
  - Nightly (full audit at 03:00 UTC)
- Results uploaded as GitHub Actions artifacts
- Optional: Require "Audit / quick-audit" to pass in branch protection

## 📚 Documentation

- **[Full Documentation](DOCUMENTATION.md)** - Complete user and developer guide
- **[Development Setup](DEVELOPMENT.md)** - Contributing and development workflow
- **[Module API Reference](DOCUMENTATION.md#api-reference)** - Simulation engine API
- **[Version History](CHANGELOG.md)** - Release notes and improvements

## 🤝 Contributing

We welcome contributions across physics, mathematics, and scientific ML:

1. **New scientific modules** in physics, mathematics, and scientific machine learning
2. **Performance enhancements** using WebGPU and ML
3. **STEM educational content** and tutorials for physics/math/ML
4. **Improved documentation** and theoretical derivations

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed guidelines.

## 📄 Citation

If you use SimCore in research or education, please cite:

```bibtex
@software{simcore2025,
  title={SimCore: Interactive Scientific Computing Laboratory},
  author={Alawein, Dr. Meshal},
  year={2025},
  url={https://github.com/alaweimm90/SimCore},
  note={Modular web-based platform for physics, mathematics, and scientific ML}
}
```

## 👨‍🔬 About

**Dr. Meshal Alawein**  
*Computational Materials Scientist & Researcher*  
University of California, Berkeley

📧 [meshal@berkeley.edu](mailto:meshal@berkeley.edu)  
🌐 [malawein.com](https://malawein.com)  
📚 [Google Scholar](https://scholar.google.com/citations?user=IB_E6GQAAAAJ&hl=en)

---

*"Science can be hard. This is my way of helping."* ⚛️

**MIT License** © 2025 Dr. Meshal Alawein