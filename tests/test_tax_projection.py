from recongraph.domain.tax.parser import DeterministicTaxParser
from recongraph.domain.tax.artifact import TaxIdentifierArtifact
from recongraph.domain.tax.interpretation import TaxPairInterpreter
from recongraph.domain.tax.projection import TaxV1ProjectionContract

def test_tax_projection_exact_match():
    # Exact GSTIN match -> 1.0
    val_a = DeterministicTaxParser.parse("27ABCDE1234F1Z5")
    val_b = DeterministicTaxParser.parse("27ABCDE1234F1Z5")
    art_a = TaxIdentifierArtifact.create(val_a)
    art_b = TaxIdentifierArtifact.create(val_b)
    
    interp = TaxPairInterpreter.interpret(art_a, art_b)
    projection = TaxV1ProjectionContract.project((interp,))
    
    assert projection.score == 1.0
    assert not projection.violations

def test_tax_projection_different_state_same_pan():
    # Interstate GSTIN match -> 1.0 (information loss)
    val_a = DeterministicTaxParser.parse("27ABCDE1234F1Z5")
    val_b = DeterministicTaxParser.parse("29ABCDE1234F1Z5")
    art_a = TaxIdentifierArtifact.create(val_a)
    art_b = TaxIdentifierArtifact.create(val_b)
    
    interp = TaxPairInterpreter.interpret(art_a, art_b)
    projection = TaxV1ProjectionContract.project((interp,))
    
    assert projection.score == 1.0
    assert not projection.violations

def test_tax_projection_distinct_pans():
    # Distinct PANs -> 0.0 with TAX_IDENTITY_CONFLICT violation
    val_a = DeterministicTaxParser.parse("27ABCDE1234F1Z5")
    val_b = DeterministicTaxParser.parse("27ZZZZZ9999Z1Z5")
    art_a = TaxIdentifierArtifact.create(val_a)
    art_b = TaxIdentifierArtifact.create(val_b)
    
    interp = TaxPairInterpreter.interpret(art_a, art_b)
    projection = TaxV1ProjectionContract.project((interp,))
    
    assert projection.score == 0.0
    assert "TAX_IDENTITY_CONFLICT" in projection.violations

def test_tax_projection_both_missing():
    # Both Missing -> None
    val_a = DeterministicTaxParser.parse(None)
    val_b = DeterministicTaxParser.parse(None)
    art_a = TaxIdentifierArtifact.create(val_a)
    art_b = TaxIdentifierArtifact.create(val_b)
    
    interp = TaxPairInterpreter.interpret(art_a, art_b)
    projection = TaxV1ProjectionContract.project((interp,))
    
    assert projection.score is None
    assert not projection.violations
