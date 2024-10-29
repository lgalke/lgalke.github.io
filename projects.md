---
title: Projects
---

## Interpretability of Language Models {#mc-interpretability}

*Since 2023*

Large language models have shown incredible results and experienced a rapid
widespread adoption. However, we do not know *how* the trained models come to
their decisions of what text to generate. Therefore, this project aims to
investigate the interpretability of language models through structural probing,
behavioral probing, and mechanistic interpretability -- and by bringing theories
and experimental paradigms from psycholinguistics into machine learning.

- Paper: What makes a language easy to deep-learn? (in final revision, to appear soon). [preprint](https://arxiv.org/abs/2302.12239) [code](https://github.com/lgalke/easy2deeplearn)
- Learning pressures in neural networks and large language models (in revision) [preprint](https://arxiv.org/abs/2403.14427)
- Paper: [Morphology Matters: Probing the Cross-linguistic Morphological Generalization Abilities of Large Language Models through a Wug Test](https://aclanthology.org/2024.cmcl-1.15/) published in the [CMCL workshop](https://cmclorg.github.io) at the [ACL 2024 conference](https://2024.aclweb.org).
- Poster at the [Highlights in the Language Sciences conference](https://hils2024.nl), July 8--11, 2024
- Poster at the workshop on [Using Artificial Neural Networks for Studying Human Language Learning and Processing](https://ann-humlang.github.io), June 10--12, 2024
- Extended abstract on Testing the Linguistic Niche Hypothesis in Large Language Models with a Multilingual Wug Test published in the [Proceedings of Evolang XV](https://pure.mpg.de/pubman/faces/ViewItemOverviewPage.jsp?itemId=item_3587960) (pp. 91--94)
- Podium presentation by Anh Dang at [Evolang 2024](https://evolang2024.github.io)
- Talk at the [Protolang 8 conference](https://sites.google.com/view/protolang8/home), Rome, September 27--28, 2023. Abstract published in the [Protolang 8 book of abstracts](https://drive.google.com/file/d/1rbBGo82zV4nCNgRiLeGXEJoR79wSGxpu/view)

## Machine Communication and the Emergence of Language {#mc-emecom}

*Since 2022*

Imagine you put artificial neural network agents into a box and give them a task
that can only be solved with communication. How do neural network agents learn
to communicate? What communication protocols emerge? What are the parallels to
human communication?

- Machine Communication and the Emergence of Language. Talk given at the MPI Proudly Presents series, July 4, 2024, [Max Planck Institute for Psycholinguistics](https://www.mpi.nl), Nijmegen, NL.
- Invited talk at the workshop on [Using Artificial Neural Networks for Studying Human Language Learning and Processing](https://ann-humlang.github.io), June 10--12, 2024
- [Machine Learning and the Evolution of Language workshop at the Joint Conference on Language Evolution](https://ml4evolang.github.io)
- [Emergent Communication workshop paper at ICLR](https://openreview.net/forum?id=rqUGZQ-0XZ5)



## What Matters for Text Classification (textclf) {#textclf}

*Since 2021*

Automatically categorizing text documents is a popular research topic with
numerous new approaches being published each year. However, do they really give
an advantage over earlier approaches? This question has triggered this line of
research and the answer we have is worrisome. For instance, many recently
proposed methods such as TextGCN are outperformed by a simple multilayer
perceptron on a bag-of-words representation -- a decade old technique enhanced
with today's best practices.

Even in the era of language models, the results on text classification are sometimes counter-intuitive.
As such, fine-tuned small models typically outperform large language models.

- [Simplifying hierarchical text classifciation](https://ebooks.iospress.nl/doi/10.3233/FAIA240661)
- [preprint of a comparative survey paper](https://arxiv.org/abs/2204.03954)
- [ACL 2022 paper](https://doi.org/10.18653/v1/2022.acl-long.279)
- [code for multi-label classification](https://github.com/drndr/multilabel-text-clf)
- [code for single-label classification](https://github.com/lgalke/text-clf-baselines)
- [extra code for single-label classification with different methods](https://github.com/FKarl/text-classification)


## Lifelong Graph Representation Learning (LGL) {#LGL}

*Since 2019*

Graph neural networks have quickly risen to be the standard technique for machine learning on graph-structured data.  Yet graph neural networks are usually only applied to static snapshots of graphs, while real-world graphs (social media, publication networks) are continually evolving.  Evolving graphs come with challenges that are rarely reflected in the graph representation learning literature, such as dealing with new classes in node classification.  We pursue a lifelong learning approach for graph neural networks on evolving graphs and investigate incremental training, out-of-distribution detection, and issues caused by an imbalanced class distribution.

- [CoLLAs 2024 conference paper on zero-shot learning in graphs](https://lifelong-ml.cc/Conferences/2024/acceptedpapersandvideos/conf-2024-38) or on [arXiv](https://arxiv.org/abs/2406.09926)
- [Code for CoLLAs 2024 paper](https://github.com/Bobowner/POWN)
- [IJCNN 2023 conference paper on new class detection in graphs](https://doi.org/10.1109/IJCNN54540.2023.10191071)
- [*Neural Networks* journal paper, 2023](https://pure.mpg.de/rest/items/item_3368482_4/component/file_3510107/content)
- [IJCNN 2021 conference paper](https://doi.org/10.1145/3197026.3197050)
- [ICLR 2019 workshop paper](https://rlgm.github.io/papers/21.pdf)
- [Code for 2023 *Neural Networks* paper](https://github.com/lgalke/lifelong-learning)
- [Code for IJCNN 2023 paper](https://github.com/Bobowner/Open-World-LGL)
- [Code for ICLR 2019 workshop paper](https://github.com/lgalke/gnn-pretraining-evaluation)
- related project: [Q-AKTIV](#q-aktiv)


## Analyzing the Scientific, Economic and Societal Impact of Research Activities and Research Networks (Q-AKTIV) {#q-aktiv}

*2019--2022, funded by the Federal Ministry of Education and Research (BMBF)*

The aim of Q-AKTIV is to improve the methods for forecasting dynamics and interactions between research, technology development, and innovation. The network analysis methods will be based on recent developments in Deep Learning. In addition to the emergence of new knowledge areas and networks, we focus on the convergence processes of established sectors. The development and evaluation of the new methods initially takes place in the field of life sciences, which is characterized by high marked dynamics. The additional application in economics enables a systematic comparison of the dynamics between the disciplines of science. The new methods will be used to predict the impact of existing research and network structures on the dynamics of knowledge and technologies as well as the future relevance of topics and actors. The result of Q-AKTIV is an implemented and evaluated instrument for the strategic analysis and prognosis of the dynamics in science and innovation. This complements today’s primarily qualitative approaches to early strategic planning and increases the decision-making ability of research institutions, policy makers, and industries. In addition to the analysis of dynamics, also valuable indicators for R & D performance measurement can be derived, e.g., the registration of patents based on scientific publications, the economic development of the companies involved, as well as the outreach of research activities. The practice partner brings in the necessary experience in the field of business valuation and strategy development and ensures a practical testing of the toolkit.

- [Scientometrics journal paper on the lack of interdisciplinarity in the scientific response to COVID-19, 2024](https://doi.org/10.1007/s11192-024-05132-x)
- [TEM journal paper evaluating the developed methods, 2023](https://doi.org/10.1109/TEM.2023.3308008)
- [project website](https://q-aktiv.github.io)
- [COVID-19++ dataset](https://doi.org/10.5281/zenodo.5531084)
- [COVID-19++ dataset paper](https://doi.org/10.1109/BigData52589.2021.9671730).
- [conference paper on learning concept representations](https://doi.org/10.18420/inf2019_26)
- [follow-up work building on concept representation learning methods](https://doi.org/10.1111/jpim.12572)
- [Python package for learning concept representations and analyzing network dynamics](https://gitlab.com/Q-Aktiv/qgraph)
- [workshop paper on data enrichment 2](https://ceur-ws.org/Vol-2773/paper-09.pdf)
- [workshop paper on data enrichment 1](https://ceur-ws.org/Vol-2451/paper-23.pdf)
- [tools for harvesting raw data](https://github.com/Q-AKTIV/covid19-harvesting-tools)
- [interview about open science tools for digital collaboration (en)](https://www.zbw-mediatalk.eu/en/2019/03/praxisbericht-open-science-diese-tools-foerdern-die-zusammenarbeit/)
- [interview about open science tools for digital collaboration (de)](https://www.zbw-mediatalk.eu/de/2019/03/praxisbericht-open-science-diese-tools-foerdern-die-zusammenarbeit/)
- [journal paper (German)](https://www.universitaetsverlagwebler.de/_files/ugd/7bac3c_24fe9adc2e3740178ad5ba98f66d1931.pdf)
- [press item (German)](https://www.b-i-t-online.de/neues/5386)
- [press release (ZB MED, German)](https://www.zbmed.de/forschen/abgeschlossene-projekte/q-aktiv)
- [funding announcement (German)](https://www.wihoforschung.de/wihoforschung/de/bmbf-projektfoerderung/foerderlinien/quantitative-wissenschaftsforschung/q-aktiv/q-aktiv_node.html)
- [final project report (German)](https://zenodo.org/records/5788648)

## Representation Learning for Texts and Graphs {#phd-project}

*2017-2022*

My PhD project. A meta-project bringing together [word2mat](#word2mat),
[textclf](#textclf), [aaerec](#aaerec), [LGL](#LGL). [phd
thesis](https://doi.org/10.21941/kcss/2023/1)

## Word Matrices for Text Representation Learning (word2mat) {#word2mat}

*2017-2022*

The idea of this project was to embed each word as a matrix as an alternative
to vectors used in word embeddings. By using matrix embeddings instead of
vector embeddings, we can use matrix multiplication as a composition function
to form a representation for phrases and sentences. While word matrices alone
did not exceed the performance of word vectors, a combination of word matrices
and word vectors turned out to be beneficial. Later, we showed that pre-trained
language models can be distilled into such a purely embedding-based model,
giving benefits in efficiency while keeping reasonable accuracy.

- [IJCNN paper on distilling the knowledge from a pre-trained language model into matrix embedding models](https://doi.org/10.1109/IJCNN55064.2022.9892144)
- [extended abstract in the best-of data science track at the INFORMATIK 2019](https://doi.org/10.18420/inf2019_47)
- [ICLR paper on self-supervised learning of word matrices](https://openreview.net/pdf?id=H1MgjoR9tQ)
- [code](https://github.com/florianmai/word2mat)

## Autoencoders for Document-based Recommendations (aaerec) {#aaerec}

*2017--2022*

The aim of this project was to build a document-level citation recommendation
system that could, for example, make users aware of missing references.  A
specialty of this project compared to other recommender systems is that we do
not use any a user data or a user profile but only operate on the contents of
the current draft. The main research question was whether models could be
enhanced by using textual side information, such as the title of the draft,
which we confirmed for a wide range of autoencoder-based recommendation models.
Interestingly, we found that the choice of the best model depends on the
semantics of item co-occurrence.  When item co-occurrence implies relatedness
(as in citations), looking at other items is far more useful than looking at
the text. In contrast, when item co-occurrence implies diversity, such as in
subject labels from professional subject indexers, the text is more useful.

- [journal paper on citation and subject label recommendation](https://doi.org/10.1007/s10791-022-09408-9)
- [conference paper on citation and subject label recommendation](https://dl.acm.org/doi/abs/10.1145/3209219.3209236)
- [RecSys challenge workshop paper on music recommendation for automatic playlist continuation](https://doi.org/10.1145/3267471.3267476)
- [codebase for all three papers](https://github.com/lgalke/aae-recommender)

## Linked Open Citation Database (LOC-DB) {#loc-db}

*2017--2020, funded by Deutsche Forschungsgemeinschaft (DFG)*

The LOC-DB project will develop ready-to-use tools and processes based on the
linked-data technology that make it possible for a single library to
meaningfully contribute to an open, distributed infrastructure for the
cataloguing of citations. The project aims to prove that, by widely
automating cataloguing processes, it is possible to add a substantial benefit
to academic search tools by regularly capturing citation relations. These
data will be made available in the semantic web to make future reuse
possible. Moreover, we document effort, number and quality of the data in a
well-founded cost-benefit analysis.  The project will use well-known methods
of information extraction and adapt them to work for arbitrary layouts of
reference lists in electronic and print media. The obtained raw data will be
aligned and linked with existing metadata sources. Moreover, it will be shown
how these data can be integrated in library catalogues. The system will be
deployable to use productively by a single library, but in principle it will
also be scalable for using it in a network.

- [conference paper on citation recommendation](https://dl.acm.org/doi/abs/10.1145/3209219.3209236)
- [main paper on the project as a whole](https://dl.acm.org/doi/abs/10.1145/3197026.3197050)
- [demo of the LOC-DB project outcome](https://locdb.bib.uni-mannheim.de/demo-frontend/frontpage)
- [collection of code for the LOC-DB project](https://github.com/locdb)
- Second Linked Open Citation Database (LOC-DB) workshop, 2018, Mannheim, Germany.
- First Linked Open Citation Database (LOC-DB) workshop, 2017, Mannheim, Germany.
- [project website (de)](https://www.bib.uni-mannheim.de/ihre-ub/projekte-der-ub/linked-open-citation-database/)

## Word Embeddings for Information Retrieval (vec4ir) {#vec4ir}

*2016--2017*

The key idea was to use word embeddings for similarity scoring in information
retrieval. The two main take-aways:

1. It is important to retain the crisp matching operation (before similarity scoring), even when using word embeddings.
2. A combination of classic information retrieval method TF-IDF and word embeddings led to the best results.

- [INFORMATIK 2017 paper](https://doi.org/10.18420/in2017_215)
- [MSc thesis](/pdf/MSc-thesis_LG.pdf)
- [codebase for studying embedded retrieval (>200 stars, >40 forks)](https://github.com/lgalke/vec4ir)

## TraininG towards a society of data-saVvy inforMation prOfessionals to enable open leadership INnovation (MOVING)

*2016--2019, EU funding, Grant Agreement Number 693092*

I engaged in this EU Horizon 2020 project as a research assistant between 2016 and 2017, leading to contributions to the deliverables 3.1, 3.2 and 3.3, as well as various conference and workshop papers:

- [Deliverable 3.3](http://moving-project.eu/wp-content/uploads/2019/03/moving_d3.3_v1.0.pdf)
- [Deliverable 3.2](http://moving-project.eu/wp-content/uploads/2018/03/moving_d3.2_v1.0.pdf)
- [Deliverable 3.1](http://moving-project.eu/wp-content/uploads/2017/04/moving_d3.1_v1.0.pdf)
- [ICADL 2018 paper on information retrieval on titles vs. full-text](https://doi.org/10.1007/978-3-030-04257-8_30)
- [DEXA 2018 workshop paper on response suggestion](https://doi.org/10.1007/978-3-319-99133-7_18)
- [code for response suggestion](https://github.com/lgalke/resuggest)
- [Project website](http://moving-project.eu)

## Extreme Multi-label Text Classification (Quadflor) {#xlmc}

*2015--2018*

This project originated from my Master's project (2015--2016), where we
developed a pipeline for extreme (=many possible classes) multi-label
text classification.  We found that a multi-layer perceptron beats the
state-of-the-art kNN approach by more than 30%.  Moreover, we compared using
either the full-text or only the title of a research paper as a basis for
classification. The result was that the full-text is only marginally better
than the title. My team member Florian Mai investigated the trade-off between
full-text and title in his Master's thesis, finding that the increased
availability of title data compensates for increased information in full-text
articles.

- [code](https://github.com/quadflor/Quadflor) (bought by [ZBW](https://zbw.eu) for production usage)
- [K-CAP 2017 paper](https://doi.org/10.1145/3148011.3148039) (outcome of the Master's project)
- [JCDL 2018 paper](https://doi.org/10.1145/3197026.3197039) (outcome of Florian's Master's thesis)
