from ViolentFlow import VioFlow
file_vio = open('non_violent_list.txt')
path = '/Users/roshni/Desktop/VideoData/Non-Violence/'
for each_file in file_vio.readlines():
    each_file = each_file[:-1]
    feature = VioFlow(path + each_file)
    out_file = each_file[:-3] + 'txt'
    print each_file + '-----------------------------------------------------'
    try:
        feature.writeFeatureToFile('violent_features_NON_VIOLENT/' + out_file)
        print each_file + '  done'
    except:
        print 'error in  ' + each_file
