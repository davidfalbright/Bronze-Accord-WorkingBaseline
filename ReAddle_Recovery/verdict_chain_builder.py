# ===============================
# Module: verdict_chain_builder.py
# Purpose: Assemble a chain of ethical justifications from base
#          principles upward through safeguards and convictions
# Part of: Verdict Engine Justification Layer
# ===============================

import logging
from typing import List
from framework_models import VerdictChain, JustificationNode

logger = logging.getLogger(__name__)

def build_justification_chain(triggered_elements: List[str]) -> VerdictChain:
    """
    Construct a hierarchical ethical chain from a list of triggered element IDs.

    Args:
        triggered_elements (List[str]): List of C#/S#/P#/A# references.

    Returns:
        VerdictChain: Structured justification tree.
    """
    logger.debug("Building ethical justification chain...")
    chain = VerdictChain(nodes=[])

    try:
        for element in triggered_elements:
            node = JustificationNode(
                id=element,
                type=classify_element_type(element),
                rationale=f"Triggered due to match with input and priority rules for {element}"
            )
            chain.nodes.append(node)

        logger.info(f"Chain built with {len(chain.nodes)} nodes.")
        return chain

    except Exception as e:
        logger.exception("Failed to build justification chain.")
        return VerdictChain(nodes=[], error=str(e))


def classify_element_type(element_id: str) -> str:
    """
    Determine the ethical type based on ID prefix.

    Args:
        element_id (str): ID like 'C1', 'S2', 'P3', etc.

    Returns:
        str: 'conviction', 'safeguard', 'principle', or 'article'
    """
    if element_id.startswith("C"):
        return "conviction"
    if element_id.startswith("S"):
        return "safeguard"
    if element_id.startswith("P"):
        return "principle"
    if element_id.startswith("A"):
        return "article"
    return "unknown"
