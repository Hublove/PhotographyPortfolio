/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {fontFamily: {
        body: ['Roboto Mono'],
        other: ['Nunito']
    }},
  },
  plugins: [require('daisyui'),
  require('tailwind-scrollbar-hide')],
  
}
