# Code injection via eval/exec
# CWE-95 | Severity: CRITICAL
# File: codes/9.virtual reader/baidu_pp_ocr/ppocr/data/imaug/__init__.py line 63

**Risk:** User input passed to eval() or exec(). Attacker executes arbitrary Python on the server.

**Fix:** Use ast.literal_eval() for parsing Python literals. Never eval user input.
