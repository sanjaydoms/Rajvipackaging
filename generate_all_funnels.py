import os

# Define B2B data for all 12 industries
industries = {
    "electronics": {
        "title": "Electronics Packaging Solutions | Rajvi Packaging",
        "description": "High-performance ESD and protective packaging solutions for PCBs, devices, telecom, and consumer electronics.",
        "badge": "Electronics",
        "hero_title": "Packaging Solutions for the <span>Electronics Industry</span>",
        "hero_sub": "Rajvi Packaging helps electronics manufacturers protect high-value components, eliminate electrostatic damage (ESD), and optimize transit safety with custom-engineered foam and shielding solutions.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-foam/",
        "hero_product_text": "See Foam Products",
        "overview": "Electronics manufacturers require high-performance protective packaging to prevent static damage, impact, moisture, and scratches during transportation and storage. Even minor electrostatic discharge (ESD) or physical vibration can ruin sensitive circuits, making specialized protective materials a critical business necessity.",
        "challenges": [
            {"icon": "⚡", "title": "Static Electricity", "desc": "Electrostatic discharge (ESD) can destroy internal circuits silently without visible physical damage."},
            {"icon": "🛡️", "title": "Fragile Components", "desc": "Precision microchips, glass displays, and connectors cannot withstand transit drops and vibrations."},
            {"icon": "📦", "title": "Transit Damage", "desc": "Multi-handling courier networks introduce physical shocks that crack outer enclosures and bend connectors."},
            {"icon": "💧", "title": "Moisture Exposure", "desc": "Humidity and condensation trigger oxidation and corrosion on metal terminals and PCB contact pads."},
            {"icon": "🌍", "title": "Export Compliance", "desc": "International electronics shipments must meet rigid international container and environmental standards."},
            {"icon": "📐", "title": "Product Scratches", "desc": "Friction between standard packaging and glossy or polished screens degrades outer product aesthetics."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Bubble Wrap"},
            {"challenge": "Cushioning", "product": "EPE Foam"},
            {"challenge": "Shock Absorption", "product": "Foam Inserts"},
            {"challenge": "Component Protection", "product": "Foam Gaskets"},
            {"challenge": "Secure Packaging", "product": "Specialty Tapes"},
            {"challenge": "Heavy Product Support", "product": "PP Boxes & Sheets"}
        ],
        "solutions_cards": [
            {"title": "Anti-Static Bubble Wrap", "desc": "Dissipates static charges safely while providing lightweight cushioning.", "benefits": "ESD Safe, Lightweight, Cost-Effective", "link": "../../product-bubble/"},
            {"title": "Precision Foam Inserts", "desc": "Custom CNC-routed polyurethane and polyethylene foam shapes for snug device placement.", "benefits": "Zero-movement fit, High G-force absorption, Lint-free", "link": "../../product-foam/"},
            {"title": "EPE Foam Pouches & Liners", "desc": "Soft closed-cell polyethylene sleeves designed for fast packing lines.", "benefits": "Scratch-resistant, Flexible, High density", "link": "../../product-epe/"}
        ],
        "applications": [
            {"icon": "⚡", "title": "PCB Boards"},
            {"icon": "💡", "title": "LED Lights"},
            {"icon": "📱", "title": "Mobile Accessories"},
            {"icon": "🖥️", "title": "Consumer Electronics"},
            {"icon": "🔌", "title": "Power Supplies"},
            {"icon": "🏥", "title": "Medical Electronics"},
            {"icon": "⚙️", "title": "Industrial Electronics"}
        ],
        "segments": ["Consumer Electronics", "Industrial Electronics", "Semiconductor", "LED Manufacturing", "Telecom Equipment", "Electrical Components"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "0%", "label": "ESD Defect Rate"},
            {"num": "99.8%", "label": "On-Time Delivery"},
            {"num": "Custom", "label": "CAD Prototyping"}
        ],
        "faqs": [
            {"q": "Which packaging material is best for electronics?", "a": "For electronics, anti-static (ESD) EPE foam and pink bubble wrap are best. They prevent static charge buildup while absorbing transport shocks."},
            {"q": "Can Rajvi manufacture custom foam inserts?", "a": "Yes, we custom-design and cut foam inserts to your exact component dimensions using CNC routing and precision die-cutting."},
            {"q": "What is the minimum order quantity?", "a": "Minimum order quantities vary by product type. Contact our sales team to discuss custom production runs for your volume requirements."},
            {"q": "Do you support export packaging?", "a": "Yes, our packaging meets international standards for ocean and air export, ensuring moisture protection and robust physical containment."},
            {"q": "Can you manufacture according to our drawings?", "a": "Absolutely. We work directly with your CAD, STEP, or DXF drawing files to ensure sub-millimeter precision in custom foam cutouts."}
        ],
        "resources": [
            {"title": "Electronics ESD Packaging Guide", "desc": "Learn how to select the right ESD foam density and resistance range for delicate boards.", "link": "#"},
            {"title": "DOA reduction Case Study", "desc": "How a medical diagnostics brand reduced transit defects to absolute zero using custom EPE foam.", "link": "#"}
        ],
        "inquiry_category": "Foam & Buffers",
        "form_industry": "Electronics",
        "form_label": "Request Custom Samples",
        "form_title": "Tell Us About Your Electronics Packaging Needs",
        "form_desc": "Send us your device specifications and our foam engineers will recommend the correct EPE thickness and layout. Prototyping samples provided quickly.",
        "form_trust": [
            "Free ESD packaging consultation",
            "CNC prototype samples available",
            "Experience with OEM electronics brands",
            "Anti-static material testing reports",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#1e293b",
            "accent": "#0ea5e9",
            "dark": "#0f172a",
            "light": "#f8fafc",
            "accent_rgb": "14,165,233"
        },
        "stats": [
            {"num": "0%", "label": "Transit Damage"},
            {"num": "ESD", "label": "Protected"},
            {"num": "Custom", "label": "Per Device"}
        ]
    },
    "automotive": {
        "title": "Automotive Packaging Solutions | Rajvi Packaging",
        "description": "Engineered returnable PP corrugated boxes, crates, and partition systems for automotive component logistics.",
        "badge": "Automotive",
        "hero_title": "Packaging Solutions for the <span>Automotive Industry</span>",
        "hero_sub": "Rajvi Packaging manufactures heavy-duty returnable PP corrugated boxes, custom partitions, and dunnage to safeguard high-value metal and painted components in closed-loop logistics.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-pp/",
        "hero_product_text": "See PP Products",
        "overview": "Automotive component logistics demand robust, moisture-resistant, and returnable packaging. Parts must move through supply chains without paint abrasion, metal corrosion, or structural collapsing. Reusable plastics optimize freight efficiency and slash packaging cost-per-trip.",
        "challenges": [
            {"icon": "📦", "title": "Transit Damage", "desc": "Heavy metal castings and delicate lights rattle during transport, causing cracks and deformities."},
            {"icon": "🌧️", "title": "Moisture & Rust", "desc": "Condensation and sea air rust bare steel parts and precision engine sub-assemblies."},
            {"icon": "📐", "title": "Paint Abrasion", "desc": "Vibration scratches high-gloss painted body panels and polished interior dashboard trims."},
            {"icon": "🏭", "title": "Line Feeding Efficiency", "desc": "Inefficient or slow unpacking cycles bottle-neck automotive assembly lines and operator flows."},
            {"icon": "🔄", "title": "High Single-Use Waste", "desc": "Cardboard boxes generate massive recycling waste, disposal fees, and ongoing purchasing costs."},
            {"icon": "⚙️", "title": "Varying Part Geometries", "desc": "Unique shapes of gears, headlights, and wiring assemblies require custom nested partition grids."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "EVA Laminated Dividers"},
            {"challenge": "Cushioning", "product": "EPE Foam Dunnage"},
            {"challenge": "Shock Absorption", "product": "Brushed Felt Sleeves"},
            {"challenge": "Component Protection", "product": "PP Partitions"},
            {"challenge": "Secure Packaging", "product": "High-Strength Straps"},
            {"challenge": "Heavy Product Support", "product": "PP Boxes & Crates"}
        ],
        "solutions_cards": [
            {"title": "PP Corrugated Boxes & Crates", "desc": "Extremely durable returnable boxes with corner reinforcements, stackable up to 4-high loaded.", "benefits": "Waterproof, stackable, long lifecycle", "link": "../../product-pp/"},
            {"title": "Custom Fabric Dividers", "desc": "Durable PP partitions laminated with soft felt or EVA foam to prevent metal surface friction.", "benefits": "No-scratch containment, CAD-designed slots", "link": "../../product-pp/"},
            {"title": "EPE Dunnage Inserts", "desc": "Custom shock-absorbent EPE foam block fitments to hold heavy auto components.", "benefits": "High weight capacity, drop-proof, stable", "link": "../../product-foam/"}
        ],
        "applications": [
            {"icon": "🚗", "title": "Body Panels"},
            {"icon": "⚙️", "title": "Engine Components"},
            {"icon": "💡", "title": "Headlights & Mirrors"},
            {"icon": "🔌", "title": "Wiring Harnesses"},
            {"icon": "🛠️", "title": "Gearboxes & Axles"},
            {"icon": "🎨", "title": "Painted Trims"},
            {"icon": "📐", "title": "Brake Assemblies"}
        ],
        "segments": ["Passenger Vehicles", "Two & Three Wheelers", "Commercial Vehicles", "Tier-1 Component Suppliers", "Heavy Machinery", "Aftermarket Spares"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "50+", "label": "Reuse Cycles per Box"},
            {"num": "Zero", "label": "Part Rejections"},
            {"num": "Pan-India", "label": "Supplier Support"}
        ],
        "faqs": [
            {"q": "Can you design custom partitions for complex metal components?", "a": "Yes, our engineers create custom PP partitions with felt or EVA foam lining configured to your parts' exact geometry to prevent metal-on-metal friction."},
            {"q": "What is the average lifespan of your returnable boxes?", "a": "Under normal operating conditions, our PP corrugated crates survive between 50 to 80 round trips in closed-loop logistics loops."},
            {"q": "Do you sign NDAs before receiving custom part drawings?", "a": "Yes. We sign strict Non-Disclosure Agreements with automotive OEMs and suppliers before receiving drawing files or CAD models."},
            {"q": "Do you support standard pallet footprint boxes?", "a": "Yes, our crates are designed to match standard European and Indian pallet dimensions to optimize container space."},
            {"q": "Can you print custom labeling or branding?", "a": "Yes, we support screen-printing for logos, handling guidelines, part names, and slot placements."}
        ],
        "resources": [
            {"title": "Returnable Packaging ROI Guide", "desc": "Learn how to calculate payback periods when switching from cardboard to PP returnable crates.", "link": "#"},
            {"title": "Automotive Dunnage Design Sheet", "desc": "Technical overview of felt, foam, and PP partitions for component logistics.", "link": "#"}
        ],
        "inquiry_category": "PP Boxes & Crates",
        "form_industry": "Automotive",
        "form_label": "Request Custom Prototype",
        "form_title": "Tell Us About Your Automotive Packaging Need",
        "form_desc": "Our packaging engineers will design a solution specific to your components, volumes, and logistics setup. Response within 24 hours.",
        "form_trust": [
            "Free packaging consultation & design",
            "Custom prototypes available",
            "OEM supplier network experience",
            "Pan-India delivery & support",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#1a3a6b",
            "accent": "#e8a020",
            "dark": "#0d1f3c",
            "light": "#f0f5ff",
            "accent_rgb": "232,160,32"
        },
        "stats": [
            {"num": "90%", "label": "Waste Reduction"},
            {"num": "50+", "label": "Reuse Cycles"},
            {"num": "8mo", "label": "ROI Achieved"}
        ]
    },
    "pharmaceutical": {
        "title": "Pharmaceutical Packaging Solutions | Rajvi Packaging",
        "description": "Cleanroom-grade EPE foam, bubble insulation, and protective packaging for pharmaceutical cold-chain and diagnostics.",
        "badge": "Pharmaceutical",
        "hero_title": "Packaging Solutions for the <span>Pharmaceutical Industry</span>",
        "hero_sub": "Rajvi Packaging manufactures cleanroom-grade, non-shedding protective liners, insulation bubble wrap, and precision die-cut gaskets to maintain product purity and temperature consistency.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-epe/",
        "hero_product_text": "See EPE Products",
        "overview": "Pharmaceutical manufacturing requires absolute sterility, thermal stability, and impact protection. Ampoules, vials, and diagnostic equipment must be secured with zero dust contamination, while cold-chain products need high-performance thermal insulation barrier wraps.",
        "challenges": [
            {"icon": "🌡️", "title": "Temperature Control", "desc": "Cold-chain medicines degrade quickly if exposed to ambient temperature spikes during airport transfers."},
            {"icon": "🧪", "title": "Purity & Contamination", "desc": "Standard fiberboard packaging sheds dust particles that compromise sterile pharmaceutical cleanrooms."},
            {"icon": "🧪", "title": "Fragile Ampoules & Vials", "desc": "Thin glass ampoules and diagnostic vials break easily under vibrations and high deceleration impacts."},
            {"icon": "💧", "title": "Moisture & Humidity", "desc": "High humidity degrades moisture-sensitive pills, foil packages, and carton liners."},
            {"icon": "📊", "title": "Strict Regulatory Standards", "desc": "Packaging must be manufactured using FDA-compliant, non-toxic, and non-reactive materials."},
            {"icon": "📦", "title": "Bulk Shipments Security", "desc": "Bulk APIs and pharmaceutical formulations need heavy-duty, tamper-evident protective wrapping."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Cleanroom EPE Pouches"},
            {"challenge": "Cushioning", "product": "Polyurethane Foam Buffers"},
            {"challenge": "Thermal Insulation", "product": "Aluminium Foil Bubble Wrap"},
            {"challenge": "Airtight Sealing", "product": "Die-Cut Foam Gaskets"},
            {"challenge": "Purity Protection", "product": "Dust-Free XLPE Inserts"},
            {"challenge": "Heavy Bulk Containment", "product": "Reusable Pallet Covers"}
        ],
        "solutions_cards": [
            {"title": "Aluminium Foil Laminated Bubble", "desc": "Combines reflective thermal barrier foil with insulation air cells to maintain cold-chain temperatures.", "benefits": "High thermal resistance, lightweight, moisture proof", "link": "../../product-bubble/"},
            {"title": "Dust-Free EPE Liners", "desc": "Chemically inert closed-cell EPE sleeves that do not shed particles, ideal for cleanroom operations.", "benefits": "FDA-compliant raw material, lint-free, soft protection", "link": "../../product-epe/"},
            {"title": "EPDM & EVA Foam Gaskets", "desc": "Precision die-cut gaskets for sealing ducting, diagnostic panels, and laboratory enclosures.", "benefits": "IP-rated sealing, high temperature stability", "link": "../../product-gaskets/"}
        ],
        "applications": [
            {"icon": "🧪", "title": "Glass Vials & Ampoules"},
            {"icon": "🌡️", "title": "Cold-Chain Vaccines"},
            {"icon": "🔬", "title": "Lab Diagnostics Equipment"},
            {"icon": "💊", "title": "Blister Pack Protection"},
            {"icon": "📦", "title": "Bulk API Shipments"},
            {"icon": "🏥", "title": "Clinical Trials Kits"},
            {"icon": "🧪", "title": "Syringes & Cartridges"}
        ],
        "segments": ["Finished Formulations", "Active Pharmaceutical Ingredients (APIs)", "Cold-Chain Logistics", "Diagnostic & Lab Instruments", "Surgical & Biotech Products", "Clinical Trial Packaging"],
        "metrics": [
            {"num": "100%", "label": "FDA Compliant Materials"},
            {"num": "Lint-Free", "label": "Cleanroom Grade"},
            {"num": "R-value", "label": "Thermal Insulation"},
            {"num": "15+", "label": "Years in Business"}
        ],
        "faqs": [
            {"q": "Are your materials safe for pharmaceutical cleanrooms?", "a": "Yes, we offer cross-linked PE (XLPE) and closed-cell EPE foams that are non-shedding, lint-free, and chemical-resistant, making them ideal for sterile environments."},
            {"q": "Do you provide thermal insulation certificates?", "a": "Yes, we test our aluminium foil bubble insulation to document thermal reflectance and conductivity performance."},
            {"q": "Can you manufacture custom-sized EPE ampoule trays?", "a": "Absolutely. We design and cut customized multi-cavity EPE foam trays to secure ampoules and vials during internal plant transport."},
            {"q": "Are the adhesives used in your lamination non-toxic?", "a": "Yes, we use food and pharmaceutical-grade adhesives that comply with relevant safety standards."},
            {"q": "Do you support custom printing for tracking?", "a": "Yes, we print handling instructions, symbols, and batch tracking directly onto bubble wraps and sheets."}
        ],
        "resources": [
            {"title": "Cold-Chain Thermal Packaging Guide", "desc": "Best practices for using laminated bubble insulation in pharmaceutical freight.", "link": "#"},
            {"title": "Cleanroom Materials Compliance Sheet", "desc": "Specifications for our dust-free closed-cell EPE and XLPE foam liners.", "link": "#"}
        ],
        "inquiry_category": "EPE Pouches",
        "form_industry": "Pharmaceutical",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your Pharmaceutical Packaging Need",
        "form_desc": "Send us your temperature parameters and dimensions. Our packaging engineers will configure the perfect protective shield.",
        "form_trust": [
            "Free thermal analysis & design",
            "Lint-free cleanroom materials",
            "FDA-compliant virgin polymers",
            "Export standards validation",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#0f766e",
            "accent": "#0d9488",
            "dark": "#115e59",
            "light": "#f0fdfa",
            "accent_rgb": "13,148,136"
        },
        "stats": [
            {"num": "100%", "label": "Non-Toxic"},
            {"num": "Clean", "label": "Lint Free"},
            {"num": "Cold", "label": "Chain Ready"}
        ]
    },
    "fmcg": {
        "title": "FMCG Packaging Solutions | Rajvi Packaging",
        "description": "High-volume protective wraps, bubble rolls, and EPE foam padding for fast-moving consumer goods.",
        "badge": "FMCG",
        "hero_title": "Packaging Solutions for the <span>FMCG Industry</span>",
        "hero_sub": "Rajvi Packaging provides high-volume, cost-effective air bubble sheets, EPE cushioning, and reusable pallet wraps to speed up packing lines and eliminate damage in retail distribution.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-bubble/",
        "hero_product_text": "See Bubble Products",
        "overview": "Fast-Moving Consumer Goods (FMCG) require packaging that balances robust protection with high-speed operational efficiency and low weight. From preventing breakages in glass jars to securing bulk pallet shipments for distribution centers, our packaging shields products through heavy transit loads.",
        "challenges": [
            {"icon": "🥛", "title": "Glass Breakage", "desc": "Liquids, food items, and cosmetics packaged in glass break under drops and box drops."},
            {"icon": " secondary", "title": "Secondary Packaging Waste", "desc": "Excessive paper and cardboard usage inflates packing times and retail floor garbage volumes."},
            {"icon": "⏱️", "title": "Slow Assembly Lines", "desc": "Complex manual packaging slows down fast-moving high-volume fulfillment throughput."},
            {"icon": "🌧️", "title": "Water & Humidity Damage", "desc": "Rain during shipping ruins outer corrugated box boxes and print aesthetics."},
            {"icon": "⚖️", "title": "High Shipping Weight", "desc": "Heavier packaging options increase freight costs across millions of product units."},
            {"icon": "📐", "title": "Variable SKU Dimensions", "desc": "Securing different sizes of jars and bottles in single boxes requires versatile wrapping."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Air Bubble Wraps"},
            {"challenge": "Cushioning", "product": "EPE Foam Sheets"},
            {"challenge": "Fast Wrapping", "product": "Pre-formed Pouches"},
            {"challenge": "Pallet Security", "product": "Reusable FLC Wraps"},
            {"challenge": "Sealing Protection", "product": "Specialty Adhesives"},
            {"challenge": "Heavy Bulk Support", "product": "PP Separator Sheets"}
        ],
        "solutions_cards": [
            {"title": "High-Quality Air Bubble Rolls", "desc": "Tough, lightweight bubble wrap rolls available in various GSM grades to wrap food, beverages, and cosmetics.", "benefits": "Lightweight, shock-absorbing, cheap at scale", "link": "../../product-bubble/"},
            {"title": "Custom Bubble Pouches", "desc": "Pre-made open-mouth bubble bags designed for swift product insert and box pack loops.", "benefits": "Halves packing time, consistent protection", "link": "../../product-bubble/"},
            {"title": "PP Corrugated Separator Sheets", "desc": "Plastic separator layers used inside boxes to stack layers of glass bottles safely.", "benefits": "Reusable, moisture resistant, flat stackable", "link": "../../product-pp/"}
        ],
        "applications": [
            {"icon": "🥛", "title": "Glass Jars & Bottles"},
            {"icon": "🧴", "title": "Cosmetics & Perfumes"},
            {"icon": "🥫", "title": "Beverage & Food Cans"},
            {"icon": "🧼", "title": "Personal Care Packs"},
            {"icon": "📦", "title": "Bulk Pallet Loads"},
            {"icon": "☕", "title": "Premium Coffee & Spices"},
            {"icon": "🧴", "title": "Liquid Detergents"}
        ],
        "segments": ["Food & Beverages", "Cosmetics & Personal Care", "Household Care Products", "Premium Retail Gift Packaging", "Logistics & Warehousing", "D2C Brand Logistics"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "Millions", "label": "Units Supplied Monthly"},
            {"num": "40%", "label": "Packing Speed Improvement"},
            {"num": "Just-In-Time", "label": "Warehouse Supply"}
        ],
        "faqs": [
            {"q": "What is the best bubble wrap thickness for glass bottles?", "a": "For glass beverage and cosmetic bottles, we recommend 50 GSM to 80 GSM bubble wrap or pre-formed pouches, which protect against drops without inflating shipping weight."},
            {"q": "Do you offer pre-cut bubble sheets?", "a": "Yes, we supply pre-cut bubble sheets bundled in packs or perforated rolls at specific distances for quick packing lines."},
            {"q": "Can you design custom dunnage for bottle crates?", "a": "Yes, we design custom EPE foam inserts and PP separator layouts to secure glass containers inside logistics crates."},
            {"q": "Are your materials safe for food packaging?", "a": "Our bubble wraps and EPE foams are made of virgin, non-toxic LDPE, which is safe for secondary food contact packaging."},
            {"q": "What is your production capacity for high volumes?", "a": "We operate high-output extruders and conversion lines, capable of supplying lakhs of bubble pouches and rolls daily."}
        ],
        "resources": [
            {"title": "FMCG High-Speed Packing Guide", "desc": "How pre-made bubble pouches speed up fulfillment lines and reduce labor cost.", "link": "#"},
            {"title": "FMCG Material Safety Sheet", "desc": "Compliance specs for our food-contact safe virgin LDPE bubble wraps.", "link": "#"}
        ],
        "inquiry_category": "Air Bubble",
        "form_industry": "FMCG",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your FMCG Bulk Requirement",
        "form_desc": "Send us your monthly volumes, product types, and size specs. Our packaging consultants will configure a custom pricing sheet.",
        "form_trust": [
            "Competitive tier pricing sheets",
            "Flexible Minimum Order Quantities",
            "Direct factory dispatch logistics",
            "Virgin non-toxic raw polymers",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#4f46e5",
            "accent": "#6366f1",
            "dark": "#3730a3",
            "light": "#f5f3ff",
            "accent_rgb": "99,102,241"
        },
        "stats": [
            {"num": "Bulk", "label": "Tier Discounts"},
            {"num": "40%", "label": "Packing Boost"},
            {"num": "Just", "label": "In Time Supply"}
        ]
    },
    "ecommerce": {
        "title": "E-commerce Packaging Solutions | Rajvi Packaging",
        "description": "High-efficiency bubble wraps, custom pouches, and foam buffers designed to slash returns and shipping weights.",
        "badge": "E-commerce",
        "hero_title": "Packaging Solutions for the <span>E-commerce Industry</span>",
        "hero_sub": "Rajvi Packaging designs high-strength air bubble bags, EPE sheets, and protective fillers to speed up D2C packing benches and eliminate shipping damage.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-bubble/",
        "hero_product_text": "See Bubble Products",
        "overview": "Last-mile e-commerce courier networks subject parcels to intense drop and vibration stress. Online brands require protective, lightweight, and fast-to-pack materials to prevent damaged returns, lower DIM weight carrier fees, and ensure an excellent customer unboxing experience.",
        "challenges": [
            {"icon": "💔", "title": "Transit Damaged Returns", "desc": "Parcels dropped onto hard concrete during sorting hubs cause cosmetics and electronics to shatter."},
            {"icon": "⚖️", "title": "High Courier Freight Costs", "desc": "Heavy packaging or unnecessarily large boxes inflate dimensional weight costs and squeeze D2C margins."},
            {"icon": "⏱️", "title": "Slow Packing Bench Cycles", "desc": "Fulfillment teams wrapping products in flat sheets manually wastes hours during peak sales seasons."},
            {"icon": "🎁", "title": "Poor Unboxing Experience", "desc": "Messy tape and over-wrapped crumpled paper look unprofessional and lead to negative customer reviews."},
            {"icon": "📦", "title": "Inconsistent Packing Quality", "desc": "Manual wrapping results in varying protective layers per box, causing unpredictable transit defect rates."},
            {"icon": "🌧️", "title": "Water Damage on Doorstep", "desc": "Packages left on doorsteps or delivered in the rain get soaked, ruining inner boxes."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Air Bubble Wrap"},
            {"challenge": "Cushioning", "product": "EPE Foam Sheets"},
            {"challenge": "Shock Absorption", "product": "Pre-formed Pouches"},
            {"challenge": "Component Protection", "product": "Foam Buffers"},
            {"challenge": "Secure Sealing", "product": "Self-Adhesive Bags"},
            {"challenge": "Heavy Product Support", "product": "PP Box Inserts"}
        ],
        "solutions_cards": [
            {"title": "Pre-formed Air Bubble Pouches", "desc": "Bags made of high-quality bubble sheets with optional peel-and-seal flaps for super fast order prep.", "benefits": "Saves 30 seconds per package, neat presentation", "link": "../../product-bubble/"},
            {"title": "Custom EPE Foam Sheets", "desc": "Lightweight polyethylene sheets in 1mm-2mm thicknesses to layer cosmetics and jewelry safely.", "benefits": "Scratch-resistant, non-abrasive, highly elastic", "link": "../../product-epe/"},
            {"title": "Specialty Sealing Tapes", "desc": "Strong self-adhesive tapes that keep outer cartons closed securely during rough sorting hub journeys.", "benefits": "High tear resistance, tamper evident, strong tack", "link": "../../product-adhesive/"}
        ],
        "applications": [
            {"icon": "🧴", "title": "Cosmetics & Perfumes"},
            {"icon": "📱", "title": "Electronics & Gadgets"},
            {"icon": "💍", "title": "Jewelry & Accessories"},
            {"icon": "🥛", "title": "Glassware & Decor"},
            {"icon": "💊", "title": "Wellness & Medicines"},
            {"icon": "👞", "title": "Apparel & Shoes"},
            {"icon": "📚", "title": "Books & Stationeries"}
        ],
        "segments": ["D2C Brands", "Online Marketplaces", "Third-Party Logistics (3PL)", "Electronics Retailers", "Beauty & Cosmetics D2C", "Home Decor Sellers"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "80%", "label": "Reduction in Damage"},
            {"num": "40%", "label": "Faster Packing Times"},
            {"num": "Flexible", "label": "MOQs for D2C"}
        ],
        "faqs": [
            {"q": "Which packaging material is best for e-commerce?", "a": "Pre-formed air bubble pouches are ideal for e-commerce because they provide great drop protection, add negligible weight, and cut order-packing time in half."},
            {"q": "Can you customize bubble pouch sizes for specific products?", "a": "Yes, we produce bubble bags in custom sizes tailored to your products—from small jewelry pouches to large laptop sleeves."},
            {"q": "Do you support self-adhesive tape flaps on pouches?", "a": "Yes, we can add peel-and-seal adhesive tapes to bubble pouches to eliminate the need for external packing tapes."},
            {"q": "What is the MOQ for custom bubble pouches?", "a": "We offer flexible Minimum Order Quantities for growing D2C brands. Contact our sales team for details."},
            {"q": "Are your plastic packaging products recyclable?", "a": "Yes, our bubble wraps and EPE foams are made of LDPE, which is 100% recyclable at recycling centers."}
        ],
        "resources": [
            {"title": "E-commerce Returns Reduction Checklist", "desc": "Practical packaging tweaks to lower transit breakages by 90% immediately.", "link": "#"},
            {"title": "Dimensional Weight Optimization Guide", "desc": "How to select packing sizes to lower courier shipping fees.", "link": "#"}
        ],
        "inquiry_category": "Air Bubble",
        "form_industry": "E-commerce",
        "form_label": "Request Quote",
        "form_title": "Let's Optimize Your E-commerce Fulfillment",
        "form_desc": "Send us your order volumes and typical product shapes. We'll configure pre-formed pouch prototypes to speed up your packing tables.",
        "form_trust": [
            "Free dimensional analysis check",
            "High-tack self adhesive backing",
            "Flexible low MOQs for brands",
            "Pan-India courier logistics support",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#6d28d9",
            "accent": "#8b5cf6",
            "dark": "#4c1d95",
            "light": "#f5f3ff",
            "accent_rgb": "139,92,246"
        },
        "stats": [
            {"num": "80%", "label": "Less Returns"},
            {"num": "40%", "label": "Lower Packing Cost"},
            {"num": "Bulk", "label": "Supply Ready"}
        ]
    },
    "furniture": {
        "title": "Furniture Packaging Solutions | Rajvi Packaging",
        "description": "Thick EPE foam cushions, edge protectors, and heavy-duty bubble wraps for modular and solid wood furniture.",
        "badge": "Furniture",
        "hero_title": "Packaging Solutions for the <span>Furniture Industry</span>",
        "hero_sub": "Rajvi Packaging manufactures thick EPE foam sheets, corner guards, and heavy-duty bubble wrap to prevent surface scratches and edge damage on furniture during shipment.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-foam/",
        "hero_product_text": "See Foam Products",
        "overview": "Wooden, metal, and glass furniture components are heavy, bulky, and highly prone to damage during transport and handling. Corner impact, surface friction, and moisture exposure can ruin premium wood finishes and glass surfaces. Professional protective packaging prevents expensive retail rejections.",
        "challenges": [
            {"icon": "📐", "title": "Corner & Edge Damage", "desc": "Heavy wood table tops and doors easily chip or split when dropped on corners in transit."},
            {"icon": "🎨", "title": "Surface Scratches", "desc": "Vibration friction rubs away premium paint finishes, veneers, and polished wood surfaces."},
            {"icon": "💧", "title": "Moisture & Mildew", "desc": "Wood absorbs humidity, causing swelling, warping, and mold during long ocean transit loops."},
            {"icon": "🥛", "title": "Glass Shatter", "desc": "Glass table tops and mirror panel inserts easily shatter under bending pressures and shocks."},
            {"icon": "📦", "title": "Bulky Transit Volume", "desc": "Securing heavy furniture sets requires robust packaging that doesn't balloon shipping volume."},
            {"icon": "⏱️", "title": "Slow Manual Wrapping", "desc": "Fitting individual foam blocks onto odd-shaped table legs and chairs manually takes too long."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "EPE Foam Rolls"},
            {"challenge": "Cushioning", "product": "Heavy-Duty Bubble Wrap"},
            {"challenge": "Edge Protection", "product": "EPE U-profile Guards"},
            {"challenge": "Glass Protection", "product": "EPE Foam Inserts"},
            {"challenge": "Secure Bundling", "product": "Stretch Films"},
            {"challenge": "Pallet Base Support", "product": "PP Corrugated Sheets"}
        ],
        "solutions_cards": [
            {"title": "EPE Foam Sheets & Rolls", "desc": "Available in thicknesses from 2mm to 10mm, EPE rolls wrap furniture components to cushion against friction.", "benefits": "Scratch-free surface protection, clean closed-cell structure", "link": "../../product-foam/"},
            {"title": "EPE Edge & Corner Guards", "desc": "Pre-formed EPE foam U-channels and corner caps that snap securely onto table edges and glass plates.", "benefits": "High corner-shock absorption, easy snap-on fitting", "link": "../../product-foam/"},
            {"title": "Heavy-Duty Laminated Bubble", "desc": "Extra-thick bubble wrap rolls to wrap sofas and heavy chairs for local and export shipment.", "benefits": "Tear-resistant, waterproof, durable cushioning", "link": "../../product-bubble/"}
        ],
        "applications": [
            {"icon": "🪑", "title": "Dining Tables & Chairs"},
            {"icon": "🚪", "title": "Cabinet Doors & Panels"},
            {"icon": "🛋️", "title": "Sofas & Armchairs"},
            {"icon": "🥛", "title": "Glass Table Tops"},
            {"icon": "🛏️", "title": "Modular Beds & Headboards"},
            {"icon": "🏢", "title": "Office Desks & Panels"},
            {"icon": "🛠️", "title": "Metal Furniture Frames"}
        ],
        "segments": ["Modular Furniture Manufacturers", "Solid Wood Furniture Brands", "Office Furniture Makers", "D2C Furniture E-commerce", "Furniture Exporters", "Premium Upholstery Makers"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "Zero", "label": "Edge Damage Reports"},
            {"num": "100%", "label": "Custom Sized Guards"},
            {"num": "Bulk", "label": "Roll supply capacity"}
        ],
        "faqs": [
            {"q": "Which packaging material is best for wooden furniture?", "a": "For wooden furniture, a combination of EPE foam sheets (for surface scratch prevention) and EPE U-profile corner guards (for edge protection) is highly recommended."},
            {"q": "Do you manufacture custom-sized corner guards?", "a": "Yes, we die-cut corner guards and profile channels to match your specific table top and panel thicknesses."},
            {"q": "What is the minimum order quantity for foam rolls?", "a": "We maintain flexible MOQs for standard EPE foam rolls. Contact our sales team to discuss custom length requirements."},
            {"q": "Can your foam packaging protect glass table tops?", "a": "Yes, we produce custom-fit EPE foam inserts that run along the perimeter of glass sheets to absorb side impacts during shipping."},
            {"q": "Is EPE foam moisture-proof?", "a": "Yes, closed-cell Expanded Polyethylene (EPE) is completely moisture-proof and prevents condensation from reaching wood finishes."}
        ],
        "resources": [
            {"title": "Furniture Transit Packaging Standard Guide", "desc": "How to package modular panels and tables to eliminate transit breakages.", "link": "#"},
            {"title": "EPE Profile Selection Sheet", "desc": "Technical specs for our U-channel and corner protection foam sizes.", "link": "#"}
        ],
        "inquiry_category": "Foam & Buffers",
        "form_industry": "Furniture",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your Furniture Protective Needs",
        "form_desc": "Send us your panel dimensions, thickness specs, and volumes. We'll design custom E-profile foam corner fittings to lock your shipments.",
        "form_trust": [
            "Free edge dunnage design & fitment",
            "Heavy-density EPE foam options",
            "Peel-and-stick backing layers",
            "Pan-India factory delivery loops",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#b45309",
            "accent": "#d97706",
            "dark": "#78350f",
            "light": "#fffbeb",
            "accent_rgb": "217,119,6"
        },
        "stats": [
            {"num": "Zero", "label": "Chipped Edges"},
            {"num": "100%", "label": "Veneer Protection"},
            {"num": "Heavy", "label": "Impact Absorbing"}
        ]
    },
    "glass-ceramic": {
        "title": "Glass & Ceramic Packaging Solutions | Rajvi Packaging",
        "description": "Heavy-duty bubble wraps, EPE inserts, and separator sheets for sanitaryware, glass, and mirrors.",
        "badge": "Glass & Ceramics",
        "hero_title": "Packaging Solutions for the <span>Glass &amp; Ceramic Industry</span>",
        "hero_sub": "Rajvi Packaging manufactures custom-engineered EPE foam inserts, high-impact bubble wrap, and dunnage templates to protect fragile glass, sanitaries, and tableware.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-foam/",
        "hero_product_text": "See Foam Products",
        "overview": "Glass and ceramic goods are chemically inert but physically fragile. Even minor shocks or bending pressures generate hair-line fractures that compromise structural integrity. Precision cushioning, vibration isolation, and corner protection are required to eliminate shipping losses.",
        "challenges": [
            {"icon": "💔", "title": "High Fragility & Cracking", "desc": "Extreme sensitivity to impact forces causes instant shattering of sanitaryware and glass sheets."},
            {"icon": "📐", "title": "Transit Shocks", "desc": "Bumps and vibration during transport transmit high energy that shatters packed products inside boxes."},
            {"icon": "🥛", "title": "Metal-on-Glass Scratches", "desc": "Friction between packed components dulls retail finishes, spoiling unboxing looks."},
            {"icon": "📦", "title": "High Return Claims", "desc": "Poor packaging creates high retail returns, leading to lost profits and administrative stress."},
            {"icon": "💧", "title": "Moisture & Dampness", "desc": "Damp packaging boxes weaken structural boxes, causing stack collapses in damp warehouses."},
            {"icon": "⚙️", "title": "Heavy Bulk Handling", "desc": "Heavy ceramic tiles and sanitaries require packaging that integrates with automated conveyor systems."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Air Bubble Wrap"},
            {"challenge": "Cushioning", "product": "EPE Foam Liners"},
            {"challenge": "Shock Absorption", "product": "CNC-Cut Foam Inserts"},
            {"challenge": "Vibration Damping", "product": "EPDM Gaskets"},
            {"challenge": "Secure Bundling", "product": "Adhesive Tapes"},
            {"challenge": "Heavy Load Support", "product": "PP Boxes & Sheets"}
        ],
        "solutions_cards": [
            {"title": "Heavy-Duty EPE Foam Trays", "desc": "Custom die-cut EPE foam trays configured to hold fragile cosmetic jars and lab glass vials securely.", "benefits": "Zero movement, shock absorption, clean look", "link": "../../product-foam/"},
            {"title": "Laminated Air Bubble Sheets", "desc": "Thick air bubble wrap laminated with a film layer to provide superior puncture resistance for sharp glass edges.", "benefits": "Tear resistant, reliable bubble preservation", "link": "../../product-bubble/"},
            {"title": "PP Corrugated Partition Grids", "desc": "Rigid plastic grid cells used to separate ceramic cups and tableware inside secondary cartons.", "benefits": "No-collision slots, reusable, moisture proof", "link": "../../product-pp/"}
        ],
        "applications": [
            {"icon": "🥛", "title": "Glassware & Tableware"},
            {"icon": "🚽", "title": "Sanitaryware & Fittings"},
            {"icon": "🖼️", "title": "Glass Sheets & Mirrors"},
            {"icon": "🧴", "title": "Cosmetic Glass Bottles"},
            {"icon": "🔬", "title": "Lab Glass Ware"},
            {"icon": "🧱", "title": "Ceramic Tiles"},
            {"icon": "🏺", "title": "Clay Pots & Artwares"}
        ],
        "segments": ["Sanitaryware Manufacturers", "Flat Glass & Mirror Processors", "Cosmetic Glass Packagers", "Laboratory Glassware Makers", "Ceramic Tile Manufacturers", "D2C Glass Decor Brands"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "98%", "label": "Reduction in Damage"},
            {"num": "Custom", "label": "Fitment Engineering"},
            {"num": "Pan-India", "label": "Wholesale Supply"}
        ],
        "faqs": [
            {"q": "What is the best way to package fragile glass sheets?", "a": "Fragile glass sheets should be packaged with EPE foam edge protectors along the perimeter and layered with 100 GSM laminated bubble wrap to prevent surface scratching and absorb shocks."},
            {"q": "Can you design custom tray configurations for cosmetic glass jars?", "a": "Yes, we design custom-fit multi-cavity EPE foam inserts that hold multiple jars securely in a single outer box, eliminating contact friction."},
            {"q": "Do you supply heavy-duty plastic divider grids?", "a": "Yes, we produce reusable PP corrugated partition dividers that isolate glass products inside crates for distribution."},
            {"q": "What is the typical thickness of foam used for ceramic protection?", "a": "EPE foam sheets of 2mm to 10mm are typically used depending on product weight and shock sensitivity."},
            {"q": "Can your packaging support automated packing lines?", "a": "Yes, our pre-cut bubble sheets and custom foam inserts are designed to fit seamlessly into high-speed assembly and packing systems."}
        ],
        "resources": [
            {"title": "Glass Transit Packaging Standard", "desc": "How to design cushioning systems that reduce transit breakage rates to near zero.", "link": "#"},
            {"title": "EPDM Gasket and Seal Selection Sheet", "desc": "Technical dimensions of EPDM seals for industrial glass panel mountings.", "link": "#"}
        ],
        "inquiry_category": "Air Bubble",
        "form_industry": "Glass & Ceramics",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your Glass & Ceramic Protection Needs",
        "form_desc": "Send us your jar sizes, weight limits, and monthly volumes. We'll design custom-nested bubble wrap sheets or foam trays to secure your wares.",
        "form_trust": [
            "Free drop-prevention consultation",
            "Heavy GSM puncture-proof bubble option",
            "Multi-cavity custom EPE trays",
            "Direct factory wholesale pricing",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#0369a1",
            "accent": "#0ea5e9",
            "dark": "#0c4a6e",
            "light": "#f0f9ff",
            "accent_rgb": "14,165,233"
        },
        "stats": [
            {"num": "98%", "label": "Fewer Breakages"},
            {"num": "±1mm", "label": "Tray Precision"},
            {"num": "Bulk", "label": "Wholesale Supply"}
        ]
    },
    "industrial-manufacturing": {
        "title": "Industrial Manufacturing Packaging | Rajvi Packaging",
        "description": "Heavy-duty returnable crates, custom dunnage, protective foam partitions, and FLC covers for machinery and metal parts.",
        "badge": "Industrial Manufacturing",
        "hero_title": "Packaging Solutions for <span>Industrial Manufacturing</span>",
        "hero_sub": "Rajvi Packaging engineers heavy-duty returnable PP boxes, custom EPE foam inserts, and reusable pallet covers to protect machined metals, castings, and sub-assemblies through long-haul logistics.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-pp/",
        "hero_product_text": "See PP Products",
        "overview": "Heavy machinery, metal castings, and precision industrial components require rugged packaging systems. Rust protection, structural stability under heavy stack loads, and efficient forklift compatibility are critical to maintaining lean supply chain flows and preventing damage.",
        "challenges": [
            {"icon": "⚙️", "title": "Heavy Weight Damage", "desc": "Industrial metal parts compress standard packaging, causing box collapses and forklift accidents."},
            {"icon": "🌧️", "title": "Corrosion & Rusting", "desc": "Bare steel castings and precision cylinders rust quickly when exposed to humidity and rain."},
            {"icon": "📦", "title": "Stretch Wrap Waste", "desc": "Wrapping pallets in disposable film daily generates substantial labor costs and plastic waste."},
            {"icon": "📐", "title": "Surface Abrasions", "desc": "Machined faces and precision threads get damaged due to loose containment during shipping."},
            {"icon": "🔄", "title": "Reverse Logistics Costs", "desc": "Bulky non-collapsible packaging containers consume precious freight space when returning empty."},
            {"icon": "⏱️", "title": "Line Feeding Bottlenecks", "desc": "Inefficient unpacking processes slow down sub-assembly feeding and assembly lines."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "EVA Laminated Inserts"},
            {"challenge": "Cushioning", "product": "High-Density Foam"},
            {"challenge": "Shock Absorption", "product": "Custom EPE Blocks"},
            {"challenge": "Weather Protection", "product": "Pallet Covers"},
            {"challenge": "Secure Containment", "product": "Tension Straps"},
            {"challenge": "Heavy Load Support", "product": "PP Crates & Pallets"}
        ],
        "solutions_cards": [
            {"title": "Heavy-Duty PP Corrugated Crates", "desc": "Returnable plastic containers with reinforced walls and stackable corner caps, load capacity up to 50+ kg.", "benefits": "Impact resistant, weatherproof, stackable", "link": "../../product-pp/"},
            {"title": "Custom Reusable FLC Covers", "desc": "Tough, weather-resistant pallet wraps with buckle straps that replace single-use stretch wrap.", "benefits": "Eco-friendly, fast packing, reusable", "link": "../../product-flc/"},
            {"title": "Precision Die-Cut XLPE Dunnage", "desc": "Chemically cross-linked PE foam blocks designed to nest machined components securely inside bins.", "benefits": "No chemical leaching, zero oil absorption, high load capacity", "link": "../../product-foam/"}
        ],
        "applications": [
            {"icon": "⚙️", "title": "Machined Castings"},
            {"icon": "🔩", "title": "Precision Shafts & Valves"},
            {"icon": "🏭", "title": "Assembly Line Components"},
            {"icon": "🔌", "title": "Heavy Control Panels"},
            {"icon": "📦", "title": "Bulk Sub-assemblies"},
            {"icon": "🛠️", "title": "Machine Tool Spares"},
            {"icon": "⚙️", "title": "Pneumatic Cylinders"}
        ],
        "segments": ["Automotive Component OEM", "Heavy Engineering & Tooling", "Electrical Switchgear Makers", "Pneumatic & Hydraulics", "Bearing Manufacturers", "Metal Fabrication Shops"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "50+ kg", "label": "Crate Load Capacity"},
            {"num": "95%", "label": "Stretch Wrap Cut"},
            {"num": "Zero", "label": "Corrosion Reports"}
        ],
        "faqs": [
            {"q": "Can your PP boxes support heavy iron castings?", "a": "Yes, we engineer our PP corrugated boxes with double-thickness fluting and internal rigid EPE/EVA dunnage to support weights up to 50+ kg per crate safely."},
            {"q": "Do you supply corrosion-resistant foam packaging?", "a": "Yes, we use chemically inert XLPE and EPE closed-cell foams that do not hold moisture or release chemicals, protecting bare metal parts from corrosion."},
            {"q": "What is the ROI on switching to reusable pallet covers?", "a": "Most manufacturing plants see full return on investment within 6 to 8 months by eliminating stretch film purchases and speeding up pallet wrap times."},
            {"q": "Can you manufacture packaging custom-designed for our automated conveyor systems?", "a": "Yes, we tailor container footprints and runner designs to fit seamlessly with your automated warehouses and assembly line rollers."},
            {"q": "Do you sign NDAs before receiving custom part drawings?", "a": "Yes, we regularly sign NDAs with tier-1 engineering and automotive brands before receiving CAD, step, or DXF files."}
        ],
        "resources": [
            {"title": "Industrial Returnable Packaging Design Book", "desc": "How to design custom foam and PP containers for supplier networks.", "link": "#"},
            {"title": "FLC Reusable Pallet Cover Cost Benefit Sheet", "desc": "Cost comparisons showing savings of reusable wraps vs stretch film.", "link": "#"}
        ],
        "inquiry_category": "PP Boxes & Sheets",
        "form_industry": "Industrial Manufacturing",
        "form_label": "Request Quote",
        "form_title": "Let's Discuss Your Industrial Packaging Requirements",
        "form_desc": "Send us your weight specs, bin footprints, and monthly volumes. Our logistics engineers will config heavy-duty PP returnable boxes and custom EPE/XLPE dunnage layout.",
        "form_trust": [
            "Free logistics dunnage design & fit",
            "Rust-resistant inert XLPE foams",
            "Reinforced stackable box options",
            "Pan-India wholesale delivery loops",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#334155",
            "accent": "#64748b",
            "dark": "#1e293b",
            "light": "#f8fafc",
            "accent_rgb": "100,116,139"
        },
        "stats": [
            {"num": "50+ kg", "label": "Load Capacity"},
            {"num": "95%", "label": "Less Stretch Wrap"},
            {"num": "15+", "label": "Years in Business"}
        ]
    },
    "electrical-components": {
        "title": "Electrical Components Packaging | Rajvi Packaging",
        "description": "Anti-static foam inserts, EPDM gaskets, and protective bubble wrap for electrical relays, panels, and meters.",
        "badge": "Electrical Components",
        "hero_title": "Packaging Solutions for <span>Electrical Components</span>",
        "hero_sub": "Rajvi Packaging manufactures custom-engineered anti-static foam inserts, die-cut gaskets, and heavy-duty bubble wraps to protect electrical components, meters, and switchgear.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-gaskets/",
        "hero_product_text": "See Gasket Products",
        "overview": "Electrical components and control systems require clean, dry, and shock-free transport environments. Sensitive relays, digital meters, and switchgears must be protected from electrostatic discharge (ESD), micro-scratches on display screens, moisture ingress, and handling impacts.",
        "challenges": [
            {"icon": "⚡", "title": "Electrostatic Discharge (ESD)", "desc": "Static charge buildup destroys electronic relays, digital displays, and microcontrollers silently."},
            {"icon": "🛡️", "title": "Physical Impact Damage", "desc": "Heavy switchgears and meters crack or fall out of calibration under transport drops."},
            {"icon": "💧", "title": "Moisture & Dust Ingress", "desc": "Humidity corrodes copper contacts, and dust settles inside mechanical relays, causing operation failure."},
            {"icon": "📐", "title": "Screen Scratches", "desc": "Friction between display windows and standard packaging boxes dulls display readability."},
            {"icon": "⏱️", "title": "Manual Assembly Line Speeds", "desc": "Complex packaging wraps slow down high-speed component packaging benches."},
            {"icon": "🌍", "title": "Export Shipping Damage", "desc": "Long transit loops expose electrical panels to corrosion and impact hazards."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Pink ESD Bubble wrap"},
            {"challenge": "Cushioning", "product": "Custom EPE Pouches"},
            {"challenge": "Shock Absorption", "product": "CNC-cut Foam Inserts"},
            {"challenge": "Enclosure Sealing", "product": "Die-Cut Foam Gaskets"},
            {"challenge": "Secure Bundling", "product": "Adhesive Sealing Tapes"},
            {"challenge": "Panel Support", "product": "PP Corrugated Sheets"}
        ],
        "solutions_cards": [
            {"title": "Anti-Static Foam Buffers", "desc": "Precision cut Pink EPE and conductive XLPE foam inserts configured to hold relays and meters securely.", "benefits": "ESD safe, custom-fit, zero screen scratches", "link": "../../product-foam/"},
            {"title": "EPDM/EVA Foam Gaskets", "desc": "Custom die-cut foam sealing gaskets designed to provide dust and moisture seals for electrical cabinets.", "benefits": "IP-rating compatible, long life, excellent compression", "link": "../../product-gaskets/"},
            {"title": "High-Strength Bubble Sheets", "desc": "Bubble rolls and bags to wrap heavy switchgears, contactors, and relays for transit.", "benefits": "Lightweight, shock absorbing, durable", "link": "../../product-bubble/"}
        ],
        "applications": [
            {"icon": "🔌", "title": "Digital Meters & Relays"},
            {"icon": "⚡", "title": "Switchgear & Contactors"},
            {"icon": "🏥", "title": "Electrical Control Panels"},
            {"icon": "⚙️", "title": "Transformers & Chokes"},
            {"icon": "📱", "title": "Industrial Enclosures"},
            {"icon": "🔌", "title": "Circuit Breakers (MCBs)"},
            {"icon": "🔌", "title": "Connectors & Busbars"}
        ],
        "segments": ["Switchgear & Control Gear Makers", "Electrical Meter Manufacturers", "Control Panel Builders", "Transformer & Power Supply Makers", "Home Automation Brands", "Electrical Spares Exporters"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "100%", "label": "ESD Safe Options"},
            {"num": "±1mm", "label": "Gasket Precision"},
            {"num": "Bulk", "label": "Volume Capacity"}
        ],
        "faqs": [
            {"q": "What type of foam is best for sensitive electrical relays?", "a": "We recommend Pink ESD EPE foam or cross-linked PE (XLPE) foam. They prevent static charge generation and do not shed fibers, keeping electrical relays clean and safe."},
            {"q": "Do you manufacture custom self-adhesive gaskets for control cabinets?", "a": "Yes, we die-cut self-adhesive EPDM and EVA foam gaskets to your exact specifications to prevent water and dust leaks in outdoor panel cabinets."},
            {"q": "Can you design custom trays for shipping multiple digital meters?", "a": "Yes, we configure multi-cavity EPE foam trays that nest multiple digital meters in a single carton for transport."},
            {"q": "Are your electrical packaging materials ESD certified?", "a": "Yes, our anti-static bubble wraps and foams are tested to meet standard surface resistance specifications for ESD protection (10^6 to 10^11 ohms)."},
            {"q": "Do you sign NDAs before receiving enclosure drawings?", "a": "Yes, we routinely sign NDAs with electrical panel and OEM brands before reviewing cabinet drawings or part specs."}
        ],
        "resources": [
            {"title": "Electrical ESD Packaging Guide", "desc": "How to select ESD safe materials for digital meters and circuit boards.", "link": "#"},
            {"title": "Cabinet Sealing and IP Gasket Guide", "desc": "Selecting the correct EPDM/EVA foam density for dust and splash seals.", "link": "#"}
        ],
        "inquiry_category": "Foam Gaskets",
        "form_industry": "Electrical Components",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your Electrical Packaging Needs",
        "form_desc": "Send us your panel drawing shapes or meter dimensions. We'll design custom-nested anti-static foam inserts and IP-grade sealing gaskets.",
        "form_trust": [
            "Free ESD & gasket design check",
            "High-compression IP-rated foam",
            "Anti-static Pink & Black materials",
            "Pan-India factory supply chains",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#0369a1",
            "accent": "#0ea5e9",
            "dark": "#0c4a6e",
            "light": "#f0f9ff",
            "accent_rgb": "14,165,233"
        },
        "stats": [
            {"num": "100%", "label": "ESD Safe"},
            {"num": "±1mm", "label": "Cut Accuracy"},
            {"num": "Bulk", "label": "Wholesale Supply"}
        ]
    },
    "consumer-durables": {
        "title": "Consumer Durables Packaging | Rajvi Packaging",
        "description": "Heavy-duty EPE foam corner blocks, custom buffers, and bubble sheets for refrigerators, TVs, and large appliances.",
        "badge": "Consumer Durables",
        "hero_title": "Packaging Solutions for <span>Consumer Durables</span>",
        "hero_sub": "Rajvi Packaging manufactures heavy-duty EPE foam buffers, custom corner protectors, and high-GSM bubble wrap to secure home appliances and consumer electronics from transit shocks.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-foam/",
        "hero_product_text": "See Foam Products",
        "overview": "Consumer durables like television panels, refrigerators, and washing machines are heavy, high-value, and sensitive to transport drops and vibrations. Edge deformation, cabinet scratches, and screen cracks can lead to costly rejections and brand damage. Engineered foam cushions provide reliable drop safety.",
        "challenges": [
            {"icon": "📺", "title": "Screen & Glass Cracks", "desc": "Fragile LCD/LED display panels shatter easily under twisting forces and direct shocks."},
            {"icon": "📐", "title": "Cabinet Dents & Cracks", "desc": "Heavy appliances dropped during forklift loading sustain dents on sheet metal or cracks on plastic trims."},
            {"icon": "📦", "title": "Bulky Volume", "desc": "Securing large appliances requires thick cushioning without ballooning total freight box volume."},
            {"icon": "💧", "title": "Humidity Condensation", "desc": "Long warehouse storage in humid climates corrodes internal metal parts and electronics."},
            {"icon": "⏱️", "title": "Slow Packing Speed", "desc": "Assembling complex multi-piece packaging slows down packaging lines during peak seasons."},
            {"icon": "🌱", "title": "Recyclability Demands", "desc": "OEMs need 100% recyclable materials to meet green packaging regulations."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "EPE Foam Sheets"},
            {"challenge": "Cushioning", "product": "Heavy-Duty Bubble Wrap"},
            {"challenge": "Edge Protection", "product": "EPE Corner Blocks"},
            {"challenge": "Shock Absorption", "product": "Custom Foam Inserts"},
            {"challenge": "Secure Sealing", "product": "High-Bond Tapes"},
            {"challenge": "Heavy Load Support", "product": "PP Corrugated Sheets"}
        ],
        "solutions_cards": [
            {"title": "Custom EPE Foam Corner Guards", "desc": "Thick, molded Expanded Polyethylene (EPE) corner blocks and edge channels designed to fit appliance edges.", "benefits": "High drop energy absorption, snap-on fit, zero paint scratch", "link": "../../product-foam/"},
            {"title": "Heavy-Duty EPE Foam Buffers", "desc": "Die-cut EPE foam cushions that secure appliances inside corrugated boxes, replacing thermoformed polystyrene.", "benefits": "Tear-resistant, 100% recyclable, high compression recovery", "link": "../../product-foam/"},
            {"title": "Thick Laminated Air Bubble Wrap", "desc": "High-GSM air bubble wrap rolls to wrap appliance accessories and fragile panels.", "benefits": "Moisture-proof, durable air cells, lightweight", "link": "../../product-bubble/"}
        ],
        "applications": [
            {"icon": "📺", "title": "LED / LCD Televisions"},
            {"icon": "🧊", "title": "Refrigerators"},
            {"icon": "🌀", "title": "Washing Machines"},
            {"icon": "💨", "title": "Air Conditioners"},
            {"icon": "🔥", "title": "Microwaves & Ovens"},
            {"icon": "🍵", "title": "Kitchen Appliances"},
            {"icon": "🔊", "title": "Audio Systems"}
        ],
        "segments": ["Home Appliance Manufacturers", "Consumer Electronics Brands", "Commercial Appliance Makers", "D2C Appliance Retailers", "Appliance Exporters", "E-commerce Fulfilment Centers"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "Zero", "label": "Dent Reports"},
            {"num": "100%", "label": "Recyclable Foam"},
            {"num": "Bulk", "label": "Supply Capacity"}
        ],
        "faqs": [
            {"q": "Why is EPE foam better than EPS (polystyrene) for appliances?", "a": "EPE foam is highly flexible, tear-resistant, and recovers its shape after impacts, whereas EPS crumbles easily and is not widely recyclable. EPE provides better multi-drop protection and supports eco-friendly policies."},
            {"q": "Can you design custom corner guards for washing machines?", "a": "Yes, we design custom-fit EPE foam corner caps and edge guards configured to match your appliance dimensions and weight."},
            {"q": "What thickness of EPE foam is recommended for TV screen protection?", "a": "We typically recommend 15mm to 30mm thick EPE foam buffers along the front and edges, depending on TV size and drop-test requirements."},
            {"q": "Are your packaging materials 100% recyclable?", "a": "Yes, our LDPE-based EPE foams and bubble wraps are 100% recyclable and eco-friendly."},
            {"q": "Do you support just-in-time delivery for high-volume factories?", "a": "Yes, we maintain a fleet of delivery vehicles and warehouse inventory to support just-in-time manufacturing schedules for appliance brands."}
        ],
        "resources": [
            {"title": "Appliance Drop-Test Packaging Guide", "desc": "How to design foam buffers to pass standard drop tests for consumer durables.", "link": "#"},
            {"title": "EPE Foam Cushion Design Specifications", "desc": "Material properties, density charts, and compression recovery data for appliance packaging.", "link": "#"}
        ],
        "inquiry_category": "Foam & Buffers",
        "form_industry": "Consumer Durables",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your Appliance Protective Needs",
        "form_desc": "Send us your cabinet weight limits, frame dimensions, and monthly runs. We'll design custom EPE foam cushions to lock your appliances safely.",
        "form_trust": [
            "Free appliance drop safety consult",
            "Molded EPE & PU foam choices",
            "100% recyclable green materials",
            "Direct factory wholesale volume supply",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#0f172a",
            "accent": "#3b82f6",
            "dark": "#020617",
            "light": "#f8fafc",
            "accent_rgb": "59,130,246"
        },
        "stats": [
            {"num": "Zero", "label": "Dents Reported"},
            {"num": "100%", "label": "Eco Recyclable"},
            {"num": "Heavy", "label": "Impact Buffer"}
        ]
    },
    "logistics": {
        "title": "Logistics & Warehousing Packaging | Rajvi Packaging",
        "description": "Heavy-duty reusable pallet covers, bubble wraps, PP separator sheets, and stretch films for logistics and warehousing.",
        "badge": "Logistics & Warehousing",
        "hero_title": "Packaging Solutions for <span>Logistics &amp; Warehousing</span>",
        "hero_sub": "Rajvi Packaging manufactures durable reusable FLC covers, heavy-duty bubble wraps, and PP separator sheets to stabilize pallet loads, protect inventory, and reduce operational waste.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-flc/",
        "hero_product_text": "See FLC Products",
        "overview": "Warehousing and distribution centers handle high-volume product movements across varied transport networks. Loose loads, dust exposure, rain, and packaging waste are primary challenges. Standardized, reusable, and tough protective materials keep operations lean and cargo safe.",
        "challenges": [
            {"icon": "📦", "title": "Load Instability", "desc": "Unsecured cartons on pallets shift and fall during transit, causing inventory loss and forklift hazards."},
            {"icon": "🗑️", "title": "High Plastic Waste", "desc": "Wrapping pallets in disposable plastic stretch film daily generates high ongoing supply costs and environmental waste."},
            {"icon": "🌧️", "title": "Weather Exposure", "desc": "Rain during dock loading and temporary outdoor storage ruins outer boxes and rusts metal parts."},
            {"icon": "⏱️", "title": "Slow Dispatch Wrapping", "desc": "Manual wrapping of pallets with orbital stretch film slows down dispatch times and increases labor costs."},
            {"icon": "📐", "title": "Product Collapsing", "desc": "Stacked pallets compress lower-tier boxes, crushing products under high weight loads."},
            {"icon": "🐀", "title": "Dust & Ingress", "desc": "Long-term warehouse storage exposes goods to dust accumulation and pest damage."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "Air Bubble Wrap"},
            {"challenge": "Cushioning", "product": "EPE Foam Rolls"},
            {"challenge": "Pallet Stability", "product": "FLC Pallet Covers"},
            {"challenge": "Stacking Support", "product": "PP Separator Sheets"},
            {"challenge": "Secure Bundling", "product": "High-Tack Tape"},
            {"challenge": "Water Protection", "product": "Waterproof Liners"}
        ],
        "solutions_cards": [
            {"title": "Reusable FLC Pallet Covers & Wraps", "desc": "Heavy-duty woven fabric wraps with tensioning straps that secure cargo on pallets, replacing stretch film.", "benefits": "100+ reuse cycles, secures a pallet in under 30 seconds, weatherproof", "link": "../../product-flc/"},
            {"title": "PP Corrugated Separator Sheets", "desc": "Rigid plastic sheets used to layer cartons on pallets, distributing weight evenly and preventing crushing.", "benefits": "Reusable, moisture-proof, flat-stackable", "link": "../../product-pp/"},
            {"title": "Heavy-Duty Air Bubble Rolls", "desc": "Thick bubble wraps to wrap fragile boxes and machinery before dispatch.", "benefits": "Tear-resistant, water-proof, highly shock-absorbent", "link": "../../product-bubble/"}
        ],
        "applications": [
            {"icon": "📦", "title": "Palletized Cartons"},
            {"icon": "🏢", "title": "High-Bay Racking"},
            {"icon": "🌧️", "title": "Outdoor Storage Goods"},
            {"icon": "🔄", "title": "Inter-Plant Transfer Loops"},
            {"icon": "⚙️", "title": "Machinery Shipping"},
            {"icon": "📦", "title": "Bulk Distribution Sets"},
            {"icon": "🚚", "title": "Cross-Dock Fulfilment"}
        ],
        "segments": ["Third-Party Logistics (3PL)", "Distribution Centers", "Automotive Supplier Loops", "Manufacturing Warehouse Docks", "Retail Logistics Networks", "Export Freight Forwarders"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "95%", "label": "Stretch Film Savings"},
            {"num": "30 sec", "label": "Pallet Wrap Time"},
            {"num": "Pan-India", "label": "Wholesale Delivery"}
        ],
        "faqs": [
            {"q": "How do reusable FLC pallet wraps save money?", "a": "Reusable FLC wraps replace single-use plastic stretch wrap completely. Since a single wrap lasts for 100+ trips, it slashes packaging supply costs and eliminates disposal fees, typically paying for itself in under 6 months."},
            {"q": "Can you manufacture pallet covers to custom height requirements?", "a": "Yes, we manufacture FLC covers in custom heights and footprints configured to your standard pallet sizes and stack heights."},
            {"q": "Do you supply heavy-duty plastic separator sheets?", "a": "Yes, we produce reusable PP corrugated separator sheets in various thicknesses to stabilize multi-tier stacked pallets."},
            {"q": "Are your FLC pallet wraps weatherproof?", "a": "Yes, our FLC covers are made of heavy-duty, water-resistant woven polyester/canvas, protecting cargo from rain and dust."},
            {"q": "What is the lifespan of your PP separator sheets?", "a": "Our PP separator sheets are highly durable and survive dozens of cycles in inter-plant manufacturing loops."}
        ],
        "resources": [
            {"title": "Warehouse Waste Reduction Guide", "desc": "How to switch from disposable stretch wrap to reusable FLC covers to cut packaging costs by 70%.", "link": "#"},
            {"title": "PP Corrugated Separator Sheet Specification", "desc": "Technical dimensions, load distribution data, and reuse cycles.", "link": "#"}
        ],
        "inquiry_category": "FLC Pallet Covers",
        "form_industry": "Logistics & Warehousing",
        "form_label": "Request Quote",
        "form_title": "Let's Optimize Your Warehouse Logistics",
        "form_desc": "Send us your pallet footprints, stack heights, and monthly load cycles. We'll design a reusable FLC pallet cover layout to speed up your dispatch docks.",
        "form_trust": [
            "Free logistics packaging audit",
            "Custom FLC cover prototypes",
            "Heavy-duty industrial canvas fabric",
            "Pan-India wholesale delivery logistics",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#047857",
            "accent": "#10b981",
            "dark": "#064e3b",
            "light": "#ecfdf5",
            "accent_rgb": "16,185,129"
        },
        "stats": [
            {"num": "95%", "label": "Stretch Wrap Saved"},
            {"num": "30 sec", "label": "Fast Wrap Time"},
            {"num": "100+", "label": "Reuse Loops"}
        ]
    },
    "export-packaging": {
        "title": "Export Packaging Solutions | Rajvi Packaging",
        "description": "Export-grade protective foam inserts, heavy-duty bubble wraps, and FLC pallet wraps meeting international cargo standards.",
        "badge": "Export Packaging",
        "hero_title": "Packaging Solutions for <span>Export Shipping</span>",
        "hero_sub": "Rajvi Packaging engineers heavy-duty, moisture-resistant, and drop-proof packaging systems meeting international export standards to protect your goods during long sea voyages.",
        "hero_cta": "Request a Quote",
        "hero_product_link": "../../product-foam/",
        "hero_product_text": "See Foam Products",
        "overview": "International export shipments encounter extreme transport challenges — including maritime humidity, rough container shifts, custom audits, and multi-mode carrier handling. Standard domestic packaging fails under these loads. Engineered, moisture-proof, and certified packaging ensures zero rejects at destination.",
        "challenges": [
            {"icon": "💧", "title": "Saltwater Corrosion", "desc": "High maritime humidity and salty sea air rust precision machinery and metal components inside containers."},
            {"icon": "📦", "title": "Container Container Shifting", "desc": "Heavy ocean swelling causes cargo to shift, crash, and collapse inside shipping containers."},
            {"icon": "📐", "title": "Multi-Country Transit Shocks", "desc": "Transferring cargo across docks, airliners, and trucks exposes packaging to severe drops and impacts."},
            {"icon": "📜", "title": "Rigid Import Regulations", "desc": "Many nations restrict wood packaging, requiring certified, non-wood, and recyclable alternatives."},
            {"icon": "⏱️", "title": "Extreme Temperature Swings", "desc": "Container interiors reach 60°C in equatorial seas, degrading glue joints and low-grade plastics."},
            {"icon": "💔", "title": "Destination Rejections", "desc": "Any transit damage at international destinations leads to expensive re-shipping fees and brand loss."}
        ],
        "solutions_mapping": [
            {"challenge": "Surface Protection", "product": "High-GSM Bubble wrap"},
            {"challenge": "Cushioning", "product": "Thick EPE Foam"},
            {"challenge": "Shock Absorption", "product": "Custom Foam Inserts"},
            {"challenge": "Moisture Protection", "product": "Aluminium Laminated wrap"},
            {"challenge": "Secure Containment", "product": "Specialty Sealing Tapes"},
            {"challenge": "Non-Wood Pallet Support", "product": "PP Crates & Pallets"}
        ],
        "solutions_cards": [
            {"title": "Aluminium Foil Laminated Bubble wrap", "desc": "Reflects heat and acts as an absolute moisture barrier to prevent corrosion and dampness in ocean freight.", "benefits": "Zero moisture transmission, heat reflective, dust-free", "link": "../../product-bubble/"},
            {"title": "Export-Grade EPE Foam Cushions", "desc": "High-density EPE foam dunnage designed to secure heavy machinery and engines inside containers.", "benefits": "Tear-resistant, high G-force absorption, ISPM-15 compliant (wood alternative)", "link": "../../product-foam/"},
            {"title": "Heavy-Duty PP Corrugated Crates", "desc": "Reusable plastic crates that replace wooden boxes, eliminating fumigation fees and import customs clearance issues.", "benefits": "Fumigation-free, stackable, water-proof", "link": "../../product-pp/"}
        ],
        "applications": [
            {"icon": "⚙️", "title": "Heavy Machineries"},
            {"icon": "🔌", "title": "Electrical Switchgears"},
            {"icon": "🚗", "title": "Auto Components"},
            {"icon": "🧪", "title": "Pharmaceutical APIs"},
            {"icon": "📱", "title": "Precision Electronics"},
            {"icon": "🏺", "title": "Ceramic Tablewares"},
            {"icon": "📦", "title": "Bulk Commodity Pallets"}
        ],
        "segments": ["Machinery Exporters", "Automotive Parts OEM", "Electrical Switchgear Exporters", "Pharma API Exporters", "Ceramic Tableware Exporters", "Biotech Goods Exporters"],
        "metrics": [
            {"num": "15+", "label": "Years in Business"},
            {"num": "Zero", "label": "Customs Rejections"},
            {"num": "100%", "label": "Fumigation Free"},
            {"num": "Global", "label": "Compliance Ready"}
        ],
        "faqs": [
            {"q": "What is the best way to prevent rust in ocean container exports?", "a": "For rust prevention, we recommend wrapping metal components in aluminum foil laminated bubble wrap. The closed-cell structure and metallic foil act as a barrier against sea humidity and condensation."},
            {"q": "Are your PP boxes and foam inserts ISPM-15 compliant?", "a": "Yes, our plastic boxes and EPE/XLPE foams are completely exempt from ISPM-15 regulations (which only apply to wood packaging). They require no fumigation or heat treatment, ensuring smooth customs clearance globally."},
            {"q": "Can you design custom dunnage for heavy export machinery?", "a": "Yes, we engineer high-density foam dunnage and dunnage blocks to distribute machinery weight and lock it securely inside shipping containers."},
            {"q": "Do you support custom printing for export handling signs?", "a": "Yes, we print international handling symbols, barcodes, and logos onto bubble wraps and sheets."},
            {"q": "What is the typical lead time for custom export orders?", "a": "Standard design and prototype phase takes 2–4 days, with bulk production delivered within 5–7 days from design approval."}
        ],
        "resources": [
            {"title": "Sea Freight Ingress and Rust Prevention Guide", "desc": "How to prevent moisture damage and oxidation in maritime transit loops.", "link": "#"},
            {"title": "ISPM-15 Fumigation-Exempt Packaging Guide", "desc": "Switching from wooden boxes to PP and foam to avoid customs clearance delays.", "link": "#"}
        ],
        "inquiry_category": "Foam & Buffers",
        "form_industry": "Export Packaging",
        "form_label": "Request Quote",
        "form_title": "Tell Us About Your Export Shipping Requirements",
"form_desc": "Send us your container size, product weight, and moisture parameters. We'll design custom foam inserts and laminated bubble shields to lock your cargo safely.",
        "form_trust": [
            "Free ocean transit design consultation",
            "Fumigation-free certified materials",
            "High-GSM laminated barrier wraps",
            "Pan-India direct factory shipping",
            "Response within 24 business hours"
        ],
        "colors": {
            "primary": "#475569",
            "accent": "#94a3b8",
            "dark": "#334155",
            "light": "#f8fafc",
            "accent_rgb": "148,163,184"
        },
        "stats": [
            {"num": "Zero", "label": "Customs Rejections"},
            {"num": "100%", "label": "Fumigation Exempt"},
            {"num": "Maritime", "label": "Moisture Proof"}
        ]
    }
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="icon" type="image/png" href="../../images/Rajvi Favicon.png">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../shared.css">
  <style>
    :root {
      --ind-primary: #0A3D2C;
      --ind-accent: #C9960A;
      --ind-dark: #072218;
      --ind-light: #F4F9F5;
      --ind-white: #FFFFFF;
      --ind-border: rgba(10, 61, 44, 0.08);
      --ind-shadow: 0 15px 35px rgba(10, 61, 44, 0.05);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    /* ── HERO ── */
    .ind-hero {
      position: relative;
      min-height: 88vh;
      display: flex;
      align-items: center;
      background: linear-gradient(135deg, var(--ind-dark) 0%, #0c3325 50%, var(--ind-dark) 100%);
      overflow: hidden;
      padding: 120px 60px 80px;
    }
    .ind-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(ellipse at 75% 50%, rgba(201, 150, 10, 0.1) 0%, transparent 60%);
      pointer-events: none;
    }
    .ind-hero-grid {
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
      background-size: 50px 50px;
      pointer-events: none;
    }
    .ind-hero-inner {
      position: relative;
      max-width: var(--max-w);
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 60px;
      align-items: center;
    }
    .ind-hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(201, 150, 10, 0.12);
      border: 1px solid rgba(201, 150, 10, 0.3);
      color: var(--ind-accent);
      font-family: 'Poppins', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 6px 16px;
      border-radius: 100px;
      margin-bottom: 24px;
    }
    .ind-hero-badge::before { content: '●'; font-size: 7px; }
    .ind-hero-title {
      font-family: 'Sora', sans-serif;
      font-size: clamp(34px, 4.5vw, 52px);
      font-weight: 800;
      color: #fff;
      line-height: 1.15;
      margin-bottom: 20px;
      letter-spacing: -0.02em;
    }
    .ind-hero-title span { color: var(--ind-accent); }
    .ind-hero-subtitle {
      font-family: 'Poppins', sans-serif;
      font-size: 16px;
      color: rgba(255,255,255,0.72);
      line-height: 1.7;
      margin-bottom: 36px;
      max-width: 520px;
    }
    .ind-hero-cta-row {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }
    .btn-ind-primary {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--ind-accent);
      color: var(--ind-dark);
      font-family: 'Poppins', sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 15px 32px;
      border-radius: 6px;
      text-decoration: none;
      transition: transform 0.2s, box-shadow 0.2s, background 0.2s;
    }
    .btn-ind-primary:hover {
      transform: translateY(-2px);
      background: #e5ac12;
      box-shadow: 0 8px 24px rgba(201, 150, 10, 0.35);
    }
    .btn-ind-secondary {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.15);
      color: #fff;
      font-family: 'Poppins', sans-serif;
      font-size: 13.5px;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 15px 28px;
      border-radius: 6px;
      text-decoration: none;
      transition: background 0.2s, border-color 0.2s;
    }
    .btn-ind-secondary:hover {
      background: rgba(255,255,255,0.12);
      border-color: rgba(255,255,255,0.3);
    }

    /* Hero stats */
    .ind-hero-stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1px;
      background: rgba(255,255,255,0.08);
      border-radius: 12px;
      overflow: hidden;
      margin-top: 48px;
    }
    .ind-stat {
      background: rgba(255,255,255,0.03);
      padding: 20px 16px;
      text-align: center;
    }
    .ind-stat-num {
      font-family: 'Sora', sans-serif;
      font-size: 26px;
      font-weight: 800;
      color: var(--ind-accent);
    }
    .ind-stat-label {
      font-family: 'Poppins', sans-serif;
      font-size: 11px;
      color: rgba(255,255,255,0.55);
      margin-top: 4px;
      letter-spacing: 0.05em;
    }

    /* Hero right — problem card */
    .ind-problem-card {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 16px;
      padding: 36px;
      backdrop-filter: blur(16px);
      box-shadow: 0 20px 50px rgba(0,0,0,0.15);
    }
    .ind-problem-label {
      font-family: 'Poppins', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #f87171;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .ind-problem-title {
      font-family: 'Sora', sans-serif;
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 20px;
      line-height: 1.35;
    }
    .ind-problem-list {
      list-style: none;
    }
    .ind-problem-list li {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-family: 'Poppins', sans-serif;
      font-size: 13.5px;
      color: rgba(255,255,255,0.72);
      padding: 10px 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      line-height: 1.5;
    }
    .ind-problem-list li:last-child { border-bottom: none; }
    .ind-problem-list li::before {
      content: '!';
      flex-shrink: 0;
      width: 18px;
      height: 18px;
      background: rgba(248,113,113,0.15);
      border: 1px solid rgba(248,113,113,0.3);
      color: #f87171;
      border-radius: 50%;
      font-size: 10px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 2px;
    }

    /* ── OVERVIEW ── */
    .ind-overview {
      padding: 100px 60px;
      background: var(--ind-white);
      border-bottom: 1px solid var(--ind-border);
    }
    .ind-overview-inner {
      max-width: 900px;
      margin: 0 auto;
      text-align: center;
    }
    .ind-section-label {
      font-family: 'Poppins', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--ind-accent);
      margin-bottom: 12px;
    }
    .ind-section-title {
      font-family: 'Sora', sans-serif;
      font-size: clamp(28px, 3.5vw, 36px);
      font-weight: 800;
      color: var(--ind-primary);
      line-height: 1.25;
      margin-bottom: 24px;
      letter-spacing: -0.02em;
    }
    .ind-overview-text {
      font-family: 'Poppins', sans-serif;
      font-size: 16px;
      color: var(--muted);
      line-height: 1.8;
    }

    /* ── CHALLENGES SECTION ── */
    .ind-challenges-sec {
      padding: 100px 60px;
      background: var(--ind-light);
    }
    .ind-challenges-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-challenges-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }
    .ind-challenge-card {
      background: var(--ind-white);
      border: 1px solid var(--ind-border);
      border-radius: 12px;
      padding: 32px;
      box-shadow: var(--ind-shadow);
      transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
    }
    .ind-challenge-card:hover {
      transform: translateY(-6px);
      border-color: rgba(201, 150, 10, 0.4);
      box-shadow: 0 20px 40px rgba(10, 61, 44, 0.08);
    }
    .ind-challenge-icon {
      font-size: 32px;
      margin-bottom: 20px;
      display: inline-block;
    }
    .ind-challenge-card-title {
      font-family: 'Sora', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: var(--ind-primary);
      margin-bottom: 12px;
    }
    .ind-challenge-card-desc {
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      color: var(--muted);
      line-height: 1.6;
    }

    /* ── SOLUTIONS SECTION ── */
    .ind-solutions-sec {
      padding: 100px 60px;
      background: var(--ind-white);
    }
    .ind-solutions-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-solutions-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
      margin-top: 50px;
      align-items: start;
    }
    .ind-mapping-box {
      background: var(--ind-light);
      border: 1px solid var(--ind-border);
      border-radius: 16px;
      padding: 40px;
      box-shadow: var(--ind-shadow);
    }
    .ind-mapping-title {
      font-family: 'Sora', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: var(--ind-primary);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ind-mapping-table {
      width: 100%;
      border-collapse: collapse;
      font-family: 'Poppins', sans-serif;
      font-size: 14.5px;
    }
    .ind-mapping-table th, .ind-mapping-table td {
      padding: 16px 20px;
      text-align: left;
      border-bottom: 1px solid var(--ind-border);
    }
    .ind-mapping-table th {
      font-weight: 700;
      color: var(--ind-primary);
      background: rgba(10, 61, 44, 0.04);
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 1px;
    }
    .ind-mapping-table td {
      color: var(--muted);
    }
    .ind-solutions-list {
      display: flex;
      flex-direction: column;
      gap: 24px;
    }
    .ind-solution-card {
      background: var(--ind-white);
      border: 1px solid var(--ind-border);
      border-radius: 16px;
      padding: 32px;
      box-shadow: var(--ind-shadow);
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .ind-solution-card:hover {
      transform: translateX(6px);
      box-shadow: 0 15px 35px rgba(10, 61, 44, 0.08);
    }
    .ind-sol-title {
      font-family: 'Sora', sans-serif;
      font-size: 19px;
      font-weight: 700;
      color: var(--ind-primary);
      margin-bottom: 12px;
    }
    .ind-sol-desc {
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      color: var(--muted);
      line-height: 1.6;
      margin-bottom: 20px;
    }
    .ind-sol-benefits {
      background: var(--ind-light);
      border-left: 3px solid var(--ind-accent);
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      font-family: 'Poppins', sans-serif;
      font-size: 12px;
      color: var(--ind-primary);
      font-weight: 600;
      margin-bottom: 24px;
      letter-spacing: 0.02em;
    }
    .btn-sol-link {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 24px;
      background: var(--ind-primary);
      color: #fff;
      font-family: 'Poppins', sans-serif;
      font-size: 13px;
      font-weight: 600;
      border-radius: 6px;
      text-decoration: none;
      transition: background 0.2s;
    }
    .btn-sol-link:hover {
      background: var(--ind-dark);
    }

    /* ── WHY CHOOSE RAJVI ── */
    .ind-why-sec {
      padding: 100px 60px;
      background: var(--ind-light);
    }
    .ind-why-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-why-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      margin-top: 48px;
    }
    .ind-why-card {
      background: var(--ind-white);
      border: 1px solid var(--ind-border);
      border-radius: 12px;
      padding: 30px;
      text-align: center;
      box-shadow: var(--ind-shadow);
      transition: transform 0.3s;
    }
    .ind-why-card:hover {
      transform: translateY(-4px);
    }
    .ind-why-icon-wrap {
      width: 60px;
      height: 60px;
      background: rgba(10, 61, 44, 0.05);
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      margin-bottom: 16px;
      color: var(--ind-primary);
    }
    .ind-why-title {
      font-family: 'Sora', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--ind-primary);
    }

    /* ── PACKAGING PROCESS ── */
    .ind-process-sec {
      padding: 100px 60px;
      background: var(--ind-white);
    }
    .ind-process-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-process-flow {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 20px;
      margin-top: 60px;
    }
    .ind-process-step {
      text-align: center;
      position: relative;
      background: var(--ind-light);
      padding: 36px 24px;
      border-radius: 12px;
      border: 1px solid var(--ind-border);
      box-shadow: var(--ind-shadow);
    }
    .ind-step-num {
      width: 40px;
      height: 40px;
      background: var(--ind-primary);
      color: #fff;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Sora', sans-serif;
      font-size: 15px;
      font-weight: 700;
      margin-bottom: 18px;
      box-shadow: 0 4px 10px rgba(10, 61, 44, 0.2);
    }
    .ind-process-step::after {
      content: '→';
      position: absolute;
      right: -15px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 20px;
      color: var(--ind-accent);
      z-index: 2;
    }
    .ind-process-step:last-child::after {
      display: none;
    }
    .ind-step-title {
      font-family: 'Sora', sans-serif;
      font-size: 14.5px;
      font-weight: 700;
      color: var(--ind-primary);
    }

    /* ── APPLICATIONS & SEGMENTS ── */
    .ind-apps-sec {
      padding: 100px 60px;
      background: var(--ind-light);
    }
    .ind-apps-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-apps-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 16px;
      margin-top: 40px;
    }
    .ind-app-card {
      background: var(--ind-white);
      border: 1px solid var(--ind-border);
      border-radius: 100px;
      padding: 14px 28px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: var(--ind-shadow);
      transition: transform 0.25s, border-color 0.25s;
    }
    .ind-app-card:hover {
      transform: scale(1.05);
      border-color: var(--ind-accent);
    }
    .ind-app-icon { font-size: 20px; }
    .ind-app-title {
      font-family: 'Poppins', sans-serif;
      font-size: 14.5px;
      font-weight: 600;
      color: var(--ind-primary);
    }

    .ind-segments-sec {
      padding: 100px 60px;
      background: var(--ind-white);
    }
    .ind-segments-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-segments-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 40px;
    }
    .ind-segment-item {
      background: var(--ind-light);
      border: 1px solid var(--ind-border);
      border-radius: 12px;
      padding: 24px;
      text-align: center;
      font-family: 'Poppins', sans-serif;
      font-size: 14.5px;
      font-weight: 600;
      color: var(--ind-primary);
      box-shadow: var(--ind-shadow);
      transition: background 0.2s, color 0.2s;
    }
    .ind-segment-item:hover {
      background: var(--ind-primary);
      color: #fff;
    }

    /* ── SUCCESS METRICS ── */
    .ind-metrics-sec {
      padding: 80px 60px;
      background: var(--ind-primary);
      color: #fff;
    }
    .ind-metrics-inner {
      max-width: var(--max-w);
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 40px;
      text-align: center;
    }
    .ind-metric-num {
      font-family: 'Sora', sans-serif;
      font-size: 44px;
      font-weight: 800;
      color: var(--ind-accent);
      margin-bottom: 8px;
    }
    .ind-metric-label {
      font-family: 'Poppins', sans-serif;
      font-size: 13.5px;
      color: rgba(255,255,255,0.72);
      letter-spacing: 0.05em;
    }

    /* ── FEATURED PRODUCTS ── */
    .ind-featured-sec {
      padding: 100px 60px;
      background: var(--ind-white);
    }
    .ind-featured-inner {
      max-width: var(--max-w);
      margin: 0 auto;
    }
    .ind-featured-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      margin-top: 48px;
    }
    .ind-featured-card {
      background: var(--ind-light);
      border: 1px solid var(--ind-border);
      border-radius: 12px;
      padding: 30px;
      text-align: center;
      display: flex;
      flex-direction: column;
      height: 100%;
      box-shadow: var(--ind-shadow);
    }
    .ind-featured-card h4 {
      font-family: 'Sora', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: var(--ind-primary);
      margin-bottom: 24px;
    }
    .btn-featured-link {
      margin-top: auto;
      display: block;
      padding: 12px;
      border: 1.5px solid var(--ind-primary);
      color: var(--ind-primary);
      text-decoration: none;
      font-family: 'Poppins', sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      border-radius: 6px;
      transition: background 0.2s, color 0.2s;
    }
    .btn-featured-link:hover {
      background: var(--ind-primary);
      color: #fff;
    }

    /* ── FAQs ── */
    .ind-faq-sec {
      padding: 100px 60px;
      background: var(--ind-light);
    }
    .ind-faq-inner {
      max-width: 800px;
      margin: 0 auto;
    }
    .faq-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 40px;
    }
    .faq-item {
      background: var(--ind-white);
      border: 1px solid var(--ind-border);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: var(--ind-shadow);
    }
    .faq-trigger {
      width: 100%;
      background: none;
      border: none;
      padding: 22px 28px;
      text-align: left;
      font-family: 'Sora', sans-serif;
      font-size: 16px;
      font-weight: 600;
      color: var(--ind-primary);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .faq-content {
      padding: 0 28px 24px;
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      color: var(--muted);
      line-height: 1.6;
      display: none;
    }
    .faq-item.active .faq-content { display: block; }
    .faq-item.active .faq-icon { transform: rotate(45deg); color: var(--muted); }
    .faq-icon { transition: transform 0.2s; font-size: 18px; color: var(--ind-accent); font-weight: 700; }

    /* ── INQUIRY SECTION ── */
    .ind-inquiry-sec {
      padding: 100px 60px;
      background: linear-gradient(135deg, var(--ind-dark) 0%, var(--ind-primary) 100%);
      color: #fff;
    }
    .ind-inquiry-inner {
      max-width: 1100px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 80px;
      align-items: start;
    }
    .ind-inquiry-left h2 {
      font-family: 'Sora', sans-serif;
      font-size: clamp(28px, 3.5vw, 42px);
      font-weight: 800;
      margin-bottom: 24px;
      letter-spacing: -0.02em;
    }
    .ind-inquiry-left p {
      font-family: 'Poppins', sans-serif;
      font-size: 15.5px;
      color: rgba(255,255,255,0.72);
      line-height: 1.7;
    }
    .ind-form-card {
      background: var(--ind-white);
      border-radius: 16px;
      padding: 40px;
      box-shadow: 0 30px 60px rgba(0,0,0,0.25);
    }
    .ind-form-card h3 {
      font-family: 'Sora', sans-serif;
      font-size: 22px;
      font-weight: 700;
      color: var(--ind-primary);
      margin-bottom: 24px;
      letter-spacing: -0.01em;
    }
    .ind-form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 18px;
    }
    .ind-form-group label {
      font-family: 'Poppins', sans-serif;
      font-size: 11px;
      font-weight: 700;
      color: var(--muted);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .ind-form-group input,
    .ind-form-group select,
    .ind-form-group textarea {
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      color: var(--text);
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      padding: 14px 16px;
      background: #f8fafc;
      outline: none;
      transition: border-color 0.2s;
    }
    .ind-form-group input:focus,
    .ind-form-group select:focus,
    .ind-form-group textarea:focus {
      border-color: var(--ind-accent);
      background: #fff;
    }
    .ind-form-group textarea {
      resize: vertical;
      min-height: 100px;
    }
    .ind-submit-btn {
      width: 100%;
      padding: 16px;
      background: var(--ind-primary);
      color: #fff;
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.2s, transform 0.2s;
    }
    .ind-submit-btn:hover {
      background: var(--ind-dark);
      transform: translateY(-1px);
    }

    /* ── FOOTER CTA ── */
    .ind-footer-cta {
      background: var(--ind-light);
      padding: 80px 60px;
      text-align: center;
      border-top: 1px solid var(--ind-border);
    }
    .ind-footer-cta-inner {
      max-width: 600px;
      margin: 0 auto;
    }
    .ind-footer-cta-title {
      font-family: 'Sora', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: var(--ind-primary);
      margin-bottom: 28px;
      letter-spacing: -0.01em;
    }
    .ind-footer-cta-btns {
      display: flex;
      justify-content: center;
      gap: 16px;
    }
    .btn-footer-primary {
      display: inline-flex;
      align-items: center;
      background: var(--ind-primary);
      color: #fff;
      border: 1.5px solid var(--ind-primary);
      padding: 14px 28px;
      border-radius: 6px;
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      font-weight: 700;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: background 0.2s, border-color 0.2s, transform 0.2s, box-shadow 0.2s;
    }
    .btn-footer-primary:hover {
      background: var(--ind-dark);
      border-color: var(--ind-dark);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(10, 61, 44, 0.15);
    }
    .btn-footer-secondary {
      display: inline-flex;
      align-items: center;
      background: transparent;
      color: var(--ind-primary);
      border: 1.5px solid var(--ind-primary);
      padding: 14px 28px;
      border-radius: 6px;
      font-family: 'Poppins', sans-serif;
      font-size: 14px;
      font-weight: 700;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: background 0.2s, color 0.2s, transform 0.2s;
    }
    .btn-footer-secondary:hover {
      background: var(--ind-primary);
      color: #fff;
      transform: translateY(-2px);
    }

    @media (max-width: 900px) {
      .ind-hero-inner, .ind-inquiry-inner, .ind-solutions-split { grid-template-columns: 1fr; gap: 40px; }
      .ind-hero { padding: 100px 24px 60px; }
      .ind-overview, .ind-challenges-sec, .ind-solutions-sec, .ind-why-sec, .ind-process-sec, .ind-apps-sec, .ind-segments-sec, .ind-metrics-sec, .ind-featured-sec, .ind-faq-sec, .ind-inquiry-sec { padding: 60px 24px; }
      .ind-challenges-grid, .ind-why-grid, .ind-process-flow, .ind-segments-grid, .ind-featured-grid { grid-template-columns: 1fr; }
      .ind-metrics-inner { grid-template-columns: 1fr 1fr; gap: 24px; }
      .ind-process-step::after { content: '↓'; right: auto; left: 50%; top: auto; bottom: -20px; transform: translateX(-50%); }
    }
  </style>
</head>
<body>
  <!-- NAV -->
  <div class="inner-page-header">
    <div class="inner-page-header-left">
      <a class="logo" href="../../">
        <img src="../../images/logo.png" alt="Rajvi Packaging" class="logo-img" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div class="logo-fallback" style="display:none">
          <div class="logo-box"></div>
          <div><div class="logo-text">Rajvi Packaging</div><div class="logo-sub">Design &middot; Protection &middot; Solutions</div></div>
        </div>
      </a>
    </div>
    <nav class="inner-page-header-nav">
      <a href="../../about/">About Us</a>
      <a href="../../products/">Products</a>
      <a href="../../solutions/">Solutions</a>
      <a href="../../blogs/">Blogs</a>
      <a href="../../contact/" class="inner-nav-cta">Contact Us</a>
    </nav>
  </div>

  <main>
    <!-- 1. HERO SECTION -->
    <section class="ind-hero">
      <div class="ind-hero-grid"></div>
      <div class="ind-hero-inner">
        <div>
          <div class="ind-hero-badge">{badge} Industry</div>
          <h1 class="ind-hero-title">{hero_title}</h1>
          <p class="ind-hero-subtitle">{hero_sub}</p>
          <div class="ind-hero-cta-row">
            <a href="#inquiry" class="btn-ind-primary">{hero_cta}</a>
            <a href="{hero_product_link}" class="btn-ind-secondary">{hero_product_text}</a>
          </div>
          <div class="ind-hero-stats">
            <div class="ind-stat"><div class="ind-stat-num">{stat1_num}</div><div class="ind-stat-label">{stat1_label}</div></div>
            <div class="ind-stat"><div class="ind-stat-num">{stat2_num}</div><div class="ind-stat-label">{stat2_label}</div></div>
            <div class="ind-stat"><div class="ind-stat-num">{stat3_num}</div><div class="ind-stat-label">{stat3_label}</div></div>
          </div>
        </div>
        <div>
          <div class="ind-problem-card">
            <div class="ind-problem-label">⚠ Industry Pain Points</div>
            <div class="ind-problem-title">{problem_title}</div>
            <ul class="ind-problem-list">
              {problems_list}
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. INDUSTRY OVERVIEW -->
    <section class="ind-overview">
      <div class="ind-overview-inner">
        <div class="ind-section-label">Industry Overview</div>
        <h2 class="ind-section-title">Protective Packaging for {badge}</h2>
        <p class="ind-overview-text">{overview}</p>
      </div>
    </section>

    <!-- 3. INDUSTRY CHALLENGES -->
    <section class="ind-challenges-sec">
      <div class="ind-challenges-inner">
        <div style="text-align:center; margin-bottom: 40px;">
          <div class="ind-section-label">Challenges</div>
          <h2 class="ind-section-title">Key Transport &amp; Storage Hazards</h2>
        </div>
        <div class="ind-challenges-grid">
          {challenges_grid}
        </div>
      </div>
    </section>

    <!-- 4. RAJVI PACKAGING SOLUTIONS -->
    <section class="ind-solutions-sec">
      <div class="ind-solutions-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Solutions</div>
          <h2 class="ind-section-title">Mapped to Customer Needs</h2>
        </div>
        
        <div class="ind-solutions-split">
          <div class="ind-mapping-box">
            <div class="ind-mapping-title">Challenge vs. Product Fitment Matrix</div>
            <table class="ind-mapping-table">
              <thead>
                <tr>
                  <th>Customer Challenge</th>
                  <th>Recommended Rajvi Product</th>
                </tr>
              </thead>
              <tbody>
                {mapping_table_rows}
              </tbody>
            </table>
          </div>
          <div class="ind-solutions-list">
            {solutions_cards_grid}
          </div>
        </div>
      </div>
    </section>

    <!-- 5. WHY CHOOSE RAJVI -->
    <section class="ind-why-sec">
      <div class="ind-why-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Why Us</div>
          <h2 class="ind-section-title">Value Propositions for {badge} Clients</h2>
        </div>
        <div class="ind-why-grid">
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">📐</div>
            <div class="ind-why-title">Custom Design</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">🏭</div>
            <div class="ind-why-title">High Volume</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">✂</div>
            <div class="ind-why-title">Precision Cutting</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">✓</div>
            <div class="ind-why-title">Consistent Quality</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">🚚</div>
            <div class="ind-why-title">Fast Delivery</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">💵</div>
            <div class="ind-why-title">Cost Effective</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">🎓</div>
            <div class="ind-why-title">Expertise</div>
          </div>
          <div class="ind-why-card">
            <div class="ind-why-icon-wrap">🗺</div>
            <div class="ind-why-title">Pan India Supply</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. PACKAGING PROCESS -->
    <section class="ind-process-sec">
      <div class="ind-process-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Engagement Flow</div>
          <h2 class="ind-section-title">Our Packaging Development Process</h2>
        </div>
        <div class="ind-process-flow">
          <div class="ind-process-step">
            <div class="ind-step-num">01</div>
            <div class="ind-step-title">Requirement Discussion</div>
          </div>
          <div class="ind-process-step">
            <div class="ind-step-num">02</div>
            <div class="ind-step-title">Packaging Design</div>
          </div>
          <div class="ind-process-step">
            <div class="ind-step-num">03</div>
            <div class="ind-step-title">Prototype / Sample</div>
          </div>
          <div class="ind-process-step">
            <div class="ind-step-num">04</div>
            <div class="ind-step-title">Manufacturing</div>
          </div>
          <div class="ind-process-step">
            <div class="ind-step-num">05</div>
            <div class="ind-step-title">Delivery</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. APPLICATIONS -->
    <section class="ind-apps-sec">
      <div class="ind-apps-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Applications</div>
          <h2 class="ind-section-title">Where Our Packaging is Used</h2>
        </div>
        <div class="ind-apps-grid">
          {apps_grid}
        </div>
      </div>
    </section>

    <!-- 8. INDUSTRIES WE SUPPORT (SEGMENTS) -->
    <section class="ind-segments-sec">
      <div class="ind-segments-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Sub-segments</div>
          <h2 class="ind-section-title">{badge} Segments We Support</h2>
        </div>
        <div class="ind-segments-grid">
          {segments_grid}
        </div>
      </div>
    </section>

    <!-- 9. SUCCESS METRICS -->
    <section class="ind-metrics-sec">
      <div class="ind-metrics-inner">
        {metrics_grid}
      </div>
    </section>

    <!-- 10. FEATURED PRODUCTS -->
    <section class="ind-featured-sec">
      <div class="ind-featured-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Portfolio</div>
          <h2 class="ind-section-title">Featured Packaging Categories</h2>
        </div>
        <div class="ind-featured-grid">
          <div class="ind-featured-card">
            <h4>EPE Foam</h4>
            <a href="../../product-epe/" class="btn-featured-link">View Product Page</a>
          </div>
          <div class="ind-featured-card">
            <h4>Bubble Wrap</h4>
            <a href="../../product-bubble/" class="btn-featured-link">View Product Page</a>
          </div>
          <div class="ind-featured-card">
            <h4>Foam Gaskets</h4>
            <a href="../../product-gaskets/" class="btn-featured-link">View Product Page</a>
          </div>
          <div class="ind-featured-card">
            <h4>PP Sheets &amp; Boxes</h4>
            <a href="../../product-pp/" class="btn-featured-link">View Product Page</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 11. FAQs ACCORDION -->
    <section class="ind-faq-sec">
      <div class="ind-faq-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Common Inquiries</div>
          <h2 class="ind-section-title">Frequently Asked Questions</h2>
        </div>
        <div class="faq-grid">
          {faqs_accordion}
        </div>
      </div>
    </section>

    <!-- 12. RELATED RESOURCES -->
    <section class="ind-faq-sec" style="background:var(--ind-white);">
      <div class="ind-faq-inner">
        <div style="text-align:center;">
          <div class="ind-section-label">Knowledge</div>
          <h2 class="ind-section-title">Related Resources &amp; Guides</h2>
        </div>
        <div class="faq-grid">
          {resources_grid}
        </div>
      </div>
    </section>

    <!-- 13. INQUIRY FORM -->
    <section class="ind-inquiry-sec" id="inquiry">
      <div class="ind-inquiry-inner">
        <div class="ind-inquiry-left">
          <div class="ind-section-label" style="color:var(--ind-accent);">Let's Discuss Your Packaging Requirements</div>
          <h2>{form_title}</h2>
          <p>{form_desc}</p>
          <div style="margin-top: 30px; display:flex; flex-direction:column; gap: 14px;">
            <div style="display:flex; align-items:center; gap: 12px;">
              <span style="color:var(--ind-accent);">✓</span> <span>{trust1}</span>
            </div>
            <div style="display:flex; align-items:center; gap: 12px;">
              <span style="color:var(--ind-accent);">✓</span> <span>{trust2}</span>
            </div>
            <div style="display:flex; align-items:center; gap: 12px;">
              <span style="color:var(--ind-accent);">✓</span> <span>{trust3}</span>
            </div>
            <div style="display:flex; align-items:center; gap: 12px;">
              <span style="color:var(--ind-accent);">✓</span> <span>{trust4}</span>
            </div>
            <div style="display:flex; align-items:center; gap: 12px;">
              <span style="color:var(--ind-accent);">✓</span> <span>{trust5}</span>
            </div>
          </div>
        </div>
        <div class="ind-form-card">
          <h3>Request Custom Solutions</h3>
          <form id="{name}-inquiry-form" onsubmit="handleIndFormSubmit(event, '{form_industry}')">
            <div class="ind-form-group">
              <label for="{name}-company">Company Name *</label>
              <input type="text" id="{name}-company" name="company" placeholder="Your Company" required>
            </div>
            <div class="ind-form-group">
              <label for="{name}-name">Contact Person *</label>
              <input type="text" id="{name}-name" name="name" placeholder="Your Name" required>
            </div>
            <div class="ind-form-group">
              <label for="{name}-email">Email Address *</label>
              <input type="email" id="{name}-email" name="email" placeholder="your@email.com" required>
            </div>
            <div class="ind-form-group">
              <label for="{name}-phone">Mobile Number *</label>
              <input type="tel" id="{name}-phone" name="phone" placeholder="91 XXXXX XXXXX" required>
            </div>
            <div class="ind-form-group">
              <label for="{name}-category">Product Category *</label>
              <select id="{name}-category" name="category" required>
                <option value="{inquiry_category}">{inquiry_category}</option>
                <option value="Air Bubble">Air Bubble Sheets/Wrap</option>
                <option value="Foam & Buffers">EPE &amp; PU Foam</option>
                <option value="Foam Gaskets">Foam Gaskets &amp; Tape</option>
                <option value="PP Boxes & Sheets">PP Corrugated Boxes &amp; Sheets</option>
                <option value="FLC Pallet Covers">FLC Pallet Covers</option>
              </select>
            </div>
            <div class="ind-form-group">
              <label for="{name}-requirement">Monthly Requirement *</label>
              <select id="{name}-requirement" name="requirement" required>
                <option value="">Select volume range</option>
                <option value="Trial Run">Less than 500 units</option>
                <option value="Standard">500 to 2,000 units</option>
                <option value="High Volume">2,000 to 10,000 units</option>
                <option value="Wholesale">10,000+ units</option>
              </select>
            </div>
            <div class="ind-form-group">
              <label for="{name}-message">Message / Specifications</label>
              <textarea id="{name}-message" name="message" placeholder="Describe sizes, shapes, density guidelines, or custom specifications..."></textarea>
            </div>
            <button type="submit" class="ind-submit-btn">Get Custom Packaging Solutions →</button>
          </form>
        </div>
      </div>
    </section>

    <!-- 14. FOOTER CTA -->
    <section class="ind-footer-cta">
      <div class="ind-footer-cta-inner">
        <h3 class="ind-footer-cta-title">Looking for reliable packaging solutions for your business?</h3>
        <div class="ind-footer-cta-btns">
          <a href="#inquiry" class="btn-footer-primary">Request Quote</a>
          <a href="tel:+919274841995" class="btn-footer-secondary">Call Our Team</a>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-v2-top">
      <div class="footer-v2-brand">
        <img src="../../images/logow.png" alt="Rajvi Packaging" class="footer-logo-img" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div class="footer-logo-fallback" style="display:none">
          <div class="footer-brand-box"></div>
          <div><div class="footer-brand-name">Rajvi Packaging</div><div class="footer-brand-sub">Design &middot; Protection &middot; Solutions</div></div>
        </div>
        <div class="footer-v2-divider"></div>
        <p class="footer-v2-desc">Custom packaging solutions designed around your product requirements, industry needs and protection goals.</p>
      </div>
      <div class="footer-v2-col">
        <div class="footer-v2-col-line"></div>
        <div class="footer-v2-col-title">Explore</div>
        <nav class="footer-v2-links">
          <a href="../../about/">About Us</a>
          <a href="../../products/">Products</a>
          <a href="../../solutions/">Solutions</a>
          <a href="../../blogs/">Blogs</a>
          <a href="../../contact/">Contact Us</a>
        </nav>
      </div>
      <div class="footer-v2-col">
        <div class="footer-v2-col-line"></div>
        <div class="footer-v2-col-title">Products</div>
        <nav class="footer-v2-links">
          <a href="../../product-foam/">Foam &amp; Buffers</a>
          <a href="../../product-bubble/">Air Bubble</a>
          <a href="../../product-pp/">PP Boxes &amp; Crates</a>
          <a href="../../product-gaskets/">Foam Gaskets</a>
          <a href="../../products/">View All Products</a>
        </nav>
      </div>
      <div class="footer-v2-col">
        <div class="footer-v2-col-line"></div>
        <div class="footer-v2-col-title">Solutions</div>
        <nav class="footer-v2-links">
          <a href="../../solutions-design/">Design Solutions</a>
          <a href="../../solutions-packaging/">Packaging Solutions</a>
          <a href="../../solutions-manufacturing/">Manufacturing Solutions</a>
          <a href="../../contact/">Contact Us</a>
        </nav>
      </div>
    </div>
    <div class="footer-v2-contact-bar">
      <div class="footer-v2-contact-cell">
        <svg class="fv2-contact-icon-plain" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0118 0z" /><circle cx="12" cy="10" r="3" />
        </svg>
        <a href="https://maps.app.goo.gl/Af2QqwHoCBzcbe7a7" target="_blank" rel="noopener" class="footer-v2-address-link">Plot No. 5 &amp; 6, City Survey No. NA/750/5 &amp; NA/750/6, Pipariya Faliya, Near Nitin Castings Ltd and Aarth Industries, Village Karvad, Vapi 396195</a>
      </div>
      <div class="footer-v2-contact-cell footer-v2-contact-cell--border">
        <svg class="fv2-contact-icon-plain" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.67A2 2 0 012 1h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 8.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z" />
        </svg>
        <a href="tel:+919274841995">+91 92748 41995</a>
      </div>
      <div class="footer-v2-contact-cell footer-v2-contact-cell--border">
        <svg class="fv2-contact-icon-plain" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" /><polyline points="22,6 12,13 2,6" />
        </svg>
        <a href="mailto:info@rajvipackaging.com">info@rajvipackaging.com</a>
      </div>
    </div>
    <div class="footer-v2-bottom">
      <div class="footer-v2-copy">&copy; 2025 Rajvi Packaging. All rights reserved.</div>
      <div class="footer-v2-doms">
        Made by
        <a href="https://www.domsglobal.co/" target="_blank" rel="noopener" class="footer-doms-link">
          <canvas id="footer-logo-canvas" class="footer-doms-canvas" width="220" height="124" aria-label="Doms Global"></canvas>
        </a>
      </div>
      <div class="footer-v2-legal">
        <a href="../../privacy policy/">Privacy Policy</a>
        <span class="fv2-legal-sep">|</span>
        <a href="../../terms of use/">Terms of Use</a>
        <span class="fv2-legal-sep">|</span>
        <a href="../../sitemap/">Sitemap</a>
      </div>
    </div>
  </footer>

  <script>
    function handleIndFormSubmit(e, industry) {
      e.preventDefault();
      const btn = e.target.querySelector('.ind-submit-btn');
      btn.textContent = '✓ Submitted! We\\'ll be in touch shortly.';
      btn.style.background = 'linear-gradient(135deg, #22543d, #276749)';
      btn.disabled = true;
    }
    
    function toggleFaq(btn) {
      const item = btn.parentElement;
      item.classList.toggle('active');
      const isExpanded = item.classList.contains('active');
      btn.querySelector('.faq-icon').textContent = isExpanded ? '✕' : '+';
    }
  </script>
  <script src="../../shared.js"></script>
</body>
</html>
"""

# Compile and output the 12 industry funnels
for name, data in industries.items():
    if not data:
        continue
    print("Processing:", name)
    # Build list string for problems and titles dynamically
    problem_title = f"What's Threatening Your {data['badge']} Shipments?"
    problems_list = "\n".join([f"              <li>{c['desc']}</li>" for c in data["challenges"][:5]])
    
    # Build challenges grid
    challenges_grid = "\n".join([
        f"""          <div class="ind-challenge-card">
            <div class="ind-challenge-icon">{c['icon']}</div>
            <div class="ind-challenge-card-title">{c['title']}</div>
            <div class="ind-challenge-card-desc">{c['desc']}</div>
          </div>""" for c in data["challenges"]
    ])
    
    # Build mapping matrix table rows
    mapping_table_rows = "\n".join([
        f"""              <tr>
                <td><strong>{m['challenge']}</strong></td>
                <td>{m['product']}</td>
              </tr>""" for m in data["solutions_mapping"]
    ])
    
    # Build solutions cards
    solutions_cards_grid = "\n".join([
        f"""          <div class="ind-solution-card">
            <div class="ind-sol-body">
              <div class="ind-sol-title">{sc['title']}</div>
              <div class="ind-sol-desc">{sc['desc']}</div>
              <div class="ind-sol-benefits">🔑 Key Benefits: {sc['benefits']}</div>
              <a href="{sc['link']}" class="btn-sol-link">View Product Page</a>
            </div>
          </div>""" for sc in data["solutions_cards"]
    ])
    
    # Build apps grid
    apps_grid = "\n".join([
        f"""          <div class="ind-app-card">
            <div class="ind-app-icon">{a['icon']}</div>
            <div class="ind-app-title">{a['title']}</div>
          </div>""" for a in data["applications"]
    ])
    
    # Build segments grid
    segments_grid = "\n".join([
        f"""          <div class="ind-segment-item">{s}</div>""" for s in data["segments"]
    ])
    
    # Build metrics grid
    metrics_grid = "\n".join([
        f"""        <div>
          <div class="ind-metric-num">{m['num']}</div>
          <div class="ind-metric-label">{m['label']}</div>
        </div>""" for m in data["metrics"]
    ])
    
    # Build FAQs accordion
    faqs_accordion = "\n".join([
        f"""          <div class="faq-item">
            <button class="faq-trigger" onclick="toggleFaq(this)">
              <span>{f['q']}</span>
              <span class="faq-icon">+</span>
            </button>
            <div class="faq-content">
              {f['a']}
            </div>
          </div>""" for f in data["faqs"]
    ])
    
    # Build resources grid
    resources_grid = "\n".join([
        f"""          <div class="faq-item" style="border:none;">
            <div class="ind-resource-title">{r['title']}</div>
            <div class="ind-resource-desc">{r['desc']}</div>
            <a href="{r['link']}" class="btn-resource" style="color:var(--gold);">Read Resource →</a>
          </div>""" for r in data["resources"]
    ])
    
    # Fill in template
    filled_html = html_template
    filled_html = filled_html.replace("{title}", data["title"])
    filled_html = filled_html.replace("{description}", data["description"])
    filled_html = filled_html.replace("{primary_color}", data["colors"]["primary"])
    filled_html = filled_html.replace("{accent_color}", data["colors"]["accent"])
    filled_html = filled_html.replace("{dark_color}", data["colors"]["dark"])
    filled_html = filled_html.replace("{light_color}", data["colors"]["light"])
    filled_html = filled_html.replace("{accent_rgb}", data["colors"]["accent_rgb"])
    filled_html = filled_html.replace("{badge}", data["badge"])
    filled_html = filled_html.replace("{hero_title}", data["hero_title"])
    filled_html = filled_html.replace("{hero_sub}", data["hero_sub"])
    filled_html = filled_html.replace("{hero_cta}", data["hero_cta"])
    filled_html = filled_html.replace("{hero_product_link}", data["hero_product_link"])
    filled_html = filled_html.replace("{hero_product_text}", data["hero_product_text"])
    filled_html = filled_html.replace("{stat1_num}", data["stats"][0]["num"])
    filled_html = filled_html.replace("{stat1_label}", data["stats"][0]["label"])
    filled_html = filled_html.replace("{stat2_num}", data["stats"][1]["num"])
    filled_html = filled_html.replace("{stat2_label}", data["stats"][1]["label"])
    filled_html = filled_html.replace("{stat3_num}", data["stats"][2]["num"])
    filled_html = filled_html.replace("{stat3_label}", data["stats"][2]["label"])
    filled_html = filled_html.replace("{problem_title}", problem_title)
    filled_html = filled_html.replace("{problems_list}", problems_list)
    filled_html = filled_html.replace("{overview}", data["overview"])
    filled_html = filled_html.replace("{challenges_grid}", challenges_grid)
    filled_html = filled_html.replace("{mapping_table_rows}", mapping_table_rows)
    filled_html = filled_html.replace("{solutions_cards_grid}", solutions_cards_grid)
    filled_html = filled_html.replace("{apps_grid}", apps_grid)
    filled_html = filled_html.replace("{segments_grid}", segments_grid)
    filled_html = filled_html.replace("{metrics_grid}", metrics_grid)
    filled_html = filled_html.replace("{faqs_accordion}", faqs_accordion)
    filled_html = filled_html.replace("{resources_grid}", resources_grid)
    filled_html = filled_html.replace("{form_label}", data["form_label"])
    filled_html = filled_html.replace("{form_title}", data["form_title"])
    filled_html = filled_html.replace("{form_desc}", data["form_desc"])
    filled_html = filled_html.replace("{trust1}", data["form_trust"][0])
    filled_html = filled_html.replace("{trust2}", data["form_trust"][1])
    filled_html = filled_html.replace("{trust3}", data["form_trust"][2])
    filled_html = filled_html.replace("{trust4}", data["form_trust"][3])
    filled_html = filled_html.replace("{trust5}", data["form_trust"][4])
    filled_html = filled_html.replace("{name}", name)
    filled_html = filled_html.replace("{form_industry}", data["form_industry"])
    filled_html = filled_html.replace("{inquiry_category}", data["inquiry_category"])
    
    # Create directory and write out
    out_dir = f"/Users/sanjaykumar/Desktop/Code/rajvi packaging website 2/industry/{name}"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w") as f:
        f.write(filled_html)

print("Successfully generated all 12 B2B industry landing pages!")
