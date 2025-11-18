"""
ATLAS Stage 4: Publication

Automated academic paper generation from research results.
"""

__version__ = "0.2.0"

from atlas.publication.paper_generator import (
    PaperGenerator,
    Paper,
    PaperSection
)

__all__ = [
    "PaperGenerator",
    "Paper",
    "PaperSection",
]
