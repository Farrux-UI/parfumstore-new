import { createClient } from '@sanity/client';

export const sanityClient = createClient({
    projectId: 'lll67s6i', // Placeholder: Developer will replace this
    dataset: 'production',
    useCdn: false, // Bypass CDN for fresh data in dev
    apiVersion: '2026-03-17', // Today's date
});
