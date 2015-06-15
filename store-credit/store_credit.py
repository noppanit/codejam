lines = []
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
        
with open('./store-credit/A-large-practice.in') as fp:
    for idx, line in enumerate(fp):
        if idx != 0 :
            lines.append(line)

cases = list(chunks(lines, 3))

with open('output.out', 'w') as output:
    for case_num, case in enumerate(cases):
        store_credit = int(case[0])
        item_values = [ int(item.replace('\n', '')) for item in case[2].split(' ')]

        for i, item in enumerate(item_values):
            for j in range(i+1, len(item_values)):
                total_of_two_items = item_values[i] + item_values[j]
                if(total_of_two_items == store_credit):
                    output.write('Case #{case_num}: {first_item} {second_item}'.format(case_num=case_num+1, first_item=i+1, second_item=j+1))
                    output.write('\n')
                    
    output.close()
                




