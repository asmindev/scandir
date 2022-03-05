import scan
from colorama import Back

arg = scan.parser.parse_args()
if __name__ == "__main__":
    scan = scan.scan.Main()
    if arg.mime in scan.allowed_type:
        val = scan.check(arg.path, arg.mime)
    elif arg.mime is not None:
        print(scan.info(f" Type \"{arg.mime}\" is wrong. allowed type: {', '.join(scan.allowed_type)}",color=Back.RED))
        exit()
    else:
        val = scan.check(arg.path)
    print(end="\n")
    if val:
        if arg.mime:
            print(
                scan.info(
                    f"{arg.mime.title()} file founds: {scan.result[arg.mime]['count']}"
                )
            )
        print(scan.info(f"{scan.directories} Directories, {scan.files} Files"))
        confirm = (
            input("Show file (Y/n): ").lower()
            if arg.mime and scan.result[arg.mime]["count"] != 0
            else exit()
        )
        if confirm == "y":
            for index, item in enumerate(scan.result[arg.mime]["files"], start=1):
                print(scan.wrap(f"{index}). {item}"))
    else:
        print(scan.info(f"Not a directory: {arg.path}", color=Back.RED))
