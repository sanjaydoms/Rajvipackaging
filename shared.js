/* ===========================================================================
   RAJVI PACKAGING — SHARED JAVASCRIPT
   Loaded on every page. Contains:
   - Mobile hamburger nav (home navbar + fp-header / inner-page-header variants)
   - Scroll-based header state + reveal-on-scroll animation
   - Blog data (BLOGS) + rendering + detail overlay
   - Case study data (CASE_STUDIES) + detail overlay
   - Product variant image swap (selectVariant)
   - Background technical-grid canvas decoration
   Extracted verbatim from the original single-file index.html. Old overlay-
   routing functions (openAboutPage, openFullPage, openSolutionPage, etc.)
   have been removed since pages now use real <a href="..."> navigation.
   =========================================================================== */

/* ===== HOME NAVBAR HAMBURGER (index.html only — guarded for other pages) ===== */
const hamburgerBtn = document.getElementById('hamburger-btn');
const mobileDrawer = document.getElementById('mobile-nav-drawer');
const mobileOverlay = document.getElementById('mobile-nav-overlay');

function openMobileNav() {
  hamburgerBtn.classList.add('open');
  mobileDrawer.style.display = 'flex';
  mobileOverlay.style.display = 'block';
  requestAnimationFrame(() => {
    mobileDrawer.classList.add('open');
    mobileOverlay.classList.add('open');
  });
  document.body.style.overflow = 'hidden';
}

function closeMobileNav() {
  hamburgerBtn.classList.remove('open');
  mobileDrawer.classList.remove('open');
  mobileOverlay.classList.remove('open');
  document.body.style.overflow = '';
  setTimeout(() => {
    if (!mobileDrawer.classList.contains('open')) {
      mobileDrawer.style.display = 'none';
      mobileOverlay.style.display = 'none';
    }
  }, 360);
}

if (hamburgerBtn) {
  hamburgerBtn.addEventListener('click', () => {
    if (mobileDrawer.classList.contains('open')) closeMobileNav();
    else openMobileNav();
  });
}

/* FP / INNER PAGE HAMBURGER — inject into fp-header / inner-page-header nav sections */
function addFpHamburgers() {
  document.querySelectorAll('.fp-header, .inner-page-header').forEach(header => {
    if (header.querySelector('.fp-hamburger')) return;
    const nav = header.querySelector('.fp-header-nav, .inner-page-header-nav');
    if (!nav) return;
    const btn = document.createElement('button');
    btn.className = 'fp-hamburger';
    btn.setAttribute('aria-label', 'Toggle menu');
    btn.innerHTML = '<span></span><span></span><span></span>';
    // Create dropdown
    const drop = document.createElement('div');
    drop.className = 'fp-mobile-menu';
    nav.querySelectorAll('a').forEach(a => {
      const clone = a.cloneNode(true);
      drop.appendChild(clone);
    });
    btn.addEventListener('click', () => {
      const isOpen = btn.classList.contains('open');
      // Close all other fp menus
      document.querySelectorAll('.fp-hamburger.open').forEach(b => {
        b.classList.remove('open');
        b.nextElementSibling && b.nextElementSibling.classList.contains('fp-mobile-menu') && b.nextElementSibling.classList.remove('open');
      });
      if (!isOpen) {
        btn.classList.add('open');
        drop.classList.add('open');
      }
    });
    // Close menu when a link is clicked
    drop.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        btn.classList.remove('open');
        drop.classList.remove('open');
      });
    });
    header.style.position = 'sticky';
    header.appendChild(btn);
    header.appendChild(drop);
  });
}

/* HEADER SCROLL STATE (home navbar only — guarded for other pages) */
const header = document.getElementById('main-header');
window.addEventListener('scroll', () => {
  if (header) header.classList.toggle('scrolled', window.scrollY > 40);
  updateActiveNav();
});

function updateActiveNav() {
  const navLinks = document.querySelectorAll('.nav-link[data-section]');
  const sectionIds = ['about', 'products', 'solutions', 'blogs', 'contact'];
  let active = '';
  sectionIds.forEach(id => {
    const el = document.getElementById(id);
    if (el && el.getBoundingClientRect().top <= 120) active = id;
  });
  navLinks.forEach(l => l.classList.toggle('active', l.dataset.section === active));
}

document.querySelectorAll('a.nav-link[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = a.getAttribute('href').replace('#', '');
    const el = document.getElementById(target);
    if (el) { e.preventDefault(); el.scrollIntoView({ behavior: 'smooth' }); }
  });
});

/* REVEAL ON SCROLL */
const revEls = document.querySelectorAll('.reveal');
const obs = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
revEls.forEach(el => obs.observe(el));

/* INNER PRODUCT PAGE BACK / NAV ACTIVE STATE HELPERS */
function setInnerNavActive(label) {
  document.querySelectorAll('.inner-page-header-nav a').forEach(a => {
    a.classList.remove('inner-nav-active');
    if (a.textContent.trim() === label) a.classList.add('inner-nav-active');
  });
}

/* ===== VARIANT IMAGE UPDATER (product inner pages) ===== */
function selectVariant(productKey, el, imgSrc) {
  const container = el.closest('.why-grid');
  if (container) container.querySelectorAll('.variant-item').forEach(v => v.classList.remove('active'));
  el.classList.add('active');
  const mainImg = document.getElementById('gallery-main-img-' + productKey);
  if (mainImg) {
    mainImg.style.opacity = '0';
    mainImg.style.transition = 'opacity 0.25s';
    setTimeout(() => { mainImg.src = imgSrc; mainImg.style.opacity = '1'; }, 200);
  }
}

