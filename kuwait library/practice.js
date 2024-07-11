const infomatics = document.querySelector('.infomatics');
const scrollIndicator = document.getElementById('scroll-indicator');

infomatics.addEventListener('scroll', () => {
    const scrollWidth = infomatics.scrollWidth - infomatics.clientWidth;
    const scrollLeft = infomatics.scrollLeft;
    const scrollPercent = (scrollLeft / scrollWidth) * 100;
    scrollIndicator.style.width = `${scrollPercent}%`;
});
