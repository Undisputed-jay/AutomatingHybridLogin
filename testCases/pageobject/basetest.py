import pytest
from datetime import datetime

@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    
    def generate_email_with_timestamp(self, domain='gmail.com', prefix='mufu'):
        current_date = datetime.now().strftime("%d%m%Y")
        email = f"{prefix}{current_date}@{domain}"
        return email