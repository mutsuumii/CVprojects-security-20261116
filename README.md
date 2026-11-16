# Security audit: enpeizhao/CVprojects

Date: 2026-11-16 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 10 issue(s): 6 critical, 4 high.

## Findings

### 1. [HIGH] Path traversal via unsanitized input

**CWE-22** | `codes/9.virtual reader/baidu_pp_ocr/ppocr/utils/network.py` line 46

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
os.path.join(model_storage_directory, 'inference.pdiparams')
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 2. [HIGH] Path traversal via unsanitized input

**CWE-22** | `codes/9.virtual reader/baidu_pp_ocr/ppocr/utils/save_load.py` line 68

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
with open(checkpoints + '.states', 'rb') as f:
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 3. [HIGH] Path traversal via unsanitized input

**CWE-22** | `codes/9.virtual reader/baidu_pp_ocr/ppocr/utils/save_load.py` line 159

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
with open(model_prefix + '.states', 'wb') as f:
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 4. [CRITICAL] Insecure deserialization

**CWE-502** | `codes/9.virtual reader/baidu_pp_ocr/ppocr/utils/save_load.py` line 69

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
states_dict = pickle.load(f) if six.PY2 else pickle.load(
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 5. [HIGH] Path traversal via unsanitized input

**CWE-22** | `codes/21.GAN老照片上色动起来/RealSR/scripts/extract_subimgs_single.py` line 35

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
path = [os.path.join(root, x) for x in file_list]  # assume only images in the input_folder
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 6. [CRITICAL] Command injection via shell=True

**CWE-78** | `codes/9.virtual reader/baidu_pp_ocr/tools/infer/utility.py` line 294

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
res = os.popen(cmd).readlines()
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---

### 7. [CRITICAL] Command injection via shell=True

**CWE-78** | `codes/9.virtual reader/baidu_pp_ocr/tools/infer/utility.py` line 301

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
env_cuda = os.popen(cmd).readlines()
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---

### 8. [CRITICAL] Code injection via eval/exec

**CWE-95** | `codes/9.virtual reader/baidu_pp_ocr/ppocr/data/imaug/__init__.py` line 63

User input passed to eval() or exec(). Attacker executes arbitrary Python on the server.

```
op = eval(op_name)(**param)
```

**Fix:** Use ast.literal_eval() for parsing Python literals. Never eval user input.
---

### 9. [CRITICAL] Code injection via eval/exec

**CWE-95** | `codes/19.OCR车牌识别/tools/eval.py` line 73

User input passed to eval() or exec(). Attacker executes arbitrary Python on the server.

```
metric = program.eval(model, valid_dataloader, post_process_class,
```

**Fix:** Use ast.literal_eval() for parsing Python literals. Never eval user input.
---

### 10. [CRITICAL] Insecure deserialization

**CWE-502** | `codes/19.OCR车牌识别/ppocr/losses/center_loss.py` line 45

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
char_dict = pickle.load(f)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---
