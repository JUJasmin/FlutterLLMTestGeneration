#!/usr/bin/env bash
# Usage: ./run_fault.sh <path_to_faulty_file> <path_to_test_file>

set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <faulty_file> <test_file>"
  exit 1
fi

FAULT_FILE="$1"
TEST_FILE="$2"

# Infer paths
PKG_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ORIG_FILE="${PKG_ROOT}/lib/$(basename "$FAULT_FILE" | sed 's/_F[0-9]\+//')"
TMP_BACKUP="${ORIG_FILE}.bak"

echo "---------------------------------------------"
echo " Running test for fault variant:"
echo "   Fault file: $FAULT_FILE"
echo "   Test file : $TEST_FILE"
echo "---------------------------------------------"

# 1. Verify original passes
echo "[*] Checking baseline (original SUT)..."
cp "$ORIG_FILE" "$TMP_BACKUP"

if flutter test "$TEST_FILE" > /dev/null 2>&1; then
  echo "    ✅ Baseline PASSED"
else
  echo "    ❌ Baseline FAILED — fix before evaluating faults."
  mv "$TMP_BACKUP" "$ORIG_FILE"
  exit 1
fi

# 2. Inject the faulty version
echo "[*] Replacing SUT with faulty variant..."
cp "$FAULT_FILE" "$ORIG_FILE"

# 3. Run the test again
if flutter test "$TEST_FILE"; then
  echo "---------------------------------------------"
  echo "    ❌ Test suite PASSED on faulty code → FAULT SURVIVED"
  echo "---------------------------------------------"
else
  echo "---------------------------------------------"
  echo "    ✅ Test suite FAILED on faulty code → FAULT KILLED"
  echo "---------------------------------------------"
fi

# 4. Restore the original file
mv "$TMP_BACKUP" "$ORIG_FILE"