// ===== BLOG DATA =====
const BLOGS = [
  { slug: 'packaging-solutions-pharma-companies-hyderabad',  title: 'Packaging Solutions for Pharma Companies in Hyderabad: What to Look For', category: 'Industry Insights', readTime: '5 min read', date: 'December 2025', img: '../images/foam3.jpg', desc: 'Learn how Hyderabad\'s pharmaceutical and life sciences companies can select compliant, protective packaging solutions that ensure product safety, regulatory compliance, and reliable transportation.', content: `<p>Hyderabad is home to one of India's largest pharmaceutical and life sciences manufacturing hubs. Packaging in this industry extends far beyond product protection—it plays a vital role in maintaining product quality, supporting regulatory compliance, and ensuring safe transportation throughout the supply chain.</p><h2>Regulatory & Compliance Requirements</h2><p>Pharmaceutical packaging must often satisfy strict industry regulations regarding material safety, product integrity, tamper evidence, and traceability. Choosing a packaging partner with experience serving pharmaceutical manufacturers helps reduce compliance risks and supports smoother regulatory inspections and quality audits.</p><h2>Protecting Temperature-Sensitive Products</h2><p>Many pharmaceutical products and intermediates are highly sensitive to environmental conditions during storage and transportation. Effective protective packaging may include:</p><ul><li>Insulated packaging systems</li><li>Moisture barrier materials</li><li>Temperature-resistant protective packaging</li><li>Protective liners</li><li>Secure transport packaging</li></ul><p>These solutions help maintain product stability while reducing the risk of contamination or environmental exposure during transit.</p><h2>Tamper-Evident & Secondary Packaging</h2><p>Secondary packaging plays an important role in protecting pharmaceutical products while supporting batch identification and product traceability. Tamper-evident seals, secure closures, clear labeling, and durable protective packaging help safeguard product integrity throughout distribution.</p><h2>Selecting the Right Pharma Packaging Partner</h2><p>Not every industrial packaging supplier understands the unique requirements of pharmaceutical manufacturing. Look for a packaging company with experience supporting pharma and life sciences organizations, strong documentation practices, customization capabilities, and reliable manufacturing quality.</p><h2>Benefits of Specialized Pharmaceutical Packaging</h2><ul><li>Improved regulatory compliance</li><li>Reduced contamination risk</li><li>Enhanced product protection</li><li>Better traceability throughout the supply chain</li><li>Reliable transportation of sensitive products</li></ul><h2>Conclusion</h2><p>Rajvi Packaging works with Hyderabad's pharmaceutical and life sciences manufacturers to provide compliant, protective packaging solutions designed for sensitive products and regulated supply chains. From moisture-resistant packaging to customized protective solutions, we help organizations improve product safety, support compliance, and protect product quality during storage and transportation. Contact our team to discuss packaging solutions tailored to your product and regulatory requirements.</p>` },
  { slug: 'chennai-guide-reliable-automotive-packaging-solutions',  title: 'Chennai\'s Guide to Reliable Automotive Packaging Solutions', category: 'Industry Insights', readTime: '6 min read', date: 'November 2025', img: '../images/flp3.jpg', desc: 'Learn how automotive suppliers in Chennai can improve JIT operations, meet OEM packaging standards, and reduce logistics costs with reliable industrial packaging solutions.', content: `<p>Chennai, widely known as the "Detroit of India," is home to one of the country's largest automotive manufacturing ecosystems. With major OEMs and hundreds of component suppliers operating across Sriperumbudur and Oragadam, reliable packaging has become an essential part of maintaining production efficiency, product quality, and uninterrupted just-in-time (JIT) supply chains.</p><h2>The Importance of Packaging in JIT Manufacturing</h2><p>Automotive manufacturers operating under just-in-time production schedules cannot afford delays caused by damaged packaging, incorrect container dimensions, or shortages of packaging materials. Reliable packaging solutions ensure components reach assembly lines safely and on schedule while minimizing production interruptions.</p><h2>Common Packaging Solutions Used Across Chennai's Automotive Cluster</h2><p>Automotive suppliers commonly rely on packaging solutions such as:</p><ul><li>Foldable Large Containers (FLC pallets)</li><li>Corrugated boxes with custom foam inserts</li><li>Returnable plastic crates</li><li>Engineered protective foam packaging</li><li>Component-specific partition systems</li></ul><p>These packaging formats improve handling efficiency, reduce transit damage, and comply with standard automotive logistics practices.</p><h2>Meeting OEM Packaging Standards</h2><p>Many automotive OEMs specify detailed packaging requirements covering container dimensions, labeling standards, material specifications, stacking configurations, and handling procedures. Working with an experienced packaging manufacturer helps suppliers meet these standards consistently while reducing costly trial-and-error during new program launches.</p><h2>Balancing Cost and Protection at High Volumes</h2><p>High-volume manufacturing means even small improvements in packaging efficiency can produce substantial long-term savings. Material optimization, improved space utilization, reusable packaging systems, and right-sized packaging all help reduce logistics costs without sacrificing product protection.</p><h2>Choosing the Right Automotive Packaging Partner</h2><p>Select a packaging partner with experience serving automotive OEMs and Tier-1 suppliers, rapid prototyping capabilities, customized packaging design expertise, and dependable production capacity to support evolving manufacturing requirements.</p><h2>Conclusion</h2><p>Rajvi Packaging supports Chennai's automotive component manufacturers with FLC pallets, foam-based protective cartons, returnable packaging systems, and OEM-compliant industrial packaging solutions designed for demanding, high-volume JIT supply chains. Contact our team to develop customized packaging solutions aligned with your production requirements and OEM specifications.</p>` },
  { slug: 'best-packaging-company-bengaluru-electronics-precision-components',  title: 'Best Packaging Company in Bengaluru for Electronics & Precision Components', category: 'Industry Insights', readTime: '6 min read', date: 'October 2025', img: '../images/epe2.jpg', desc: 'Discover how ESD-safe packaging, anti-static materials, and custom die-cut trays help Bengaluru\'s electronics and precision engineering manufacturers reduce handling damage and improve production efficiency.', content: `<p>Bengaluru's electronics manufacturing and precision engineering industries produce components where even the smallest handling damage can result in product failure. For manufacturers of PCBs, sensors, connectors, and optical components, packaging is not simply a logistics requirement—it is an essential part of quality control and product protection.</p><h2>Precision Components Require Precision Packaging</h2><p>Electronic and precision-engineered components often have delicate surfaces, tight dimensional tolerances, and sensitive connectors. Standard packaging materials such as generic foam or loose bubble wrap frequently fail to secure these parts properly, increasing the risk of scratches, connector damage, and misalignment that may only become apparent during testing or final assembly.</p><h2>Why Anti-Static & ESD-Safe Packaging Matters</h2><p>Electrostatic discharge (ESD) is one of the most common causes of hidden failures in electronic components. To reduce this risk, manufacturers should use packaging specifically designed for electronics, including:</p><ul><li>ESD-safe foam inserts</li><li>Conductive trays</li><li>Anti-static bags</li><li>Protective component separators</li><li>Custom electronic packaging solutions</li></ul><p>These materials help prevent electrostatic damage while protecting components during storage, transportation, and assembly.</p><h2>Custom Die-Cut Trays Improve Production Efficiency</h2><p>Precision die-cut trays designed around the exact footprint of each component help organize parts, simplify assembly-line feeding, reduce manual handling, and prevent movement during transportation. These advantages become increasingly valuable in high-volume manufacturing environments where consistency and efficiency are critical.</p><h2>Choosing a Packaging Partner for Electronics Manufacturing</h2><p>Packaging requirements for electronics differ significantly from conventional industrial packaging. Select a manufacturer with experience serving electronics and precision engineering companies, in-house design capabilities, rapid prototyping, and the ability to customize packaging for evolving component designs.</p><h2>Benefits of Customized Electronics Packaging</h2><ul><li>Reduced handling damage</li><li>Improved assembly efficiency</li><li>Enhanced component protection</li><li>Lower product rejection rates</li><li>Reliable protection during transportation and storage</li></ul><h2>Conclusion</h2><p>Rajvi Packaging supplies ESD-safe foam, anti-static packaging materials, conductive trays, and custom die-cut packaging solutions designed specifically for Bengaluru's electronics and precision component manufacturers. Our packaging solutions help safeguard delicate components, improve manufacturing efficiency, and reduce costly transit and handling damage. Contact our team to develop packaging tailored to your component specifications and production requirements.</p>` },
  { slug: 'protective-packaging-solutions-surat-textile-industrial-exporters',  title: 'Protective Packaging Solutions in Surat for Textile & Industrial Exporters', category: 'Industry Insights', readTime: '6 min read', date: 'September 2025', img: '../images/epe3.jpg', desc: 'Learn how protective packaging helps Surat\'s textile and industrial exporters prevent moisture damage, compression, corrosion, and transit losses during domestic and international shipments.', content: `<p>Surat's export-driven textile and industrial manufacturing sector depends on packaging that protects products throughout long domestic and international supply chains. During transportation, shipments are exposed to moisture, compression, dust, rough handling, and multiple loading and unloading stages. Selecting the right protective packaging helps maintain product quality while reducing transit damage and customer claims.</p><h2>Common Risks During Export Shipments</h2><p>Export consignments typically pass through trucks, warehouses, ports, shipping containers, and multiple logistics partners before reaching their destination. Textile rolls and fabric bales are vulnerable to moisture damage and compression, while industrial products can suffer corrosion, dust contamination, scratches, and impact damage during handling.</p><h2>Moisture & Corrosion Protection</h2><p>Humidity is one of the biggest challenges during long-distance transportation, particularly for exports moving through coastal ports or overseas sea routes. Effective protection may include:</p><ul><li>VCI (Vapor Corrosion Inhibitor) wraps</li><li>Polyethylene liners</li><li>Moisture barrier films</li><li>Desiccant packs</li><li>Protective sealing solutions</li></ul><p>These materials help minimize corrosion, moisture absorption, and contamination during storage and transit.</p><h2>Compression-Resistant Packaging for Textile Products</h2><p>Textile exporters benefit from packaging solutions designed to withstand stacking pressure inside containers. Corrugated wraps, edge protectors, stretch wrapping, and reinforced protective materials help prevent crushing, tearing, and deformation while maintaining product presentation.</p><h2>Meeting Export Compliance Requirements</h2><p>Many international shipments must comply with customer specifications and export regulations. Packaging suppliers should understand requirements such as ISPM-15 compliance for wooden packaging, customer-specific packaging standards, labeling requirements, and documentation needed for international logistics.</p><h2>Choosing the Right Export Packaging Partner</h2><p>An experienced packaging manufacturer can recommend protective materials based on product type, shipping route, climate conditions, and handling requirements. Customized packaging protocols help improve shipment reliability while reducing damage-related costs.</p><h2>Conclusion</h2><p>Rajvi Packaging supplies protective packaging solutions for Surat's textile and industrial exporters, including VCI wraps, moisture-resistant packaging, compression-resistant wrapping systems, protective liners, and customized export packaging solutions. Contact our team to develop a packaging strategy tailored to your products, export destinations, and logistics requirements.</p>` },
  { slug: 'flc-pallet-solutions-vapi-gujarat-automotive-supply-chains',  title: 'FLC Pallet Solutions in Vapi, Gujarat: Built for Automotive Supply Chains', category: 'Industry Insights', readTime: '6 min read', date: 'August 2025', img: '../images/flp2.jpg', desc: 'Discover how Foldable Large Containers (FLCs) help automotive manufacturers in Vapi improve logistics efficiency, reduce transport costs, and protect components throughout the supply chain.', content: `<p>Vapi's industrial belt, with its strong concentration of automotive component manufacturers and chemical processing industries, relies heavily on Foldable Large Containers (FLCs) for efficient, damage-free movement of parts between suppliers and OEM manufacturing plants. Selecting the right FLC pallet solution directly improves handling efficiency, storage utilization, and transportation costs.</p><h2>Why FLCs Are the Preferred Choice for Automotive Supply Chains</h2><p>Foldable Large Containers combine high load capacity with space-saving foldability, making them ideal for returnable packaging systems. Their standardized dimensions ensure compatibility with forklifts, pallet jacks, warehouse racking systems, and automated material handling equipment commonly used by automotive OEMs and Tier-1 suppliers.</p><h2>Design Considerations for Automotive Components</h2><p>Automotive components differ significantly in size, weight, and fragility. Effective FLC solutions often include customized internal features such as:</p><ul><li>Protective foam liners</li><li>Custom partitions and dividers</li><li>Engineered base inserts</li><li>Component-specific support structures</li><li>Anti-scratch protective materials</li></ul><p>Proper internal packaging reduces movement during transit, minimizes damage, and maximizes payload capacity for every shipment.</p><h2>Reduce Logistics Costs Through Foldability</h2><p>One of the greatest advantages of FLCs is their ability to fold flat after unloading. This significantly reduces the space occupied during return transportation, lowering freight costs and improving the efficiency of closed-loop logistics networks between suppliers and OEM plants across Gujarat and Maharashtra.</p><h2>Built for Demanding Industrial Environments</h2><p>Manufacturing facilities in Vapi often expose packaging to dust, humidity, and occasional chemical contact. Durable FLC pallets with reinforced corners, strong weld points, and high-quality materials maintain their structural integrity even under challenging industrial conditions, delivering long service life and consistent performance.</p><h2>Selecting the Right FLC Packaging Partner</h2><p>Choose a packaging manufacturer capable of delivering customized FLC designs, consistent manufacturing quality, high load-bearing capacity, and solutions tailored to your component dimensions and logistics requirements.</p><h2>Conclusion</h2><p>Rajvi Packaging designs Foldable Large Container (FLC) pallet solutions engineered for the demanding requirements of Vapi's automotive supply chains. Our custom FLC packaging solutions combine durability, foldability, optimized load capacity, and component-specific protection to improve logistics efficiency while reducing transportation costs. Contact our team to discuss an FLC configuration designed specifically for your products and supply chain.</p>` },
  { slug: 'custom-pp-boxes-crates-ahmedabad-buyers-guide',  title: 'Custom PP Boxes & Crates in Ahmedabad — A Buyer\'s Guide for Procurement Teams', category: 'Industry Insights', readTime: '6 min read', date: 'July 2025', img: '../images/pp2.jpg', desc: 'Learn how procurement teams in Ahmedabad can evaluate custom PP boxes and crates based on durability, specifications, customization, and long-term cost efficiency.', content: `<p>Ahmedabad's manufacturing and pharma-adjacent industries increasingly rely on polypropylene (PP) boxes and crates for their durability, chemical resistance, and reusability. For procurement teams evaluating suppliers, understanding what differentiates one PP packaging vendor from another can significantly reduce long-term packaging costs and improve operational efficiency.</p><h2>Why Choose PP Boxes Over Corrugated or Wooden Packaging?</h2><p>PP boxes and crates provide superior resistance to moisture, chemicals, and repeated handling compared to traditional corrugated cartons or wooden crates. They are washable, reusable for hundreds of shipping cycles, and maintain their structural integrity even in humid industrial environments. This makes them an excellent choice for returnable packaging systems and closed-loop logistics.</p><h2>Key Specifications Procurement Teams Should Evaluate</h2><p>When comparing suppliers, evaluate the following technical specifications:</p><ul><li>Wall thickness and material quality</li><li>Static and dynamic load-bearing capacity</li><li>UV stabilization for outdoor storage</li><li>Foldable or collapsible designs for return logistics</li><li>Dimensional accuracy and manufacturing consistency</li></ul><p>These specifications directly influence durability, storage efficiency, and long-term operating costs.</p><h2>Customization Options That Improve Operations</h2><p>Beyond standard sizes, leading packaging manufacturers offer custom solutions such as:</p><ul><li>Internal dividers and partitions</li><li>Ventilation slots</li><li>Tamper-evident locking mechanisms</li><li>Embossed company logos and branding</li><li>Custom dimensions for specific components</li></ul><p>These customizations improve product protection, simplify material handling, and increase efficiency throughout manufacturing and warehouse operations.</p><h2>Evaluate Total Cost of Ownership, Not Just Unit Price</h2><p>The lowest purchase price does not always provide the best value. A PP crate that lasts more than 300 usage cycles delivers significantly lower lifetime cost than one that fails after only a few dozen trips. Ask suppliers about expected cycle life, material quality, warranty options, and trial samples before placing large-volume orders.</p><h2>Choosing the Right Packaging Partner</h2><p>Select a manufacturer with proven experience in industrial packaging, in-house customization capabilities, consistent production quality, and the ability to support large-scale procurement requirements with dependable delivery schedules.</p><h2>Conclusion</h2><p>Rajvi Packaging manufactures custom PP boxes and industrial crates for manufacturers and procurement teams across Ahmedabad. Designed for durability, reusability, and demanding industrial environments, our packaging solutions help reduce replacement costs while improving logistics efficiency. Contact us to request technical specifications, sample products, or customized packaging solutions tailored to your operational requirements.</p>` },
  { slug: 'top-packaging-solutions-provider-mumbai-ecommerce-brands',  title: 'Top Packaging Solutions Provider in Mumbai for E-commerce Brands', category: 'Industry Insights', readTime: '5 min read', date: 'June 2025', img: '../images/air3.jpg', desc: 'Discover how Mumbai e-commerce businesses can reduce shipping damage, optimize packaging costs, and improve customer experience with the right industrial packaging solutions.', content: `<p>Mumbai's e-commerce ecosystem—from D2C fashion brands to electronics resellers—depends on packaging that survives multiple handling touchpoints, protects products, and still looks good when the customer opens the box. Achieving this balance is critical for reducing damage, improving customer satisfaction, and controlling logistics costs.</p><h2>The E-commerce Packaging Challenge</h2><p>Unlike traditional B2B shipments, e-commerce parcels move through courier hubs, sorting centers, last-mile delivery networks, and doorstep handling. Every stage increases the risk of drops, compression, vibration, and moisture exposure. Packaging must therefore provide reliable protection while remaining lightweight and cost-effective.</p><h2>Right-Sized Packaging Reduces Cost and Waste</h2><p>Oversized cartons increase packaging material usage and shipping expenses because many logistics providers calculate charges based on volumetric weight. Choosing right-sized cartons for each product category minimizes waste, lowers freight costs, and improves operational efficiency without compromising protection.</p><h2>Protective Packaging Materials Worth Considering</h2><ul><li>Air bubble rolls for shock absorption</li><li>Honeycomb paper wrap for eco-friendly cushioning</li><li>Corrugated inserts for structural protection</li><li>Poly mailers for apparel and lightweight products</li><li>Anti-static liners for electronics</li><li>Moisture-resistant liners for beauty and personal care products</li></ul><p>Selecting the right protective material depends on the product's fragility, shipping distance, and storage conditions.</p><h2>Branding Without Compromising Protection</h2><p>Packaging also plays a key role in customer experience. Custom-printed tapes, branded mailers, and marketing inserts enhance brand recall during unboxing while maintaining structural integrity. An experienced packaging partner can integrate branding elements without reducing product protection.</p><h2>Choosing the Right Packaging Partner</h2><p>Look for a packaging manufacturer that can provide custom carton sizes, protective packaging materials, consistent quality, quick turnaround times, and scalable production to support growing order volumes.</p><h2>Conclusion</h2><p>Rajvi Packaging supports Mumbai-based e-commerce businesses with right-sized cartons, protective cushioning materials, branded packaging solutions, and custom packaging designed for the realities of modern logistics. Whether you're shipping apparel, electronics, cosmetics, or consumer goods, our packaging solutions help reduce transit damage, optimize shipping costs, and deliver a better customer experience.</p>` },
  { slug: 'pune-manufacturers-custom-foam-packaging-auto-components',  title: 'Why Pune Manufacturers Choose Custom Foam Packaging for Auto Components', category: 'Industry Insights', readTime: '6 min read', date: 'May 2025', img: '../images/foam1.jpg', desc: 'Pune\'s auto-ancillary cluster ships precision components daily. Learn why custom-engineered foam packaging is becoming essential for protecting parts and maintaining OEM relationships.', content: `<p>Pune's auto-ancillary cluster — spanning Chakan, Talegaon, and Pimpri — ships a huge volume of precision components daily, from engine parts to sensors. Standard packaging often fails to protect these parts adequately, leading to returns, rework, and strained OEM relationships. That is why more Pune-based manufacturers are shifting to custom-engineered foam packaging.</p><h2>The Cost of Getting Packaging Wrong</h2><p>Damaged auto components during transit don't just mean a replacement cost — they trigger quality audits, delay production lines downstream, and can affect a supplier's standing with OEMs who run strict PPM (parts-per-million) defect tracking. Generic packaging that doesn't match component geometry is one of the most common and preventable causes of these failures.</p><h2>How Custom Foam Solves the Problem</h2><p>Custom-cut foam inserts are designed around the exact shape, weight distribution, and fragility of each component. This eliminates internal movement during transit, protects finished surfaces from scuffing, and allows components to be packed in a way that maximizes container or truck utilization — reducing per-unit logistics cost.</p><h2>Reusable & Returnable Packaging Trends</h2><p>Many Pune auto-ancillary units are moving toward returnable foam trays and bins as part of closed-loop supply chains with OEMs. This reduces packaging waste and long-term costs, but requires a packaging partner experienced in designing foam that withstands repeated handling cycles without losing its protective shape.</p><h2>What to Look For in a Foam Packaging Partner</h2><p>Prioritize a supplier with in-house CNC foam cutting or fabrication, a track record with auto-ancillary clients, and the ability to run design trials quickly. Fast turnaround on prototypes matters especially when a new component or variant is being introduced on short notice.</p><h2>Conclusion</h2><p>Rajvi Packaging designs and manufactures custom foam packaging tailored to auto components, helping Pune-based manufacturers cut transit damage and streamline returnable packaging cycles. Reach out for a component-specific packaging assessment.</p>` },
  { slug: 'best-industrial-packaging-solutions-hyderabad',  title: 'Best Industrial Packaging Solutions in Hyderabad for Automotive & Electronics Manufacturers', category: 'Industry Insights', readTime: '7 min read', date: 'April 2025', img: '../images/mfg_cnc.jpg', desc: 'Learn how automotive and electronics manufacturers in Hyderabad can reduce packaging damage, improve logistics efficiency, and choose the right industrial packaging solutions.', content: `<p>Hyderabad has grown into a major hub for automotive component makers and electronics assemblers, and both industries share one non-negotiable requirement: packaging that protects precision parts through handling, transit, and storage without adding unnecessary cost. Choosing the right industrial packaging partner in the city can mean fewer rejections, lower freight damage, and smoother line-side operations.</p><h2>What Automotive & Electronics Units in Hyderabad Actually Need</h2><p>Automotive component manufacturers around the Pashamylaram, Patancheru, and Gaddapotharam industrial belts typically ship gears, brackets, sensors, and wiring harnesses that are sensitive to scratches and corrosion.</p><p>Electronics manufacturers deal with static-sensitive PCBs, connectors, and delicate housings. Both industries require packaging that combines cushioning, dimensional accuracy, and reusability for returnable supply chains.</p><h2>Key Packaging Formats to Look For</h2><p>For automotive manufacturing:</p><p>- Engineered foam inserts<br>- Corrugated FLC pallets<br>- PP corrugated boxes</p><p>These provide excellent protection while maintaining stackability.</p><p>For electronics manufacturing:</p><p>- Anti-static foam<br>- Bubble sheets<br>- Precision die-cut trays</p><p>These help prevent scratches, vibration damage, and electrostatic discharge during transit.</p><p>A good packaging partner should prototype custom inserts using actual component dimensions rather than relying on generic sizes.</p><h2>Why Local Manufacturing Matters</h2><p>Working with a Hyderabad-based packaging manufacturer reduces lead times, enables faster packaging design iterations for new component variants, and lowers inbound logistics costs associated with transporting bulky packaging materials over long distances.</p><h2>Questions to Ask Before Finalizing a Vendor</h2><p>Evaluate suppliers based on:</p><p>- In-house tooling capability<br>- Custom foam manufacturing<br>- Die-cut tray development<br>- Minimum order quantities<br>- Quality certifications<br>- JIT (Just-in-Time) delivery capability<br>- Experience supporting OEM manufacturing requirements<br>- Packaging validation and trial support before mass production</p><h2>Conclusion</h2><p>Rajvi Packaging works closely with automotive and electronics manufacturers across Hyderabad's industrial corridors, offering custom foam, FLC pallets, PP corrugated boxes, and protective packaging engineered around exact component specifications.</p><p>If packaging damage, rework, or logistics costs have become recurring issues, discussing a tailored packaging solution with an experienced packaging partner is an effective first step.</p>` },
  { slug: 'why-pp-returnable-boxes-automotive-supply-chains',  title: 'Why PP Returnable Boxes Are Replacing Single-Use Packaging in Automotive Supply Chains', category: 'Automotive Packaging', readTime: '5 min read', date: 'March 2025', img: 'https://images.unsplash.com/photo-1610891015188-5369212db097?q=80&w=1529&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', desc: 'How reusable PP crate systems reduce cost, waste and handling damage for component manufacturers supplying to automotive assembly units.', content: `<p>How reusable PP crate systems reduce cost, waste and handling damage for component manufacturers supplying to automotive assembly units.</p><p>The automotive supply chain is one of the most demanding packaging environments in any industry. Components move between suppliers, sub-assemblers and final assembly plants in high volumes and at high frequency. Every packaging decision — material, design, reusability — compounds across millions of transactions per year.</p><p>Single-use cardboard boxes were the default for decades. They were cheap per unit, widely available and easy to source. But when you start counting the full cost — cardboard management at assembly plants, disposal costs, the environmental burden, and the handling inconsistencies that come with packaging that degrades from day one — the economics look very different.</p><p>PP corrugated returnable boxes solve these problems systematically. A well-designed PP crate system can complete 50 to 100 use cycles before replacement, which means the cost per trip drops to a fraction of single-use cardboard. The boxes maintain consistent dimensions throughout their service life, which improves warehouse organization, forklift compatibility, and automated handling reliability. They withstand moisture, which matters in plants where temperature changes cause condensation. And at end of service life, PP corrugated is recyclable.</p><p>For component manufacturers, the transition requires upfront investment and supply chain coordination with receiving plants. But businesses that have made the shift consistently report payback periods of less than 12 months on the packaging capital, with ongoing savings in disposal costs, reduced component damage, and more organized inbound logistics at assembly plants.</p><p>Rajvi Packaging develops PP returnable box systems specifically for automotive supply chains — standardized dimensions for common component categories, custom configurations for specific parts, and partition and insert systems that hold components in position throughout transit.</p>` },
  { slug: 'epe-vs-xlpe-foam-right-for-product',  title: 'EPE vs XLPE Foam: Which Is Right for Your Product?', category: 'Material Guide', readTime: '4 min read', date: 'February 2025', img: 'https://images.unsplash.com/photo-1716191300020-b52dec5b70a8?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', desc: 'A practical guide to understanding the difference between expanded and cross-linked polyethylene foam — when to use each and how to choose for your application.', content: `<p>A practical guide to understanding the difference between expanded and cross-linked polyethylene foam — when to use each and how to choose for your application.</p><p>EPE (Expanded Polyethylene) and XLPE (Cross-Linked Polyethylene) are both polyethylene-based foams, but their manufacturing processes produce materials with meaningfully different properties. Getting the choice right affects packaging performance, cost and product protection significantly.</p><p><strong>EPE Foam</strong> is produced by expanding polyethylene with a chemical or physical blowing agent. The result is a lightweight, flexible foam with good cushioning properties, moisture resistance and chemical inertness. It is cost-effective, easy to process into pouches and cut shapes, and suitable for a wide range of packaging applications — electronics, glassware, automotive parts, consumer goods.</p><p><strong>XLPE Foam</strong> goes through an additional cross-linking step that bonds the polymer chains together. This produces a foam with superior dimensional stability, higher density options, better compression set resistance, and improved surface smoothness. XLPE is the choice when product protection requirements are more demanding — high-value electronics, precision instruments, components that need exact-fit protection over many handling cycles, or applications where thermal insulation matters alongside cushioning.</p><p>The practical choice comes down to three questions: How fragile is the product? How many handling cycles will the packaging go through? And does the application have any thermal insulation requirements? If the answer to any of those tilts toward demanding, XLPE is worth the additional cost. For standard protective packaging applications, EPE delivers excellent performance at lower cost.</p><p>Rajvi Packaging supplies both EPE and XLPE in sheet, roll and custom-cut form — and the team can help you select the right specification for your specific product and application requirements.</p>` },
  { slug: 'understanding-flc-pallet-systems-industrial-logistics',  title: 'Understanding FLC Pallet Systems for Industrial Logistics', category: 'Logistics', readTime: '6 min read', date: 'January 2025', img: 'https://media.istockphoto.com/id/471824724/photo/factory-industrial-plant.webp?a=1&b=1&s=612x612&w=0&k=20&c=gWXuwD7XTdUyZ1xpXugousvLqGFu4mbG6DlPJ6j-XAc=', desc: 'What foldable large containers are, how they work and when they make economic and operational sense for your warehouse or supply chain.', content: `<p>What foldable large containers are, how they work and when they make economic and operational sense for your warehouse or supply chain.</p><p>FLC — Foldable Large Container — pallets are a category of heavy-duty returnable packaging designed for industrial bulk logistics. Understanding what they are and when they make sense requires looking at the problem they solve.</p><p>In industrial supply chains, heavy components — engine assemblies, machined castings, large fabricated parts — need to move between suppliers, manufacturers and assembly plants repeatedly. The packaging has to handle significant loads, survive forklift operations, and maintain its structural integrity across many use cycles. Traditional wooden crates or rigid metal containers do this, but they have a critical operational problem: when empty, they take up almost as much space as when full.</p><p>FLC pallets solve this by folding flat when empty. A standard FLC pallet that holds 600–800kg of components when in use can collapse to a fraction of its assembled height when empty. A truck that would carry 10 assembled rigid containers can carry 50 or 60 collapsed FLC pallets. Return logistics costs drop dramatically, and empty container storage at both ends of the supply chain is dramatically reduced.</p><p>The economic case depends on supply chain length and volume. For high-volume, long-distance supply chains where return freight is a significant line item, FLC systems typically pay back the capital investment within 12–18 months and deliver ongoing savings for the life of the equipment.</p><p>Rajvi Packaging supplies FLC systems in standard sizes (1200x1000, 1200x800, 800x600 and custom) as full sets or sleeves only — including second-hand imported sets for cost-sensitive applications.</p>` },
  { slug: 'pharmaceutical-hygienic-secure-packaging-solutions',  title: 'Why Pharmaceutical Companies Need Hygienic and Secure Packaging Solutions', category: 'Pharmaceutical', readTime: '6 min read', date: 'December 2024', img: 'https://media.istockphoto.com/id/1136735121/photo/industrial-plant-for-the-production-of-large-mechanisms-machines-and-structures.webp?a=1&b=1&s=612x612&w=0&k=20&c=4DtPULzc9pNEovM4YVuiprmJYmfAOk96U1lW09yhSj8=', desc: 'Most industries can absorb a packaging failure as a financial problem. In pharmaceuticals, the consequences can go further than that.', content: `<p>Most industries can absorb a packaging failure as a financial problem. In pharmaceuticals, the consequences can go further than that.</p><p>A medicine that has been exposed to moisture during transit may no longer be effective. A medical device that has been contaminated may be unsafe to use. A blister pack that has been compromised loses its tamper-evidence function, which is not just a quality issue — it is a regulatory one.</p><p>The range of threats that pharmaceutical products face during transportation is wider than most people appreciate. Moisture degrades tablets and capsules. Temperature changes during long transit periods compromise certain medicines and vaccines. Physical impact can shatter glass bottles, crack blister packs, or damage delicate medical instruments. Dust and bacteria need to be kept out of products that will be applied to or introduced into the human body.</p><p>Rajvi Packaging provides solutions built around these requirements. For fragile medical devices and precision instruments, foam-based protective packaging holds items securely in place and absorbs the forces that would otherwise reach them. Foam inserts can be shaped to fit around specific instruments, preventing movement entirely. Polypropylene boxes serve as organized, hygienic, reusable storage that can be disinfected between uses.</p>` },
  { slug: 'ecommerce-businesses-depend-strong-packaging-solutions',  title: 'How E-Commerce Businesses Depend on Strong Packaging Solutions', category: 'E-Commerce', readTime: '5 min read', date: 'November 2024', img: 'https://images.unsplash.com/photo-1676451727332-790e79f6cc59?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGZhY3RvcnklMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D', desc: 'Online shopping has changed a lot of things about how businesses sell. One thing it has not changed is the moment when a customer opens their delivery.', content: `<p>Online shopping has changed a lot of things about how businesses sell and how customers buy. One thing it has not changed is the moment when a customer opens their delivery and decides whether the experience was worth it.</p><p>That moment happens entirely without the seller present. There is no shop assistant to explain a scuff on the packaging or reassure the customer that the product inside is fine. If the product has shifted during transit, that is unsettling. If the packaging is crushed or torn, trust drops immediately.</p><p>The financial stakes extend beyond the cost of a single damaged product. When a customer returns an item, the business absorbs the cost of return shipping, processing time, customer service, and potentially a product that can no longer be sold as new. On marketplace platforms where ratings are public, a pattern of damaged deliveries affects visibility and future sales in ways that compound over time.</p><p>Rajvi Packaging's solutions for e-commerce are manufactured specifically for shipping conditions. Bubble rolls wrap individual items quickly and effectively. Foam inserts and EPE foam pouches provide structured cushioning that holds products in position rather than just surrounding them loosely. For premium brands, rigid boxes make a statement about the brand before the customer even sees the product.</p>` },
  { slug: 'electronics-industry-preventing-damage-transit',  title: 'Packaging Solutions for the Electronics Industry: Preventing Damage During Transit', category: 'Electronics', readTime: '7 min read', date: 'October 2024', img: 'https://images.unsplash.com/photo-1511454493857-0a29f2c023c7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGZhY3RvcnklMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D', desc: 'One of the most challenging things about packaging electronics is that the damage you most need to prevent is often the damage you cannot see.', content: `<p>One of the most challenging things about packaging electronics is that the damage you most need to prevent is often the damage you cannot see.</p><p>Drop a glass and the result is obvious. Subject a circuit board to the wrong kind of vibration over a long transit journey and it might look perfectly fine while internal connections have fractured. Expose a processor to an electrostatic discharge during packing and there may be no visible sign at all — just a product that underperforms or stops working before it should.</p><p>Electrostatic discharge deserves particular attention because it is so consistently underestimated. Static charges can be generated by something as ordinary as a person's hand moving across a plastic surface. Many consumer electronics components — circuit boards, processors, display drivers — can be permanently damaged by levels of static that are completely undetectable to human senses. ESD-safe foam, which dissipates static charges safely rather than allowing them to build up, is not an optional upgrade — it is a basic requirement.</p><p>Rajvi Packaging builds electronics packaging around a layered approach. The outer box provides structural defense against external forces. The inner foam layer provides cushioning and static protection. Custom foam inserts eliminate internal movement entirely — and that alone significantly reduces damage rates.</p>` },
  { slug: 'fmcg-brands-need-smart-packaging-solutions',  title: 'Why FMCG Brands Need Smart Packaging Solutions', category: 'FMCG', readTime: '5 min read', date: 'September 2024', img: 'https://plus.unsplash.com/premium_photo-1682146920372-bd950e25125d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjV8fGZhY3RvcnklMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D', desc: 'Packaging decisions in the FMCG industry have a multiplying effect that does not exist in most other sectors.', content: `<p>Packaging decisions in the FMCG industry have a multiplying effect that does not exist in most other sectors.</p><p>When you are moving millions of units through a distribution network, a cost saving of one rupee per unit sounds attractive. But if that saving comes at the expense of packaging performance, and your damage rate rises by even a fraction of a percent, the financial impact of those damaged products at scale can easily exceed what was saved.</p><p>At the same time, the FMCG supply chain is genuinely demanding. Products move from manufacturing facilities through regional distribution centers, local warehouses, and retail outlets, handled repeatedly at each stage. The packaging has to survive all of that without failing — while staying light enough not to add unnecessary shipping cost, and economical enough not to erode margins that are already tight.</p><p>Rajvi Packaging manufactures corrugated boxes for FMCG clients engineered for real distribution environments — strong enough for stacking loads, consistent enough that warehouse operations can rely on them. For glass bottles, ceramic containers and premium cosmetics, bubble rolls, foam packaging, and EPE foam pouches reduce breakage rates and the associated costs of damaged goods moving through high-volume distribution.</p>` },
  { slug: 'role-packaging-textile-garment-industry',  title: 'The Role of Packaging in the Textile and Garment Industry', category: 'Textile', readTime: '5 min read', date: 'August 2024', img: 'https://plus.unsplash.com/premium_photo-1677695581626-2a75bdece138?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fGZhY3RvcnklMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D', desc: 'Fabric and clothing do not shatter or short-circuit. But that does not mean they arrive in perfect condition without proper packaging.', content: `<p>Fabric and clothing do not shatter or short-circuit. But that does not mean they arrive in perfect condition without proper packaging — and in the textile trade, a product that reaches a retailer looking anything less than perfect is a problem that costs real money.</p><p>A wrinkled garment needs rework before it can go on the floor. A dusty or damp fabric roll needs inspection and potentially cleaning. Moisture is one of the most persistent problems. Natural fiber garments — cotton, wool, silk — respond to humidity in ways that synthetic fabrics do not.</p><p>Compression is another challenge specific to bulk textile shipping. When garments are stacked tightly for transportation, the weight of upper layers presses down on lower layers over extended periods. Fabrics that do not recover well from sustained pressure can arrive permanently creased.</p><p>Rajvi Packaging's corrugated boxes for textile shipments provide structural containment that prevents external stacking loads from reaching the garments inside. Polypropylene boxes offer reusable, cleanable storage for warehouse management. For premium garments, bubble rolls and foam packaging create a protective layer between the garment and the packaging walls, preventing surface damage during transit.</p>` },
  { slug: 'industrial-manufacturers-customized-packaging-solutions',  title: 'How Industrial Manufacturers Benefit from Customized Packaging Solutions', category: 'Industrial', readTime: '6 min read', date: 'July 2024', img: 'https://plus.unsplash.com/premium_photo-1682144873944-ac733dbe7828?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzd8fGZhY3RvcnklMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D', desc: 'In industrial manufacturing, the cost of a packaging failure is rarely just the cost of the damaged part.', content: `<p>In industrial manufacturing, the cost of a packaging failure is rarely just the cost of the damaged part.</p><p>When a precision component arrives damaged and needs to be replaced, the clock starts running immediately on production downtime. Depending on the part, the replacement might take days to source or weeks — some industrial components are made to order and simply cannot be rushed.</p><p>Industrial products present packaging challenges that are meaningfully different from consumer industries. Many components are very heavy, requiring packaging with load-bearing capacity that standard materials simply do not have. Many are irregularly shaped — with protruding shafts, complex surface geometries, flanges, and connection points that make off-the-shelf box sizes impractical.</p><p>Rajvi Packaging approaches industrial packaging with the recognition that standard solutions are almost never appropriate for this sector. PU foam can be molded or cut to create inserts that hold complex components in precisely defined positions, distributing weight across the foam surface rather than concentrating it at vulnerable points. When packaging is designed around a specific component, packing operations become faster and more consistent.</p>` },
  { slug: 'food-industry-requires-reliable-packaging-solutions',  title: 'Why the Food Industry Requires Reliable Packaging Solutions', category: 'Food Industry', readTime: '6 min read', date: 'June 2024', img: 'https://images.unsplash.com/photo-1741591646737-e634ae96e83d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fGZhY3RvcnklMjBpbWFnZXN8ZW58MHx8MHx8fDA%3D', desc: 'There is one thing that makes food packaging different from almost every other packaging category: the product inside is going to be consumed by a person.', content: `<p>There is one thing that makes food packaging different from almost every other packaging category: the product inside is going to be consumed by a person.</p><p>That simple fact raises the stakes of packaging failure in a way that does not apply to most other industries. A food product that has been contaminated, spoiled, or compromised by packaging failure is a potential health issue — one that carries regulatory, legal, and reputational consequences well beyond the value of the product itself.</p><p>The threats that food packaging has to manage are varied. Moisture weakens packaging materials, accelerates microbial growth, affects texture and taste. Contamination from dust, insects, and environmental bacteria needs to be prevented at every stage. Physical damage is a constant concern for products in glass containers — sauces, beverages, oils, condiments.</p><p>Rajvi Packaging manufactures corrugated boxes for the food industry that provide structural strength needed to handle real stacking loads while staying light enough to keep logistics costs manageable. For fragile food containers, internal protective materials — bubble rolls, foam padding, protective buffers — absorb impact and vibration energy, significantly reducing breakage rates.</p>` }
];

