#!/usr/bin/env python3
import subprocess
import sys

def run_tests():
    print("Running Calculator Tests...")
    print("=" * 50)
    
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "test_calculator.py", "-v", "--tb=short"
    ])
    
    print("\n" + "=" * 50)
    if result.returncode == 0:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed. Check the issues above.")
    
    return result.returncode

if __name__ == "__main__":
    exit(run_tests())