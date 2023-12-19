/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./doormot_app/templates/**/*.html",
    "./doormot_reg_users/templates/**/*.html",
    "./doormot_users_profiles/templates/**/*.html",
    "./doormot_property_listing/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily:{
        'popins':['Poppins', 'sans-serif'],
        'open':['Open Sans', 'sans-serif'],
        'nunito':['Nunito Sans', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
