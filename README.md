![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Point Load to UCS Converter
 
*For geotechnical engineers and engineering geologists: enter the point load strength index (Is50) and select rock type to instantly compute unconfined compressive strength (UCS) with ISRM classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geotechnical Engineering
 
Inputs: (1) Point load strength index Is50 [MPa] – a float, typically 0.1 to 10 MPa. (2) Rock type – a dropdown with options: 'General (k=24)', 'Low-porosity sandstone (k=20)', 'Limestone/dolomite (k=20)', 'Granite/gneiss (k=25)', 'Basalt/diabase (k=22)', or a 'Custom k factor' option that reveals an additional numeric input for k between 15 and 30. The default is 'General (k=24)'. If custom is selected, a number input for k appears. Logic: UCS = k × Is50. The result is displayed in MPa with two decimal places. Additionally, the tool classifies the UCS according to the ISRM (1981) scale: <1 MPa = 'Extremely weak', 1-5 MPa = 'Very weak', 5-25 MPa = 'Weak', 25-50 MPa = 'Medium strong', 50-100 MPa = 'Strong', 100-250 MPa = 'Very strong', >250 MPa = 'Extremely strong'. The classification is shown as text next to the UCS value. Gradio UI: A title 'Point Load to UCS Converter', then a row with the Is50 number input (label 'Point Load Index Is50 (MPa)') and the rock type dropdown. Below, a 'Compute UCS' button. Below that, an output textbox showing 'UCS = X.XX MPa – Classification: Y'. Optionally, a small info icon next to the classification that shows the ISRM table on hover or click. No chart. No AI/ML component, purely arithmetic and look-up.
 
## Run it
 
```bash
docker build -t point-load-to-ucs-converter .
docker run -p 7860:7860 point-load-to-ucs-converter
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-26.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