// ===== CASE STUDY DATA =====
const CASE_STUDIES = {
  'foam-cs-1': { num: '01', title: 'Automotive Components Manufacturer Reduces Transit Damage', industry: 'Automotive', challenge: 'A leading automotive parts manufacturer was experiencing significant transit damage to dashboard assemblies and interior trim components during transportation between manufacturing facilities and assembly plants. The company was incurring high replacement costs and facing customer satisfaction issues due to damaged components arriving at assembly lines.', solution: 'The company implemented customized EPE and PU foam buffers designed specifically for the shape and dimensions of the components. Foam inserts were integrated into corrugated shipping containers to prevent movement and absorb shocks during transit. Each insert was CNC-cut to match the exact geometry of the dashboard assembly, eliminating all internal movement during transportation.', result: '70% reduction in transit-related damage. Lower product replacement costs. Improved customer satisfaction. Reduced warranty claims. Increased operational efficiency.', stats: [{ num: '70%', label: 'Reduction in Transit Damage' }, { num: '0', label: 'Surface Damage Incidents' }] },
  'foam-cs-2': { num: '02', title: 'ESD Foam Solution for PCB Export Packaging', industry: 'Electronics', challenge: 'An electronics manufacturer needed ESD-safe packaging for sensitive PCBs destined for international export. Previous packaging had resulted in electrostatic discharge damage during handling at various transit points, leading to significant warranty claims and damaged customer relationships.', solution: 'Multi-layer ESD foam inserts with anti-static film lamination were designed to provide full component protection. The foam inserts were precisely cut to hold each PCB in a fixed position, preventing any movement. ESD film outer layers dissipated any static charges generated during handling, protecting the sensitive electronic components throughout the entire export journey.', result: 'Electrostatic damage incidents reduced to zero. Export compliance achieved. Warranty claims eliminated. Customer confidence restored.', stats: [{ num: '100%', label: 'ESD Damage Prevention' }, { num: '0', label: 'Transit Damage Claims' }] },
  'foam-cs-3': { num: '03', title: 'PU Foam Corners for Home Appliance Shipments', industry: 'White Goods', challenge: 'A white goods manufacturer faced persistent corner damage during domestic distribution. Refrigerators, washing machines and coolers were arriving at retailers and customers with visible corner dents and scratches, resulting in returns, replacements and brand reputation damage.', solution: 'Custom die-cut PU foam corner protectors were developed to fit precisely around each appliance corner. The protectors were engineered to absorb drop impact energy, preventing force from reaching the appliance body. The PU foam specification was selected for its optimal balance of softness (for surface protection) and energy absorption (for impact resistance).', result: 'Customer return rate from transit damage reduced by over 60%. Brand reputation improved. Distribution partner satisfaction increased significantly.', stats: [{ num: '60%+', label: 'Reduction in Returns' }, { num: 'Zero', label: 'Surface Marking Claims' }] },
  'bubble-cs-1': { num: '01', title: 'Bubble Wrap Solution for Fragile Glassware Fulfilment', industry: 'E-Commerce', challenge: 'A home goods e-commerce brand required consistent wrapping protection for fragile glassware being shipped through their fulfilment operations. High breakage rates were driving up replacement costs and generating negative customer reviews, while inconsistent manual wrapping was creating quality variability.', solution: 'Pre-cut bubble pouches in multiple sizes were supplied to match the specific glassware product range. The standardised pouch sizes allowed packing staff to select the right pouch for each item quickly. The bubble specification was matched to the weight and fragility profile of the glassware range.', result: 'Breakage in transit reduced by 85%. Packing time per unit reduced significantly. Customer satisfaction scores improved.', stats: [{ num: '85%', label: 'Reduction in Breakage' }, { num: '3×', label: 'Faster Packing Speed' }] },
  'bubble-cs-2': { num: '02', title: 'Anti-Static Bubble Wrapping for Medical Device Export', industry: 'Pharmaceutical', challenge: 'A medical device exporter needed ESD-safe protective wrapping for electronic diagnostic instruments being exported internationally. Standard bubble wrap was generating static during the wrapping process, potentially damaging sensitive electronic components within the medical devices.', solution: 'Anti-static bubble pouches were custom-sized for the device geometry and certified for export compliance. The ESD-safe material dissipates static charges during handling rather than allowing them to accumulate, protecting sensitive electronic components throughout all handling stages of the international export journey.', result: 'Device damage in transit eliminated. Export compliance achieved. Customer confidence in shipment integrity restored.', stats: [{ num: '0', label: 'Devices Damaged in Transit' }, { num: '100%', label: 'Export Compliance Rate' }] },
  'bubble-cs-3': { num: '03', title: 'Laminated Bubble Sheets for Component Interleaving', industry: 'Automotive', challenge: 'An automotive components manufacturer required moisture-resistant interleaving between metal parts during sea freight. Salt air and humidity during long ocean voyages were causing surface corrosion on metal components despite outer carton protection.', solution: 'Aluminium-laminated bubble sheets were specified for interleaving between metal components. The aluminium foil layer provides a complete moisture barrier, preventing salt-laden air from reaching metal surfaces. The bubble layer provides cushioning that prevents metal-to-metal contact and surface scratching during transit movement.', result: 'Surface corrosion eliminated across all sea freight routes. Component rejection on arrival eliminated. Significant cost saving in replacement and re-processing.', stats: [{ num: '0', label: 'Corrosion Incidents' }, { num: '100%', label: 'Components Accepted on Arrival' }] },
  'epe-cs-1': { num: '01', title: 'EPE Pouches for Consumer Electronics Retail Packaging', industry: 'Electronics', challenge: 'A consumer electronics brand required surface-safe packaging for assembled products ahead of retail distribution. Products were experiencing scratching and minor surface damage during handling in the warehouse and distribution phases, affecting the unboxing experience for end customers.', solution: 'Custom EPE pouches in branded sizes provided scratch-free protection and a consistent unboxing presentation. The pouch dimensions were matched to each product size to prevent internal movement. The smooth closed-cell EPE surface provided gentle, non-marking protection against warehouse and transit handling.', result: 'Zero surface damage reported across 18-month production run. Unboxing experience consistently positive. No warranty claims related to surface damage.', stats: [{ num: '18+', label: 'Months Zero Damage' }, { num: '100%', label: 'Surface Protection Rate' }] },
  'epe-cs-2': { num: '02', title: 'EPE Pouches for Precision Machined Part Protection', industry: 'Automotive', challenge: 'A precision components manufacturer needed individual protection for machined metal parts during internal logistics transfers. Parts were experiencing surface scratching and marking from contact with other parts during bin transfers, causing quality rejections.', solution: 'Custom EPE pouches matched to each part dimension were introduced as individual part protection throughout the internal logistics flow. Each part was pouched immediately after machining and remained pouched through all handling stages until final assembly.', result: 'Part rejection from handling damage reduced by 70%. Machining scrap rate reduced. Internal quality complaints eliminated.', stats: [{ num: '70%', label: 'Reduction in Rejections' }, { num: '0', label: 'Surface Damage Complaints' }] },
  'epe-cs-3': { num: '03', title: 'EPE Roll Stock for Fulfilment Centre Void Fill', industry: 'Logistics', challenge: 'A multi-category logistics operator needed to standardise void fill and product wrapping materials across fulfilment centres. Bubble wrap was the previous standard but its bulk and weight were adding unnecessary cost to packaging material usage and shipping weight calculations.', solution: 'EPE foam roll stock was introduced as the standard void fill and wrapping material across fulfilment operations. The material provided equivalent cushioning protection at lower weight per unit area than bubble wrap, reducing both packaging material costs and the weight contribution to shipping calculations.', result: 'Packaging material costs reduced by 40% vs previous bubble wrap. Shipping weight calculations improved. Operations efficiency maintained.', stats: [{ num: '40%', label: 'Cost Reduction vs Bubble Wrap' }, { num: '25%', label: 'Weight Reduction Per Unit' }] },
  'pp-cs-1': { num: '01', title: 'PP Returnable Boxes for Automotive Assembly Supply Chain', industry: 'Automotive', challenge: 'A major automotive OEM was generating massive volumes of single-use cardboard packaging waste at their assembly plants from inbound supplier packaging. The disposal cost, the environmental impact, and the handling inconsistency of degrading cardboard were all creating operational problems.', solution: 'Standardized PP corrugated returnable boxes were implemented across the supplier network. Uniform dimensions improved forklift handling, automated conveyor compatibility and line-side organization. A collection and return system was established between the assembly plant and suppliers.', result: 'Inbound packaging waste reduced by over 90%. Capital investment returned within 8 months from waste disposal savings alone. Handling efficiency improved significantly.', stats: [{ num: '90%', label: 'Waste Reduction' }, { num: '8mo', label: 'Payback Period' }] },
  'pp-cs-2': { num: '02', title: 'PP Crates for Precision Component Inter-Plant Transfers', industry: 'Engineering', challenge: 'An engineering manufacturer required reusable crates for transferring precision machined components between plants. Existing cardboard packaging was degrading quickly and providing inconsistent protection, with component damage in transit creating production disruption.', solution: 'PP crates with custom foam inserts were designed for each component category transferred between plants. The crates provided consistent structural performance across all use cycles and the foam inserts held components in fixed positions, preventing any transit movement.', result: 'Component damage in transit reduced to zero. Crate cost per trip significantly lower than cardboard alternatives over service life. Production disruption from transit damage eliminated.', stats: [{ num: '0', label: 'Transit Damage Incidents' }, { num: '60+', label: 'Use Cycles Per Crate' }] },
  'pp-cs-3': { num: '03', title: 'PP Sheet Dividers for Multi-Tier Pallet Storage', industry: 'Warehousing', challenge: 'A logistics operator required lightweight, moisture-resistant dividers for multi-tier pallet storage. Cardboard sheet dividers were failing in the warehouse environment due to humidity and compression, causing product damage and requiring frequent replacement.', solution: 'PP corrugated sheets replaced cardboard throughout the facility\'s multi-tier pallet storage operations. The moisture-resistant PP material maintained consistent rigidity throughout service life. Custom-cut sizes were produced to match the pallet dimensions and storage configuration.', result: 'Product losses from storage moisture damage eliminated. Divider replacement cost reduced significantly. Warehouse operations improved.', stats: [{ num: '0', label: 'Product Damage from Storage' }, { num: '12×', label: 'Longer Service Life vs Cardboard' }] },
  'gasket-cs-1': { num: '01', title: 'Foam Gasket for LED Lighting — BrightGlow Electronics', industry: 'LED Lighting Manufacturing', challenge: 'BrightGlow Electronics manufactures LED panel lights and outdoor lighting systems for commercial buildings. The company faced repeated customer complaints: small gaps between the LED panel body and cover allowed dust and moisture to enter, reducing product life. During shipping, vibrations caused internal components to loosen or crack. Customer returns increased by 18%.', solution: 'EVA Closed-Cell Foam Gaskets (5mm thickness, waterproof and dust-resistant) were placed between the LED frame, protective cover and internal circuit housing. This created an airtight seal. Additional foam gasket strips were inserted around corners, sensitive electronic sections and connector areas to reduce vibration during transport.', result: 'Product damage rate reduced from 18% to 4%. Dust complaints reduced to very low. Transportation damage reduced from frequent to minimal. Product life increased from 2 years average to 4+ years.', stats: [{ num: '18%→4%', label: 'Product Damage Rate' }, { num: '2×', label: 'Product Life Improvement' }] },
  'gasket-cs-2': { num: '02', title: 'Vibration Dampening Gaskets for Motor Mount Applications', industry: 'Automotive', challenge: 'An automotive component supplier needed precision foam gaskets to reduce vibration transmission between motor mounts and chassis panels. Vibration from motor operation was being transmitted through the chassis, causing noise and accelerating fatigue in structural components.', solution: 'XLPE foam gaskets were engineered for compression set resistance and long-term performance in the motor mount application. The gasket specification was developed through compression testing to match the dynamic loading conditions of motor operation.', result: 'Vibration transmission reduced by 65% compared to previous standard gaskets. Noise levels at chassis reduced measurably. Component fatigue life extended.', stats: [{ num: '65%', label: 'Vibration Reduction' }, { num: 'IP65', label: 'Protection Rating Achieved' }] },
  'gasket-cs-3': { num: '03', title: 'PU Foam Gaskets for HVAC Panel Thermal Insulation', industry: 'HVAC', challenge: 'An HVAC systems manufacturer required thermal break gaskets for panel assembly joints to prevent condensation and heat loss. Gaps between panel joints were allowing cold bridging, which caused condensation buildup inside equipment enclosures and increased energy losses across the system.', solution: 'Custom PU foam gaskets were developed to fill panel assembly joints with a consistent compressive thermal barrier. The gasket specification was selected for both thermal resistance and long-term compression set performance across the operating temperature range of the HVAC systems.', result: 'Thermal bridging at panel joints eliminated. Condensation incidents within enclosures reduced to zero. System energy efficiency improved across the installed product range.', stats: [{ num: '0', label: 'Condensation Incidents' }, { num: '100%', label: 'Joints Sealed to Spec' }] },
  'adhesive-cs-1': { num: '01', title: 'Foam + Film Laminate for Appliance Surface Protection', industry: 'White Goods', challenge: 'A home appliance manufacturer required scratch-resistant surface protection for pre-assembled panels during assembly line handling and transit. Surface defects from handling were appearing on visible appliance panels before reaching end customers, generating warranty claims and return logistics costs.', solution: 'Adhesive-laminated PE film on EPE foam delivered a peel-clean protective layer with zero adhesive residue. The laminate was supplied in roll form, cut to panel dimensions on the production floor, and applied immediately after assembly. The peel-clean film was removed by the end customer on unboxing.', result: 'Assembly line surface defects reduced by 80%. Warranty claims related to surface scratching eliminated. Customer unboxing experience improved significantly.', stats: [{ num: '80%', label: 'Reduction in Surface Defects' }, { num: '0', label: 'Adhesive Residue Claims' }] },
  'adhesive-cs-2': { num: '02', title: 'Multi-Layer Foam Composite for ESD-Safe Packaging Inserts', industry: 'Electronics', challenge: 'An electronics OEM required packaging inserts combining structural rigidity, ESD protection and surface cushioning in one component. Previously, three separate materials were being assembled on the packing floor, creating inconsistency and increasing packing time per unit.', solution: 'A three-layer adhesive lamination of ESD film, EPE foam and board provided all three performance requirements in a single pre-laminated component. Custom inserts were die-cut to product geometry, allowing packing staff to place one component rather than three.', result: 'Packaging cost lowered by 30%. Packing time per unit reduced significantly. ESD protection consistency improved across the product range.', stats: [{ num: '30%', label: 'Packaging Cost Reduction' }, { num: '3×', label: 'Faster Insert Placement' }] },
  'adhesive-cs-3': { num: '03', title: 'Fabric-Laminated Foam for Automotive Interior Component Protection', industry: 'Automotive', challenge: 'An automotive interior parts supplier needed protective wrapping for finished seat and trim components. Standard foam wrapping was leaving surface marks on premium fabric seat covers and soft-touch trim panels during logistics handling, creating quality rejections at the assembly plant.', solution: 'Fabric-laminated foam was developed with a soft, non-marking woven fabric surface bonded to EPE foam. The fabric surface provided gentle contact with finished trim surfaces while the foam layer absorbed any handling impacts. Custom cut sizes were supplied to match each component.', result: 'Zero surface marking claims from the dealer network. Component rejection at assembly plant eliminated. Supplier quality rating improved.', stats: [{ num: '0', label: 'Surface Marking Claims' }, { num: '100%', label: 'Components Accepted on Arrival' }] },
  'sundry-cs-1': { num: '01', title: 'Sun Dry Board Pallet Liners for Humid Warehouse Storage', industry: 'Warehousing', challenge: 'A logistics operator in a coastal warehouse environment required moisture-resistant pallet liners to protect goods from floor humidity. Cardboard pallet liners were absorbing moisture from the warehouse floor and transferring it to stored goods, causing product damage across the facility.', solution: 'Sun Dry Board provided consistent moisture separation with structural rigidity across high-stack pallet loads. Custom-cut board sizes were produced to match standard pallet dimensions. The moisture-resistant board maintained structural performance throughout extended storage periods in the high-humidity coastal environment.', result: 'Product moisture damage eliminated across coastal warehouse facilities. Pallet liner replacement frequency reduced significantly. Operational storage costs reduced.', stats: [{ num: '0', label: 'Moisture Damage Incidents' }, { num: '5×', label: 'Longer Liner Service Life' }] },
  'sundry-cs-2': { num: '02', title: 'Board Dividers for Multi-Product Export Container Packing', industry: 'Export', challenge: 'An export packing operation needed lightweight, rigid dividers for segregating mixed-product shipments in sea freight containers. Product contact damage was occurring during long ocean voyages, with movement between product types causing surface damage and contamination.', solution: 'Custom-cut Sun Dry Board dividers prevented product contact throughout transit. The lightweight board reduced the additional packaging weight contribution while the rigid structure maintained separation under stacking loads inside the container. Sizes were cut to match standard container internal dimensions.', result: 'Product contact damage during sea freight eliminated. Export rejection rate reduced to zero. Packing operation efficiency improved with pre-cut divider sizing.', stats: [{ num: '0', label: 'Product Contact Damage' }, { num: '100%', label: 'Shipments Arrived Intact' }] },
  'sundry-cs-3': { num: '03', title: 'Floor Protection Boards for Equipment Installation Projects', industry: 'Manufacturing', challenge: 'An industrial equipment installer required temporary floor protection boards for machinery installation in finished production facilities. Existing protection materials were inadequate for the point loads generated by heavy equipment positioning, causing floor damage in customers\' facilities.', solution: 'Sun Dry Board provided load distribution and floor protection without requiring removal between installation phases. The rigid board structure distributed point loads across a larger floor area, preventing indentation damage. Boards were supplied in standard sheet sizes that could be arranged and repositioned throughout the installation sequence.', result: 'Zero floor damage incidents recorded across 30+ installations. Customer satisfaction with facility protection significantly improved. Installer liability claims eliminated.', stats: [{ num: '0', label: 'Floor Damage Incidents' }, { num: '30+', label: 'Installations Protected' }] },
  'tapes-cs-1': { num: '01', title: 'High-Tack Sealing Tape for Export Carton Closure', industry: 'Packaging', challenge: 'An export packer required reliable high-tack carton sealing tape with consistent adhesion performance across temperature variations encountered during sea freight. Previous tape was failing at carton joints during transit, with boxes opening in transit and product exposure occurring on delivery.', solution: 'Custom tape specification was developed and validated across export conditions. The tape adhesion profile was matched to the corrugated board grade used by the packer. Batch testing was conducted to verify performance at the temperature extremes encountered during sea freight routes.', result: 'Zero carton seal failures reported across export shipments. Product exposure incidents eliminated. Customer delivery complaints related to carton integrity reduced to zero.', stats: [{ num: '0', label: 'Seal Failures in Transit' }, { num: '100%', label: 'Cartons Delivered Intact' }] },
  'tapes-cs-2': { num: '02', title: 'Masking Tapes for Automotive Paint Shop Operations', industry: 'Automotive', challenge: 'An automotive body shop required clean-release masking tapes for precision paint masking across complex contoured surfaces. Previous tapes were leaving adhesive residue on masked surfaces after removal, requiring rework that was adding significant time and cost to the paint process.', solution: 'Custom tape widths and liner specifications were developed for clean removal with zero adhesive residue. The tape adhesive formulation was selected for automotive paint shop temperature conditions and the specific paint chemistry in use at the facility.', result: 'Zero rework incidents from adhesive contamination. Paint shop throughput improved. Masking accuracy improved with correctly specified tape widths for contour masking.', stats: [{ num: '0', label: 'Adhesive Residue Incidents' }, { num: '25%', label: 'Rework Time Eliminated' }] },
  'tapes-cs-3': { num: '03', title: 'Double-Sided Foam Tape for PCB and Component Mounting', industry: 'Electronics', challenge: 'An electronics manufacturer required precision double-sided foam tape for mounting small PCBs onto housings during assembly. The mounting method needed to provide vibration damping, height compensation across tolerance variations, and reliable adhesion — without mechanical fasteners that added weight and assembly time.', solution: 'Custom tape thickness and adhesion profile eliminated the need for mechanical fasteners in low-profile assemblies. The foam layer provided compliance for height variation between mating surfaces while the double-sided adhesive provided reliable long-term bonding. Tape was supplied in die-cut pads matched to PCB mounting footprints.', result: 'Assembly time reduced by 35% versus mechanical fastening. PCB mounting consistency improved. Vibration-related field failures from loose mounting eliminated.', stats: [{ num: '35%', label: 'Assembly Time Reduction' }, { num: '0', label: 'Mounting Failure Claims' }] },
  'paperbag-cs-1': { num: '01', title: 'Kraft Paper Bags for Premium Retail Brand Rollout', industry: 'Retail', challenge: 'A premium lifestyle brand required kraft paper carry bags with reinforced handles and branded printing for retail store deployment across a national rollout. Previous bags were inconsistent in handle strength and print registration, undermining the premium brand presentation.', solution: 'Custom bags were produced with consistent material weight and print registration across high retail volumes. Reinforced twisted paper handles were specified for load performance. Print registration was controlled through a dedicated production run with quality inspection at key process stages.', result: 'Brand presentation consistency maintained across 200+ stores. Handle failure complaints eliminated. Customer feedback on unboxing and carry experience improved significantly.', stats: [{ num: '200+', label: 'Stores Supplied' }, { num: '0', label: 'Handle Failure Complaints' }] },
  'paperbag-cs-2': { num: '02', title: 'Laminated Paper Bags for Food-Grade Distribution', industry: 'FMCG', challenge: 'An FMCG distributor required food-grade laminated paper bags for dry goods distribution through retail and wholesale channels. Existing packaging was failing food-safety audit requirements, creating regulatory compliance exposure and risking distribution partner relationships.', solution: 'Food-safe laminated kraft bags provided moisture resistance with recyclable material compliance. The laminate specification was selected to meet food-contact material regulations. Bags were produced with consistent laminate adhesion and seal integrity across production volumes.', result: 'Regulatory compliance achieved across all distribution channels. Customer complaints related to packaging reduced to zero. Distribution partner audit outcomes improved significantly.', stats: [{ num: '100%', label: 'Compliance Rate' }, { num: '0', label: 'Customer Complaints' }] },
  'paperbag-cs-3': { num: '03', title: 'Heavy-Duty Paper Bags for Industrial Powder Products', industry: 'Industrial', challenge: 'An industrial chemicals company required multi-wall paper bags for packaging and distributing powder products at industrial scale. Single-wall bags were failing under the weight and abrasion of powder products during automated filling and palletised distribution, causing product leakage and contamination incidents.', solution: 'Multi-wall kraft construction provided the structural performance needed for automated filling and palletised distribution. The bag structure was engineered for the fill weight and the abrasion conditions of the filling line. Valve closure design enabled clean filling without dust emission.', result: 'Zero bag integrity failures across production volumes. Product leakage incidents eliminated. Palletised distribution performance improved significantly.', stats: [{ num: '0', label: 'Bag Failures in Production' }, { num: '100%', label: 'Fill Weight Integrity' }] },
  'flc-cs-1': { num: '01', title: 'FLC Pallets for Cross-Plant Automotive Component Logistics', industry: 'Automotive', challenge: 'A Tier-1 automotive supplier was incurring high return freight costs for empty packaging moving between manufacturing plants. Standard rigid containers occupied full truck volume on return journeys, making return logistics costs nearly equal to outbound costs.', solution: 'FLC pallets were implemented for heavy component transfers across manufacturing plants. Foldable design reduced return freight volume by 75%, while heavy-duty construction maintained performance across multiple use cycles. A standardised fleet of FLC pallets replaced the mixed rigid container inventory.', result: 'Return freight cost reduced by 75%. Packaging capital cost recovered within 14 months. Empty container storage space at both plants reduced significantly.', stats: [{ num: '75%', label: 'Return Freight Cost Reduction' }, { num: '14mo', label: 'Capital Recovery Period' }] },
  'flc-cs-2': { num: '02', title: 'FLC Containers for Heavy Machinery Component Export', industry: 'Engineering', challenge: 'An engineering equipment exporter required robust, space-efficient containers for exporting heavy machined components by sea. The cost of returning empty rigid containers from export destinations was making certain routes economically unviable.', solution: 'FLC pallets loaded flat for the return journey, eliminating the cost of sending empty rigid containers back to origin. The FLC construction was specified for the load weights of the machined components and the handling conditions of sea freight and port operations.', result: 'Empty return shipping cost eliminated. Export route economics improved significantly. Several previously unviable export routes became commercially attractive.', stats: [{ num: '0', label: 'Empty Return Freight Cost' }, { num: '3×', label: 'More Export Routes Viable' }] },
  'flc-cs-3': { num: '03', title: 'FLC Pallet System for Automotive Assembly Kanban Logistics', industry: 'Warehousing', challenge: 'An automotive assembly plant was experiencing line-side congestion from empty pallet accumulation across their internal kanban logistics system. Empty pallets were occupying valuable line-side space between collection cycles, disrupting assembly operations.', solution: 'FLC pallets were introduced across the internal kanban logistics system for small batch component supply to line. The foldable system allowed empty pallets to be collapsed and stacked at line side, dramatically reducing the footprint of empty packaging between collection rounds.', result: 'Storage space for empty pallets reduced by 70%. Line-side congestion incidents eliminated. Kanban system efficiency improved with more predictable empty pallet management.', stats: [{ num: '70%', label: 'Empty Pallet Storage Reduction' }, { num: '0', label: 'Line Congestion Incidents' }] }
};

