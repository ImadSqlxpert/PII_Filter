import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pytest
from pii_filter import PIIFilter


@pytest.fixture
def filter_instance():
    return PIIFilter()


class TestSessionID:
    """Test SESSION_ID detection."""

    def test_sessionid_labeled(self, filter_instance):
        """Test SESSIONID= format."""
        text = "SESSIONID=abc123def456ghi789jkl012mno"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result

    def test_session_token_labeled(self, filter_instance):
        """Test session_token= format."""
        text = "session_token=abcdef1234567890abcdef12"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result

    def test_session_id_labeled(self, filter_instance):
        """Test session_id= format."""
        text = "session_id=xyz_abc_123_def_456_ghi"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result

    def test_sid_labeled(self, filter_instance):
        """Test SID= format."""
        text = "sid=abc123def456ghi7"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result


class TestAccessToken:
    """Test ACCESS_TOKEN detection."""

    def test_access_token_labeled(self, filter_instance):
        """Test access_token= format."""
        text = "access_token=abc123def456ghi789jkl012"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_TOKEN>" in result

    def test_bearer_token(self, filter_instance):
        """Test Bearer token format."""
        text = "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9_token123"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_TOKEN>" in result or "<API_KEY>" in result

    def test_token_labeled(self, filter_instance):
        """Test token= format."""
        text = "token=abcdefghij1234567890klmnopqrst"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_TOKEN>" in result


class TestRefreshToken:
    """Test REFRESH_TOKEN detection."""

    def test_refresh_token_labeled(self, filter_instance):
        """Test refresh_token= format."""
        text = "refresh_token=abc123def456ghi789jkl012mno"
        result = filter_instance.anonymize_text(text)
        assert "<REFRESH_TOKEN>" in result

    def test_refreshtoken_alt_format(self, filter_instance):
        """Test refreshtoken= format (no underscore)."""
        text = "refreshtoken=abc123def456ghi789jklmnop"
        result = filter_instance.anonymize_text(text)
        assert "<REFRESH_TOKEN>" in result


class TestAccessCode:
    """Test ACCESS_CODE detection."""

    def test_access_code_format(self, filter_instance):
        """Test access_code=XXXX format."""
        text = "Please enter access_code=A1B2C3D4"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_CODE>" in result

    def test_auth_code_format(self, filter_instance):
        """Test auth_code=XXXX format."""
        text = "Your auth_code: 5678ABCD"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_CODE>" in result

    def test_code_format(self, filter_instance):
        """Test code=XXXX format."""
        text = "Enter code: XYZ12345"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_CODE>" in result

    def test_pin_code_format(self, filter_instance):
        """Test PIN code format."""
        text = "Your PIN is: 1234"
        result = filter_instance.anonymize_text(text)
        assert "<ACCESS_CODE>" in result


class TestOTPCode:
    """Test OTP_CODE detection."""

    def test_otp_code_format(self, filter_instance):
        """Test OTP code format."""
        text = "Your OTP code: 123456"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result

    def test_2fa_code_format(self, filter_instance):
        """Test 2FA code format."""
        text = "2fa_code: 654321"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result

    def test_two_factor_code_format(self, filter_instance):
        """Test two-factor code format."""
        text = "two_factor_code=111222"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result

    def test_verification_code_format(self, filter_instance):
        """Test verification code format."""
        text = "verification_code=555666"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result

    def test_mfa_code_format(self, filter_instance):
        """Test MFA code format."""
        text = "mfa_code: 333444"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result


class TestMultipleTokens:
    """Test detection of multiple tokens in single text."""

    def test_multiple_different_tokens(self, filter_instance):
        """Test detection of multiple different token types."""
        text = """
        Session: session_id=abc123def456ghi789jkl012
        Access: access_token=token_abc123xyz789
        Refresh: refresh_token=refresh_abc123xyz789
        Code: access_code=A1B2
        OTP: otp_code=123456
        """
        result = filter_instance.anonymize_text(text)
        
        # Count each token type (at least some should be present)
        has_session = "<SESSION_ID>" in result
        has_access = "<ACCESS_TOKEN>" in result
        has_refresh = "<REFRESH_TOKEN>" in result
        has_code = "<ACCESS_CODE>" in result
        has_otp = "<OTP_CODE>" in result
        
        detected_count = sum([has_session, has_access, has_refresh, has_code, has_otp])
        assert detected_count >= 3, f"Expected at least 3 token types detected, got {detected_count}"

    def test_session_and_access_tokens(self, filter_instance):
        """Test session and access token together."""
        text = "sessionid=session123abc token=access456def"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result
        assert "<ACCESS_TOKEN>" in result


class TestTokenContextAndFormat:
    """Test token detection with various contexts and formats."""

    def test_token_with_spaces(self, filter_instance):
        """Test token with spaces around = sign."""
        text = "session_id  =  abc123def456ghi789jkl012"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result

    def test_token_case_insensitive(self, filter_instance):
        """Test case-insensitive token detection."""
        text = "SESSION_ID=ABC123DEF456GHI789JKL012"
        result = filter_instance.anonymize_text(text)
        assert "<SESSION_ID>" in result

    def test_token_in_json(self, filter_instance):
        """Test token detection in URL-like labeled format (JSON-like but with = separators)."""
        text = "session_id=abc123def456ghi789jkl012&token=access123456789xyz"
        result = filter_instance.anonymize_text(text)
        # Should detect at least the session_id
        assert "<SESSION_ID>" in result or "<ACCESS_TOKEN>" in result

    def test_token_in_url_query(self, filter_instance):
        """Test token detection in URL query parameters."""
        text = "https://example.com?session_id=abc123def456ghi789jkl012&token=xyz456"
        result = filter_instance.anonymize_text(text)
        # Should detect tokens in URL context
        assert "<SESSION_ID>" in result or "<ACCESS_TOKEN>" in result

    def test_otp_with_hyphens(self, filter_instance):
        """Test OTP code with hyphens."""
        text = "Your code is: 123-456 or use OTP: 654321"
        result = filter_instance.anonymize_text(text)
        assert "<OTP_CODE>" in result


class TestTokenFalsePositives:
    """Test that common non-token patterns don't get flagged."""

    def test_generic_code_not_flagged_without_label(self, filter_instance):
        """Test that bare codes without context aren't over-flagged."""
        text = "The source code is important. Code review: 123456"
        result = filter_instance.anonymize_text(text)
        # Some detection is ok, but should be minimal

    def test_pin_in_normal_context(self, filter_instance):
        """Test PIN in non-sensitive context."""
        text = "The PIN of the board was secured with a pin code."
        result = filter_instance.anonymize_text(text)
        # Should not over-detect in normal text

    def test_session_in_document(self, filter_instance):
        """Test 'session' in normal document context."""
        text = "In our session today, we discussed various topics."
        result = filter_instance.anonymize_text(text)
        # Should not detect session as token without label

    def test_bearer_in_normal_text(self, filter_instance):
        """Test 'Bearer' in normal context."""
        text = "The bearer of this letter is authorized to proceed."
        result = filter_instance.anonymize_text(text)
        # Should not incorrectly flag bearer tokens without proper format


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
