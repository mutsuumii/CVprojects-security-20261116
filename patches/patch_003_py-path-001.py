# Path traversal via unsanitized input
# CWE-22 | Severity: HIGH
# File: codes/9.virtual reader/baidu_pp_ocr/ppocr/utils/save_load.py line 159

**Risk:** File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
