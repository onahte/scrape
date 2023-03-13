from config import FILE_SCRAPE

target = FILE_SCRAPE

packages = []
with open(target, 'r') as f:
    for i, line in enumerate(f):
        if 'import' not in line:
            continue
        line = line[:-1]
        line = line.split(' ')
        package = ''
        for j, l in enumerate(line):
            if l == 'as':
                break
            if l != 'import' and l != 'from':
                if package != '':
                    package += '.'
                package += l
        packages.append((package))
print(packages)