"""
Unit tests for reference/tracking identifier detection and anonymization.
Tests FILE_NUMBER, TRANSACTION_NUMBER, CUSTOMER_NUMBER, TICKET_ID.
"""

import pytest
from PII_filter.pii_filter import PIIFilter


class TestFileNumberDetection:
    """Test FILE_NUMBER detection in multiple languages."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_file_number_english(self, filter_instance):
        """Test English file number detection."""
        text = "File Number: FN-2024-001234"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "FN-2024-001234" not in result

    def test_file_number_with_prefix(self, filter_instance):
        """Test file number with country/office prefix."""
        text = "File ID: DE-FN-2024-567890"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "DE-FN-2024-567890" not in result

    def test_file_number_german(self, filter_instance):
        """Test German Aktenzeichen (file number) detection."""
        text = "File ID: ACZ2024123456"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "ACZ2024123456" not in result

    def test_file_number_with_label(self, filter_instance):
        """Test file number with explicit label."""
        text = "File no: FILE20240987654"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "FILE20240987654" not in result

    def test_file_number_italian(self, filter_instance):
        """Test Italian fascicolo detection."""
        text = "Fascicolo number: FASC2024345678"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "FASC2024345678" not in result

    def test_file_number_alphanumeric(self, filter_instance):
        """Test alphanumeric file numbers."""
        text = "File no: FILE20240987654A"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "FILE20240987654A" not in result

    def test_file_number_with_hyphens(self, filter_instance):
        """Test file numbers with hyphens."""
        text = "Dossier-number: DOS-2024-456789"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "DOS-2024-456789" not in result

    def test_unrelated_numbers_partially_untouched(self, filter_instance):
        """Test that bare numbers without labels remain untouched."""
        text = "The file was from 2024 with reference 567890."
        result = filter_instance.anonymize_text(text)
        # Unlabeled bare numbers should not be matched
        assert "<FILE_NUMBER>" not in result


class TestTransactionNumberDetection:
    """Test TRANSACTION_NUMBER detection in multiple languages."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_transaction_number_english(self, filter_instance):
        """Test English transaction number detection."""
        text = "Transaction number: TRX2024123456"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "TRX2024123456" not in result

    def test_transaction_number_abbreviated(self, filter_instance):
        """Test abbreviated transaction number (txn)."""
        text = "TXN no: 789012345678"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "789012345678" not in result

    def test_transaction_number_german(self, filter_instance):
        """Test German transaction number detection."""
        text = "Transaktionsnummer: TRX2024456789"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "TRX2024456789" not in result

    def test_transaction_number_french(self, filter_instance):
        """Test French transaction number detection."""
        text = "Numero transaction: TR234567890123"
        result =filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "TR234567890123" not in result

    def test_transaction_number_italian(self, filter_instance):
        """Test Italian transaction detection."""
        text = "Transazione numero: TR567890123456"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "TR567890123456" not in result

    def test_transaction_number_spanish(self, filter_instance):
        """Test Spanish transaction detection."""
        text = "Trans ID: TR345678901234"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "TR345678901234" not in result

    def test_transaction_number_numeric_only(self, filter_instance):
        """Test numeric-only transaction numbers."""
        text = "Transaction number: 987654321098"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "987654321098" not in result

    def test_transaction_with_separators(self, filter_instance):
        """Test transaction numbers with internal separators."""
        text = "Trans ID: 2024-12-345678"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "2024-12-345678" not in result


class TestCustomerNumberDetection:
    """Test CUSTOMER_NUMBER detection in multiple languages."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_customer_number_english(self, filter_instance):
        """Test English customer number detection."""
        text = "Cust no: CUST987654321"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CUST987654321" not in result

    def test_customer_id_abbreviated(self, filter_instance):
        """Test abbreviated customer ID."""
        text = "Cust ID: CUSTID001234"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CUSTID001234" not in result

    def test_client_number_english(self, filter_instance):
        """Test English client number."""
        text = "Client no: CL567890123"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CL567890123" not in result

    def test_customer_number_german(self, filter_instance):
        """Test German customer number (Kundennummer)."""
        text = "Client ID: KUNDEN234567"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "KUNDEN234567" not in result

    def test_customer_number_french(self, filter_instance):
        """Test French customer number (numero client)."""
        text = "Numero client: CLNUMBER345678"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CLNUMBER345678" not in result

    def test_customer_number_italian(self, filter_instance):
        """Test Italian customer number (codice cliente)."""
        text = "Codice cliente: CLIENTI456789"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CLIENTI456789" not in result

    def test_customer_number_spanish(self, filter_instance):
        """Test Spanish customer number (numero cliente)."""
        text = "Numero cliente: CLNUMBER567890"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CLNUMBER567890" not in result

    def test_customer_number_alphanumeric(self, filter_instance):
        """Test alphanumeric customer numbers."""
        text = "Customer number: CUS987654321ABC"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CUS987654321ABC" not in result


class TestTicketIDDetection:
    """Test TICKET_ID detection in multiple languages."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_ticket_number_english(self, filter_instance):
        """Test English ticket number detection."""
        text = "Issue number: TKT2024123456ABC"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TKT2024123456ABC" not in result

    def test_case_id_english(self, filter_instance):
        """Test English case ID detection."""
        text = "Task number: TASKNUMBER2024789012"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TASKNUMBER2024789012" not in result

    def test_issue_number_english(self, filter_instance):
        """Test English issue number detection."""
        text = "Issue number: ISSUE345678XYZ"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "ISSUE345678XYZ" not in result

    def test_task_id_english(self, filter_instance):
        """Test English task ID detection."""
        text = "Task ID: TASK567890PQR"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TASK567890PQR" not in result

    def test_ticket_id_german(self, filter_instance):
        """Test German ticket detection."""
        text = "Ticketnummer: TKTDE234567"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TKTDE234567" not in result

    def test_ticket_id_french(self, filter_instance):
        """Test French ticket/task detection (tâche)."""
        text = "Tâche ID: TACHEFR345678"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TACHEFR345678" not in result

    def test_ticket_id_italian(self, filter_instance):
        """Test Italian task detection (compito)."""
        text = "Compito numero: COMPIT456789"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "COMPIT456789" not in result

    def test_ticket_id_spanish(self, filter_instance):
        """Test Spanish task detection (tarea)."""
        text = "Tarea numero: TAREAES567890"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TAREAES567890" not in result

    def test_ticket_reference_number(self, filter_instance):
        """Test ticket reference format."""
        text = "Task no: REFNUMBER678901"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "REFNUMBER678901" not in result

    def test_ticket_alphanumeric(self, filter_instance):
        """Test alphanumeric ticket IDs."""
        text = "Ticket ID: TKT2024A789012B"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TKT2024A789012B" not in result


