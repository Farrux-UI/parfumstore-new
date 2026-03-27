/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Cormorant Garamond"', 'serif'],
        sans: ['"Montserrat"', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '700',
      },
      letterSpacing: {
        'widest': '0.2em',
        'luxury': '0.15em',
        'wide': '0.025em',
      },
      spacing: {
        'section': '6rem',
        'section-xl': '8rem',
      },
      transitionDuration: {
        '700': '700ms',
        '1000': '1000ms',
      },
      colors: {
        'ruby': '#C41E47',
        'blood': '#e60000',
        'blood-dark': '#8a0303',
        'bordeaux': '#2D0A0A',
        'amber-btn': '#FFB347',
        'charcoal': '#2d2d2d',
        'charcoal-light': '#333333',
        'night': '#0a0a0a',
        'pure-white': '#FFFFFF',
      },
    },
  },
  plugins: [],
};
