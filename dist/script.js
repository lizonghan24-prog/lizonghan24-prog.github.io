'use strict';
const profile = window.SITE_PROFILE || {};
document.querySelectorAll('[data-profile]').forEach(element => {
  const value = profile[element.dataset.profile];
  if (typeof value === 'string' && value.trim()) {
    element.textContent = value;
    element.style.whiteSpace = 'pre-line';
  }
});
if (profile.siteName) document.title = profile.siteName;
if (profile.description) document.querySelector('meta[name="description"]').content = profile.description.replace(/\n/g, ' ');
document.querySelectorAll('[data-year]').forEach(element => { element.textContent = String(new Date().getFullYear()); });
const links = [];
if (typeof profile.github === 'string' && profile.github.trim()) {
  try {
    const url = new URL(profile.github);
    if (url.protocol === 'https:' && url.hostname === 'github.com' && !url.username && !url.password) {
      links.push({ label: 'GitHub', href: url.href, external: true });
    }
  } catch { /* 未填写有效网址时保留空状态。 */ }
}
if (typeof profile.email === 'string' && /^[^\s@?&#]+@[^\s@?&#]+\.[^\s@?&#]+$/.test(profile.email)) {
  links.push({ label: profile.email, href: `mailto:${profile.email}`, external: false });
}
if (links.length) {
  const container = document.getElementById('contact-links');
  container.replaceChildren();
  links.forEach(({ label, href, external }) => {
    const anchor = document.createElement('a');
    anchor.href = href;
    anchor.textContent = label;
    if (external) { anchor.target = '_blank'; anchor.rel = 'noopener noreferrer'; anchor.setAttribute('aria-label', `${label}（在新标签页打开）`); }
    const arrow = document.createElement('span');
    arrow.textContent = '↗';
    arrow.setAttribute('aria-hidden', 'true');
    anchor.append(arrow);
    container.append(anchor);
  });
}
