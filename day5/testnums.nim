

# trying to convince myself nim can hold the numbers
# too lazy to look up datatypes

from std/strutils import strip, split, parseInt

proc makefilebuffer*(inputfile:string) : seq[string] =
    var buffer : seq[string]
    for line in lines(inputfile):
        buffer.add(line)
    return buffer

let outf = open("outs.txt",fmWrite)
let outf2 = open("outn.txt",fmWrite)

let data = makefilebuffer("input.txt")
for line in data:
    let tmpline = line.strip()
    if tmpline=="": continue
    if len(tmpline.split())>3:continue
    if len(tmpline.split())==2:continue
    for n in tmpline.split():
        let nn = parseInt(n)
        echo(tmpline," ",nn)
        outf2.write(nn)
        outf2.write(" ")
    outf2.write("\n")
    outf.write(tmpline)
    outf.write("\n")
outf.close()
outf2.close()