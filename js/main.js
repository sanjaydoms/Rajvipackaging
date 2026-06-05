/* HEADER */
const header = document.getElementById('main-header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 40);
  updateActiveNav();
});

function updateActiveNav() {
  const navLinks = document.querySelectorAll('.nav-link[data-section]');
  const sectionIds = ['about','products','solutions','blogs','contact'];
  let active = '';
  sectionIds.forEach(id => {
    const el = document.getElementById(id);
    if (el && el.getBoundingClientRect().top <= 120) active = id;
  });
  navLinks.forEach(l => l.classList.toggle('active', l.dataset.section === active));
}

document.querySelectorAll('a.nav-link[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = a.getAttribute('href').replace('#','');
    const el = document.getElementById(target);
    if (el) { e.preventDefault(); el.scrollIntoView({ behavior:'smooth' }); }
  });
});

/* SOLUTIONS EXPAND */
document.querySelectorAll('.sol-item').forEach(item => {
  item.querySelector('.sol-item-head').addEventListener('click', () => {
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.sol-item.open').forEach(o => o.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  });
});

/* CONVEYOR DRAG */
const conveyor = document.getElementById('conveyor');
let isDragging = false, startX, scrollLeft;
conveyor.addEventListener('mousedown', e => {
  isDragging = true;
  conveyor.style.cursor = 'grabbing';
  startX = e.pageX - conveyor.offsetLeft;
  scrollLeft = conveyor.scrollLeft;
});
window.addEventListener('mouseup', () => { isDragging = false; conveyor.style.cursor = 'grab'; });
conveyor.addEventListener('mousemove', e => {
  if (!isDragging) return;
  e.preventDefault();
  const x = e.pageX - conveyor.offsetLeft;
  conveyor.scrollLeft = scrollLeft - (x - startX);
});
conveyor.addEventListener('touchstart', e => { startX = e.touches[0].pageX; scrollLeft = conveyor.scrollLeft; }, {passive:true});
conveyor.addEventListener('touchmove', e => {
  const x = e.touches[0].pageX;
  conveyor.scrollLeft = scrollLeft - (x - startX);
}, {passive:true});




/* REVEAL */
const revEls = document.querySelectorAll('.reveal');
const obs = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
revEls.forEach(el => obs.observe(el));

/* INNER PAGES */
function openInner(type) {
  document.getElementById('inner-' + type).classList.add('open');
  document.body.style.overflow = 'hidden';
}
function openInner2(id) {
  document.getElementById(id).classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeInner() {
  document.querySelectorAll('.inner-page.open').forEach(p => p.classList.remove('open'));
  document.body.style.overflow = '';
}

/* THUMB GALLERY — swap main display when thumbnail clicked */
const galleryData = {};

function selectThumb(product, idx, el) {
  const thumbsEl = el.closest('.inner-gallery-thumbs');
  const mainEl   = thumbsEl.previousElementSibling; // .inner-gallery-main

  // deactivate all siblings
  thumbsEl.querySelectorAll('.ig-thumb').forEach(t => t.classList.remove('active'));
  el.classList.add('active');

  // store original placeholder content once
  if (!galleryData[product]) {
    galleryData[product] = mainEl.innerHTML;
  }

  if (idx === 0) {
    // restore placeholder
    mainEl.innerHTML = galleryData[product];
  } else {
    const img = el.querySelector('img');
    if (img) {
      mainEl.innerHTML = `
        <img src="${img.src.replace('w=220','w=900')}" alt="${img.alt}"
          style="width:100%;height:100%;object-fit:cover;display:block;opacity:0.9;transition:opacity .3s">
        <div class="inner-gallery-overlay"></div>
        <div class="inner-gallery-tech"></div>
        <div class="inner-gallery-frame"></div>
        <div class="inner-gallery-frame-tr"></div>
        <div class="inner-gallery-frame-bl"></div>
      `;
    }
  }
}

/* THUMB STRIP — drag-to-scroll */
document.querySelectorAll('.inner-gallery-thumbs').forEach(strip => {
  let isDown = false, startX, sLeft;
  strip.addEventListener('mousedown', e => {
    isDown = true; startX = e.pageX - strip.offsetLeft; sLeft = strip.scrollLeft;
  });
  window.addEventListener('mouseup', () => { isDown = false; });
  strip.addEventListener('mousemove', e => {
    if (!isDown) return;
    e.preventDefault();
    strip.scrollLeft = sLeft - (e.pageX - strip.offsetLeft - startX);
  });
  strip.addEventListener('touchstart', e => { startX = e.touches[0].pageX; sLeft = strip.scrollLeft; }, {passive:true});
  strip.addEventListener('touchmove', e => {
    strip.scrollLeft = sLeft - (e.touches[0].pageX - startX);
  }, {passive:true});
});

/* TECHNICAL GRID CANVAS — scattered coordinate labels + dots overlay */
(function() {
  const canvas = document.createElement('canvas');
  canvas.style.cssText = 'position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:0;';
  document.body.appendChild(canvas);

  const ctx = canvas.getContext('2d');
  const labels = [
    {x:0.07, y:0.28, t:'B.02'}, {x:0.37, y:0.08, t:'A.01'}, {x:0.78, y:0.05, t:'C.03'},
    {x:0.55, y:0.31, t:'2'},    {x:0.73, y:0.80, t:'B.02'}, {x:0.20, y:0.72, t:'—'},
    {x:0.62, y:0.55, t:'C.03'},
  ];
  // Reduced to 4 dots — very faint
  const dots = [
    {x:0.26, y:0.24, r:2.5, type:'fill'},
    {x:0.57, y:0.32, r:2.5, type:'fill'},
    {x:0.82, y:0.26, r:2.5, type:'ring'},
    {x:0.46, y:0.50, r:2.5, type:'fill'},
  ];

  function draw() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // coordinate labels — very faint
    ctx.font = '500 9px Poppins, sans-serif';
    ctx.letterSpacing = '0.12em';
    ctx.fillStyle = 'rgba(10,61,44,0.10)';
    labels.forEach(l => {
      ctx.fillText(l.t, l.x * canvas.width, l.y * canvas.height);
    });

    // dots / rings — reduced opacity to blend in
    dots.forEach(d => {
      const x = d.x * canvas.width, y = d.y * canvas.height;
      if (d.type === 'fill') {
        ctx.beginPath();
        ctx.arc(x, y, d.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(10,61,44,0.22)';
        ctx.fill();
      } else {
        ctx.beginPath();
        ctx.arc(x, y, d.r + 1.5, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(10,61,44,0.15)';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    });

    // scattered small "+" crosshair marks — fewer, very faint
    const plusPositions = [
      [0.04,0.18],[0.14,0.30],[0.48,0.15],[0.70,0.13],[0.93,0.11],
      [0.89,0.35],[0.92,0.55],[0.88,0.74],[0.04,0.50],[0.04,0.74],
      [0.24,0.90],[0.56,0.88],[0.78,0.91],
    ];
    ctx.strokeStyle = 'rgba(10,61,44,0.08)';
    ctx.lineWidth = 0.7;
    plusPositions.forEach(([px, py]) => {
      const cx = px * canvas.width, cy = py * canvas.height, s = 5;
      ctx.beginPath(); ctx.moveTo(cx - s, cy); ctx.lineTo(cx + s, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - s); ctx.lineTo(cx, cy + s); ctx.stroke();
    });

    // small open squares scattered — ghost level
    const squares = [
      [0.05,0.10],[0.20,0.38],[0.76,0.38],[0.90,0.50],[0.60,0.75],[0.38,0.60],
    ];
    ctx.strokeStyle = 'rgba(10,61,44,0.07)';
    squares.forEach(([sx, sy]) => {
      const cx = sx * canvas.width, cy = sy * canvas.height, s = 4;
      ctx.strokeRect(cx - s/2, cy - s/2, s, s);
    });

    // dotted measurement lines (horizontal)
    ctx.setLineDash([4, 6]);
    ctx.strokeStyle = 'rgba(10,61,44,0.07)';
    ctx.lineWidth = 0.6;
    [[0.18, 0.14, 0.36, 0.14],[0.26, 0.50, 0.44, 0.50]].forEach(([x1,y1,x2,y2]) => {
      ctx.beginPath();
      ctx.moveTo(x1 * canvas.width, y1 * canvas.height);
      ctx.lineTo(x2 * canvas.width, y2 * canvas.height);
      ctx.stroke();
    });
    ctx.setLineDash([]);
  }

  draw();
  window.addEventListener('resize', draw);
})();

updateActiveNav();
