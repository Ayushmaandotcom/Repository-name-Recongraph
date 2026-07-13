import os
import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # We need to make sure we don't inject multiple times if run multiple times.
    if 'record_id="dummy"' in content or 'record_id="P' in content or 'record_id="G' in content:
        # Actually some experiments might have record_id="dummy" already?
        # Let's just do a blind replace of 'PurchaseRecord(' -> 'PurchaseRecord(record_id="dummy_p", '
        pass

    # We can do this safely: 
    # find `PurchaseRecord(` and replace with `PurchaseRecord(record_id="dummy_p", `
    # UNLESS it's the class definition `class PurchaseRecord:` -> wait, class def doesn't have `(` usually, unless it's inheriting, but here it's `@dataclass`.
    
    # We will exclude src/recongraph/domain/records.py from the blind replace.
    if "records.py" not in filepath:
        # ensure we haven't already replaced
        if 'record_id="dummy' not in content:
            content = re.sub(r'PurchaseRecord\(', r'PurchaseRecord(record_id="dummy_p", ', content)
            content = re.sub(r'GSTRecord\(', r'GSTRecord(record_id="dummy_g", ', content)

    with open(filepath, 'w') as f:
        f.write(content)

# Walk the repo
for root, dirs, files in os.walk('.'):
    if '.venv' in root or '.git' in root or '__pycache__' in root:
        continue
    for file in files:
        if file.endswith('.py'):
            process_file(os.path.join(root, file))

# Fix src/recongraph/domain/records.py
records_path = 'src/recongraph/domain/records.py'
with open(records_path, 'r') as f:
    records_content = f.read()

if 'record_id: str' not in records_content:
    records_content = records_content.replace(
        'class PurchaseRecord:\n    """Represent purchase-side financial evidence."""\n',
        'class PurchaseRecord:\n    """Represent purchase-side financial evidence."""\n\n    record_id: str\n'
    )
    records_content = records_content.replace(
        'class GSTRecord:\n    """Represent GST-side financial evidence."""\n',
        'class GSTRecord:\n    """Represent GST-side financial evidence."""\n\n    record_id: str\n'
    )
    with open(records_path, 'w') as f:
        f.write(records_content)

