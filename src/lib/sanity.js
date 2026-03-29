import { createClient } from '@sanity/client';
import imageUrlBuilder from '@sanity/image-url';

export const sanityClient = createClient({
    projectId: 'lll67s6i',
    dataset: 'production',
    useCdn: false,
    apiVersion: '2026-03-17',
});

const builder = imageUrlBuilder(sanityClient);

/**
 * Optimized image URL builder with WebP/AVIF auto-format and quality
 * @param {object} source - Sanity image asset
 * @param {number} width - Target width (mobile: 400, desktop: 800-1200)
 * @param {number} quality - Image quality 0-100 (default: 75)
 * @returns {object} Sanity image URL builder
 */
export function urlFor(source, width = 800, quality = 75) {
    if (!source) return { url: () => '' };
    return builder
        .image(source)
        .width(width)
        .quality(quality)
        .auto('format');
}

/**
 * Get optimized image URL string directly
 * @param {object} source - Sanity image asset  
 * @param {number} width - Target width
 * @param {number} quality - Image quality
 * @returns {string} Optimized image URL
 */
export function getOptimizedImageUrl(source, width = 800, quality = 75) {
    if (!source) return '';
    return builder
        .image(source)
        .width(width)
        .quality(quality)
        .auto('format')
        .url();
}
