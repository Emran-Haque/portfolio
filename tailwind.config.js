/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './portfolio/templates/**/*.{html,js}',
    './home/templates/**/*.{html,js}',
    './*/templates/**/*.{html,js}',
    './**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
