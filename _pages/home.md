---
layout: splash
permalink: /
hidden: true
title: Computational Materials Science
header:
  overlay_filter: "0.1"
  overlay_image: /assets/images/splash.jpg
  actions:
    - label: "<i class='fas fa-book-reader'></i> &nbsp;Learn more"
      url: "/research/"
excerpt: >
  Understanding the fundamental structure and properties of materials toward discovery and new design.
intro: 
  - excerpt: 'We employ a variety of computational methods, including atomistic simulation based on _molecular dynamics_ and _Monte Carlo_ techniques, _density functional theory-_ (DFT) based electronic structure methods, and structure prediction techniques using _evolutionary algorithms_.<br />
  <br />
  Our goal is to discover and design new materials in the following aspects:'
feature_row:
  - image_path: /assets/images/mm-customizable-feature.png
    alt: "materials under extreme conditions"
    title: "Materials Under Extreme Conditions"
    excerpt: "Extended solids formed under ultrahigh pressure exhibit dramatic changes in their properties and may offer significant improvements over their original forms."
    url: "/research/materials-under-extreme-conditions/"
    btn_class: "btn--primary"
    btn_label: "Learn more" 
  - image_path: /assets/images/mm-responsive-feature.png
    alt: "organic crystal polymorphism"
    title: "Organic Crystal Polymorphism"
    excerpt: "Predicting the crystal structures for a given molecule could help determine the existence of different forms and suggest as yet unseen polymorphs of currently known structures."
    url: "/research/organic-crystal-polymorphism/"
    btn_class: "btn--success"
    btn_label: "Learn more"
  - image_path: /assets/images/mm-free-feature.png
    alt: "defects in materials"
    title: "Defects in High-Performance Materials"
    excerpt: "Understanding the structural and functional properties influenced by defects is key to optimizing next-gen materials needed for advanced energy applications."
    url: "/research/defects-in-materials/"
    btn_class: "btn--info"
    btn_label: "Learn more"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}
