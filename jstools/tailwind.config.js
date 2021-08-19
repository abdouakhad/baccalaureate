module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
      extend: {
        colors:{
            'my-gray': '#6B7280',
            'my-blue':'#1E40AF',
            'my-green': '#10B981',
            'white': '#ffffff',
          },
          width:{
            'iconWidth':'30px',
            'serieIconWidth':'100px',
            'profileWidth':'250px',
          },
          height:{
            'iconHeight':'30px',
          }
      },
  },
  variants: {
    extend:{
      opacity:['disabled']
    }
  },
  plugins: [],
}