/* ===== BLOG NAVIGATION (homepage preview pagination — unused outside index.html) ===== */
let blogPage = 0;
const BLOGS_PER_PAGE = 3;

function renderBlogs() {
  const container = document.getElementById('blogs-container');
  const prevBtn = document.getElementById('blogs-prev');
  const nextBtn = document.getElementById('blogs-next');
  if (!container) return;
  const totalPages = Math.ceil(BLOGS.length / BLOGS_PER_PAGE);
  const start = blogPage * BLOGS_PER_PAGE;
  const paginated = BLOGS.slice(start, start + BLOGS_PER_PAGE);
  container.innerHTML = paginated.map((b, i) => `
    <article class="blog-card" onclick="window.location.href='blogs/${b.slug}/'" tabindex="0" onkeydown="if(event.key==='Enter')window.location.href='blogs/${b.slug}/'">
      <div class="blog-card-img">
        <img src="${b.img}" alt="${b.title}" style="width:100%;height:100%;object-fit:cover;display:block;"/>
        <div class="blog-card-overlay"></div>
      </div>
      <div class="blog-card-body">
        <div class="blog-card-date">${b.category} &nbsp;·&nbsp; ${b.readTime}</div>
        <h3 class="blog-card-title">${b.title}</h3>
        <p class="blog-card-desc">${b.desc}</p>
        <a class="blog-read-more" href="blogs/${b.slug}/">Read More <span class="blog-arrow">&#8594;</span></a>
      </div>
    </article>
  `).join('');
  prevBtn.disabled = blogPage === 0;
  nextBtn.disabled = blogPage >= totalPages - 1;
}

