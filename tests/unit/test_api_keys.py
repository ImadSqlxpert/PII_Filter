import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pytest
from pii_filter import PIIFilter


@pytest.fixture
def filter_instance():
    return PIIFilter()


class TestAPIKeyDetection:
    """Test API Key detection and anonymization."""

    # AWS Keys
    def test_aws_access_key_id(self, filter_instance):
        """Test AWS Access Key ID detection."""
        text = "My AWS access key is AKIA2JFAKJ1234ABCD."
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_aws_secret_access_key(self, filter_instance):
        """Test AWS Secret Access Key detection."""
        text = "AWS_SECRET_ACCESS_KEY = wJalrXUtnFEMI/K7MDENG+pBxwgnitqLqLcKTest1234"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # GitHub Keys
    def test_github_personal_access_token(self, filter_instance):
        """Test GitHub Personal Access Token detection."""
        text = "github_pat_11ABCDEFGHIJKLMNOPQRST1234567890AB"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_github_oauth_token(self, filter_instance):
        """Test GitHub OAuth token detection."""
        text = "gho_1234567890abcdefghijklmnopqrstuvwxyzAB"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_github_user_to_server_token(self, filter_instance):
        """Test GitHub User-to-Server token detection."""
        text = "ghu_1234567890abcdefghijklmnopqrstuvwxyzAB"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Stripe Keys
    def test_stripe_live_secret_key(self, filter_instance):
        """Test Stripe Live Secret Key detection."""
        text = "Stripe secret key: sk_live_1234567890abcdefghijk"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_stripe_test_secret_key(self, filter_instance):
        """Test Stripe Test Secret Key detection."""
        text = "Test key sk_test_123456789abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_stripe_live_public_key(self, filter_instance):
        """Test Stripe Live Public Key detection."""
        text = "Public key: pk_live_1234567890abcdefghijk"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_stripe_test_public_key(self, filter_instance):
        """Test Stripe Test Public Key detection."""
        text = "pk_test_123456789abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Slack Keys
    def test_slack_bot_token(self, filter_instance):
        """Test Slack Bot Token detection."""
        text = "slack_token=SLACK_TOKEN_REDACTED"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_slack_user_token(self, filter_instance):
        """Test Slack User Token detection."""
        text = "My Slack token: SLACK_TOKEN_REDACTED"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Google Keys
    def test_google_api_key(self, filter_instance):
        """Test Google API Key detection."""
        text = "google_api_key=AIzaSyDummyKeyForTestingPurposesOnly123456"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # SendGrid Keys
    def test_sendgrid_api_key(self, filter_instance):
        """Test SendGrid API Key detection."""
        text = "sendgrid_key=SG.1234567890abcdefghijklmnopqrstuv"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Mailchimp Keys
    def test_mailchimp_api_key(self, filter_instance):
        """Test Mailchimp API Key detection."""
        text = "mailchimp_api_key=MAILCHIMP_KEY_REDACTED"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Twilio Keys
    def test_twilio_auth_token(self, filter_instance):
        """Test Twilio Auth Token detection."""
        text = "twilio_auth_token=1234567890abcdef1234567890ABCD"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Azure Keys
    def test_azure_api_key(self, filter_instance):
        """Test Azure API Key detection."""
        text = "azure_api_key=12345678-1234-1234-1234-123456789012"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # OpenAI Keys
    def test_openai_api_key(self, filter_instance):
        """Test OpenAI API Key detection."""
        text = "openai_api_key=sk-proj-1234567890abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Firebase Keys
    def test_firebase_api_key(self, filter_instance):
        """Test Firebase API Key detection."""
        text = "firebase_api_key=AIzaSyDummyFirebaseKeyForTestingOnly1234567"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # JWT Tokens
    def test_jwt_bearer_token(self, filter_instance):
        """Test JWT Bearer Token detection."""
        text = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Cloudflare Keys
    def test_cloudflare_api_token(self, filter_instance):
        """Test Cloudflare API Token detection."""
        text = "cloudflare_token=1234567890abcdef1234567890abcdef1234567890"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # DigitalOcean Keys
    def test_digitalocean_token(self, filter_instance):
        """Test DigitalOcean API Token detection."""
        text = "digitalocean_api_key=dop_v1_1234567890abcdefghijklmnopqrst"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Webhook Secrets
    def test_webhook_secret(self, filter_instance):
        """Test Webhook Secret detection."""
        text = "webhook_secret=whsec_1234567890abcdefghijklmnopqrstuv"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # False positive tests - ensure we don't over-match
    def test_no_false_positive_short_strings(self, filter_instance):
        """Ensure short strings don't trigger API_KEY false positives."""
        text = "The api key format is sk_test but this is not a real key."
        result = filter_instance.anonymize_text(text)
        # Should not contain <API_KEY> tag since 'sk_test' alone is too short
        assert "<API_KEY>" not in result

    def test_no_false_positive_common_words(self, filter_instance):
        """Ensure common words don't trigger false positives."""
        text = "API-Key-Management System is important for security."
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" not in result

    # Multiple keys in one text
    def test_multiple_api_keys(self, filter_instance):
        """Test detection of multiple API keys in single text."""
        text = """
        AWS: AKIA2JFAKJ1234ABCD
        Stripe: sk_live_1234567890abcdefghijk
        GitHub: ghp_1234567890abcdefghijklmnopqrstuvwxyz
        """
        result = filter_instance.anonymize_text(text)
        # Count API_KEY occurrences
        count = result.count("<API_KEY>")
        assert count >= 3

    # Key in URL
    def test_api_key_in_url(self, filter_instance):
        """Test API key detection in URLs."""
        text = "https://api.example.com?api_key=sk_test_1234567890abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    # Key with special formatting
    def test_api_key_with_equals_sign(self, filter_instance):
        """Test API key detection with = separator."""
        text = "export GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrstuvwxyz"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result

    def test_api_key_with_colon(self, filter_instance):
        """Test API key detection with : separator."""
        text = "stripe_secret_key: sk_live_1234567890abcdefghijk"
        result = filter_instance.anonymize_text(text)
        assert "<API_KEY>" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
