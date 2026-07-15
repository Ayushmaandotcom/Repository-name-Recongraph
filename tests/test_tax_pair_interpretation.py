import pytest
from recongraph.domain.tax.parser import DeterministicTaxParser
from recongraph.domain.tax.artifact import TaxIdentifierArtifact
from recongraph.domain.tax.interpretation import TaxPairInterpreter
from recongraph.domain.tax.factors import GSTINRelationState, PANRelationState

def test_tpi_001_exact_gstin_match():
    # Same GSTIN
    gstin = "27ABCDE1234F1Z5"
    p_val = DeterministicTaxParser.parse(gstin)
    g_val = DeterministicTaxParser.parse(gstin)
    
    p_art = TaxIdentifierArtifact.create(p_val)
    g_art = TaxIdentifierArtifact.create(g_val)
    
    interp = TaxPairInterpreter.interpret(p_art, g_art)
    
    assert interp.gstin_relation.state == GSTINRelationState.EXACT_MATCH
    assert interp.pan_relation.state == PANRelationState.EXACT_MATCH
    assert interp.pan_relation.derived_from_gstin is True

def test_tpi_002_different_state_same_pan():
    # State 27 vs 29, same PAN
    gstin_27 = "27ABCDE1234F1Z5"
    gstin_29 = "29ABCDE1234F1Z5"
    p_val = DeterministicTaxParser.parse(gstin_27)
    g_val = DeterministicTaxParser.parse(gstin_29)
    
    p_art = TaxIdentifierArtifact.create(p_val)
    g_art = TaxIdentifierArtifact.create(g_val)
    
    interp = TaxPairInterpreter.interpret(p_art, g_art)
    
    assert interp.gstin_relation.state == GSTINRelationState.DIFFERENT_STATE_SAME_PAN
    assert interp.pan_relation.state == PANRelationState.EXACT_MATCH

def test_tpi_003_distinct_pans():
    # Different PANs
    gstin_1 = "27ABCDE1234F1Z5"
    gstin_2 = "27ZZZZZ9999Z1Z5"
    p_val = DeterministicTaxParser.parse(gstin_1)
    g_val = DeterministicTaxParser.parse(gstin_2)
    
    p_art = TaxIdentifierArtifact.create(p_val)
    g_art = TaxIdentifierArtifact.create(g_val)
    
    interp = TaxPairInterpreter.interpret(p_art, g_art)
    
    assert interp.gstin_relation.state == GSTINRelationState.DISTINCT
    assert interp.pan_relation.state == PANRelationState.DISTINCT

def test_tpi_004_pan_vs_gstin_same_pan():
    # One is PAN, one is GSTIN derived PAN
    pan = "ABCDE1234F"
    gstin = "27ABCDE1234F1Z5"
    p_val = DeterministicTaxParser.parse(pan)
    g_val = DeterministicTaxParser.parse(gstin)
    
    p_art = TaxIdentifierArtifact.create(p_val)
    g_art = TaxIdentifierArtifact.create(g_val)
    
    interp = TaxPairInterpreter.interpret(p_art, g_art)
    
    assert interp.gstin_relation.state == GSTINRelationState.ONE_MISSING
    assert interp.pan_relation.state == PANRelationState.EXACT_MATCH
    assert interp.pan_relation.derived_from_gstin is True

def test_tpi_005_both_missing():
    p_val = DeterministicTaxParser.parse(None)
    g_val = DeterministicTaxParser.parse("")
    
    p_art = TaxIdentifierArtifact.create(p_val)
    g_art = TaxIdentifierArtifact.create(g_val)
    
    interp = TaxPairInterpreter.interpret(p_art, g_art)
    
    assert interp.gstin_relation.state == GSTINRelationState.BOTH_MISSING
    assert interp.pan_relation.state == PANRelationState.BOTH_MISSING
