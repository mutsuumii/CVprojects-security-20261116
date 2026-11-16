# Insecure deserialization
# CWE-502 | Severity: CRITICAL
# File: codes/19.OCR车牌识别/ppocr/losses/center_loss.py line 45

**Risk:** Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