function blogNav(dir) {
  blogPage = Math.max(0, Math.min(Math.ceil(BLOGS.length / BLOGS_PER_PAGE) - 1, blogPage + dir));
  renderBlogs();
}
function blogGoTo(page) { blogPage = page; renderBlogs(); }

// ===== BLOG DETAIL (homepage preview cards) =====
function openBlogDetail(idx) {
  const b = BLOGS[idx];
  document.getElementById('blog-detail-category').textContent = b.category;
  document.getElementById('blog-detail-title').textContent = b.title;
  document.getElementById('blog-detail-date').textContent = b.date;
  document.getElementById('blog-detail-readtime').textContent = b.readTime;
  document.getElementById('blog-detail-img').src = b.img;
  document.getElementById('blog-detail-img').alt = b.title;
  document.getElementById('blog-detail-content').innerHTML = b.content;
  const el = document.getElementById('inner-blog-detail');
  el.style.display = 'block';
  requestAnimationFrame(() => el.style.opacity = '1');
  document.body.style.overflow = 'hidden';
  el.scrollTop = 0;
}
function closeBlogDetail() {
  const el = document.getElementById('inner-blog-detail');
  el.style.opacity = '0';
  setTimeout(() => { el.style.display = 'none'; document.body.style.overflow = ''; }, 300);
}

