# Code injection via eval/exec
# CWE-95 | Severity: CRITICAL
# File: codes/19.OCR车牌识别/tools/eval.py line 73

**Risk:** User input passed to eval() or exec(). Attacker executes arbitrary Python on the server.

**Fix:** Use ast.literal_eval() for parsing Python literals. Never eval user input.
