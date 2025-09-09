---
layout: page
title: Feedback
permalink: /feedback/
---

Once you've finished everything, it would be fantastic if you could provide us
with your progress on the notebooks.

1. Navigate to the Hub
2. Right click anywhere on the view of the notebook
3. Click on the option "New Console for Notebook"
4. Copy and paste the following, and then run it with `Shift+Enter`

```
!zip -r feedback.zip Module_* -x \*/.mypy_cache/\* \*/.ipynb_checkpoints/\* \*/__pycache__/\*
```

5. Now, on the left side, you should see a file browser (if you don't, try
   hitting `Ctrl+Shift+F`)
6. Right click on the file that says `feedback.zip`, and then click "Download"
7. Send the downloaded `feedback.zip` to Barend Beekhuizen at `barend (dot)
   beekhuizen (at) utoronto (dot) ca`

