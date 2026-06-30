// ============ Footer year ============
document.getElementById('year').textContent = new Date().getFullYear();

// ============ Mobile nav toggle ============
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen);
});

// Close mobile nav after a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
    });
});

// ============ Scroll reveal + skill bar fill + counters (single observer) ============
const revealEls = document.querySelectorAll(
    '.section, .project-card, .cert-card, .timeline-item, .achievement-card, .skill-category'
);
revealEls.forEach(el => el.setAttribute('data-reveal', ''));

const fillEls = document.querySelectorAll('.fill');
const counterEls = document.querySelectorAll('.counter');

const animateCounter = (el) => {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1200;
    const start = performance.now();

    function step(now) {
        const progress = Math.min((now - start) / duration, 1);
        el.textContent = Math.floor(progress * target) + suffix;
        if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
};

const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in-view');

        // fill any skill bars within this element
        entry.target.querySelectorAll('.fill').forEach(f => f.classList.add('in-view'));

        // trigger counters within this element
        entry.target.querySelectorAll('.counter').forEach(c => {
            if (!c.dataset.done) {
                c.dataset.done = 'true';
                animateCounter(c);
            }
        });

        io.unobserve(entry.target);
    });
}, { threshold: 0.2 });

revealEls.forEach(el => io.observe(el));
// Also observe bars/counters directly in case their parent already animated
fillEls.forEach(el => io.observe(el.closest('.skill-category') || el));
counterEls.forEach(el => io.observe(el.closest('.achievement-card') || el));

// ============ Project modal (kept for compatibility / future use) ============
function openProjectModal(title, goal, problem, accuracy, tech, github, demo) {
    document.getElementById('projectTitle').innerText = title;
    document.getElementById('projectGoal').innerText = goal;
    document.getElementById('projectProblem').innerText = problem;
    document.getElementById('projectAccuracy').innerText = accuracy;
    document.getElementById('projectTech').innerText = tech;
    document.getElementById('projectGithub').href = github;
    document.getElementById('projectDemo').href = demo;
    document.getElementById('projectModal').style.display = 'block';
}
function closeProjectModal() {
    document.getElementById('projectModal').style.display = 'none';
}

// ============ Certificate modal ============
function openCertModal(title, image, topics, credential, link) {
    document.getElementById('certTitle').innerText = title;
    document.getElementById('certImage').src = image;
    document.getElementById('certTopics').innerText = topics;
    document.getElementById('certCredential').innerText = credential;
    document.getElementById('certLink').href = link;
    document.getElementById('certModal').style.display = 'block';
}
function closeCertModal() {
    document.getElementById('certModal').style.display = 'none';
}

// Close modals on outside click or Escape
window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) e.target.style.display = 'none';
});
window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.getElementById('projectModal').style.display = 'none';
        document.getElementById('certModal').style.display = 'none';
    }
});

// Allow opening cert cards with Enter/Space (keyboard accessibility)
document.querySelectorAll('.cert-card').forEach(card => {
    card.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            card.click();
        }
    });
});

// ============ Back to top ============
const backToTop = document.getElementById('backToTop');
backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ============ Sticky nav shadow on scroll ============
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.style.boxShadow = window.scrollY > 10 ? '0 4px 20px rgba(0,0,0,.3)' : 'none';
});