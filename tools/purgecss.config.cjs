module.exports = {
  content: ['index.html', 'realizace.html', 'ochrana-osobnich-udaju/index.html', '404.html', 'assets/src/site.js'],
  css: ['assets/src/site.css'],
  safelist: {
    standard: ['active','fade','flash','in','in-view','is-off','menu-lock','menu-open','on','open','out','rail-cta','scrolled','scrolling','sent','shake','show','swap','tilt','fw','hidden','js-rv','rv-in','lenis','lenis-smooth','lenis-stopped','lenis-scrolling'],
    greedy: [/^lenis/, /view-transition/, /^ck/, /^bn-/, /^sp$/, /^s[12]$/, /^o[12]$/, /^arr$/, /^serif$/],
    keyframes: []
  },
  keyframes: true,
  dynamicAttributes: ['style', 'data-f', 'data-sec', 'data-section', 'aria-expanded', 'aria-pressed', 'data-theme', 'hidden'],
  fontFace: false,
  variables: false
};