// ===== CASE STUDY DETAIL =====
function openCaseStudy(id) {
  const cs = CASE_STUDIES[id];
  if (!cs) return;
  document.getElementById('cs-label').textContent = 'Case Study ' + cs.num;
  document.getElementById('cs-title').textContent = cs.title;
  document.getElementById('cs-industry').textContent = cs.industry;
  document.getElementById('cs-challenge').textContent = cs.challenge;
  document.getElementById('cs-solution').textContent = cs.solution;
  document.getElementById('cs-result').textContent = cs.result;
  const sw = document.getElementById('cs-stats-wrap');
  sw.innerHTML = cs.stats ? cs.stats.map(s => `<div class="cs-stat"><div class="cs-stat-num">${s.num}</div><div class="cs-stat-label">${s.label}</div></div>`).join('') : '';
  sw.style.display = cs.stats && cs.stats.length ? 'grid' : 'none';
  const el = document.getElementById('inner-case-study');
  el.style.display = 'block';
  requestAnimationFrame(() => el.style.opacity = '1');
  document.body.style.overflow = 'hidden';
  el.scrollTop = 0;
}
function closeCaseStudy() {
  const el = document.getElementById('inner-case-study');
  el.style.opacity = '0';
  setTimeout(() => { el.style.display = 'none'; document.body.style.overflow = ''; }, 300);
}

