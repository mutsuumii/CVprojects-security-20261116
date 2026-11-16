# Command injection via shell=True
# CWE-78 | Severity: CRITICAL
# File: codes/9.virtual reader/baidu_pp_ocr/tools/infer/utility.py line 301

**Risk:** User input passed to a shell command. Attacker can execute arbitrary OS commands.

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
