
def count(sentence):
	return len([i for i in sentence if i in 'aeiuoAEIOU'])



def disemvowel (string_):
	return ''.join([i for i in string_ if i not in  'aeiuoAEIOU'])


def is_square (n):
	return True if n > -1 and n**0.5 == int(n**0.5) else False