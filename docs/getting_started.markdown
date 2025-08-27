---
layout: page
title: Getting Started
permalink: /getting-started/
config:
  flowchart:
    htmlLabels: false
---

<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true });
</script>

### Modules

Computer Programming for Linguists (CPFL) is a modular approach to learning how to
program in Python, targetted to anyone with a background in linguistics. It
currently consists of four modules that will teach you the basics of Python
(variables, statements, conditionals, loops, lists). In the future, it will
also contain material covering introductory computational linguistics.

<pre class="mermaid">
flowchart LR
    A("<b>Module A</b> <br> Values and variables")
    B("<b>Module B</b> <br> Functions")
    C("<b>Module C</b> <br> Conditional execution")
    D("<b>Module D</b> <br> Iteration")
    E("<b>Module E</b> <br> Strings")
    F("<b>Module F</b> <br> Useful iterations")
    G("<b>Module G</b> <br> More container types")
    H("<b>Module H</b> <br> Working w/ text data")

    A --> B --> C --> D
    D --> E
    D --> F
    D --> G
    E --> H
    F --> H
    G --> H
</pre>

Modules consist of some lessons, and some problem sets corresponding to those
lessons. Problem sets are automatically graded so that you can check your
progress as you go. We recommend that you do every problem set. At the end of
each module is a test. Autograding the test and getting at least 80% will give
you a password that you can use to access the next module.

Modules E and beyond are not yet implemented

### Jupyter

Every lesson in CPFL is built as a Jupyter notebook. Jupyter notebooks are
convenient ways of representing text information right alongside Python code.

If you're a student at the University of Toronto, then you can do everything right from your browser.

1. Go to [https://datatools.utoronto.ca/][datatools-url]
2. From the three options you see, choose "JupyterLab" ![image][datatools-img]
3. Log in with your UTORid
4. <a href="{{site.url}}{{site.baseurl}}/assets/notebooks/Hub.ipynb"
      download>Download this notebook</a>
5. Click the upload button (from the image below)
   ![image][upload-img]{:width="50%"}
6. Select the notebook you just downloaded

You should now see the notebook `Hub.ipynb` displayed in the right sidebar
(file-browser). Double click on the notebook to open it. Once you've opened
it, follow the instructions in the notebook to start on module A.

### Configuring Jupyter

No configuring should be necessary for modules A through D. However, when more
modules are released, you may want to return here for further instructions.

### Downloading New Modules

TODO. For now, follow the instructions from `Hub.ipynb`.

### Autograding

TODO. For now, follow the instructions from the notebooks.

[datatools-url]: https://datatools.utoronto.ca/
[datatools-img]: assets/images/datatools.png
[upload-img]: assets/images/upload.png

