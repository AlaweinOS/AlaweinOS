# Contributing to QMLab

Thank you for your interest in contributing to QMLab! This document provides guidelines for contributing to our open-source quantum machine learning playground.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Coding Standards](#coding-standards)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming, inclusive environment for all contributors regardless of background or experience level.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/qml-playground.git
   cd qml-playground
   ```
3. **Install dependencies**:
   ```bash
   npm install
   ```
4. **Start the development server**:
   ```bash
   npm run dev
   ```

## Development Setup

### Prerequisites
- Node.js (v18 or higher)
- npm or yarn
- Git

### Project Structure
```
src/
├── components/          # React components
├── hooks/              # Custom React hooks  
├── lib/                # Utility functions
├── pages/              # Page components
└── contexts/           # React contexts
```

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run test` - Run tests
- `npm run test:a11y` - Run accessibility tests

## How to Contribute

### Types of Contributions
- **Bug fixes** - Fix issues in existing functionality
- **New features** - Add quantum algorithms, visualizations, or educational content
- **Documentation** - Improve README, code comments, or tutorials
- **Accessibility** - Improve screen reader support or keyboard navigation
- **Performance** - Optimize quantum simulations or UI rendering
- **Tests** - Add unit tests or accessibility tests

### Areas Where Help is Needed
- Quantum algorithm implementations
- Educational content and tutorials
- Mobile optimization
- Accessibility improvements
- Performance optimizations
- Translation/internationalization

## Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clear, concise code
   - Add tests for new functionality
   - Update documentation as needed
   - Ensure accessibility compliance

3. **Test your changes**:
   ```bash
   npm run lint
   npm run build
   npm run test:a11y
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add quantum algorithm visualization"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub with:
   - Clear title and description
   - Screenshots/GIFs for UI changes
   - Reference to related issues
   - Checklist of completed tasks

### Pull Request Checklist
- [ ] Code follows our style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Accessibility tested
- [ ] No breaking changes (or clearly documented)

## Issue Guidelines

### Bug Reports
Include:
- Steps to reproduce
- Expected vs actual behavior
- Browser/OS information
- Screenshots if applicable

### Feature Requests
Include:
- Problem description
- Proposed solution
- Alternative solutions considered
- Educational value for quantum computing

### Issue Labels
- `bug` - Something isn't working
- `enhancement` - New feature request
- `documentation` - Documentation improvements
- `accessibility` - Accessibility-related issues
- `good-first-issue` - Good for newcomers
- `help-wanted` - Extra attention needed

## Coding Standards

### TypeScript
- Use TypeScript for type safety
- Define interfaces for props and data structures
- Use meaningful variable names

### React
- Use functional components with hooks
- Follow React best practices
- Implement proper error boundaries

### Accessibility
- Use semantic HTML
- Add ARIA labels where needed
- Test with keyboard navigation
- Ensure color contrast compliance

### Performance
- Lazy load components when appropriate
- Optimize quantum calculations
- Use React.memo for expensive components

### Commit Messages
Follow conventional commits format:
```
type(scope): description

feat(quantum): add Grover algorithm visualization
fix(ui): resolve mobile navigation issue
docs(readme): update installation instructions
```

## Development Tips

### Quantum Computing Implementation
- Keep simulations lightweight for browser performance
- Add educational tooltips and explanations
- Provide both beginner and advanced modes

### UI/UX Guidelines
- Maintain consistent design system
- Ensure mobile responsiveness
- Test accessibility with screen readers

### Testing
- Write unit tests for utility functions
- Add accessibility tests for new components
- Test across different browsers and devices

## Questions?

- Open an issue for discussion
- Check existing issues and PRs first
- Join our discussions tab for questions

## Recognition

Contributors are recognized in our README and release notes. All contributions, no matter how small, are valued and appreciated.

Thank you for helping make quantum computing education more accessible! 🚀