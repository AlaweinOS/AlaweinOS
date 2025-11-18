"""
Unit tests for QAP adapter mathematical correctness

Tests verify that the QAP formulation fixes have been correctly applied.
"""

import numpy as np
import pytest

from optilibria.adapters.qap import QAPAdapter


def test_qap_formulation_correctness():
    """
    Verify QAP formulation matches theoretical trace formulation.

    Tests that the corrected QAP adapter uses the proper mathematical
    formulation: min trace(A @ P @ B @ P.T) instead of the incorrect
    Kronecker product formulation.
    """
    # Simple 2x2 test case with known solution
    A = np.array([[0, 1], [1, 0]])  # Flow matrix
    B = np.array([[0, 2], [2, 0]])  # Distance matrix

    adapter = QAPAdapter()
    adapter.A = A
    adapter.B = B
    adapter.n = 2

    # Test identity permutation [0, 1]
    identity = np.array([0, 1])
    result = adapter.compute_objective(identity)

    # Expected: trace(A @ I @ B @ I.T) = trace(A @ B)
    # A @ B = [[2, 0], [0, 2]]
    # trace = 4
    expected = float(np.trace(A @ B))

    assert abs(result - expected) < 1e-10, f"Expected {expected}, got {result}"


def test_qap_formulation_swap_permutation():
    """Test QAP objective with a swap permutation"""
    A = np.array([[0, 1], [1, 0]])
    B = np.array([[0, 2], [2, 0]])

    adapter = QAPAdapter()
    adapter.A = A
    adapter.B = B
    adapter.n = 2

    # Test swap permutation [1, 0]
    swap = np.array([1, 0])
    result = adapter.compute_objective(swap)

    # For swap: P = [[0, 1], [1, 0]]
    # A @ P @ B @ P.T should give same result due to symmetry
    P = np.array([[0, 1], [1, 0]])
    expected = float(np.trace(A @ P @ B @ P.T))

    assert abs(result - expected) < 1e-10, f"Expected {expected}, got {result}"


def test_qap_formulation_3x3():
    """Test QAP formulation with 3x3 instance"""
    A = np.array([[0, 1, 2],
                  [1, 0, 3],
                  [2, 3, 0]])

    B = np.array([[0, 5, 10],
                  [5, 0, 15],
                  [10, 15, 0]])

    adapter = QAPAdapter()
    adapter.A = A
    adapter.B = B
    adapter.n = 3

    # Test identity permutation
    identity = np.array([0, 1, 2])
    result = adapter.compute_objective(identity)

    # Expected: trace(A @ B)
    expected = float(np.trace(A @ B))

    assert abs(result - expected) < 1e-10, f"Expected {expected}, got {result}"


def test_qap_is_permutation():
    """Test permutation validation"""
    adapter = QAPAdapter()
    adapter.n = 3

    # Valid permutation
    assert adapter._is_permutation(np.array([0, 1, 2]))
    assert adapter._is_permutation(np.array([2, 0, 1]))
    assert adapter._is_permutation(np.array([1, 2, 0]))

    # Invalid permutations
    assert not adapter._is_permutation(np.array([0, 0, 1]))  # Duplicate
    assert not adapter._is_permutation(np.array([0, 1, 3]))  # Out of range
    assert not adapter._is_permutation(np.array([0, 1]))     # Wrong length


def test_qap_verify_properties():
    """Test QAP instance property verification"""
    # Valid symmetric QAP instance
    A = np.array([[0, 1], [1, 0]])
    B = np.array([[0, 2], [2, 0]])

    adapter = QAPAdapter()
    adapter.A = A
    adapter.B = B
    adapter.n = 2

    properties = adapter.verify_qap_properties()

    assert properties['instance_loaded']
    assert properties['square_matrices']
    assert properties['positive_flows']
    assert properties['positive_distances']
    assert properties['symmetric_flows']
    assert properties['symmetric_distances']
    assert properties['mathematical_valid']


def test_qap_negative_flows_detected():
    """Test that negative flows are detected in validation"""
    # Invalid QAP with negative flow
    A = np.array([[0, -1], [1, 0]])
    B = np.array([[0, 2], [2, 0]])

    adapter = QAPAdapter()
    adapter.A = A
    adapter.B = B
    adapter.n = 2

    properties = adapter.verify_qap_properties()

    assert not properties['positive_flows']
    assert not properties['mathematical_valid']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
