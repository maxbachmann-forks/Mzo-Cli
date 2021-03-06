module.exports = {
  title: 'MZO CLI',
  description: 'Sometimes typing is more convenient then swiping and tapping... Sometimes.',
  ga: 'UA-33148627-2',
  // base: '/Monzo-Cli/', // For github pages. Not needed for custom domain
  themeConfig: {
    nav: [
      { text: 'Documentation', link: '/docs/' },
      { text: 'GitHub', link: 'https://github.com/jamesstidard/mzo-cli' },
    ],
    sidebar: [
      '/docs/',
      '/docs/install',
      '/docs/usage',
      '/docs/uninstall',
    ],
  },
}
