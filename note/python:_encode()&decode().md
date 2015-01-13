# Python: encode()&decode()

## Basic:
* encode(): Convert "Unicode" to "String"

	```
	u'你好'.encode('utf-8')
	```

* decode(): Convert "String" to "Unicode"

	```
	'你好'.decode('utf-8')
	```

## Tricks:
* When using encode() method on "Unicode"

	```
	u'你好'.encode('utf-8')
	# same as
	# u'你好'.decode().encode('utf-8')
	# there would be a error
	```
* When using decode() method on "String"

	```
	'你好'.decode('utf-8')
	# same as
	# '你好'.encode().encode('utf-8')
	# there would be a error
	```
* When call print on "Unicode"

	```
	print u'你好'
	# same as
	# print u'你好'.encode()
	# there would be a error
	```
