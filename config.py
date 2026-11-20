# ============================================================
# Is file mein sirf apni organization ki maloomat badlein.
# Baqi poora project (chat page, bot) khud update ho jata hai.
# ============================================================

CONFIG = {
    # --- Organization (page ke header, footer aur contact section mein dikhta hai) ---
    "name": "Corvit Systems",
    "campus": "Rawalpindi Campus",
    "email": "rwp@corvit.com",
    "website": "www.corvit.com.pk",
    "phone": "051-4928004-5",
    "whatsapp": "0311-1444473",
    "address": "2nd Floor Zarwar Center, Opp Rabi Center, Muree Road, Rawalpindi",
    "hours_en": "9:00 AM to 9:00 PM",

    # Logo: agar static/logo.png (ya .webp/.jpg/.svg) rakhi hui hai to wo use hoti hai,
    # warna Corvit ki website se ye link.
    "logo_url": "https://corvit.com.pk/wp-content/uploads/2026/03/corvit-logo-png-copy-1024x478.webp",

    # --- Bot ke jawab dene ki jagah (in pages se bot seekhta hai) ---
    "crawl_urls": [
        "https://corvit.com.pk/rawalpindi/",
        "https://corvit.com.pk/rawalpindi-fees/",
        "https://corvit.com.pk/contact-us/",
        "https://corvit.com.pk/fees-structure/",
        "https://corvit.com.pk/about/",
        "https://corvit.com.pk/services/",
        "https://corvit.com.pk/course-category/web-development/",
        "https://corvit.com.pk/course-category/artificial-intelligence/",
        "https://corvit.com.pk/course-category/cloud-computing/",
        "https://corvit.com.pk/course-category/cyber-security/",
        "https://corvit.com.pk/course-category/network-administration/",
    ],

    # Aik page se doosre page ke darmiyan intezar (seconds), website par bojh na paray
    "crawl_delay": 1.5,
}
