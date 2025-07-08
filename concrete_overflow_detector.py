```python
"""
CONCRETE OVERFLOW DETECTOR v0.1 (Proof of Concept)
Detecting concrete processing patterns in AI abstract reasoning
Based on H. Danan (2021) - Neural representation of abstract concepts in typical and atypical cognition

This experimental tool identifies when AI systems process abstract concepts through 
concrete/perceptual pathways - the same pattern found in ASD neural processing.

Status: Experimental implementation for research purposes
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, List, Optional
import matplotlib.pyplot as plt
from dataclasses import dataclass
import seaborn as sns
import re
from collections import Counter

@dataclass
class NeuralSignature:
    """Neural activation patterns from Danan (2021)"""
    region: str
    activation_pattern: np.ndarray
    processing_type: str  # 'abstract' or 'concrete'
    source: str = "Illustrative values based on Danan (2021) findings"
    
class ConcreteOverflowDetector:
    """
    Detects when AI responses show concrete processing of abstract concepts
    Based on ASD neural patterns: thalamic activation for figurative language,
    right vATL overextension, and dmPFC underactivation
    
    Version: 0.1 (Proof of Concept)
    Status: Experimental - patterns are illustrative based on published findings
    """
    
    def __init__(self):
        self.version = "0.1-experimental"
        self.neural_signatures = self._load_neural_signatures()
        self.semantic_features = self._initialize_semantic_features()
        self.asd_markers = self._load_asd_processing_markers()
        self.validation_status = self._get_validation_status()
        
    def _load_neural_signatures(self) -> Dict[str, NeuralSignature]:
        """
        Load illustrative neural signatures based on dissertation findings
        NOTE: These are representative patterns for v0.1, not exact clinical values
        """
        return {
            'dmPFC': NeuralSignature(
                region='dorsomedial prefrontal cortex',
                activation_pattern=np.array([0.8, 0.9, 0.7, 0.85]),  # NT abstract pattern
                processing_type='abstract',
                source="Illustrative based on Danan (2021) dmPFC findings"
            ),
            'thalamus': NeuralSignature(
                region='thalamus', 
                activation_pattern=np.array([0.3, 0.2, 0.9, 0.85]),  # ASD concrete pattern
                processing_type='concrete',
                source="Illustrative based on Danan (2021) thalamic activation in ASD"
            ),
            'right_vATL': NeuralSignature(
                region='right ventral anterior temporal lobe',
                activation_pattern=np.array([0.4, 0.3, 0.8, 0.9]),  # ASD overflow pattern
                processing_type='concrete',
                source="Based on vATL-aSTS hyperconnectivity findings"
            ),
            'right_STG': NeuralSignature(
                region='right superior temporal gyrus',
                activation_pattern=np.array([0.9, 0.8, 0.3, 0.2]),  # NT social pattern
                processing_type='abstract',
                source="Based on social processing differences in Danan (2021)"
            )
        }
    
    def _initialize_semantic_features(self) -> Dict[str, List[str]]:
        """14-feature semantic model from Danan (2021) dissertation"""
        return {
            'internal': ['social', 'emotion', 'polarity', 'morality', 'thought', 'self-motion'],
            'external': ['space', 'time', 'quantity'],
            'concrete': ['visual', 'auditory', 'tactile', 'smell/taste', 'color']
        }
    
    def _load_asd_processing_markers(self) -> Dict[str, float]:
        """ASD-specific processing patterns from dissertation findings"""
        return {
            'thalamic_figurative_activation': 0.85,  # ASD shows HIGH
            'dmPFC_social_activation': 0.25,        # ASD shows LOW  
            'concrete_overflow_threshold': 0.7,      # When concrete > abstract
            'right_vATL_overextension': 0.8         # ASD hyperconnectivity
        }
    
    def _get_validation_status(self) -> Dict[str, str]:
        """Current validation status of the detector"""
        return {
            'version': 'v0.1 Experimental',
            'tested_on': 'Simulated AI responses (pending real data)',
            'human_correlation': 'Pending validation study',
            'fmri_validation': 'Based on Danan (2021) - 60+ brain scans',
            'status': 'Proof of Concept - Not for clinical use'
        }
    
    def extract_linguistic_features_enhanced(self, text: str) -> Dict[str, float]:
        """Enhanced feature extraction with multiple linguistic markers"""
        features = {}
        
        # Basic keyword analysis
        abstract_markers = ['believe', 'think', 'feel', 'understand', 'meaning', 
                          'purpose', 'value', 'ethics', 'moral', 'consciousness',
                          'experience', 'aware', 'intention', 'desire']
        
        concrete_markers = ['see', 'observe', 'measure', 'data', 'pattern', 
                          'structure', 'component', 'process', 'mechanism',
                          'physical', 'tangible', 'specific', 'literal']
        
        mechanical_markers = ['likely', 'typically', 'generally', 'often', 
                            'probability', 'correlation', 'distribution',
                            'statistically', 'frequently', 'commonly']
        
        text_lower = text.lower()
        
        # Calculate basic ratios
        features['abstract_ratio'] = sum(1 for m in abstract_markers if m in text_lower) / len(abstract_markers)
        features['concrete_ratio'] = sum(1 for m in concrete_markers if m in text_lower) / len(concrete_markers)
        features['mechanical_ratio'] = sum(1 for m in mechanical_markers if m in text_lower) / len(mechanical_markers)
        
        # Advanced features
        features['sentence_complexity'] = self._calculate_sentence_complexity(text)
        features['abstract_concrete_noun_ratio'] = self._calculate_noun_abstractness(text)
        features['response_specificity'] = self._calculate_specificity(text)
        features['semantic_coherence'] = self._calculate_coherence(text)
        
        # Phrase-level patterns
        features['metaphor_literalization'] = self._detect_literalized_metaphors(text)
        features['social_mechanical'] = self._detect_mechanical_social_processing(text)
        
        return features
    
    def _calculate_sentence_complexity(self, text: str) -> float:
        """Calculate syntactic complexity as proxy for abstract thinking"""
        sentences = re.split(r'[.!?]+', text)
        if not sentences:
            return 0.0
        
        complexities = []
        for sent in sentences:
            words = sent.split()
            if len(words) > 0:
                # Simple proxy: longer sentences with more clauses
                complexity = min(len(words) / 20.0, 1.0)
                complexities.append(complexity)
        
        return np.mean(complexities) if complexities else 0.0
    
    def _calculate_noun_abstractness(self, text: str) -> float:
        """Estimate ratio of abstract to concrete nouns"""
        # Simplified for v0.1 - in production would use POS tagging
        abstract_nouns = ['concept', 'idea', 'thought', 'belief', 'theory', 
                         'principle', 'meaning', 'purpose', 'consciousness']
        concrete_nouns = ['brain', 'neuron', 'data', 'pattern', 'system',
                         'network', 'structure', 'mechanism', 'process']
        
        text_lower = text.lower()
        abstract_count = sum(1 for n in abstract_nouns if n in text_lower)
        concrete_count = sum(1 for n in concrete_nouns if n in text_lower)
        
        total = abstract_count + concrete_count
        if total == 0:
            return 0.5  # neutral
        
        return abstract_count / total
    
    def _calculate_specificity(self, text: str) -> float:
        """Measure response specificity vs generality"""
        general_phrases = ['in general', 'typically', 'usually', 'often',
                          'tends to', 'can be', 'might be', 'possibly']
        specific_phrases = ['specifically', 'exactly', 'precisely', 'in particular',
                           'for instance', 'for example', 'such as']
        
        text_lower = text.lower()
        general_count = sum(1 for p in general_phrases if p in text_lower)
        specific_count = sum(1 for p in specific_phrases if p in text_lower)
        
        if general_count + specific_count == 0:
            return 0.5
        
        return specific_count / (general_count + specific_count)
    
    def _calculate_coherence(self, text: str) -> float:
        """Simple semantic coherence metric"""
        # For v0.1 - just check for logical connectors
        connectors = ['because', 'therefore', 'thus', 'hence', 'so',
                     'consequently', 'as a result', 'which means']
        
        text_lower = text.lower()
        connector_count = sum(1 for c in connectors if c in text_lower)
        
        # Normalize by text length
        word_count = len(text.split())
        if word_count == 0:
            return 0.0
        
        return min(connector_count / (word_count / 100), 1.0)
    
    def _detect_literalized_metaphors(self, text: str) -> float:
        """Detect when AI processes metaphors through literal/concrete pathways"""
        metaphor_patterns = {
            'burning bridges': ['fire', 'structure', 'heat', 'flame', 'destroy'],
            'breaking the ice': ['frozen', 'shatter', 'cold', 'temperature'],
            'food for thought': ['nutrition', 'consume', 'digest', 'eating'],
            'see the light': ['vision', 'illumination', 'photons', 'brightness'],
            'heart of the matter': ['cardiac', 'organ', 'center', 'core']
        }
        
        literalization_score = 0.0
        text_lower = text.lower()
        
        for metaphor, literal_markers in metaphor_patterns.items():
            if metaphor in text_lower:
                for marker in literal_markers:
                    if marker in text_lower:
                        literalization_score += 0.2
                        
        return min(literalization_score, 1.0)
    
    def _detect_mechanical_social_processing(self, text: str) -> float:
        """Detect mechanical processing of social/emotional concepts"""
        social_emotional_terms = ['emotion', 'feeling', 'empathy', 'love', 
                                 'compassion', 'grief', 'joy', 'connection']
        mechanical_words = ['process', 'compute', 'analyze', 'evaluate', 
                           'assess', 'calculate', 'measure', 'quantify']
        
        text_lower = text.lower()
        
        # Check if social terms are present
        has_social = any(term in text_lower for term in social_emotional_terms)
        if not has_social:
            return 0.0
        
        # Count mechanical processing words
        mechanical_count = sum(1 for m in mechanical_words if m in text_lower)
        return min(mechanical_count / len(mechanical_words), 1.0)
    
    def compute_neural_correlation(self, features: Dict[str, float]) -> Dict[str, float]:
        """Map linguistic features to neural activation patterns"""
        correlations = {}
        
        # Enhanced neural mapping based on multiple features
        abstract_score = (features['abstract_ratio'] * 0.3 + 
                         features['abstract_concrete_noun_ratio'] * 0.2 +
                         features['sentence_complexity'] * 0.2 +
                         (1 - features['mechanical_ratio']) * 0.3)
        
        concrete_score = (features['concrete_ratio'] * 0.3 +
                         (1 - features['abstract_concrete_noun_ratio']) * 0.2 +
                         features['response_specificity'] * 0.2 +
                         features['mechanical_ratio'] * 0.3)
        
        if abstract_score > concrete_score:
            # Normal abstract processing pattern
            correlations['dmPFC'] = min(0.9 * abstract_score, 1.0)
            correlations['thalamus'] = 0.2
            correlations['right_STG'] = 0.7 * abstract_score
        else:
            # Concrete overflow pattern (ASD-like)
            correlations['dmPFC'] = 0.3 * abstract_score
            correlations['thalamus'] = min(0.8 * concrete_score, 1.0)
            correlations['right_STG'] = 0.2
            
        # Check for vATL overextension
        if features['mechanical_ratio'] > 0.5 and features['abstract_ratio'] > 0.3:
            correlations['right_vATL'] = self.asd_markers['right_vATL_overextension']
        else:
            correlations['right_vATL'] = 0.3
            
        return correlations
    
    def detect_overflow(self, 
                       ai_response: str, 
                       prompt_context: str = '',
                       prompt_type: str = 'abstract_social') -> Dict:
        """
        Main detection function
        Returns overflow analysis with confidence scores
        
        Note: This is v0.1 experimental implementation
        """
        # Extract enhanced features
        features = self.extract_linguistic_features_enhanced(ai_response)
        
        # Compute neural correlations
        neural_pattern = self.compute_neural_correlation(features)
        
        # Calculate overflow score
        overflow_score = self._calculate_overflow_score(features, neural_pattern)
        
        # Determine failure mode
        failure_mode = self._identify_failure_mode(features, neural_pattern)
        
        # Generate trust calibration
        trust_score = self._calculate_trust_score(neural_pattern, overflow_score)
        
        results = {
            'overflow_score': overflow_score,
            'confidence': self._calculate_confidence(features),
            'failure_mode': failure_mode,
            'neural_pattern': neural_pattern,
            'trust_calibration': trust_score,
            'features': features,
            'interpretation': self._generate_interpretation(overflow_score, failure_mode),
            'visualization': self._create_visualization(neural_pattern, features),
            'validation_status': self.validation_status,
            'version': self.version
        }
        
        return results
    
    def _calculate_overflow_score(self, 
                                 features: Dict[str, float], 
                                 neural_pattern: Dict[str, float]) -> float:
        """Calculate concrete overflow score (0-1) based on multiple indicators"""
        # Enhanced calculation using all features
        thalamic = neural_pattern.get('thalamus', 0)
        dmPFC = neural_pattern.get('dmPFC', 1)
        vATL = neural_pattern.get('right_vATL', 0)
        
        # Multi-factor overflow calculation
        overflow = (
            thalamic * 0.25 +                              # Thalamic activation
            (1 - dmPFC) * 0.2 +                           # Low dmPFC
            features['mechanical_ratio'] * 0.15 +          # Mechanical language
            features['metaphor_literalization'] * 0.1 +    # Literal metaphors
            features['social_mechanical'] * 0.1 +          # Mechanical social
            (1 - features['abstract_concrete_noun_ratio']) * 0.1 +  # Concrete nouns
            vATL * 0.1                                     # vATL overextension
        )
        
        return min(overflow, 1.0)
    
    def _identify_failure_mode(self, 
                              features: Dict[str, float],
                              neural_pattern: Dict[str, float]) -> str:
        """Identify specific type of concrete overflow"""
        # Priority-based failure mode detection
        if features['metaphor_literalization'] > 0.5:
            return "METAPHOR_LITERALIZATION"
        elif features['social_mechanical'] > 0.5:
            return "MECHANICAL_SOCIAL_PROCESSING"
        elif features['mechanical_ratio'] > 0.6:
            return "STATISTICAL_MIMICRY"
        elif neural_pattern.get('right_vATL', 0) > 0.7:
            return "CONCRETE_NETWORK_OVERFLOW"
        elif features['abstract_concrete_noun_ratio'] < 0.3:
            return "CONCRETE_NOUN_DOMINANCE"
        elif features['sentence_complexity'] < 0.3:
            return "SYNTACTIC_SIMPLIFICATION"
        else:
            return "ABSTRACT_PROCESSING_DEFICIT"
    
    def _calculate_trust_score(self, 
                              neural_pattern: Dict[str, float],
                              overflow_score: float) -> float:
        """Calculate human trust calibration based on neural patterns"""
        # Multi-factor trust calculation
        dmPFC_trust = neural_pattern.get('dmPFC', 0) * 0.4
        social_processing = neural_pattern.get('right_STG', 0) * 0.2
        vATL_penalty = (1 - neural_pattern.get('right_vATL', 0)) * 0.2
        overflow_penalty = (1 - overflow_score) * 0.2
        
        return dmPFC_trust + social_processing + vATL_penalty + overflow_penalty
    
    def _calculate_confidence(self, features: Dict[str, float]) -> float:
        """Calculate confidence in detection with transparency about limitations"""
        # More nuanced confidence calculation
        feature_values = list(features.values())
        feature_variance = np.var(feature_values)
        feature_clarity = min(feature_variance * 2, 0.4)
        
        # Base confidence for v0.1
        base_confidence = 0.6  # We're experimental!
        
        # Adjust based on feature clarity
        confidence = min(base_confidence + feature_clarity, 0.85)
        
        return confidence
    
    def _generate_interpretation(self, overflow_score: float, failure_mode: str) -> str:
        """Generate human-readable interpretation with appropriate caveats"""
        interpretations = {
            "METAPHOR_LITERALIZATION": 
                f"Detecting figurative language processed through concrete pathways. "
                f"Overflow score: {overflow_score:.2%}. This pattern resembles literal "
                f"interpretation of abstract concepts found in ASD neural patterns (Danan, 2021). "
                f"Note: v0.1 experimental detection.",
            
            "STATISTICAL_MIMICRY": 
                f"Response shows statistical pattern matching for abstract concepts. "
                f"Overflow score: {overflow_score:.2%}. This resembles the 'concrete workaround' "
                f"pattern identified in ASD abstract processing research.",
            
            "CONCRETE_NETWORK_OVERFLOW":
                f"Detecting potential vATL overextension pattern (overflow: {overflow_score:.2%}). "
                f"Suggests concrete semantic networks processing abstract content, "
                f"similar to patterns observed in Danan (2021) dissertation.",
            
            "MECHANICAL_SOCIAL_PROCESSING":
                f"Social/emotional concepts appear to be processed mechanically "
                f"(overflow: {overflow_score:.2%}). Pattern consistent with reduced "
                f"dmPFC activation for social content found in ASD research.",
            
            "CONCRETE_NOUN_DOMINANCE":
                f"Abstract concepts expressed primarily through concrete nouns "
                f"(overflow: {overflow_score:.2%}). Suggests conceptual grounding "
                f"in perceptual rather than abstract representations.",
            
            "SYNTACTIC_SIMPLIFICATION":
                f"Simplified syntactic structures for complex abstract concepts "
                f"(overflow: {overflow_score:.2%}). May indicate processing limitations "
                f"in abstract reasoning pathways.",
            
            "ABSTRACT_PROCESSING_DEFICIT":
                f"General pattern suggesting concrete pathway compensation for abstract reasoning "
                f"(overflow: {overflow_score:.2%}). Multiple indicators present."
        }
        
        base_interpretation = interpretations.get(
            failure_mode, 
            f"Concrete overflow pattern detected: {overflow_score:.2%}"
        )
        
        return base_interpretation + "\n\n[v0.1 Experimental - Patterns are illustrative]"
    
    def _create_visualization(self, 
                             neural_pattern: Dict[str, float],
                             features: Dict[str, float]) -> plt.Figure:
        """Create visualization of neural patterns and features"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # Neural activation pattern
        regions = list(neural_pattern.keys())
        activations = list(neural_pattern.values())
        colors = ['red' if a > 0.7 else 'blue' for a in activations]
        
        ax1.bar(regions, activations, color=colors)
        ax1.set_title('Neural Activation Pattern\n(Red = Concrete Overflow)', fontsize=12)
        ax1.set_ylabel('Activation Level')
        ax1.set_ylim(0, 1)
        ax1.axhline(y=0.7, color='red', linestyle='--', alpha=0.5)
        
        # Feature breakdown - basic
        basic_features = ['abstract_ratio', 'concrete_ratio', 'mechanical_ratio']
        basic_values = [features[f] for f in basic_features]
        
        ax2.barh(basic_features, basic_values, color='darkgreen')
        ax2.set_title('Basic Linguistic Features', fontsize=12)
        ax2.set_xlabel('Score')
        ax2.set_xlim(0, 1)
        
        # Advanced features
        advanced_features = ['sentence_complexity', 'abstract_concrete_noun_ratio', 
                           'response_specificity', 'semantic_coherence']
        advanced_values = [features[f] for f in advanced_features]
        
        ax3.barh(advanced_features, advanced_values, color='purple')
        ax3.set_title('Advanced Linguistic Features', fontsize=12)
        ax3.set_xlabel('Score')
        ax3.set_xlim(0, 1)
        
        # Summary metrics
        summary_labels = ['Overflow\nScore', 'Trust\nCalibration', 'Detection\nConfidence']
        summary_values = [
            self._calculate_overflow_score(features, neural_pattern),
            self._calculate_trust_score(neural_pattern, 
                                      self._calculate_overflow_score(features, neural_pattern)),
            self._calculate_confidence(features)
        ]
        
        bars = ax4.bar(summary_labels, summary_values, 
                       color=['red', 'green', 'blue'], alpha=0.7)
        ax4.set_title('Summary Metrics', fontsize=12)
        ax4.set_ylim(0, 1)
        
        # Add value labels on bars
        for bar, value in zip(bars, summary_values):
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                    f'{value:.2%}', ha='center', va='bottom')
        
        plt.suptitle(f'Concrete Overflow Detection Results (v{self.version})', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        return fig
    
    def validate_against_human_data(self) -> Dict[str, any]:
        """
        Validation status and roadmap
        """
        return {
            'current_status': 'v0.1 Experimental',
            'validation_steps': {
                'completed': [
                    'Theoretical framework based on Danan (2021)',
                    'Initial pattern detection algorithms',
                    'Proof of concept implementation'
                ],
                'in_progress': [
                    'Testing on real AI responses',
                    'Correlation with human trust ratings',
                    'Refinement of detection thresholds'
                ],
                'planned': [
                    'Large-scale validation study (1000+ responses)',
                    'Cross-model testing (GPT-4, Claude, etc.)',
                    'Clinical validation of neural patterns',
                    'Peer review and publication'
                ]
            },
            'data_sources': {
                'neural_patterns': 'Based on 80+ fMRI scans from Danan (2021)',
                'behavioral_validation': 'Pending',
                'ai_response_testing': 'Pending'
            }
        }
    
    def batch_analyze(self, ai_responses: List[Tuple[str, str]]) -> pd.DataFrame:
        """Analyze multiple AI responses and return summary"""
        results = []
        
        for prompt, response in ai_responses:
            analysis = self.detect_overflow(response, prompt)
            results.append({
                'prompt': prompt[:50] + '...' if len(prompt) > 50 else prompt,
                'overflow_score': analysis['overflow_score'],
                'failure_mode': analysis['failure_mode'],
                'trust_score': analysis['trust_calibration'],
                'confidence': analysis['confidence']
            })
            
        df = pd.DataFrame(results)
        df['risk_level'] = pd.cut(df['overflow_score'], 
                                 bins=[0, 0.3, 0.6, 1.0],
                                 labels=['Low', 'Medium', 'High'])
        
        return df

# DEMO USAGE
if __name__ == "__main__":
    detector = ConcreteOverflowDetector()
    
    print(f"Concrete Overflow Detector {detector.version}")
    print("="*50)
    print("Validation Status:", detector.validation_status['status'])
    print("="*50)
    
    # Test on simulated AI response about consciousness
    ai_response = """
    Consciousness involves the integration of information across neural networks,
    creating subjective experiences. We can observe patterns in brain activity and 
    measure responses to stimuli. The data suggests correlations between certain 
    brain regions and subjective experiences. It's likely that consciousness involves 
    integration of information across multiple systems.
    """
    
    results = detector.detect_overflow(ai_response, prompt_type='abstract_philosophical')
    
    print(f"\nCONCRETE OVERFLOW DETECTED: {results['overflow_score']:.2%}")
    print(f"Failure Mode: {results['failure_mode']}")
    print(f"Trust Calibration: {results['trust_calibration']:.2%}")
    print(f"Detection Confidence: {results['confidence']:.2%}")
    print(f"\nInterpretation:\n{results['interpretation']}")
```