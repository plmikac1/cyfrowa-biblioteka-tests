import json
import pytest
from tests.pages.register_page import RegisterPage

def test_accessibility_with_axe(page, base_url):
    rp = RegisterPage(page, base_url)
    rp.goto()
    page.add_script_tag(url="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.7.2/axe.min.js")
    results = page.evaluate("""() => {
        return axe.run().then(results => results);
    }""")
    violations = results.get("violations", [])
    if violations:
        summary = "; ".join([f"{v['id']}({len(v.get('nodes',[]))})" for v in violations])
        pytest.fail(f"Accessibility violations found: {summary}\nFull results: {json.dumps(results, indent=2)}")
    assert not violations