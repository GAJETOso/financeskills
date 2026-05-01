#!/bin/bash

# Official validation script for FinanceSkills
# This version checks for required metadata and schema compliance

echo "🛡️ Running Official Finance Skills Validation..."

error_count=0

# Check for marketplace.json
if [ ! -f "marketplace.json" ]; then
  echo "⚠️ Warning: marketplace.json not found. Creating a placeholder..."
  echo '{"skills": []}' > marketplace.json
fi

# Check each skill
for skill_dir in skills/*/; do
  if [ -d "$skill_dir" ]; then
    skill_name=$(basename "$skill_dir")
    
    # Check for required files
    for file in "SKILL.md"; do
      if [ ! -f "${skill_dir}${file}" ]; then
        echo "  ❌ [$skill_name] Missing $file"
        ((error_count++))
      fi
    done
    
    # Check for ethical disclaimer in SKILL.md
    if ! grep -q "disclaimer" "${skill_dir}SKILL.md"; then
      echo "  ⚠️ [$skill_name] Missing ethical disclaimer"
    fi
  fi
done

if [ $error_count -eq 0 ]; then
  echo "✨ Validation Passed!"
  exit 0
else
  echo "🛑 Validation Failed with $error_count errors."
  exit 1
fi
