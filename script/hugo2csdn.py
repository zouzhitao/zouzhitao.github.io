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
        line = "<img src=\"{}\" width=\"60%\" />".format(url_head + link)
        # line =line.replace(link,url_head+link)
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
    
    output_file = "tmp.md"
    with open(file_name,"rb") as f:
        with open(output_file,"w",encoding="utf-8") as out:
            skip = False
            for line in f:
                # print(line)
                line = line.decode("utf-8")
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
                out.write(line)

if __name__ == "__main__":
    
    import sys
    file_name = sys.argv[1]
    main(file_name)
            
