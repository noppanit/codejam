

with open('output.out', 'w') as output:
    with open('B-large-practice.in') as fp:
        next(fp)
        for idx, line in enumerate(fp):
            output.write("Case #%d: %s" % (idx+1, ' '.join(line.split()[::-1])))
            output.write("\n")

    output.close()
