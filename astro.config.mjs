// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  i18n: {
    defaultLocale: "az",
    locales: ["az", "ru", "en"],
    routing: {
      prefixDefaultLocale: false
    }
  }
});
