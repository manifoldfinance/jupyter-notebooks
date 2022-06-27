# Jupyter Notebooks

## Attribution 

Contains notebooks from:

[https://github.com/flashbots/eth2-research](https://github.com/flashbots/eth2-research) <br />
[https://github.com/ethereum/rig](https://github.com/ethereum/rig) <br />


## Assessing the nature and impact of MEV in eth2.

### Starting up (locally)
Requirements: 
* python, pip, and [jupyter-notebook](https://jupyter.readthedocs.io/en/latest/install/notebook-classic.html)

Instructions:
* create a virtualenv: (optional)

    `python3 -m venv ~/venv`
* activate the virtualenv: (optional)

    `source ~/venv/bin/activate`
* install dependencies:

    `pip3 install -r binder/requirements.txt`
* open notebooks in a browser:

    `jupyter notebook`


### Notebooks

#### [Analysis of staking rewards with MEV](notebooks/mev-in-eth2/eth2-mev-calc.ipynb)
This analysis is executed alongside the post we've released on MEV in eth2. Thanks to Taarush Vemulapalli and Alejo Salles for their contributions, as well as Pintail for the original code this analysis is based on. We re-use the code from this article by Pintail, adding additional considerations for MEV rewards using Flashbots data as a proxy for it. The Flashbots data we use has been collected by running an MEV-Geth node, querying the public mev-blocks API and looking at data in the public dashboard of Flashbots activity.

Live: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/flashbots/eth2-research/HEAD?filepath=notebooks%2Fmev-in-eth2%2Feth2-mev-calc.ipynb)

### Articles
#### [MEV in eth2 - an early exploration](https://hackmd.io/@flashbots/ryuH4gn7d)
In this post, we study transaction ordering in eth2 and analyze MEV-enabled staking yields. We find that MEV will significantly boost validator rewards but may reinforce inequalities within participants of eth2. We also discuss qualitative aspects of MEV in eth2 such as the potential dynamics that will unfold between its largest stakeholders like exchanges and validator pools.

### Videos
* [MEV after The Merge with Nethermind and Flashbots](https://youtu.be/Hjd9WowOa3g) by Tomasz Stańczak & Alex Obadia (ETHGlobal Scaling Ethereum eth2 conference)
* [MEV on eth2](https://youtu.be/zsgC6mNP9eU) by Alex Obadia (ETHGlobal Scaling Ethereum Roast)
* [MEV after EIP-1559 and the Merge](https://youtu.be/XhZ2FDMdVUM) by Alejo Salles & Alex Obadia (EthCC 4)
* [The MEV in Nethermind in eth2](https://youtu.be/6MeKNSqC2es) by Tomasz Stańczak & Marcello Bardus (EthCC 4)


### Related Repos
- https://github.com/flashbots/raytracing

#### FRPs
- [FRP 11: MEV in eth2 exploration](https://github.com/flashbots/mev-research/blob/main/FRPs/FRP-11.md)
- [FRP 13: Flashbots in eth2](https://github.com/flashbots/mev-research/blob/main/FRPs/FRP-13.md)
- [FRP 14: Cryptoeconomic design exploration](https://github.com/flashbots/mev-research/blob/main/FRPs/FRP-14.md)

