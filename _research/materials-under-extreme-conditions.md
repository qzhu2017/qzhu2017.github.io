---
title: "Materials Under Extreme Conditions"
permalink: /research/materials-under-extreme-conditions/
gallery1:
  - url: /assets/images/materials-under-extreme-conditions/Cs-F.jpg
    image_path: /assets/images/materials-under-extreme-conditions/Cs-F.jpg
    title: "Variable compositional structure prediction applied Cs-F system yields an extremely rich chemistries with further oxidation of Cs+ and the stabilization of F3-, F42-, F5-."
gallery2:
  - url: /assets/images/materials-under-extreme-conditions/Si-Decompression.jpg
    image_path: /assets/images/materials-under-extreme-conditions/Si-Decompression.jpg
    title: "Decompression of Si-II yields a new form promising for solar cell applications."
---
# Introduction
Materials formed under ultrahigh pressure, known as extended solids, exhibit dramatic changes in physical, mechanical and functional properties and may offer significant improvements to the original forms. Given that the difficulty in materials high pressure syntheses and characterization, computer simulation is playing a major role. Our group is focusing on developing a heuristic strategy and several advanced methods to search for novel binary and compounds which are of either fundamental or industrial interests.

{% include figure image_path="/assets/images/materials-under-extreme-conditions/HP.jpg" caption="**Figure 1.** Schematics of the core of a diamond anvil cell. The culets (tip) of the two diamond anvils are typically 100–250 microns across." %}

# Thermodynamical Equilibrium and Stoichiometries
To determine the crystal structure for a material under high pressure is a big headache for high pressure experimentalists. Recently, the emerging computational crystal structure prediction techniques demonstrated that crystal structures can be reliably predicted, as long as the chemical position is known. Although quite successful, this fails to satisfy the needs for discovering new materials with unknown stoichiometries. Therefore, we developed a method including the variation of chemical composition to make it more applicable to explore the materials under extreme high pressure conditions. Our recent work has found that materials often exhibit unusual physical and chemical behaviors. Some "impossible" chemical compounds such as Na3Cl, NaCl3, Mg3O2, NaHe2, CsF3, CsF5 were found to become thermodynamically stable. We have also attempted to predict ternary systems such as Na-Au-Ga. It has been found that a number of brand new stable compositions have not been reported so far. This offers great opportunities to computationally explore the new materials with complex stoichiometries, thus provide the guidance for experiments.

{% include gallery id="gallery1" caption="**Figure 2.** Variable compositional structure prediction applied Cs-F system yields an extremely rich chemistries with further oxidation of Cs+ and the stabilization of F3-, F42-, F5- ([source](/assets/pdfs/CsF-2015-SR.pdf))." %}

{% include figure image_path="/assets/images/materials-under-extreme-conditions/NaGaAu.jpg" caption="**Figure 3.** Variable compositional structure prediction applied Na-Ga-Au system yields a number of stable compositions which haven't been reported in the experiment." %}

# Metastability and Kinetics
Whenever the novel materials with superior properties (superhardness, superconductivity, ultrahigh thermal conductivity, .etc) are made under high pressure, the ultimate goal is to quench them back without losing these properties. Indeed, there exists a number of materials (e.g., diamond) can retain their high pressure forms upon the release of pressure. However, most of the materials might undergo phase transition to:

1. the equilibrium states (thermodynamically stable form);
2. the new nonequilibrium states (metastable form).

The possible divergent decompression pathway provides alternatives to make new materials, but requires a thorough understanding of the kinetic behavior. To address this challenge, we developed a so called Generalized Evolutionary Dynamics (GEM) to enable an automated scheme to systematically sample energy landscapes of crystalline solids, based on the ideas of metadynamics and evolutionary algorithms. We have applied this method to study several systems, including carbon, silicon, Al2SiO5, MgSiO3. In particular, we observed a low-energy metastable structure of Si(T32) which is likely to be a product of decompression on Si-II. T32 is calculated to have a quasidirect band gap of 1.28 eV, making it promising for photovoltaic applications.

{% include gallery id="gallery2" caption="**Figure 4.** Decompression of Si-II yields a new form promising for solar cell applications ([source](/assets/pdfs/GEM-2015-PRB.pdf))." %}
