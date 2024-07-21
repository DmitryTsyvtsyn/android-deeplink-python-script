# A simple script for calling deep links on Android via adb utility 

- no need to look for a long command on StackOverflow
- escapes symbols: pipe <b>|</b>, ampersand <b>&</b>, semicolon <b>;</b>
- easy to modify

Example:

    python3 android_deeplink_script.py -a "/Android/platform-tools/adb" -d "https://example.com/deeplink_path/111"