class TestMultilingualIntegration:
    """Test reference identifiers in mixed-language documents."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_multilingual_document(self, filter_instance):
        """Test mixed-language document with multiple identifier types."""
        text = """
        English: File Number FN2024001, Transaction TRX2024002, Customer CUST123
        German: Aktenzeichen ACZ2024003, Kundennummer KUNDEN456
        French: Dossier-number DOS2024004, Numero client CLI789
        Spanish: Numero expediente EXP2024005, Numero transaccion TR345678
        """
        result = filter_instance.anonymize_text(text)
        
        # Verify each identifier is anonymized
        assert result.count("<FILE_NUMBER>") >= 1
        assert result.count("<TRANSACTION_NUMBER>") >= 1
        assert result.count("<CUSTOMER_NUMBER>") >= 2
        
        # Verify original values are removed
        assert "FN2024001" not in result
        assert "TRX2024002" not in result
        assert "ACZ2024003" not in result
        assert "EXP2024005" not in result


class TestFalsePositiveAvoidance:
    """Test that non-identifier numbers are not mistakenly flagged."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_regular_numbers_untouched(self, filter_instance):
        """Test that regular numbers remain untouched without labels."""
        text = "Processing took 567 seconds to complete."
        result = filter_instance.anonymize_text(text)
        # Plain numbers without labels should not be flagged as reference identifiers
        assert "<FILE_NUMBER>" not in result
        assert "<TRANSACTION_NUMBER>" not in result
        assert "<CUSTOMER_NUMBER>" not in result
        assert "<TICKET_ID>" not in result

    def test_phone_numbers_not_confused(self, filter_instance):
        """Test that phone numbers are not confused with identifiers."""
        text = "Call 555-123-4567 for details"
        result = filter_instance.anonymize_text(text)
        # Phone should be detected as PHONE_NUMBER, not as identifier types
        assert "<FILE_NUMBER>" not in result
        assert "<TRANSACTION_NUMBER>" not in result
        assert "<CUSTOMER_NUMBER>" not in result
        assert "<TICKET_ID>" not in result

    def test_dates_not_confused(self, filter_instance):
        """Test that dates are not confused with transaction numbers."""
        text = "Meeting on 2024-12-31 and 2024-01-15"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" not in result

    def test_zip_codes_not_confused(self, filter_instance):
        """Test that ZIP codes are not confused with customer numbers."""
        text = "Address: 12345 Main Street"
        result = filter_instance.anonymize_text(text)
        # Zip code may be detected as part of address or location, not as customer number
        assert "<CUSTOMER_NUMBER>" not in result


class TestAnonymizationPlaceholders:
    """Verify correct placeholder insertion."""

    @pytest.fixture
    def filter_instance(self):
        return PIIFilter()

    def test_file_number_placeholder(self, filter_instance):
        """Verify FILE_NUMBER placeholder is correct."""
        text = "File Number: FN2024123ABC"
        result = filter_instance.anonymize_text(text)
        assert "<FILE_NUMBER>" in result
        assert "FN2024123ABC" not in result

    def test_transaction_number_placeholder(self, filter_instance):
        """Verify TRANSACTION_NUMBER placeholder is correct."""
        text = "Transaction number: TRX999888777"
        result = filter_instance.anonymize_text(text)
        assert "<TRANSACTION_NUMBER>" in result
        assert "TRX999888777" not in result

    def test_customer_number_placeholder(self, filter_instance):
        """Verify CUSTOMER_NUMBER placeholder is correct."""
        text = "Cust no: CUST555666ABC"
        result = filter_instance.anonymize_text(text)
        assert "<CUSTOMER_NUMBER>" in result
        assert "CUST555666ABC" not in result

    def test_ticket_id_placeholder(self, filter_instance):
        """Verify TICKET_ID placeholder is correct."""
        text = "Issue number: TKT333444555"
        result = filter_instance.anonymize_text(text)
        assert "<TICKET_ID>" in result
        assert "TKT333444555" not in result