// Render only 3 blogs on homepage (first 3)
function renderHomepageBlogs() {
  const container = document.getElementById('blogs-container');
  if (!container) return;
  const homepageBlogs = BLOGS.slice(0, 3);
  container.innerHTML = homepageBlogs.map((b, i) => `
    <article class="blog-card">
      <a href="blogs/${b.slug}/" class="blog-card-img-link">
        <picture class="blog-card-img">
          <img src="${b.img}" alt="${b.title}" style="width:100%;height:100%;object-fit:cover;display:block;" loading="lazy"/>
          <div class="blog-card-overlay"></div>
        </picture>
      </a>
      <div class="blog-card-body">
        <div class="blog-card-date">${b.category} &nbsp;·&nbsp; ${b.readTime}</div>
        <h3 class="blog-card-title">${b.title}</h3>
        <a class="blog-read-more" href="blogs/${b.slug}/">Read Article <span class="blog-arrow">→</span></a>
      </div>
    </article>
  `).join('');
}

// Render all blogs (blogs.html)
function renderAllBlogs() {
  const container = document.getElementById('blogs-all-container');
  if (!container) return;
  container.innerHTML = BLOGS.map((b, i) => `
    <article class="ba-card" onclick="window.location.href='./${b.slug}/'" tabindex="0" onkeydown="if(event.key==='Enter')window.location.href='./${b.slug}/'">
      <div class="ba-card-img">
        <img src="${b.img}" alt="${b.title}" loading="lazy"/>
      </div>
      <div class="ba-card-body">
        <div class="ba-card-date">${b.category} &nbsp;&middot;&nbsp; ${b.readTime}</div>
        <h3 class="ba-card-title">${b.title}</h3>
        <p class="ba-card-desc">${b.desc}</p>
        <span class="ba-card-rm">Read Article <span>&#8594;</span></span>
      </div>
    </article>
  `).join('');
}

// Blog overlay for blogs.html
function openBlogOverlay(idx) {
  const b = BLOGS[idx];
  document.getElementById('bov-category').textContent = b.category;
  document.getElementById('bov-title').textContent = b.title;
  document.getElementById('bov-date').textContent = b.date;
  document.getElementById('bov-readtime').textContent = b.readTime;
  const img = document.getElementById('bov-img');
  img.src = b.img; img.alt = b.title;
  document.getElementById('bov-content').innerHTML = b.content;
  const overlay = document.getElementById('blog-detail-overlay');
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
  overlay.querySelector('.blog-overlay-box').scrollTop = 0;
}

function closeBlogOverlay() {
  document.getElementById('blog-detail-overlay').classList.remove('open');
  document.body.style.overflow = '';
}

// Close blog overlay on background click
document.addEventListener('DOMContentLoaded', function () {
  const overlay = document.getElementById('blog-detail-overlay');
  if (overlay) {
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeBlogOverlay();
    });
  }
});

