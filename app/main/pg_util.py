# coding=utf-8
from log import logger

# input origindatas:[()] return:[]
def get_column_from(index,origindatas):
	if not origindatas or len(origindatas) == 0:
		return []
	if index >= len(origindatas[0]):
		return []
	ret = []
	for line in origindatas:
		ret.append(line[index])
	return ret

# input origindatas:[()] indexs:[] return:[[]]
def get_columns_by_indexs(indexs,origindatas):
	if not origindatas or len(origindatas) == 0:
		return []
	ret = []
	for line in origindatas:
		datas = []
		for index in indexs:
			if index >= len(line):
				continue
			datas.append(line[index])
		ret.append(datas)
	return ret

#input origindatas:[[]] return:[{},{}]
def combine_datanames(columnnames,origindatas):
	if not columnnames or len(columnnames) == 0:
		return origindatas

	if not origindatas or len(origindatas[0]) == 0:
		return origindatas

	if not len(columnnames) == len(origindatas[0]):
		return origindatas

        datas = origindatas
        datafinal = []
        for line in datas:
                map = {}
                for i in range(len(columnnames)):
                        c = line[i]
                        map[columnnames[i]] = c
                datafinal.append(map)

        return datafinal

if __name__ == '__main__':
	origindatas=[(1,2,'a'),(3,4,'b')]
	indexs=[0,2]
	print get_columns_by_indexs(indexs,origindatas)

