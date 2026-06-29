import os
import re

# Task 2: Replace footer in all pages/*.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract footer from index.html
footer_match = re.search(r'(<footer class="site-footer">.*?</footer\s*>)', index_content, re.DOTALL | re.IGNORECASE)
if footer_match:
    index_footer = footer_match.group(1)
    
    # Adjust paths for inner pages
    inner_footer = index_footer.replace('src="images/', 'src="../images/')
    inner_footer = inner_footer.replace('href="pages/', 'href="')
    inner_footer = inner_footer.replace('href="contact.html"', 'href="contact.html"') 
    # wait, in index.html footer contact link is 'pages/contact.html', it becomes 'contact.html' which is correct.
    # What about index.html? If they click on logo, index footer doesn't have link to index.html on logo?
    # In index.html, footer logo doesn't have an 'a' tag around it, let's check:
    # <div class="footer-v2-brand"><img src="images/logow.png" ... 
    
    pages_dir = 'pages'
    for filename in os.listdir(pages_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(pages_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                page_content = f.read()
            
            # Replace existing footer. 
            # In blogs.html we saw: <footer>...</footer>
            new_page_content = re.sub(r'<footer[^>]*>.*?</footer\s*>', inner_footer, page_content, flags=re.DOTALL | re.IGNORECASE)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_page_content)
    print("Footers updated.")
else:
    print("Could not find footer in index.html")

# Task 1: Fix mobile responsiveness in shared.css
css_append = '''
/* ===========================================================================
   MOBILE RESPONSIVENESS FIXES
   =========================================================================== */
@media (max-width: 1024px) {
  .products-grid-4col {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  .standards-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  .blogs-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  .hero-h1 {
    font-size: 3rem !important;
  }
  .hero-sub {
    font-size: 1rem !important;
  }
}

@media (max-width: 768px) {
  /* Navbar */
  .fp-header-nav {
    display: none !important;
  }
  .hamburger {
    display: flex !important;
  }

  /* Hero */
  .hero-h1 {
    font-size: 2.2rem !important;
  }
  .hero-btns {
    flex-direction: column !important;
    align-items: stretch !important;
  }
  .hero-left {
    padding: 20px !important;
  }

  /* About */
  .about-inner {
    flex-direction: column !important;
  }
  .about-left, .about-video-wrap {
    width: 100% !important;
    padding-right: 0 !important;
  }
  .about-video-wrap {
    margin-top: 2rem !important;
  }
  
  /* Products */
  .products-grid-4col {
    grid-template-columns: 1fr !important;
  }

  /* Solutions */
  .sol-list {
    flex-direction: column !important;
  }
  .sol-item {
    width: 100% !important;
    margin-bottom: 1rem !important;
  }
  .sol-item-head {
    padding: 15px !important;
  }

  /* Standards */
  .standards-grid {
    grid-template-columns: 1fr !important;
  }

  /* Blogs */
  .blogs-grid {
    grid-template-columns: 1fr !important;
  }

  /* Contact */
  .contact-info-only {
    flex-direction: column !important;
  }
  .contact-info-only > div {
    width: 100% !important;
    margin-bottom: 2rem !important;
  }

  /* Footer */
  .footer-v2-top {
    flex-direction: column !important;
  }
  .footer-v2-col {
    margin-bottom: 2rem !important;
  }
  .footer-v2-contact-bar {
    flex-direction: column !important;
  }
  .footer-v2-contact-cell {
    border: none !important;
    border-bottom: 1px solid rgba(255,255,255,0.1) !important;
    padding: 15px 0 !important;
  }
  .footer-v2-contact-cell--border {
    border-left: none !important;
  }
  .footer-v2-bottom {
    flex-direction: column !important;
    text-align: center !important;
    gap: 15px !important;
  }
}

@media (max-width: 480px) {
  .hero-h1 {
    font-size: 1.8rem !important;
  }
  .hero-tag-line {
    font-size: 0.9rem !important;
  }
  .sect-label {
    font-size: 0.8rem !important;
  }
  .about-heading, .products-heading, .solutions-heading, .standards-heading, .blogs-heading, .contact-heading {
    font-size: 1.8rem !important;
  }
}
'''

with open('shared.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("CSS appended.")
