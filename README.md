# Concrete Overflow Detection Framework v0.1

> Part of the [Cognitive Architectures for AI](https://github.com/HillaryDanan/cognitive-architectures-ai) research program


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HillaryDanan/concrete-overflow-detector/blob/main/Concrete_Overflow_Detector_Demo.ipynb)

**A linguistic analysis framework for evaluating AI abstract reasoning patterns**

Based on neuroscience research showing how individuals with ASD process abstract concepts through concrete neural pathways - achieving similar behavioral outputs through fundamentally different mechanisms.

## What This Is

This v0.1 prototype demonstrates a **linguistic analysis framework** that identifies patterns suggesting concrete vs abstract processing in text responses. 

### Current Implementation:
- 📝 **Linguistic Pattern Analysis**: Detects mechanical language, literalized metaphors, and concrete noun usage
- 🧠 **Theoretical Neural Mapping**: Maps linguistic patterns to neural signatures from my dissertation research
- 📊 **Scoring Framework**: Provides metrics for "concrete overflow" in abstract reasoning
- 🔍 **Pattern Visualization**: Shows the breakdown of detected patterns

### What This Is NOT (Yet):
- ❌ A consciousness test
- ❌ A validated clinical tool
- ❌ Based on actual AI neural data
- ❌ A finished product

## The Science

My dissertation (Levinson, 2021) identified neural signatures distinguishing genuine from compensatory abstract reasoning:
- **dmPFC activation** → Genuine abstract processing
- **Thalamic activation** → Concrete processing of abstractions (ASD pattern)
- **Right vATL overextension** → Concrete semantic overflow

This framework applies these insights to analyze linguistic patterns in AI responses.

## The Vision

With proper validation, this framework could enable:
- 🔬 **Biological validation** of AI reasoning patterns
- 🎯 **Trust calibration** based on processing mechanisms
- 🛡️ **Safety verification** for AI systems claiming understanding
- 📈 **Benchmarks** for genuine vs simulated abstraction

## Current Limitations

**This is a proof-of-concept that:**
- Analyzes linguistic patterns, not neural activity
- Uses theoretical mappings, not validated correlations
- Demonstrates the framework, not final results
- Needs extensive validation with real data

## Try It

**Interactive Demo**: Analyze text patterns that may indicate concrete vs abstract processing
- Works with any text input
- See the linguistic analysis in action
- Understand the framework's approach

## Validation Roadmap

### ✅ Completed:
- Theoretical framework based on neuroscience
- Linguistic pattern detection algorithms
- Working prototype implementation

### 🔄 Needed:
- Testing on 1000+ real AI responses
- Correlation with human trust ratings
- Validation against fMRI data
- Cross-model comparison studies
- Peer review and publication

## For Potential Collaborators

**I bring:**
- PhD in cognitive neuroscience with 60+ fMRI scans of abstract reasoning
- Published research on neural signatures of understanding in different types of cognition
- A novel framework bridging neuroscience and AI

**Looking for:**
- Access to AI systems for testing
- Collaboration on validation studies
- Resources for large-scale analysis
- Partnership on biological AI validation

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from concrete_overflow_detector import ConcreteOverflowDetector

detector = ConcreteOverflowDetector()
result = detector.detect_overflow(text_sample)

# Returns linguistic pattern analysis and theoretical neural mapping
print(f"Linguistic patterns suggest: {result['overflow_score']:.1%} concrete processing")
print(f"Pattern type: {result['failure_mode']}")
```

### Contributing
This is an open research project. I welcome:
- Feedback on the framework
- Real AI responses for testing
- Collaboration on validation
- Ideas for improvement

### Citation
Levinson, H. (2021). The Neural Representation of Abstract Concepts in 
Typical and Atypical Cognition. Doctoral Dissertation, Rutgers University.
