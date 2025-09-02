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

For some exercises, we might ask you to refer to a "line number". To enable
these, press `Shift+L`. We'll remind you of this in any exercises where we use
this.

No more configuring should be necessary for modules A through D. However, when more
modules are released, you may want to return here for further instructions.

### Downloading New Modules

(These instructions are repeated in `Hub.ipynb`)

For your first module, you should be able to simply press the "Restart the
kernel and run all cells" button at the top of your screen (see image).
![image][runall-img]. Then, in the table showcasing the content for modules A
through D, click on module A lesson 1 to get started.

For each next module, you'll get a password from passing the previous
end-of-module test. Specifically, when you autograde the notebook and get a score of 4/5, at the bottom of the output you should see the password in quotation marks. Enter this into the `password = "..."` variable, save the
file with `Ctrl+S`, and then run all cells. This will download the next module for you.

### Autograding

The autograder is a way to check your progess. In any notebook that can be
autograded, you should see a cell with some code and a comment saying "run this
cell to autograde this notebook". Running this cell might take a while, but you
should see as output below which questions you got wrong, what your final score
was, and some hints on what might fix your errors.

**Remember to always save your notebook with `Ctrl+S` before running the
autograder**.

[datatools-url]: https://datatools.utoronto.ca/
[datatools-img]: assets/images/datatools.png
[upload-img]: assets/images/upload.png
[runall-img]: assets/images/runall.png

