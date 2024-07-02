/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      colors: {
        primary: '#2c2d3f',
        accent: '#9adc70',
        blue: '#0068f7',
        yellow: '#ffb62b',
        white: '#fefefe'
      }
    }
  },
  plugins: []
}
