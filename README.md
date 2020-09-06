# linguistic-processses-ld
Source files and resources for a project on evaluation of reference resolution.

Note that some further external dependencies are required in order to run the English and German systems, as the big tools had to be omitted to fit the project on GitHub. Both systems are designed for use in a Debian environment.

## For English

One needs to download a copy of the Stanford CoreNLP server following the instructions [here](https://stanfordnlp.github.io/CoreNLP/download.html). It should have a copy of the English pretrained models contained. This server needs to be located in a `./english/corenlp` folder to make the system work without code changes.

## For German

Firstly, `sfst` and its requirements need to be installed on the machine. After this, running the `./german/ParZu/install.sh` should download and configure all the relevant external tools and models for tagging and morphological analysis.
