#################################### Basic Conifg #############################
THREAD_NUM = 4
USER_AGENT = '''Mozilla/5.0 (Windows NT 6.3; WOW64) 
				AppleWebKit/537.36 (KHTML, like Gecko) 
				Chrome/55.0.2883.87 Safari/537.36'''
############################## Database Config #####################################
MYSQL = {
	'DB_USER': 'root',
	'DB_PASSWD': 'aliyunmysql@',
	# 'DB_PASSWD': '283319',
	'DB_HOST': '127.0.0.1',
	'DB_DATABASE': 'twitter',
	'DB_CHARSET': 'utf8mb4'
}

MongoDB = {
	'DB_HOST': '127.0.0.1',
	'DB_PORT': 27017,
	'DB_DATABASE': 'twitter'
}
############################## App Config(58) #####################################
APP_INFO = [{
		#========================50=======================================
		'consumer_key':'bRJ4nxfQ1lQpc0b9OiGyznwTP',
		'consumer_secret':'duDNQlvxtYInexf8kBiSTUwAuaskty4iGd6HnPKfoWzLoSvJgc',
		'access_token_key':'716652054446379008-4wz9tWCPDUa61FglUqrhk58zmJmtnP2',
		'access_token_secret':'hNFCesJ2rADFcmIljjEmywxGcDc6HrV6ORGZqrqNDWLXF'
	},{
		'consumer_key':'4ixfrtJrgWSAPG1vp4Po6Ee2H',
		'consumer_secret':'88GYXXQIU9CMetxnEXiCrgunvACppEDzbbqpaQ3EU7hX1uZuwG',
		'access_token_key':'716652054446379008-tASFLVR5oyMzODigI995shpFXkZQnOM',
		'access_token_secret':'RJb1gou7r4qxI0DETt4b40xqeulObL9JhZlX83VgAzufL'
	},{
		'consumer_key':'bvax5vKso8AvSoHk73TDwhhGC',
		'consumer_secret':'HgPpPDYzczxNESi5IiovReqkSB9wqWRwm1IEi2RBwqzsvEkV5o',
		'access_token_key':'716652054446379008-VJEnRJLUz16BUFpS3WZ4s4TIwiseJUI',
		'access_token_secret':'xsEGR8Z8XaDJrFbFLoW7QbabmuXm3V5DvdU8535FQLbw9'
	},{
		'consumer_key':'S2enzmwVFoyJDWvD0YGBKr83Z',
		'consumer_secret':'rVbQkqSj0PHQv4msLrvdq4RBbCLdNt1rjB3dbBuq2uuACAZP3v',
		'access_token_key':'716652054446379008-kIaFYqfupIMBPfXxrYiUGXzYxU3IPHU',
		'access_token_secret':'llR2D51dmSHOhsBYBSUzlqHPN6xqARI8K4JzLwwTeYFFZ'
	},{
		'consumer_key':'1PuhS8rjfnsx1ypPRuG190mOE',
		'consumer_secret':'ov8v1UTcqTcNzHxYZglIWy95ExBPElSUzczZ3KhxXcONEHqjqw',
		'access_token_key':'819902790923390976-nLUVtg7ih9RUaBb9qp71rW85cVmSqRF',
		'access_token_secret':'tkcwaZ7QMFfDtmnROlvCyUIW63t739RvPkql9EQZ3vQYN'
	},{
		'consumer_key':'1wxvLj2dE9PPX6Hfwowkx1zhU',
		'consumer_secret':'tVQN67jmdmV7mancwy0DA0I3ww7XartFQRij6qhCBEyXOPmPTA',
		'access_token_key':'819902790923390976-w8uj3yiQhTBgr05zqeTcDRsS4TxHnC0',
		'access_token_secret':'VM9p65rjqCirx2bD3oB9HFVreTta47TQAUCwCW78NuxaG'
	},{
		'consumer_key':'uYHEV8STdg3jkxMakhjao5SU2',
		'consumer_secret':'QiZK4mmVdRLHwXpHGDrbKlyazv58GJCY1XJ2Bx4v9NgtnxasZy',
		'access_token_key':'819902790923390976-jBnkIkGS6hCfCf40fEYNul2kLkNj2cp',
		'access_token_secret':'UejCqBgVkq7y7cM0t2XogO56fjj3CJFm1LU7BgABIDOMe'
	},{
		'consumer_key':'yfhLGRLvovMPiPU72e0HYtBp3',
		'consumer_secret':'A0KIT2psZybXPtxsToSfGGgZ3XEW1cRSxfYszIoSIquo0Lqfzs',
		'access_token_key':'819902790923390976-yC4JTWCFVuV2JTnirwLTwt7pKWNNjC5',
		'access_token_secret':'ZGEUUk8PI52ftlwZgoldYSpBYYp7smsd77QpvD0acICcB'
	},{
		'consumer_key':'bqsScHZYbNJfuT2OQHP0atyPb',
		'consumer_secret':'HNPWeCTW1aDNLEpuwMwHixsGQffezjnCWKYGg92kmnbreh7feM',
		'access_token_key':'830023501721448449-UwvcObeXzQtjLYiexEEwed0GUEooaAJ',
		'access_token_secret':'Fi6bpRHpTjzCEW0ebrD9sxGMg2rnvDj7a1Lf79jbp58u7'
	},{
		'consumer_key':'U80AP9Arm46RVduPbt6XruBrS',
		'consumer_secret':'9y9kdundtqy0wEsHF0vibIBc4w6mkjiQtgOZgUoDZQuKof6B2G',
		'access_token_key':'830023501721448449-hNzCTb1qZtZMlEi9a2UZYwHVoJaZNxe',
		'access_token_secret':'8Kx5y8my2Ld4vMN0cgR8wXLTUOAGdHfhAscxYloIvuwyr'
	},{
		'consumer_key':'epkuCrMQT7Kv8xc2KE7ZwGIQK',
		'consumer_secret':'UEC7TG5queg40T3CP4X8r0P8Po6FDTRbLcjaMw7JZNWxwh6gZm',
		'access_token_key':'830023501721448449-woJPByc30Vcr2liTnGo73Y1Gp4hep3m',
		'access_token_secret':'rmkPVPhJG0HQEdV79ylem50FeAR0hM3LE2RuD9JUb6ct2'
	},{
		'consumer_key':'ZDS4BTVJhnSvPBKmLJPqp2V4C',
		'consumer_secret':'iiyxNpiqBdwTmfyCoe8xBJRA1s1WCjBAkzs8aN8p4XolIMGnfz',
		'access_token_key':'830023501721448449-c1tX7BotohjB8wxDNOUfd9xvMFMiw1t',
		'access_token_secret':'ye2spsFDHxvoncw1mRbPSzIVuDzu9TzcIliCx5Cy92i33'
	},{
		'consumer_key':'Vkc6R1aJnxFoGLP4ZiOPFCVnq',
		'consumer_secret':'5Ecdx2ZkU6Z8Wn53DPaHZWyeKAFqkjEPhWh9uoi3zirmjvFbk6',
		'access_token_key':'830023501721448449-KzJnUGtuqkly3VHi4okFLh0NPhs4DlJ',
		'access_token_secret':'vQ8OolYIo5FtQdzRc9IaF0HxNMkm6tokC934lge7gnUV7'
	},{
		'consumer_key':'tOild7WnZDjKAJrF7DOtSdcTj',
		'consumer_secret':'sr4LJGLbJgXIrbYCf4L9UtQWk0odIGFYt26BTtRqLzzBWbKmRv',
		'access_token_key':'830023501721448449-kG14sXY8ftZJYnqTrUKtzD6HTZUqXGP',
		'access_token_secret':'hV7btDzCwh5vBPFR6MvWwwQDfwiSeelCsl1kuIvqDAHZ0'
	},{
		'consumer_key':'DSCtYmcL2iGg0kP5ZKkABlImW',
		'consumer_secret':'jO8SiXsQI93UmGQqBbdRshAYfj5bWN14jcX5p7cXeGgKY4t3Za',
		'access_token_key':'716652054446379008-ghqGu81aCSH45tS3FqT6E8UXleRHwyg',
		'access_token_secret':'Xgr48NU7OneezMJhQajJzDWmvwrW71m4piHb27YCBTysr'
	},{
		'consumer_key':'LTryJHuyavG5oXlZNEjaQ69eA',
		'consumer_secret':'tSjkIVN7qadGcbZs2pW7q3WY7jTbQMObtLlCr1SupmQKKqr8VU',
		'access_token_key':'716652054446379008-h8d8QuxoYQCEPlAuabd1IeURqOprXKz',
		'access_token_secret':'p9jp0f3cYjPFttgPvWEMDIvQi9L3lo6Zg7UmHFOJeNQNF'
	},{
		'consumer_key':'lRfKWoWExJuhpTAxRLNiT9F9p',
		'consumer_secret':'AcDP5N6zDbYTZ0Een5MOQV4Gmeq7Cy89NPckX2iNHArUpmdCnk',
		'access_token_key':'716652054446379008-OotpeLCspWQjxF1dsD2H6TWzFbb6BMy',
		'access_token_secret':'wlINpllscUaDMYiPevZT4aR6brfdEaaOgq21QYSBqiwwu'
	},{
		'consumer_key':'YuHOAWfbeVeOa0fQlaRFf3VVm',
		'consumer_secret':'kTdVlU4idHuveDJcefbzeAYyTN5oUMmAX6UJyjFw8sieQefXFZ',
		'access_token_key':'830023501721448449-wN6wS6AMKGGuyoQe2vHBSoB3vFCuxdl',
		'access_token_secret':'klSeDdYOBlLt5r7v2ZbsEX0VkN9kTVXhJtmfHWhYSHXPE'
	},{
		'consumer_key':'P6UnF4YfcIYljrh94d6F2ytNV',
		'consumer_secret':'iqDJ7iJu2LsHmKSbaCAvJW5ZrNHBuwlCpPdGect6HkXw15FpDm',
		'access_token_key':'830023501721448449-KiD3iTvRxqmArkUqztARVbOmvNtgQFg',
		'access_token_secret':'8QY9wa8C3QtwimWebwL3i9DFMIMx3AWdwkqTBRyKJKuJZ'
	},{
		'consumer_key':'5thgnhtzd5UtxoG9K47dcd0P4',
		'consumer_secret':'fJZR2JflsrfyEJqJISQON4CLKmkItXZ9kaGgoowYeAwWWJDQCN',
		'access_token_key':'830023501721448449-CN2ifA9lzq2ftN22aKRhsvHG7m2TPBW',
		'access_token_secret':'bl9VwVMp1ZwrBfwaNSIqFr58MYfrpJbzcWxDu4G2aQpoH'
	},{
		'consumer_key':'YFUeSw837XuKkGsNvg9z5WrjB',
		'consumer_secret':'qBJ0uYcwa0MDIdqdUGUJjqYljhUx6PcJtsAV9bGuGEDW6CBYZc',
		'access_token_key':'716652054446379008-QfYhynExGKuRMXzRh8LPKbwqqjPkpH3',
		'access_token_secret':'BRLt24OzjO2DPV8BQQXM5aRkb0vWYOU3s5uRsAB5bSa8Q'
	},{
		'consumer_key':'RPnO7fghGrjrjDFZyjM7t5Bnm',
		'consumer_secret':'bLmLsjNR72AjXly885kHTthgQDwPMA8xBUnwuuMgxeiaI83cu0',
		'access_token_key':'716652054446379008-j41wiY44gelasTyZOQWLCJvHHv8rhN7',
		'access_token_secret':'FVCQEOXZj4OVVJctmx5kgmfrsgX9t4HRMmo8QA53fjA9b'
	},{
		'consumer_key':'wQdNWsIDvqv5l0tOv7feyc5JN',
		'consumer_secret':'fIXgPly1J2GHMAkw0q62a6V4HqzRL4avV2oOT7p7ULLxnz8eJB',
		'access_token_key':'716652054446379008-XweYna5plX2gbyObODKJHClrgwWXUJk',
		'access_token_secret':'6MlxmqwhmVlw3wTvk27lr0C3J2EOzBcsAnZNKZ4P98auf'
	},{
		'consumer_key':'TwTqrGKHaSGsJtpnvRVYGahFI',
		'consumer_secret':'F8UJqUhJ8dseGQFgdz8J6QA4KbunA99azQJM2CQPBGTANGPApk',
		'access_token_key':'819902790923390976-fjchG0hbxBaXLrb1KJCUfyB4fAXU7wC',
		'access_token_secret':'eksOiHjJRoCYF3wrgvU2eSQMaFMopOlVxN1uZ5NaXeSrF'
	},{
		'consumer_key':'6FCU8amNthTHyGb2zFsjepmGW',
		'consumer_secret':'IxL8pUMmzmUttXaPuKFafWcltPCmYesS6NuKC3160jg0LQbf9E',
		'access_token_key':'819902790923390976-hbx7JRpSbqwBp02m32rKAx75ARJgBMa',
		'access_token_secret':'Ovp4R1B3Th9qTlV1qBjazAZORCeNrej8V7uOuFGq72sBM'
	},{
		'consumer_key':'rXdZfZyrSYHrbXvntCdDgkLkf',
		'consumer_secret':'xiWSgmDrIhQGAQQxA504M0lXEBPQB8aeTg6n2134QK4VBYe6I1',
		'access_token_key':'819902790923390976-mqrjVZPmdqnpzahobGOYVWA3zNz5Scp',
		'access_token_secret':'RJnAOw66QrNH4sPjycAjQwfaicZ1lK7myKqlTpktDI0Jc'
	},{
		'consumer_key':'mC7CsKEJyRnJBoRdHif0REwty',
		'consumer_secret':'88OGRRlcHWPx4VzLHBXO7tXEFFcAqgzedBBNAUPuCZBeA6hLQe',
		'access_token_key':'830023501721448449-sp4tLnjCMx3BUncsiCdAAr9C740ots6',
		'access_token_secret':'u3A0uWJZOZdN0SJuA998LdHUCPtrQHfB8dZqoPTVuBH9Q'
	},{
		'consumer_key':'crdLisAoLrNH7dQ1bmIEw0GOt',
		'consumer_secret':'TxFIzNxZpe8QHDvnYGULjFomui5C1CKrjV3kObqCEAA8PYX6rs',
		'access_token_key':'830023501721448449-WGSDyMy77lhC2TSh5iXG0UlxQHoU7dA',
		'access_token_secret':'fvKzzaz2MdcjHaehSasvnaKNiRZx0P3vAEIrOvpkz8Quk'
	},{
		'consumer_key':'mnjNHT4g31ZlbAWSpWQC1X6rK',
		'consumer_secret':'gNmT627PUQjAw6vdzMjrXs9Ni5xRmQFoS7VMMXR9Adwhaab0QJ',
		'access_token_key':'830023501721448449-a2wMCRfsbHIGYNGZUMM6QxffhtokRBc',
		'access_token_secret':'7TKOeXaUuvg6RDdSsUxmD0kAPw4pdrPZ1J85rxUaiue6Y'
	},{
		'consumer_key':'PFhFJtoLoiY0xHScDfP2fWz88',
		'consumer_secret':'bmlJQCAP1RjaQHOUvjqfoAegBftT6COEdR5wM289VEyme4RKll',
		'access_token_key':'716652054446379008-ewY3Dawrg5S2KqTIabkCIQfisJl8MAy',
		'access_token_secret':'GJ90Z24TAmsNQhzmzVtsGnglrUDGht4Fj6n6IdQHAUkjp'
	},{
		'consumer_key':'Y3ZxNXq55ENVQ0YjvcN90X0Gb',
		'consumer_secret':'oWg5xXKmmVbVCL5LddUMwskrCnVytI5OqNkt8PrIHwWmQK6jKy',
		'access_token_key':'716652054446379008-k5ssnQTnkB71Tc8Udfa1i1wRLKe2yg8',
		'access_token_secret':'lSUrocsgGikjUOkC2AffcIYPX6wnjjqDri7OA0g8NEf21'
	},{
		'consumer_key':'TXOyecjatZ9AmPGUuIogt0KTE',
		'consumer_secret':'cNuFvZS6sSLiiPihNnSereIGXsum9KLB5LzksahUWdDIea22lm',
		'access_token_key':'716652054446379008-NXE4ACdbbHrOLzGWgLeU2G96GEllaYh',
		'access_token_secret':'rYQepEJipWa48r7jTVQTnz6fRmrJmdR8DyEeO4qmfExZN'
	},{
		'consumer_key':'hTCJQyhlQwo0jfsJq9btnIOpa',
		'consumer_secret':'83SaHBTnZcxYgtlFmAMjd3OL3jqkTmBuu2zQBkxQUv1qF8Dv6X',
		'access_token_key':'819902790923390976-5iNOK9i0Ug7xTi2dXogliQ5a0nzmygC',
		'access_token_secret':'upZUv4q9sspV6Mc6EwigHlkjXXsoOJcdkzCIu5oL4P6aa'
	},{
		'consumer_key':'LUWRw4NnKjGjeXPUIorvkSpPm',
		'consumer_secret':'gtsW2OkXpNhNTaDVEt9Zs5QPdLRoNSscFm4lA8yNxe9KBQ2QTz',
		'access_token_key':'819902790923390976-hWDmUXpigWkXtnWyurmXmbppy7Eg2Rb',
		'access_token_secret':'IX56ajcsGS9PLpdyVt4xlXYDOUcKJ20RGKg7Pc2tZUNoU'
	},{
		'consumer_key':'w21qjR4nGbd0P3CuRKbeUZ92X',
		'consumer_secret':'rPt6x7LPGq7QqwmtiGRgETQSamuJLwX5u8X2IHenjfweh3Wb9R',
		'access_token_key':'819902790923390976-o75jcltt9i1AyYQjxC4YB7yeIH0L0ae',
		'access_token_secret':'nc4fyj69WWgaqHBwdZONTDwBFfl2T7VPuhFBxRoLiWKr8'
	},{
		'consumer_key':'Ki2K4tyLTzwzKgqjN8gMQqCrD',
		'consumer_secret':'RtdF1aqaSvl76jhn6lp2Jr5VULohXrOgPFbstKSF13xHRfe3aN',
		'access_token_key':'716652054446379008-dO57xwo1fumR1nrnivN3ycYXFm1dd5l',
		'access_token_secret':'jaO5VlwyIBxw2MoUuR9Y3axeOHK9uZMULuxMLjSDyvl2C'
	},{
		'consumer_key':'oCjc5JaCIob2ORr4ci3aWLwiA',
		'consumer_secret':'SlEL7DdKCzR96ibgaRVGhVJ17pIZqat7r4UNxksOZbztCVK6Iy',
		'access_token_key':'716652054446379008-9KCXA5X7QvhPdchCwgX4GSlELsgAKMD',
		'access_token_secret':'P4m7vWYB8nh5Y2liCG7QIx3CCKKU2MFoTTfPBqs67yueT'
	},{
		'consumer_key':'6ciYnYk4KrgujSwuegiqH05c6',
		'consumer_secret':'Hj8F6Gyx9rjcNKBhtINGMnx6XQgUPia4E1NqgfqPeDKkkcLXUS',
		'access_token_key':'716652054446379008-uh3Cz6rOFUHheJKOPb0Nm224G8GQ1H2',
		'access_token_secret':'dquCHv6Qz3Iyt6MoaSDrnslHgH9Voan0ozdP26dml5jZE'
	},{
		'consumer_key':'Xh3rKiXw7pQAiHVWHPXCOKGvu',
		'consumer_secret':'bmepUWD3DuJuCzMBECaLnsZzTc4wttEvDN3ZWLDcOb7IhDyzMw',
		'access_token_key':'830023501721448449-FdKtuDnGf49wfoKXC1zNdvUj5GDjyIo',
		'access_token_secret':'M2hBBtNZeNZHJfeMaJ7H6DBukOpWTh5GU0Gb8pV2guiWy'
	},{
		'consumer_key':'u4B7tKQtZPkugw1RjAn17bQxQ',
		'consumer_secret':'psr93Eoqwn0plJTCuYnIeMFuMoXM4QrSQiPFstCVDvGmSGFlGy',
		'access_token_key':'830023501721448449-FqvjPodL0v8xp8riAusaFLtKlCdznIl',
		'access_token_secret':'Zz0XplBRroObpSfDzrTcjWs6WW5dIAdd7nA570vkSbho8'
	},{
		'consumer_key':'SiUilsW27Q2uvbrB5k4BF6wqq',
		'consumer_secret':'dg7qjjlnIqR2Nwo7pAAS9zTsWIyNpWMyj0TcgMjSgNUkQvDdyV',
		'access_token_key':'830023501721448449-VgpQbF1gS3MfkJ8hvhzgko4WdOUKsfK',
		'access_token_secret':'f8PryNKdaCViUQNK7Xl9EweSIUIMOpJPVICqlCrE7YEb9'
	},{
		'consumer_key':'SFQ9YPmNFmj2xLzLb3Zmb8hk4',
		'consumer_secret':'XcqHXelsJhiqk3hy9V3ENr2MJX951Zsz10ewG1lDcS2UKrDlxF',
		'access_token_key':'819902790923390976-jKWKaEC6GkRfCvYNS8q6Ijy3x5V8W5d',
		'access_token_secret':'4lFjYNyNKFJgm0BGhQCA6yCinrCS83F0FiLFraPkRzmXu'
	},{
		'consumer_key':'4lOqbhhsHdbbrgcz6kmIqANx6',
		'consumer_secret':'qd9evSu7J2TS2KHkc5BNO7qFEMM4kTSB8SvRAcNsmq0Pqp4Pva',
		'access_token_key':'819902790923390976-kpUOqUSbaPHPTMu3cUU3RinhYdC8RRA',
		'access_token_secret':'GCKqbHuHwL0JcRMjnHSbOFUK0ibCrgOT5Pm3W18BHhRrs'
	},{
		'consumer_key':'2vVbNMdaLZfuuWXbtsrs9HM7M',
		'consumer_secret':'irdWygAmgg0cK5wCtO61cSyCwzw5cmqwPfyab51oXHVka0E1k5',
		'access_token_key':'819902790923390976-pTFB2vzf02znRgPuM7RXeCpHewwNLdU',
		'access_token_secret':'rQtmoyqqD2hA32qlJ5hOETxFcQ5UGxNjwukj0i2lvVSnz'
	},{
		'consumer_key':'Tx5tnj69s2FvF50Mu0nf39m4o',
		'consumer_secret':'GPwzIoNtMi2cD2kTxGPxHaVkAirWgP6I81CjHRrlT22Mm6mamI',
		'access_token_key':'716652054446379008-YGHm0Y3H0AYTBQyzQOziDxFJMDJ0tbx',
		'access_token_secret':'t3zMd5e7KGFKZTVZA1FDbDymvqVqvFRc4NBCTKG1uQo1m'
	},{
		'consumer_key':'vE1Uxqswyxlxy42aaXxUecPfA',
		'consumer_secret':'40xC4FvFljJeLVwA8vak4GzfEsrMybq8gvwsqKFMYpjaXtM9f1',
		'access_token_key':'716652054446379008-tmE850ktawX7oseh42uedwFktGopRW8',
		'access_token_secret':'3L2vsndjkqU42uhG4m5KZPC4eMMsuAU1ck3H88dNMM2ZY'
	},{
		'consumer_key':'79i2d3z8Z5dkzGMqGxGdxiwCS',
		'consumer_secret':'HGBjiqVUGhKMI6fk49e3VkJeychYNy6E1qQLfx79lx6fCEN86S',
		'access_token_key':'716652054446379008-welcvkifU8L5QDyemNqxED7hTd8RnGG',
		'access_token_secret':'1fXKoTrpoAsNFjiKLrIWTdx7xwFBaGtqMr7chYZbzQLdw'
	},{
		'consumer_key':'XlXEJnqGqqynBcJdeJUXriyKV',
		'consumer_secret':'kaqd6SERnINIQJeU6BVyDkMNySLz4vtifUFdSmhdZsPbubIitI',
		'access_token_key':'819902790923390976-XAEnVZjxb0hyrM65TwQ8s3ty70QnJCp',
		'access_token_secret':'ug5MESIMHeaElg2oQD6mvOh2g1MwyEFNtDxI8FlGQdnGs'
	},{
		'consumer_key':'gPkQKNKPPyp9ngmde2TXI7YRi',
		'consumer_secret':'JOrU7Fp8zXbTSy9HAza5rXpYkoKpgOSDqLYJcdlZ38KnSv2DDL',
		'access_token_key':'819902790923390976-MEAIoZkNRH67zJcwUIYJt4jHzl3Ju1I',
		'access_token_secret':'pJaJZ2F9uFIBIKB3TpdwpbrCDfSU28bVGYo4Iq5DB9s9y'
	},{
		'consumer_key':'6OxVrARWdg2t8KILzX0yqHT1u',
		'consumer_secret':'k32OKsd1u2eiStlaP3gMvxngyaaFlIKUxQcRwIi3rEkGByv46o',
		'access_token_key':'819902790923390976-dTEwL2JeR7nijwunIa6oMuQbwIZRs7q',
		'access_token_secret':'bfWbyoGP0ozUl7jjlnOJ8ZQ1TOGidbynma21Kog6FEXsM'
	},{
		#========================8=======================================
		'consumer_key':'p64x0KdShuSalqB8ZI9Qh2IvQ',
		'consumer_secret':'ZlOSaBd9VZFcbmbWkO6iBhGZQ6kJOYyBy7MZmx8j0NZUfv5MIT',
		'access_token_key':'819902790923390976-3XZISuci6bGJjKi1VzsMsgmwvCHk9EG',
		'access_token_secret':'pSAu83o84TjmsUQEm80XZZTehojehGNrSb0F6VNIMGkNc'
	},{
		'consumer_key':'ozAREI6YG1cWNqCxkXh2LosAu',
		'consumer_secret':'Bl5IrF6KAXfUvcMsFLhTtXqRsBXodt4JgepBX74PZHUm8N470i',
		'access_token_key':'819902790923390976-hflU4JnyCMGtxzt7oVBD7SpDp7wIDz2',
		'access_token_secret':'SSZWPxThDmcG5qJfFpHXmQFHuZNY4hCfw8qMyL98Nswaa'
	},{
		'consumer_key':'eXGER9GVrRHU4o6B2XkhlTqTM',
		'consumer_secret':'Q7BXUQodMZIIGuw2E8o53CtXQLc9ITWP7IVmCEsFTppunBORfy',
		'access_token_key':'819902790923390976-bngerVeK8eedjK9X4Y5SfagvStWAKfp',
		'access_token_secret':'qbAiDsYlKN7RhLoT78Rhy6iUnN3GMKcffBTeO1RkPkAbh'
	},{
		'consumer_key':'T66cCXwwG5KhFLzMxrJcEpXci',
		'consumer_secret':'SNK2Dn48mr3Ufb0H4HXgjeXbflxBG1mI9ofSlhsptrf3RrOCyq',
		'access_token_key':'830023501721448449-0qJIEfnNZSEfrYpMPXatBzs5BkLLTyy',
		'access_token_secret':'9TEJZQaqPHFMHv7gpoB2EKlSIodcC8RNrhRAzYFtr98pO'
	},{
		'consumer_key':'UI8AOG9QrFsQ8LxI2UBSYeQic',
		'consumer_secret':'bJqTeAKxkJqz8JlLCiaLu57qI4NDdEN8bxOdMiCJ9abKx4eSf4',
		'access_token_key':'830023501721448449-z8V3CoxmdbojPadmRCOukeQHdmhKagf',
		'access_token_secret':'WF7NNoyOY7anxVzry1gtfRtM6s6d25owL0tB9tSqoynAA'
	},{
		'consumer_key':'NZDvjgzJ8YxpAEQ5nArk5uFea',
		'consumer_secret':'e7xxvhOOKJSV8OqJtEBlFMnmFA1Ekz812MY2yqsaThGCBd6Tzn',
		'access_token_key':'830023501721448449-hEXQ9l3BA30Sx4k6pu8ghlyzKcDRX1S',
		'access_token_secret':'h64UELHTJbmjVP2MlHe0vpB8aoSUCFK29oPgYn6hPPnNj'
	},{
		'consumer_key':'ED43dimZs23ogcXhvCMEFLvJt',
		'consumer_secret':'XYewj0zEKNg5EZEDpVjhsgWsqxq5tt07uRnuNOurdg8jr5Tw6r',
		'access_token_key':'830023501721448449-V1TZ51qW5a5huNXaCGKpbyqRpa6vrS3',
		'access_token_secret':'HrN4EvSV6FNgVqwkKxjzCKGQi8RYHXQVIFrGxN9GxR5WG'
	},{
		'consumer_key':'lYIQKsDT0EpB6IzeU8ggieFQM',
		'consumer_secret':'Kur7vAkaggdm3IYrTB7I8lR9cgGSsnArSqaBz2hcNyweAbkNiv',
		'access_token_key':'830023501721448449-9qpwlvYwEVhcZ7c6bdpPt6OxnVg7oaG',
		'access_token_secret':'v4HeDHrPQgeWsLu1ZIkKP1HieObIO00uoJS6j802TFwQG'
	}
]
####################################################################################
