import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_c2rust_baseline.py"
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("run_c2rust_baseline", SCRIPT)
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)


class C2RustRulePolicyTests(unittest.TestCase):
    def test_signed_wrapping_requires_compiler_policy(self):
        ordinary = baseline.c2rust_rule_args("clang -std=gnu11 -c input.c")
        wrapping = baseline.c2rust_rule_args(
            "clang -std=gnu11 -fno-strict-overflow -c input.c"
        )

        self.assertNotIn("--enable-rule=signed-integer-wrapping", ordinary)
        self.assertIn("--enable-rule=signed-integer-wrapping", wrapping)

    def test_batches_do_not_mix_overflow_policies(self):
        entries = [
            {"file": "lib/ordinary.c", "command": "clang -c lib/ordinary.c"},
            {
                "file": "lib/wrapping.c",
                "command": "clang -fno-strict-overflow -c lib/wrapping.c",
            },
        ]

        batches = baseline.make_batches(entries, None)

        self.assertEqual(len(batches), 2)
        policies = {
            tuple(baseline.c2rust_rule_args(batch[0]["command"])) for batch in batches
        }
        self.assertEqual(len(policies), 2)


if __name__ == "__main__":
    unittest.main()
