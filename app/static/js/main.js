// 主要 JavaScript 文件

document.addEventListener('DOMContentLoaded', function() {
    console.log('网站已加载');
    
    // 平滑滚动
    setupSmoothScroll();
    
    // 导航栏激活状态
    updateActiveNav();
});

// 平滑滚动
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

// 更新导航栏激活状态
function updateActiveNav() {
    const currentPage = window.location.pathname;
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
}

// 延迟加载图片
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// 获取 API 数据示例
async function fetchProjects() {
    try {
        const response = await fetch('/api/projects');
        const projects = await response.json();
        console.log('Projects:', projects);
        return projects;
    } catch (error) {
        console.error('Error fetching projects:', error);
    }
}

async function fetchSkills() {
    try {
        const response = await fetch('/api/skills');
        const skills = await response.json();
        console.log('Skills:', skills);
        return skills;
    } catch (error) {
        console.error('Error fetching skills:', error);
    }
}
