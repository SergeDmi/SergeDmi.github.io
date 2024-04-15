[//]: # ( __WEIGHT__ 1000 )
[//]: # ( __TITLE__ Projects )
## Ongoing projects  

### Pushing force by branched actin networks
Branched actin networks exert pushing forces in conditions in-vivo, wether in [yeast endocytosis](https://www.sciencedirect.com/science/article/pii/S0092867418308006), in lamelipodia, or in [podosomes in macrophages](https://www.nature.com/articles/s41467-022-30652-6).  Because actin nucleation-promoting factors locate at the plasma membrane, tt is widely believed that actin networks exert pushing forces by polymerizing at the membrane/actin interface. While for individual actin filaments, the force-distance relationship is well described by the [brownian ratchet](https://www.cell.com/biophysj/pdf/S0006-3495(93)81035-X.pdf) model, things are more complicated for complex actin networks, including because force generation [depend on filament orientation](https://pubmed.ncbi.nlm.nih.gov/27002174/).

We use simulations and elasticity theory to understand the force-velocity relationship in branched networks. Current results highlight that the growth speed of such networks depend on both filament stall force, and on the stress applied on the network, in a non-trivial manner. This project is spearheaded by [Magid Badaoui](https://www.ijm.fr/linstitut/annuaire/name/magid-badaoui/).

### Simulations of helical actin filaments
While actin filaments are often represented theoretically as semi-flexible filaments, they are actually helical filaments, that can be seen as helices of two protofilaments. This has important consequences, as the filament mechanical properties depend on their molecular architecture. Moreover, actin chirality can result in [chirality at the cell level](https://pubmed.ncbi.nlm.nih.gov/30467170/).
 
We implemented in the software platform [cytosim](https://gitlab.com/f-nedelec/cytosim) a helical actin filament, that is compatible with the wide variety of the functionalities of the simulations. We thus can simulate chiral mesoscopic assemblies of actin filaments. This work is spearheaded by [Amir Khosravanizadeh](https://www.ijm.fr/linstitut/annuaire/name/amir-khosravanizadeh/).

### Cytoplasm visco-elasticity and fluidization 
The cytoskeleton is a densely packed medium that behaves as an elastic medium at short times, and as a viscous fluid at longer times. In a [recent work](https://www.biorxiv.org/content/10.1101/2022.09.27.509722.abstract), we showed that, somewhat surprisingly, a simple linear 3-elements visco-elastic model (Jeffrey's model, a.k.a. standard linear liquid) adequately reprends the cytoplasm, even when moving large objects. For large objects, the finite size of the cell effectively increases the viscous and elastic moduli, because there is less space to accomodate velocity gradients than in an infinite medium. We were able to show that half of the viscous and elastic moduli of the cytoplasm is due to actin.

Now our goal is to understand how viscosity and elasticity emerge from the bulk actin, despite a seemingly low density (with Amir Khosravanizadeh, Javad Najafi, and Nicolas Minc).

### Contractile actin networks as active fluids
The active gel formalism is popular to model contractile actin networks, because of its simplicity and near-linearity. However, it is not obvious that a complex network of filaments, motors and crosslinkers actually behaves according to such simple equations. Moreover, the link between the microscopic parameters (motor and actin properties) and macroscopic parameters (visco-elastic moduli) is far from obvious.

We aim at finding regimes in which actin does behave as an active contractile fluid, the properties of which can be predicted by its components.

### Simulations of coupled actin-membrane mechanics

### Dimensionality reduction in theory and simulation
