def ngram(string,slice_index=1):
    def slice(l,slicer):
        return [l[i:i+slicer] for i in range(len(l)-slicer+1)]
    graham_cracker = {}
    if slice_index=='word':
        for i in string.split(' '):
            graham_cracker[i] = string.count(i)/len(string.split(' '))
        return graham_cracker
    listings = len(list(set(slice(string,slice_index))))
    for i in slice(string,slice_index):
        graham_cracker[i] = string.count(i)/listings
    return  graham_cracker

def plot_dict(D,type='bar',mode=0):
    if type=='bar':
        plt.bar(range(len(D)), D.values(), align='center')
    elif type=='plot':
        plt.plot(list(D.keys()), list(D.values()))
    plt.xticks(list(range(len(D))), list(D.keys()))
    if not(mode):
        plt.show()

def l2d(l):
    return dict(enumerate(l))

def slice(l,slicer):
    return [l[i:i+slicer] for i in range(len(l)-slicer+1)]

