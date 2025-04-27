'use strict';
{
  window.addEventListener('load', () => {
    function getRandomInt(max) {
      return Math.floor(Math.random() * max);
    }
    function updateStars() {
      const el = document.querySelector('.stars');
      let w = el.clientWidth;
      let h = el.clientHeight;
      let starsCount = Math.floor((w * h) * 0.00015);
      let starsDuration = Math.floor((h / 8.3));
      let stars2Duration = Math.floor((starsDuration / 2));
      let stars = [];
      for (let i = 0; i < starsCount; i++)
        stars.push(getRandomInt(w) + 'px ' + getRandomInt(h) + 'px ' + '#fff');
      let stars2 = [];
      for (let i = 0; i < (starsCount / 4); i++)
        stars2.push(getRandomInt(w) + 'px ' + getRandomInt(h) + 'px ' + '#fff');
      document.documentElement.style.setProperty('--stars', stars.join(','));
      document.documentElement.style.setProperty('--stars2', stars2.join(','));
      document.documentElement.style.setProperty('--stars-duration', starsDuration + 's');
      document.documentElement.style.setProperty('--stars2-duration', stars2Duration + 's');
      document.documentElement.style.setProperty('--stars-top', h + 'px');
      document.documentElement.style.setProperty('--stars-translate', '-' + (h) + 'px');
    }
    updateStars();
    window.addEventListener('resize', updateStars);
  });
}