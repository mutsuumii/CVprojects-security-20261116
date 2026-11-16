# Insecure deserialization
# CWE-502 | Severity: CRITICAL
# File: codes/9.virtual reader/baidu_pp_ocr/ppocr/utils/save_load.py line 69

**Risk:** Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
