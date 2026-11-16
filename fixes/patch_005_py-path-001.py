# Path traversal via unsanitized input
# CWE-22 | Severity: HIGH
# File: codes/21.GAN老照片上色动起来/RealSR/scripts/extract_subimgs_single.py line 35

**Risk:** File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
