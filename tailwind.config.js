/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // './templates/**/*.html',
    './**/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        light: '#EEEEEE',
        secondary: '#00ADB5',
        dark: '#393E46',
        darkest: '#222831',
      }
    },
  },
  plugins: [],
}

