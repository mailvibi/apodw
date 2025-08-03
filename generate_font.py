FONT_FILE="rsw.ttf"
FONT_PY_FILE="font.py"

def main():
    fb = None
    font_file_name = FONT_FILE
    font_py_file_name = FONT_PY_FILE
    with open(font_file_name, "rb") as ff:
        fb = ff.read()
    with open(font_py_file_name, "w") as fpyfn:
        fpyfn.write("font=\"")
        fpyfn.write(fb.hex())
        fpyfn.write("\"")

if __name__ == "__main__":
    main()