
# E. Топология сети
# Ограничение времени 	3 секунды
# Ограничение памяти 	512Mb
# Ввод 	стандартный ввод или input.txt
# Вывод 	стандартный вывод или output.txt

# Решение, проходящее все тесты, будет оценено в 5 баллов.

# Распределённая сеть Александра состоит из n вычислительных узлов, соединённых с помощью помощью n−1 кабелей. Каждый кабель соединяет ровно два различных узла, при этом любые два узла соединены кабелем напрямую, либо через цепочку промежуточных узлов.

# Александр очень переживает за сохранность данных в системе, поэтому хочет установить дополнительные жесткие диски на два компьютера-хранилища. Расстоянием между двумя узлами Александр называет минимальное количество соединений на цепочке от одного узла к другому. После выбора узлов для установки дополнительных хранилищ, для каждого узла сети Александр определяет ближайшее к нему хранилище. Ненадёжностью сети он называет максимальное значение этой величины по всем узлам.

# Помогите Александру, сообщите, на какие различные компьютеры необходимо установить дополнительные жесткие диски, чтобы ненадёжность сети была минимальна. 

def get_slices(slic, dic, from_ends=False):
	visited = slic.copy()
	slices = []
	while slic:
		slices.append(slic.copy())
		nx_slice = set()
		for end in slic:
			neibs = dic[end]
			for neib in neibs:
				if neib not in visited:
					nx_slice.add(neib)
		if from_ends:
			nx_slice = {e for e in nx_slice if len(dic[e] - visited) < 2}
		slic = nx_slice
		visited.update(slic)
	return slices


def get_pair(node, pairs):
	for pair in pairs:
		if node in pair:
			return pair


def f(pairs):
	dic = {}
	if len(pairs) == 1:
		return pairs[0]
	for a, b in pairs:
		if a not in dic:
			dic[a] = set()
		if b not in dic:
			dic[b] = set()
		dic[a].add(b)
		dic[b].add(a)
	ends = {e for e in dic if len(dic[e]) == 1}
	slices = get_slices(ends, dic, from_ends=True)
	steps = len(slices) // 2
	slices = slices[steps:]
	while len(slices[0]) > 2:
		slices.pop(0)
		steps += 1
	slic = slices.pop(0)
	slices_center = get_slices(slic, dic)
	steps_center = len(slices_center) - 1
	slices_center.clear()
	diff = steps_center - steps
	if diff > 1:
		slic = slices[diff // 2 - 1]
	if len(slic) == 1:
		[r] = slic
		return get_pair(r, pairs)
	return slic
