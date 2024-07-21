import sys
import getopt
import subprocess

def printHelp():
    print('Incorrect parameters, example:\n{} -a "/Android/platform-tools/adb" -d "https://example.com/deeplink_path/111"'.format(sys.argv[0]))
    sys.exit()

def main():
    try:
        options, _ = getopt.getopt(sys.argv[1:], "ha:d:", ["adb=", "deeplink="])
    except getopt.GetoptError:
        printHelp()

    adb_path = ''
    deeplink = ''

    for option_key, option_value in options:
        if option_key == '-h':
            printHelp()
        elif option_key in ('-a', '--adb'):
            adb_path = option_value
        elif option_key in ('-d', '--deeplink'):
            deeplink = option_value

    if not adb_path:
        printHelp()

    if not deeplink:
        printHelp()

    deeplink = deeplink.replace('&', '\&').replace(';', '\;').replace('|', '\|')

    subprocess.call('{} shell am start -a android.intent.action.VIEW -c android.intent.category.BROWSABLE -d "{}"'.format(adb_path, deeplink), shell=True)

if __name__ == "__main__":
    main()