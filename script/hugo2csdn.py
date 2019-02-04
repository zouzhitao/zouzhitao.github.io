import re

url_head = "https://zouzhitao.github.io"

img_pat = re.compile(r'!\[.*\]\((/.*)\)')

def matchpic(line):
    """
    assume at least a img in one line
    """
    ret = img_pat.match(line)
    if ret is not None:
        link = ret.groups()[0]
        line =line.replace(link,url_head+link)
    return line
    
# math latex

def latex(line):
    line = line.replace('\\_','_')
    line = line.replace('\\*','*')
    line = line.replace('\\\\\\','\\')
    line = line.replace('\\\\{','\\{')
    line = line.replace('\\\\}','\\}')
    return line

process = [matchpic,latex]

def main(file_name):
    
    with open(file_name,"rb",encoding="utf-8") as f:
        skip = False
        for line in f:
            # print(line)
            if line=='---\n':
                if not skip:
                    skip=True
                else:
                    skip =False
                continue
            
            if skip:
                continue
            for func in process:
                line = func(line)
            print(line,end="")

if __name__ == "__main__":
    
    import sys
    file_name = sys.argv[1]
    main(file_name)
            
