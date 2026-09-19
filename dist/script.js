'use strict';
document.querySelectorAll('[data-year]').forEach(el => { el.textContent = String(new Date().getFullYear()); });
const filters = document.querySelector('.filters');
if (filters) {
  const cards = [...document.querySelectorAll('.project-card')];
  const buttons = [...filters.querySelectorAll('button')];
  const count = document.querySelector('.result-count');
  filters.hidden = false;
  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const category = button.dataset.filter;
      buttons.forEach(item => {
        const selected = item === button;
        item.classList.toggle('active', selected);
        item.setAttribute('aria-pressed', String(selected));
      });
      cards.forEach(card => { card.hidden = category !== 'all' && card.dataset.category !== category; });
      count.textContent = `显示 ${cards.filter(card => !card.hidden).length} 个项目`;
    });
  });
}
