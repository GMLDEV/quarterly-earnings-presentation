---
marp: true
size: 16:9
theme: product-docs
paginate: true
header: "Product Docs — © 2025"
footer: "Contact: 23f2005402@ds.study.iitm.ac.in"
---

<!-- theme: product-docs -->
<!-- paginate: true -->
<!-- header: "Product Docs — © 2025" -->
<!-- footer: "Contact: 23f2005402@ds.study.iitm.ac.in" -->
<!-- class: lead -->
<!-- style: "section.lead h1{font-size:2.2em}" -->

# Product Documentation

Maintainable documentation slides built with Marp.

- Version-controlled (Git)
- Export to HTML/PDF/PPTX
- Custom theme + styling
- Math support

---

![bg opacity:0.25](https://images.unsplash.com/photo-1529101091764-c3526daf38fe?q=80&w=1600&auto=format&fit=crop)

<!-- _class: invert -->
<!-- _color: #ffffff -->
<!-- style: "h1{color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.5)}" -->

# Beautiful Backgrounds

This slide demonstrates a background image using Marp's `![bg]` syntax with inverted text colors.

---

<!-- style: "h1{color:#0b69c7} ul{line-height:1.9}" -->

# Author & Contact

- Technical writer: You
- Email: 23f2005402@ds.study.iitm.ac.in
- Team: DevEx Docs

---

<!-- style: "table{width:100%} th,td{padding:.4rem .6rem}" -->

# Feature Matrix

| Feature | Status |
|---|---|
| Custom theme | ✅ |
| Page numbers | ✅ |
| Background image | ✅ |
| Marp directives | ✅ |
| Math | ✅ |

---

<!-- style: "pre,code{font-size:.9em}" -->

# Snippet (CLI)

```bash
# Convert to HTML
marp slides.md -o slides.html

# Convert to PDF (needs Chrome)
marp slides.md -o slides.pdf

# Convert to PPTX
marp slides.md -o slides.pptx
```

---

# Algorithmic Complexity

We can document complexity using LaTeX:

$$
T(n) = a\,T\!\left(\frac{n}{b}\right) + f(n) \;\Rightarrow\; T(n) = O(n\,\log n)
$$

And specific examples:

- Merge sort: $O(n \log n)$
- Binary search: $O(\log n)$
- Insertion sort (avg): $O(n^2)$

---

<!-- style: "blockquote{border-left:4px solid #0b69c7;padding-left:10px}" -->

# Notes

> Keep slides atomic. Store `slides.md` in Git for clear reviews and diffs.
> Use a custom theme for consistent branding across products.

---

# Thanks

Questions? Email: 23f2005402@ds.study.iitm.ac.in

Generated with Marp.
