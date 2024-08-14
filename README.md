# Thesis: Search for rare associated production of a Higgs boson and a single top quark in the two lepton plus one hadronic tau final state with the ATLAS detector

The discovery of a Higgs boson in 2012 opened a new field for exploration in the realm of particle physics. To better understand the Standard Model of particle physics, it is of prominent interest to study the Yukawa coupling of the Higgs boson to the top quark ($`y_{t}`$), the most massive fundamental particle and, consequently, the one with the largest coupling to the Higgs boson.

The direct measurement of $y_{t}$ at LHC is only possible via two associated Higgs productions: with a top-quark-antiquark pair ($`t\bar{t}H`$) and with a single-top quark ($tHq$). While the $t\bar{t}H$ just permits the determination of the magnitude of $`y_{t}`$, the only way of directly measuring its sign is through the $tHq$ production. This is due to the fact that the two leading order Feynman diagrams for the $tHq$ production interfere with each other depending on the $y_{t}$ sign. Current experimental constrains on $y_{t}$ favour the SM predictions, but an opposite sign with respect to the expectations of the SM is not completely excluded yet.

In this work, a search for the $tHq$ production is presented in a final state with two light-flavoured-charged leptons (electrons or muons) and one hadronically-decaying tau lepton (named $2\ell+\tau_{had}$ channel). This analysis uses an integrated luminosity of 140 fb$^{-1}$ of proton-proton collision data at centre-of-mass energy of 13 TeV collected by the ATLAS detector during LHC Run 2.  This search for the $tHq$ production in the $2\ell+\tau_{had}$ channel is an important contribution to the exploration of the Higgs-top quark Yukawa coupling and a step forward in the search for new physics beyond the SM.

This search is exceptionally challenging due to the extremely small cross-section of the $tHq$ process (70 fb), and of the $2\ell+\tau_{had}$ final-state channel, in particular, which only accounts for a 3.5\% of the total $tHq$ production. Therefore, the separation of the $tHq$ signal events from background events is done by means of machine-learning (ML) techniques using boosted-decision trees to define both signal and control regions to constrain the most important background processes, which are those related to top-quark-antiquark-pair production without and with an additional boson($t\bar{t}$, $t\bar{t}H$, $t\bar{t}W$ and $t\bar{t}Z$) and $Z$ boson plus jets.

Significant suppression of the background events with jets wrongly selected as leptons or non-prompt leptons originating from heavy-flavour decays is achieved by demanding electrons and muons to pass strict identification and isolation requirements. Simultaneously, hadronic $`\tau`$ leptons are demanded to pass the requirement of a recurrent-neural-network-based discriminator to reduce misidentifications from jets.

The reconstruction of the events is also enhanced by similar ML methods since in the scenario in which the light-flavour leptons have the same sign, a priori, it is not possible to determine which lepton is originated from the Higgs boson and which from the top quark.

Overall, the search for the $tHq$ production in the $2\ell+\tau_{had}$ channel is an important milestone in the exploration of the Higgs-top quark Yukawa coupling and the possible observation of an excess of signal events with respect to the SM prediction, would be an evidence of new physics in terms of CP-violating $y_{t}$ coupling. This analysis also demonstrates the power of ML techniques in high-energy physics, and paves the way for future analyses.

<!--
For corrections: The folder [TaggedVersions](https://gitlab.cern.ch/martinpa/Thesis/-/tree/master/TaggedVersions) contains different pdf versions of the thesis with the date in which they where uploaded and linenumbers.

To compile the thesis use :
 `pdflatex Thesis_main`
 `pdflatex Thesis_main`
 `bibtex Thesis_main` 


Structure and comments in the google doc [Tésis Pablo](https://docs.google.com/document/d/1T1lZr6PcvGLb45otwd3PxfvnDkrHU_tpNTIXtzvrZR4/edit?usp=sharing)


`thesis.py`: Script to modify thesis chapters to compile them individually or compile the entire thesis. It just comments or uncomments preambles in individual chapters.  Not really using this.

`source cleaner.sh `:  To clean unnecesary files
-->

