# Flaky test fix

- Test: test_status_ready
- Symptom: passed 4 to 6 times out of 10, with no code change
- Cause: a fixed wait (wait_for_timeout 500) against a page that took 100 to 900 ms
- Evidence: error showed 'Loading...' instead of 'Ready'
- Fix: expect(...).to_have_text("Ready") keeps checking up to 5 seconds
- Result: 10 passed