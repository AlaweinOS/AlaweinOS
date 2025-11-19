import { test, expect } from '@playwright/test';

test('reduced-motion: main visible without heavy animations', async ({ context, page }) => {
  await context.addInitScript(() => {
    // Emulate prefers-reduced-motion
    const _mql = window.matchMedia;
    // @ts-expect-error - Mocking matchMedia for reduced motion testing
    window.matchMedia = (q: string) => ({
      matches: q.includes('prefers-reduced-motion'),
      media: q,
      addEventListener: () => {},
      removeEventListener: () => {}
    });
  });
  await page.goto('/', { waitUntil: 'networkidle' });
  await expect(page.locator('#main-content')).toBeVisible();
});

