from playwright.sync_api import expect
import pytest

HTML = """
<p id="status">Loading...</p>
<script>
  setTimeout(() => {
    document.getElementById('status').textContent = 'Ready';
  }, 100 + Math.random() * 800);
</script>
"""

@pytest.mark.parametrize("run", range(10))
def test_status_ready(page, run):
    page.set_content(HTML)
    expect(page.locator("#status")).to_have_text("Ready")