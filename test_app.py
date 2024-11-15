import pytest
from app import square

def test_positive_case():
  assert square(5) == 25

def test_negative_case():
  assert square(-3) == 9

def test_edge_case():
  assert square(0) == 0
