# Filename: src/L2/S8/03_file_operations.py

"""
🔄 Complete File Operations with Error Handling
Level 2, Session 8: File Handling

This file demonstrates practical file operations including
error handling, file existence checks, and real-world patterns.
"""

import os
from datetime import datetime

print("=" * 50)
print("🔄 COMPLETE FILE OPERATIONS")
print("=" * 50)

cleanup_files = ["test_file.txt", "config.txt", "highscore.txt", "app.log"]


def cleanup_demo_files():
    """Remove temporary demo files created by this lesson."""
    for filename in cleanup_files:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"  Removed: {filename}")


# ============================================================
# ERROR HANDLING: FileNotFoundError
# ============================================================
print("\n" + "=" * 50)
print("🛡️ ERROR HANDLING: File Not Found")
print("=" * 50)


def read_file_safely(filename):
    """Read a file with error handling."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"❌ Error: '{filename}' not found!")
        return None
    except PermissionError:
        print(f"❌ Error: No permission to read '{filename}'!")
        return None
    except OSError as e:
        print(f"❌ Unexpected error: {e}")
        return None


# Test with a non-existent file
print("Trying to read 'nonexistent.txt':")
result = read_file_safely("nonexistent.txt")
print(f"Result: {result}")

# Test with a real file
with open("test_file.txt", "w") as f:
    f.write("This file exists!\n")

print("\nTrying to read 'test_file.txt':")
result = read_file_safely("test_file.txt")
print(f"Result: {result}")


# ============================================================
# CHECKING IF FILE EXISTS
# ============================================================
print("\n" + "=" * 50)
print("🔍 CHECKING IF FILE EXISTS")
print("=" * 50)


def file_info(filename):
    """Get information about a file."""
    if os.path.exists(filename):
        print(f"✅ '{filename}' exists!")

        # Get file size
        size = os.path.getsize(filename)
        print(f"   Size: {size} bytes")

        # Check if it's a file or directory
        if os.path.isfile(filename):
            print("   Type: File")
        elif os.path.isdir(filename):
            print("   Type: Directory")

        return True
    else:
        print(f"❌ '{filename}' does not exist")
        return False


file_info("test_file.txt")
file_info("nonexistent.txt")


# ============================================================
# CREATE FILE IF NOT EXISTS
# ============================================================
print("\n" + "=" * 50)
print("📝 CREATE FILE IF NOT EXISTS")
print("=" * 50)


def ensure_file(filename, default_content=""):
    """Create a file if it doesn't exist, return True if created."""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write(default_content)
        print(f"✅ Created new file: {filename}")
        return True
    else:
        print(f"ℹ️ File already exists: {filename}")
        return False


# Create a config file with defaults
default_config = """# Application Settings
volume = 50
brightness = 80
theme = dark
language = en
"""

ensure_file("config.txt", default_config)
ensure_file("config.txt", default_config)  # Won't recreate

print("\nConfig file contents:")
with open("config.txt", "r") as f:
    print(f.read())


# ============================================================
# PRACTICAL EXAMPLE: High Score Tracker
# ============================================================
print("=" * 50)
print("🏆 PRACTICAL EXAMPLE: High Score Tracker")
print("=" * 50)


def load_high_score(filename):
    """Load the high score from a file."""
    try:
        with open(filename, "r") as file:
            score = int(file.read().strip())
            print(f"📊 Loaded high score: {score}")
            return score
    except FileNotFoundError:
        print("📊 No high score file found. Starting fresh!")
        return 0
    except ValueError:
        print("⚠️ Invalid high score data. Resetting to 0.")
        return 0


def save_high_score(filename, score):
    """Save the high score to a file."""
    with open(filename, "w") as file:
        file.write(str(score))
    print(f"💾 Saved high score: {score}")


def update_high_score(filename, new_score):
    """Update high score if new score is higher."""
    current = load_high_score(filename)
    if new_score > current:
        save_high_score(filename, new_score)
        print(f"🎉 NEW HIGH SCORE! {current} → {new_score}")
        return True
    else:
        print(f"Score {new_score} didn't beat {current}")
        return False


# Demo the high score system
print("\n--- High Score Demo ---")
update_high_score("highscore.txt", 100)
update_high_score("highscore.txt", 75)  # Won't update
update_high_score("highscore.txt", 150)  # Will update!
update_high_score("highscore.txt", 125)  # Won't update


# ============================================================
# PRACTICAL EXAMPLE: Simple Log System
# ============================================================
print("\n" + "=" * 50)
print("📋 PRACTICAL EXAMPLE: Simple Log System")
print("=" * 50)


def log(filename, message, level="INFO"):
    """Add a timestamped log entry."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}\n"

    with open(filename, "a") as file:
        file.write(entry)


def show_log(filename, last_n=None):
    """Display log entries."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            if last_n:
                lines = lines[-last_n:]
                print(f"\n📋 Last {last_n} log entries:")
            else:
                print(f"\n📋 All log entries:")

            print("-" * 60)
            for line in lines:
                print(line.strip())
            print("-" * 60)

    except FileNotFoundError:
        print("No log file found.")


# Demo the log system
log_file = "app.log"

# Clear any existing log
if os.path.exists(log_file):
    os.remove(log_file)

log(log_file, "Application started", "INFO")
log(log_file, "Loading configuration...", "INFO")
log(log_file, "Database connection established", "INFO")
log(log_file, "User 'admin' logged in", "INFO")
log(log_file, "Failed to load module X", "WARNING")
log(log_file, "Data processing complete", "INFO")

show_log(log_file)
print("\nShowing last 3 entries:")
show_log(log_file, last_n=3)


# ============================================================
# FILE MODES REFERENCE
# ============================================================
print("\n" + "=" * 50)
print("📚 FILE MODES REFERENCE")
print("=" * 50)

print("""
| Mode  | Description              | Creates? | Erases? |
|-------|--------------------------|----------|---------|
| 'r'   | Read only                | No       | No      |
| 'w'   | Write only               | Yes      | YES!    |
| 'a'   | Append only              | Yes      | No      |
| 'r+'  | Read and write           | No       | No      |
| 'w+'  | Write and read           | Yes      | YES!    |
| 'a+'  | Append and read          | Yes      | No      |

💡 Most common:
   • 'r'  - Reading existing files
   • 'w'  - Creating new files / overwriting
   • 'a'  - Adding to logs / appending data
""")


# ============================================================
# BEST PRACTICES SUMMARY
# ============================================================
print("=" * 50)
print("✅ BEST PRACTICES SUMMARY")
print("=" * 50)

print("""
1. 🛡️ ALWAYS use 'with' statement
   → Ensures files are closed properly

2. 🔍 CHECK before reading
   → Use os.path.exists() or try/except

3. ⚠️ BE CAREFUL with 'w' mode
   → It ERASES existing content!

4. 📝 USE 'a' for logs
   → Append mode keeps history

5. 🧹 STRIP your lines
   → Use .strip() to remove \\n

6. 🛡️ HANDLE errors
   → FileNotFoundError, PermissionError
""")


# ============================================================
# Cleanup
# ============================================================
print("\n" + "=" * 50)
print("🧹 Cleaning up...")
print("=" * 50)

cleanup_demo_files()

print("\n✨ Session 8 complete! You've learned file handling! 📁")
