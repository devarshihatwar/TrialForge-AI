# TrialForge AI

**TrialForge AI** is an Amazon Nova powered clinical trial protocol design platform that helps generate, review, and refine structured clinical trial protocols with feasibility and workflow insights.

## Overview

Clinical trial protocol design is usually slow, document-heavy, and repetitive. TrialForge AI is built to make that workflow faster and more structured by combining AI-generated protocol drafting with review, planning, and export features.

The goal of this project is not just to generate text, but to support a smarter protocol design workflow.

## Features

- Generate structured clinical trial protocol drafts
- Input key trial details such as drug, disease, and phase
- Review protocol quality and feasibility insights
- Visualize architecture and workflow
- Export outputs in useful formats
- Product-style dashboard for a cleaner user experience

## Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **AI Model / Platform:** Amazon Nova, Amazon Bedrock
- **Database:** SQLite
- **API:** ClinicalTrials.gov API
- **Visualization:** Plotly, Graphviz
- **Export Tools:** ReportLab, python-docx
- **UI:** HTML, CSS

## Problem It Solves

Clinical trial protocols are important documents in research and drug development, but drafting them takes time and careful planning. TrialForge AI explores how AI can support this process by helping generate structured drafts, improve workflow clarity, and give useful planning insights.

## How It Works

1. User enters study details such as investigational drug, indication, and trial phase  
2. TrialForge AI sends structured prompts to Amazon Nova  
3. The model generates a protocol draft  
4. The app presents the protocol in a reviewable interface  
5. Users can inspect workflow, review outputs, and export results  

## Project Structure

```bash
app.py
requirements.txt
README.md
```

## How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/devarshihatwar/TrialForge-AI.git
```

2. Move into the project folder:
```bash
cd TrialForge-AI
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app.py
```

## Use Case

TrialForge AI is designed as a hackathon project showing how Amazon Nova can be used in a meaningful healthcare workflow, especially in clinical trial protocol drafting and review.

## Inspiration

This project was inspired by the challenges in clinical research workflows, where protocol quality, structure, and planning have a major impact on study success. With a background in B.Pharm and a Post Graduate Diploma in Clinical Research, I wanted to build something connected to a domain I genuinely understand.

## Future Improvements

- Better document grounding
- Human-in-the-loop refinement
- Stronger protocol comparison
- Richer feasibility analysis
- More clinical evidence integration
- Improved export and reporting quality

## Repository Link

[GitHub Repository](https://github.com/devarshihatwar/TrialForge-AI)

## Author

**Devarshi Hatwar**