/* TECHNICAL GRID CANVAS — scattered coordinate labels + dots overlay (all pages) */
(function () {
  const canvas = document.createElement('canvas');
  canvas.style.cssText = 'position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:0;';
  document.body.appendChild(canvas);

  const ctx = canvas.getContext('2d');
  const labels = [
    { x: 0.07, y: 0.28, t: 'B.02' }, { x: 0.37, y: 0.08, t: 'A.01' }, { x: 0.78, y: 0.05, t: 'C.03' },
    { x: 0.55, y: 0.31, t: '2' }, { x: 0.73, y: 0.80, t: 'B.02' }, { x: 0.20, y: 0.72, t: '—' },
    { x: 0.62, y: 0.55, t: 'C.03' },
  ];
  // Reduced to 4 dots — very faint
  const dots = [
    { x: 0.26, y: 0.24, r: 2.5, type: 'fill' },
    { x: 0.57, y: 0.32, r: 2.5, type: 'fill' },
    { x: 0.82, y: 0.26, r: 2.5, type: 'ring' },
    { x: 0.46, y: 0.50, r: 2.5, type: 'fill' },
  ];

  function draw() {
    canvas.width = window.innerWidth;
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
      [0.04, 0.18], [0.14, 0.30], [0.48, 0.15], [0.70, 0.13], [0.93, 0.11],
      [0.89, 0.35], [0.92, 0.55], [0.88, 0.74], [0.04, 0.50], [0.04, 0.74],
      [0.24, 0.90], [0.56, 0.88], [0.78, 0.91],
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
      [0.05, 0.10], [0.20, 0.38], [0.76, 0.38], [0.90, 0.50], [0.60, 0.75], [0.38, 0.60],
    ];
    ctx.strokeStyle = 'rgba(10,61,44,0.07)';
    squares.forEach(([sx, sy]) => {
      const cx = sx * canvas.width, cy = sy * canvas.height, s = 4;
      ctx.strokeRect(cx - s / 2, cy - s / 2, s, s);
    });

    // dotted measurement lines (horizontal)
    ctx.setLineDash([4, 6]);
    ctx.strokeStyle = 'rgba(10,61,44,0.07)';
    ctx.lineWidth = 0.6;
    [[0.18, 0.14, 0.36, 0.14], [0.26, 0.50, 0.44, 0.50]].forEach(([x1, y1, x2, y2]) => {
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

/* ===== PAGE INIT ===== */
document.addEventListener('DOMContentLoaded', function () {
  renderHomepageBlogs();
  addFpHamburgers();
});

/* ===== "WHY CHOOSE US" CARD CAROUSEL (About page) ===== */
document.addEventListener('DOMContentLoaded', function () {
  const track = document.getElementById('whyCarouselTrack');
  if (!track) return;
  
  const dotsContainer = document.getElementById('whyCarouselDots');
  
  // Update active dot on scroll
  track.addEventListener('scroll', function () {
    const width = track.getBoundingClientRect().width;
    if (width <= 0) return;
    const index = Math.round(track.scrollLeft / width);
    updateActiveDot(index);
  });
  
  function updateActiveDot(index) {
    if (!dotsContainer) return;
    const dots = dotsContainer.querySelectorAll('.why-dot');
    dots.forEach((dot, idx) => {
      if (idx === index) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }
});

function whyCarouselGoTo(index) {
  const track = document.getElementById('whyCarouselTrack');
  if (!track) return;
  const width = track.getBoundingClientRect().width;
  track.scrollTo({ left: index * width, behavior: 'smooth' });
}

function whyCarouselNav(dir) {
  const track = document.getElementById('whyCarouselTrack');
  if (!track) return;
  const width = track.getBoundingClientRect().width;
  if (width <= 0) return;
  const cards = track.querySelectorAll('.why-card');
  const totalCards = cards.length;
  if (totalCards <= 0) return;
  
  let currentIndex = Math.round(track.scrollLeft / width);
  let nextIndex = currentIndex + dir;
  
  if (nextIndex < 0) {
    nextIndex = totalCards - 1;
  } else if (nextIndex >= totalCards) {
    nextIndex = 0;
  }
  
  whyCarouselGoTo(nextIndex);
}

/* ===== SOLUTIONS ACCORDION ===== */
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.sol-item').forEach(function (item) {
    item.querySelector('.sol-item-head').addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.sol-item.open').forEach(function (o) {
        o.classList.remove('open');
      });
      if (!isOpen) item.classList.add('open');
    });
  });
});

/* ===== FOOTER LOGO — PNG SEQUENCE ANIMATION ===== */
(function () {
  var FRAME_COUNT = 126;        // ANIMATION 4000 → ANIMATION 4125
  var FPS = 24;
  var BASE = 4000;              // starting frame number
  // Resolve prefix relative to the location of shared.js
  var prefix = '';
  var scriptTag = document.querySelector('script[src*="shared.js"]');
  if (scriptTag) {
    var src = scriptTag.getAttribute('src');
    var idx = src.indexOf('shared.js');
    if (idx !== -1) {
      prefix = src.substring(0, idx);
    }
  }
  var FRAME_DIR = prefix + 'images/PNG Sequence Final/';

  document.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById('footer-logo-canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');

    var frames = [];
    var loaded = 0;
    var started = false;

    for (var i = 0; i < FRAME_COUNT; i++) {
      var img = new Image();
      img.src = FRAME_DIR + 'ANIMATION ' + (BASE + i) + '.png';
      (function (idx, image) {
        image.onload = function () {
          loaded++;
          if (loaded === FRAME_COUNT && !started) {
            started = true;
            startAnim();
          }
        };
        image.onerror = function () {
          loaded++;
          if (loaded === FRAME_COUNT && !started) {
            started = true;
            startAnim();
          }
        };
        frames[idx] = image;
      })(i, img);
    }

    function startAnim() {
      var current = 0;
      var interval = 1000 / FPS;
      var last = 0;

      function draw(ts) {
        if (ts - last >= interval) {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          if (frames[current] && frames[current].complete && frames[current].naturalWidth) {
            ctx.drawImage(frames[current], 0, 0, canvas.width, canvas.height);
          }
          current = (current + 1) % FRAME_COUNT;
          last = ts;
        }
        requestAnimationFrame(draw);
      }
      requestAnimationFrame(draw);
    }
  });
})();

/* ===== CONTACT FORM SUCCESS POPUP ===== */
(function() {
  function showSuccessModal() {
    let modal = document.getElementById('enquiry-success-modal');
    if (!modal) {
      var prefix = '';
      var scriptTag = document.querySelector('script[src*="shared.js"]');
      if (scriptTag) {
        var src = scriptTag.getAttribute('src');
        var idx = src.indexOf('shared.js');
        if (idx !== -1) {
          prefix = src.substring(0, idx);
        }
      }
      var productsPath = prefix + 'products/';

      const modalHtml = `
<div id="enquiry-success-modal" style="position: fixed; inset: 0; background: rgba(10, 61, 44, 0.6); backdrop-filter: blur(8px); display: flex; align-items: center; justify-content: center; z-index: 10000; opacity: 0; pointer-events: none; transition: opacity 0.3s ease-in-out; font-family: 'Poppins', sans-serif;">
  <style>
    @media (max-width: 480px) {
      .modal-buttons {
        flex-direction: column !important;
        gap: 12px !important;
      }
      .modal-buttons a, .modal-buttons button {
        width: 100% !important;
        margin: 0 !important;
      }
    }
  </style>
  <div class="modal-card" style="background: var(--white, #FFFFFF); border: 1px solid var(--border, rgba(0,0,0,0.08)); border-radius: 16px; padding: 40px; max-width: 520px; width: 90%; text-align: center; box-shadow: 0 24px 48px rgba(10, 61, 44, 0.18); transform: translateY(20px) scale(0.95); transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease-in-out;">
    <div style="width: 72px; height: 72px; background: rgba(34, 197, 94, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; border: 2px solid #22c55e;">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="20 6 9 17 4 12"></polyline>
      </svg>
    </div>
    <h3 style="font-size: 22px; font-weight: 700; color: var(--g1, #0A3D2C); margin-bottom: 16px; font-family: 'Sora', sans-serif; line-height: 1.3;">Thank You for Choosing Rajvi Packaging!</h3>
    <p style="font-size: 15px; line-height: 1.6; color: var(--muted, #3A3A3A); margin-bottom: 12px; font-family: 'Poppins', sans-serif; font-weight: 500;">
      Your enquiry has been received successfully.
    </p>
    <p style="font-size: 14px; line-height: 1.6; color: var(--muted, #3A3A3A); margin-bottom: 32px; font-family: 'Poppins', sans-serif;">
      Our team will contact you shortly to understand your needs and help you find the right packaging solution for your business.
    </p>
    <div class="modal-buttons" style="display: flex; gap: 16px; justify-content: center; align-items: center;">
      <a href="${productsPath}" style="display: inline-flex; align-items: center; justify-content: center; flex: 1; font-size: 14px; font-weight: 600; padding: 14px 20px; border-radius: 8px; cursor: pointer; text-decoration: none; background: var(--g1, #0A3D2C); color: var(--white, #FFFFFF); transition: background 0.2s, transform 0.1s; font-family: 'Poppins', sans-serif; box-shadow: 0 4px 12px rgba(10, 61, 44, 0.15); border: none; box-sizing: border-box;">
        Explore Products
      </a>
      <button id="enquiry-success-close" style="display: inline-flex; align-items: center; justify-content: center; flex: 1; font-size: 14px; font-weight: 600; padding: 14px 20px; border-radius: 8px; cursor: pointer; border: 1.5px solid var(--g1, #0A3D2C); background: transparent; color: var(--g1, #0A3D2C); transition: all 0.2s; font-family: 'Poppins', sans-serif; box-sizing: border-box;">
        Submit Another
      </button>
    </div>
  </div>
</div>`;
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = modalHtml.trim();
      modal = tempDiv.firstChild;
      document.body.appendChild(modal);

      // Event listener to close
      modal.querySelector('#enquiry-success-close').addEventListener('click', hideSuccessModal);
      
      // Submit another button style tweaks
      const submitAnother = modal.querySelector('#enquiry-success-close');
      submitAnother.addEventListener('mouseenter', function() {
        this.style.background = 'rgba(10, 61, 44, 0.05)';
      });
      submitAnother.addEventListener('mouseleave', function() {
        this.style.background = 'transparent';
      });

      // Explore products button style tweaks
      const exploreBtn = modal.querySelector('.modal-buttons a');
      exploreBtn.addEventListener('mouseenter', function() {
        this.style.background = 'var(--g2, #0F5240)';
      });
      exploreBtn.addEventListener('mouseleave', function() {
        this.style.background = 'var(--g1, #0A3D2C)';
      });

      // Click outside to close
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          hideSuccessModal();
        }
      });
    }

    // Show
    document.body.style.overflow = 'hidden'; // prevent scroll behind modal
    modal.style.pointerEvents = 'auto';
    modal.style.opacity = '1';
    setTimeout(() => {
      modal.querySelector('.modal-card').style.transform = 'translateY(0) scale(1)';
    }, 10);
  }

  function hideSuccessModal() {
    const modal = document.getElementById('enquiry-success-modal');
    if (modal) {
      modal.style.opacity = '0';
      modal.style.pointerEvents = 'none';
      modal.querySelector('.modal-card').style.transform = 'translateY(20px) scale(0.95)';
      document.body.style.overflow = ''; // restore scroll
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-page-form');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        showSuccessModal();
        form.reset();
      });
    }
  });
})();