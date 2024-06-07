import { useEffect } from 'react';

const useSmoothScroll = () => {
  useEffect(() => {
    const handleScroll = (event: Event) => {
      event.preventDefault();
      const targetId = (event.target as HTMLAnchorElement).getAttribute('href')?.slice(1);
      const targetElement = targetId ? document.getElementById(targetId) : null;

      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 64, 
          behavior: 'smooth',
        });
      }
    };

    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach((link) => {
      link.addEventListener('click', handleScroll);
    });

    return () => {
      links.forEach((link) => {
        link.removeEventListener('click', handleScroll);
      });
    };
  }, []);
};

export default useSmoothScroll;
