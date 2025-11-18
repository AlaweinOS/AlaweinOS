import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      thresholds: {
        lines: 0.7,
        functions: 0.7,
        branches: 0.6,
        statements: 0.7,
      },
    },
  },
})
